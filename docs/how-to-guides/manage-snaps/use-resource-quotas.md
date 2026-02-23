(how-to-guides-manage-snaps-use-resource-quotas)=
# Use resource quotas

A quota group sets resource limits on [services](/how-to-guides/manage-snaps/control-services) running inside snaps.

Resource limits can be set for the following attributes:
- **Journal log messages**: as a maximum size for the log and as a rate limit
- **Memory**: as a maximum amount of RAM
- **CPU usage**: as a percentage across a number - or specific - CPU cores, and as a given number of threads

Quota groups are created, removed and queried with the following _snap_ commands:

- **set-quota**: create or update a quota group
- **quota**: show quota group for a set of snaps
- **quotas**: show all quota groups
- **remove-quota**: remove a quota group

Quota groups require snap version _2.59+_. Setting quotas for journal log messages is currently considered experimental and requires that an *experimental feature-flag* is first be enabled:

```
sudo snap set system experimental.quota-groups=true
```

## Create a quota group

To create a quota group, use the `snap set-quota` command with a group name and a limiting attribute, such as `--memory=<amount>`:

`snap set-quota mygroup --memory=64MB`

### Add snaps to a quota group

Snaps that contain services can be optionally added to a quota group when a group is created:

`snap set-quota mygroup --memory=64MB snap1 snap2`

After a group has been created, a snap can be added to a group when it's installed:

`snap install snap1 --quota-group=mygroup`

A pre-installed snap can be added to a pre-existing quota group by running the `set-quota` command again:

`snap set-quota highmem hello-world`

See below for details on which limiting attributes are supported by quota groups.

## Limiting attributes

### Journal log limits

