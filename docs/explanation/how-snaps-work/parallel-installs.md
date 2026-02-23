(interfaces-parallel-installs)=
# Parallel installs

Parallel installs enable you to run multiple instances of the same snap on the same system. Each instance is completely isolated from all other instances, including its name, configuration, interface connections, data locations, services, applications and aliases.

This feature is currently considered experimental. In particular, *snap install* will fail if the same snap is already installed. See below for a workaround and see [Current limitations](#limitations) for more details. As a result, to experiment with parallel installs, an *experimental feature-flag* must first be enabled:

```bash
sudo snap set system experimental.parallel-instances=true
```

We recommend rebooting the system after toggling the _experimental.parallel-instances_  flag state to avoid potential namespace problems with snap applications that have already been run.

## Installing multiple instances

The process for installing multiple instances of a snap is identical to installing a single snap except you *must* provide a unique identifier, called an *instance key*, separated by an underscore (`_`) from the target snap name.

For example, the following command will install two instances of the [hello-world](https://snapcraft.io/hello-world) snap with the second given an instance key of `foo`:

```bash
sudo snap install hello-world hello-world_foo
```

To specify a specific [channel and track](/) for each instance, install each instance separately.

For example, to install [Juju](https://juju.is/) 2.9 alongside Juju 3.0, run the following commands:

```
sudo snap install --channel 2.9/stable juju_29 --classic
sudo snap install --channel 3.0/stable juju_30 --classic
```

When installing from snap file, the instance key is set by passing `--name=<snap>_<instance>` explicitly:

```bash
sudo snap install --name hello-world_foo hello-world_27.snap
```

### Instance key naming

The instance key needs to be manually appended to the snap name, and takes the following format: `<snap>_<instance-key>`

For example, the following are valid instance names, for example:

* `hello-world`
* `hello-world_foo`
* `hello-world_0123456789`

Only lowercase letters or digits are valid, and the instance name can be up to 10 characters long. After being set during the installation of a snap, an instance name cannot be changed.

> ⓘ  The instance key **must** match the following regular expression: `^[a-z0-9]{1,10}$`.

## Instance management

When working with instances, the vast majority of snap commands function just as they would with a single snap. To remove an instance, for example, use *remove*: 

```bash
$ snap remove hello-world_foo
hello-world_foo removed
```

### Interfaces

[Interfaces](/) work across multiple snap instances just as they do from any one snap to another. For example, *xkcd-webserver* includes a *network* plug, as will all of its instances, any of which can be connected to the system's *:network* slot:

```bash
$ snap connections xkcd-webserver_foo
Interface     Plug                             Slot           Notes
network       xkcd-webserver_foo:network       :network       -
network-bind  xkcd-webserver_foo:network-bind  :network-bind  -

$ sudo snap disconnect xkcd-webserver_foo:network

$ snap connections xkcd-webserver_foo
Interface     Plug                             Slot           Notes
network       xkcd-webserver_foo:network       -              -
network-bind  xkcd-webserver_foo:network-bind  :network-bind  -

$ sudo snap connect xkcd-webserver_foo:network

$ snap connections xkcd-webserver_foo
Interface     Plug                             Slot           Notes
network       xkcd-webserver_foo:network       :network       manual
network-bind  xkcd-webserver_foo:network-bind  :network-bind  -
```

### Services

As with Interfaces, [Services](/) function the same with multiple instances of a snap as they do from any one snap to another.

However, with multiple instances, you're more likely to run into port allocation issues, such as two web servers needing access to port 80. In such cases, only the service from one instance will be active.

```bash
$ snap services
Service                            Startup  Current
xkcd-webserver.xkcd-webserver      enabled  active
xkcd-webserver_foo.xkcd-webserver  enabled  inactive
```

You can see why *xkcd-webserver_foo.xkcd-webserver* is inactive by looking at its logs:

```bash
$ sudo snap logs xkcd-webserver_foo.xkcd-webserver
2018-10-03T12:31:59Z xkcd-webserver_foo.xkcd-webserver[1760]: OSError: [Errno 98] Address already in use
(...)
```
As with single snap service collisions, the solution is to stop the service on one instance and start the service on the other: 

```bash
$ sudo snap stop xkcd-webserver.xkcd-webserver
Stopped.

$ sudo snap start xkcd-webserver_foo.xkcd-webserver
Started.

$ snap services
Service                            Startup  Current
xkcd-webserver.xkcd-webserver      enabled  inactive
xkcd-webserver_foo.xkcd-webserver  enabled  active
```

## Application names and aliases

Snap application names for multiple instances are adjusted according to the following pattern:

`<instance-name>.<app>`

When an application name matches the snap name, a short alias is created to match the
instance name.

For example, with *hello-world* and *hello-world_foo* installed, *hello-world.env* has an alias of *hello-world_foo.env* in the *_foo* instance:

```bash
$ hello-world.env  |grep SNAP_INSTANCE_NAME
SNAP_INSTANCE_NAME=hello-world
$ hello-world_foo.env  |grep SNAP_INSTANCE_NAME
SNAP_INSTANCE_NAME=hello-world_foo
```

As with regular snaps, aliases can be added separately:

```bash
$ sudo snap alias hello-world_bar bar_env
Added:
  - hello-world_bar as bar_env

$ sudo snap alias hello-world_foo foo_env
Added:
  - hello-world_foo as foo_env

$ snap aliases
Command          Alias    Notes
hello-world_bar  bar_env  manual
hello-world_foo  foo_env  manual
```

Aliases from instances generate conflict errors, just as they would with distinct snaps:

```bash
$ sudo snap alias hello-world_foo bar_env
error: cannot perform the following tasks:
- Setup manual alias "bar_env" => "hello-world" for snap "hello-world_foo"
(cannot enable alias "bar_env" for "hello-world_foo", already enabled for "hello-world_bar")
```

When aliases trigger a conflict during snap installation, try passing `--unaliased` with the command to disable automatic aliase generation:

```bash
$ sudo snap install snap-with-conflicting-alias_foo --unaliased
```

## Snap environment, data and namespace

When a snap application is run, its environment is populated with a number of `SNAP*` environment variables. 

The following environmental variables are potentially affected when installing multiple instances of a snap:

* **SNAP_NAME**: the name of the snap, eg. `hello-world`
* **SNAP_INSTANCE_NAME**: the name of the instance, eg. `hello-world_foo`
* **SNAP_INSTANCE_KEY**: instance key, eg, `foo` for `hello-world_foo`
* **SNAP**: location of files for the snap
* **SNAP_DATA**: data for this particular snap revision
* **SNAP_COMMON**: data shared between revisions of the same snap
* **SNAP_USER_DATA**: user data for this particular snap revision
* **SNAP_USER_COMMON**: user data shared between revisions of the same snap
* **HOME**: user's home, equivalent to `SNAP_USER_DATA`
* **XDG_RUNTIME_DIR**: user's XDG runtime directory

For example, if *hello-world* and its instance, *hello-world_foo*, are installed, the following name variables would be set:

| snap             | hello-world | hello-world_foo |
|--------------------|-------------|-----------------|
| SNAP_NAME          | hello-world | hello-world     |
| SNAP_INSTANCE_NAME | hello-world | hello-world_foo |
| SNAP_INSTANCE_KEY  |             | foo             |

The data and mount points of parallel installed snaps are kept separate on the host filesystem. Assuming the snap mount directory is `/snap`, the following locations are used:


| snap      | hello-world             | hello-world_foo             |
|-------------|-------------------------|-----------------------------|
| mount point | /snap/hello-world/27    | /snap/hello-world_foo/27    |
| system data | /var/snap/hello-world/  | /var/snap/hello-world_foo/  |
| user data   | $HOME/snap/hello-world/ | $HOME/snap/hello-world_foo/ |

Within the mount namespace of a snap, adjustments are made to map instance-specific locations to the snap locations. Taking *hello-world* as an example, system data locations are set to the following:

| snap     | hello-world                  | hello-world_foo              |
|-------------|------------------------------|------------------------------|
| SNAP        | /snap/hello-world/27         | /snap/hello-world/27         |
| SNAP_DATA   | /var/snap/hello-world/27     | /var/snap/hello-world/27     |
| SNAP_COMMON | /var/snap/hello-world/common | /var/snap/hello-world/common |

However, due to security concerns, user data locations are *not* similarly adjusted:

| snap          | hello-world                         | hello-world_foo                         |
|------------------|-------------------------------------|-----------------------------------------|
| SNAP_USER_DATA   | /home/<usr>/snap/hello-world/27     | /home/<usr>/snap/hello-world_foo/27     |
| SNAP_USER_COMMON | /home/<usr>/snap/hello-world/common | /home/<usr>/snap/hello-world_foo/common |
| HOME             | /home/<usr>/snap/hello-world/27     | /home/<usr>/snap/hello-world_foo/27     |
| XDG_RUNTIME_DIR  | /run/user/<uid>/snap.hello-world    | /run/user/<uid>/snap.hello-world_foo   |

## Current limitations

There are a few limitations with parallel installs that will be addressed in subsequent `snapd` releases.

### User data and runtime locations

As described in [Snap environment, data and namespace](#environment), the user data locations are kept separate across multiple instances. Applications that hard code paths to either user data directories or the XDG runtime directory may not function correctly as the AppArmor profile has been updated to allow accessing instance specific paths only.

Applications need to use `SNAP_USER_DATA`, `SNAP_USER_COMMON` or fallback to using `HOME`.

Applications built using most popular frameworks, such as Gtk/glib or Qt, and that are already capable of observing both `HOME` and `XDG_RUNTIME_DIR`, should continue to work.

### Ports, DBus names, shared memory and socket activation

Snaps may provide APIs consumed by other snaps or the host system at some well known locations or addresses, such as DBus service names, /dev/shm objects or semaphores, abstract socket addresses. While the default AppArmor template has been updated to allow only instance specific access, connecting interfaces may allow a wider access capabilities that can lead to conflicts between instances of the same snap.

#### Ports

When snapd installs a snap with services, the services are automatically started. Services trying to bind to the same port may fail or function incorrectly. Such snaps should deliver means for configuration of the service via configure hooks.

A demo snap https://github.com/bboozzoo/parallel-installs-demo provides an example of reconfiguration via configure hooks.

#### DBus names

Services exporting the API on DBus under a well known name may conflict with other instances of the same snap. Those may require fixes from application or snap developers.

#### `/dev/shm`

The default AppArmor profile allows instance specific access only. Applications hardcoding paths can break. Note that some interfaces such as `mir` allow a wider access to `/dev/shm`. Such snap would need to be updated to made instance aware.

#### Socket activation

Snaps using socket activation will collide with each other when parallel installed. The socket unit file may need manual adjustment.