While the `snap logs` command is used to retrieve the _systemd journal_ logs for a specific service, or for all services within a snap (see [Inspecting logs](/how-to-guides/manage-snaps/control-services.md#inspecting-logs) for further details), a quota can be used to limit the output.

Log output can be limited by both size and rate within a quota group.

####  Journal size

`journal-size=<value>[KB|MB|GB]`

Limit the size of the aggregated journal log for all the snaps in the quota group. This is useful when service log output is verbose on devices with limited storage capacity.

Accepts a value in either kilobytes(KB), megabytes(MB) or gigabytes(GB), including aggregated values:

```
sudo snap set-quota loggroup --journal-size=64MB
```

#### Journal rate limit

`journal-rate-limit=<number-of-messages>/<time-period>`

Limit the number of messages logged to a maximum per time period. This is a useful way of limiting the number of messages for snaps.

The time period is can be nanoseconds(us), milliseconds (ms), seconds(s), minutes (m), and hours(h), including aggregated periods:

```
sudo snap set-quota loggroup --journal-rate-limit=10/1h2m3s4ms5us
```

### Memory limits

`memory=value[KB|MB|GB]`

Memory units can be 'B', 'KB', 'MB or 'GB' with a size greater than 4KB:

```
sudo snap set-quota highmem --memory=2GB
```

The memory limit for a quota group can only be increased.  Increasing the memory limit for a quota group *does not* restart any services associated with snaps in the quota group.

To decrease the memory limit for a quota group, the entire group must be removed with the _remove-quota_ command and recreated with a lower limit.

### CPU limits

CPU limits can be set in 4 different ways, some of which can be combined depending on requirements:

- Percentage of total CPU resources
- Percentage of a given number of CPU cores
- Percentage for specific cores
- Limit the number of threads

Without a specified CPU limit, all quota groups can use the full system capacity. 

#### Percentage of total CPU resources 
`cpu=<percentage>%`

Sets a relative percentage limit on how much execution time a process receives, regardless of the number of cores available, up to 100%.

#### Percentage of a given number of CPU cores
`--cpu=<number of cores>x<percentage>%`

<!-- TODO: this behaviour is on systems using cgroupsv2 (grep ^cgroup /etc/mtab).  Without this, CPU limits use CPUQuota (200% means two cores). This needs to be tested and documented. -->

One or more cores can be specified alongside a CPU percentage to allocate relative CPU resources across only that number of cores.

For example, `--cpu=2x100%` on a 4 core system would permit a process to run at full capacity on only two cores, which is equivalent to 50% of full system capacity. 

#### Percentage for specific cores

 `cpu-set=<core number 1>,<core number 2> --cpu=<percentage>%`

Using an additional `--cpu-set` argument with `--cpu` , it's possible to specify exactly which cores to be used as the CPU resources for that quota group.

For example, `--cpu-set=0,1 --cpu=100%` will permit up to 100% CPU resource usage on 2 specific cores (0 and 1).

The following example will allow up to a maximum of half usage combined on four specific cores which means the sum of usage across all 4 specific cores cannot exceed 200%:

```
snap set-quota max-two-specific-cores --cpu-set=0,1,2,3 --cpu=50%
```

In the above example, services in the _max-two-specific-cores_ quota group could run using 100% of two cores and 0% of the other two cores, or 25% of each core, 33% of 3 of the cores and 0% of the last core, or any other combination that does not exceed 200%. The number 200% comes from the size of the `--cpu-set` set multiplied by the `--cpu` setting. 

#### 4. Limit the number of threads 

`threads=<thread limit>`

The `--threads` option is used to limit the number of threads or processes that can be created by the snaps within the quota group. 

For example, `--threads=4096` will limit a quota group to no more than 4096 threads or processes.

The _threads_ option can also be used with both `--cpu` and `--cpu-set` options to target specific requirements:

```
snap set-quota max-two-specific-cores --cpu-set=0,1,2,3 --cpu=50% --threads=8092
```

By default, quota groups are not limited in the number of threads they can create.


## View quotas

If the group already exists, _set-quota_ will update its resource limits.

Use the _quotas_ command to view created quota groups:

```
$ snap quotas
Quota      Parent  Constraints                        Current
highmem            memory=2.00GB cpu=50%,cpu-set=0,1
cpuhalf            cpu=50%,cpu-set=0,1
manycores          cpu=2x,cpu=100%,threads=4096
maxcores           cpu=100%
memcpu             memory=2.00GB,cpu=50%
threads            threads=4096
loggroup           journal-size=64.0MB,journal-rate=10/1h2m3.004005s
```
Snaps can belong to only one quota group, but quota groups can be nested.

## Nested quota groups

To create a nested quota group, add the `--parent=<parent group>` argument to the _set-quota_ command when creating a new quota group:

```
sudo snap set-quota lowmem --memory=1GB --parent=highmem
```

The *quotas* command will also show nested quota groups:

```
$ snap quotas
Quota    Parent   Constraints    Current
highmem           memory=2.00GB  
lowmem   highmem  memory=1.00GB  
```
The total resource use of nested quota groups cannot exceed that of the parent group.

## Update a quota group
 
Add the names of one or more snaps to the _set-quota_ command to include those snaps in the quota group when its created:

```
sudo snap set-quota lowmem go-example-webserver --parent=highmem
```

If the quota group already exists, snaps can be added by using _set-quota_ without the resource limit:

```
sudo snap set-quota lowmem go-example-webserver
```

Adding new a snap to a quota group will result in all non-disabled services in
that snap being restarted.

New quotas can be set on existing quota groups, but existing quotas cannot be removed from a quota group, without removing and recreating the entire group.

The CPU set limit for a quota group can be modified to include new cores, or to remove existing cores from the quota already set.

The threads limit for a quota group can be increased but not decreased. To
decrease the _threads_ limit for a quota group, the entire group must be removed
with the remove-quota command and recreated with a lower limit.

Updating quotas in a group, or imposing new quotas on an existing quota group, will per default require restarting any running services in that quota group.

## View group members and resource usage

The _quota_ command shows information about a quota group, including the set of 
snaps it includes and any subgroups it contains, as well as its resource constraints and 
the current usage of those constrained resources by snap services in those snaps:

```
$ snap quota lowmem
name:    lowmem
parent:  highmem
constraints:
  memory:  1.00GB
current:
  memory:  5.32MB
snaps:
  - go-example-webserver
```

Use the _quota_ command on the parent of any nested groups to view total resource usage and subgroups:

```
$ snap quota highmem
name:  highmem
constraints:
  memory:  2.00GB
current:
  memory:  5.35MB
subgroups:
  - lowmem
```

## Remove snaps and quota groups

To remove a snap from a quota group, the entire group must be removed with the _remove-quota_ command and the quota group recreated without the snaps:


```
$ sudo snap remove-quota lowmem
$ sudo snap set-quota lowmem --memory=1GB
$ snap quota lowmem
name:  lowmem
constraints:
  memory:  1.00GB
current:
  memory:  0B
```

Currently, only quota groups with no subgroups can be removed. In order to remove a quota group with subgroups, the subgroups must be first removed until there are no further subgroups in the group, then the group itself can be removed.

An existing subgroup cannot be moved from one parent to another.

To remove a subgroup from a quota group, the subgroup must be first removed directly with the remove-quota command.
