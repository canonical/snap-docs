---
myst:
  html_meta:
    description: Prepare a snap for parallel instances by using instance-aware paths, avoiding shared-resource conflicts, and checking unsupported features.
---

(how-to-guides-snap-development-support-parallel-instances)=
# Support parallel instances

{ref}`Parallel instances <interfaces-parallel-installs>` lets users install a snap more than once, with separate data, configuration, services and interface connections. This feature is enabled by default from snapd version 2.79.

If snapd considers that your snap supports parallel instances, you should ensure that instances installed in parallel on a system will work properly. Parallel instances work properly when all of them can run independently at the same time, without clashes and without smashing data from each other.

To ensure that multiple instances of your snap work properly, your application, and its hooks must work when another instance is running. Successful installation alone does not prove that a snap is ready for parallel instances.

Snap developers should first {ref}`check support for parallel instances of your snap <support-parallel-instances-check-support>`. If your snap is not supported for parallel instances, then you don't need perform to take any further action. Otherwise, ensure that you {ref}`use the snapd-provided environment variables <support-parallel-instances-use-environment-variables>` and {ref}`make shared resources configurable <support-parallel-instances-make-shared-resources-configurable>` in your snap. Finally, you can {ref}`test your snap for correct behavior with parallel instances <support-parallel-instances-test-snap>`.

For more details see {ref}`Parallel installs <interfaces-parallel-installs>`.

(support-parallel-instances-check-support)=
## Check snapd support for parallel instances of your snap

To determine whether your snap is compatible with parallel instances, inspect {ref}`snap.yaml <reference-development-yaml-schemas-the-snap-format>`. If your snap declares any {ref}`unsupported plug, slot <interfaces-parallel-installs-unsupported-table>`, or {ref}`app property <interfaces-parallel-installs-unsupported-app-properties>`, snapd refuses to install multiple instances of it.

Compare your snap's declared plugs and slots against the table in {ref}`Unsupported interfaces <interfaces-parallel-installs-unsupported-table>`. Plugs and slots of the same interface can have different support coverage. For example, `dbus` plugs are supported, while `dbus` slots are not.

If your snap is not compatible with parallel instances, you don't need to worry about the rest of this guide since your snap will be unaffected by parallel instances support due to incompatibility.

```{note}
Be aware that advanced users have a mechanism to bypass the support checks; see {ref}`Installing an unsupported snap anyway <interfaces-parallel-installs-bypass>`.
```
(support-parallel-instances-use-environment-variables)=
## Use the snapd-provided environment variables

To make sure that multiple instances of your snap can run in parallel, all apps, hooks, and scripts must refer to the right instance. That requires using the correct environment variables. Snapd provides variables to identify an instance of the snap, as well as path variables pointing to the files it needs to access. Note that the instance key is optional and, even when it is not provided, `SNAP_INSTANCE_NAME` refers to the installed snap's name.

### Identify the running instance

When installing a parallel instance, users choose an instance key (`^[a-z0-9]{1,10}$`), giving the instance a name of the form `<snap>_<key>`. Use `SNAP_INSTANCE_NAME` to refer to the name of that snap instance.

For the full list of runtime variables and example values, see {ref}`Snap environment, data and namespace <interfaces-parallel-installs-environment>` and {ref}`Environment variables <reference-development-environment-variables>`. The following tables show the most relevant variables to keep in mind.

| Variable | Use case |
| --- | --- |
| `SNAP_NAME` | Use when you need the store name of your snap |
| `SNAP_INSTANCE_NAME` | Use whenever referring to the snap (unless you need to refer to the snap store name) |
| `SNAP_INSTANCE_KEY` | Use to determine if the snap is running as an instance; it will be empty if the snap is not a parallel installed instance |

### Use instance-specific paths

To ensure that the snap instance points to the correct files, use snapd-provided paths, instead of constructing them from the hard-coded snap name. Snapd maps $SNAP`, `$SNAP_DATA`, and `$SNAP_COMMON` to the instance's files. Therefore, the same path strings can be used on multiple instances. Do not append the instance key to these variables, as it would result in the wrong path.

| Variable | Purpose |
| --- | --- |
| `$SNAP` | Read-only files shipped in the snap |
| `$SNAP_DATA` | System data for this revision only |
| `$SNAP_COMMON` | System data shared across all revisions of this instance only |
| `$SNAP_USER_DATA` | User data for this revision only |
| `$SNAP_USER_COMMON` | User data shared across all revisions of this instance only |
| `$XDG_RUNTIME_DIR` | Per-user runtime files (instance-specific for strict snaps) |

For example, a user application's database of one specific instance can be set up this way:

```sh
mkdir -p "$SNAP_USER_COMMON"
exec "$SNAP/bin/<app-name>" --database "$SNAP_USER_COMMON/state.db"
```

For classic snaps, use the snap data variables for instance-specific state and check how you access the user's home directory and other host paths. See {ref}`Classic confinement <parallel-installs-classic-confinement>` and {ref}`Parallel installs <interfaces-parallel-installs>` for the native-package and reboot requirements for classic instances.

(support-parallel-instances-make-shared-resources-configurable)=
## Avoid conflicts in shared resources

Snapd does not coordinate how a supported interface access its resources. To ensure that the resources shared between instances of your snap do not cause them to clash, provide explicit coordination between instances or document that only one instance can run at a time. Alternatively, avoid clashes by configuring each instance to use a separate resource. 

Review everything your application owns outside its snap data directories and see {ref}`Current limitations<parallel-installs-current-limitations>` for details on specific features. Note the possible solution for conflicts with {ref}`Ports <interfaces-parallel-installs-ports>`.

(support-parallel-instances-test-snap)=
## Test parallel instances of your snap

Test your snap's behavior when installed as a parallel instance to avoid unexpected issues. The tests below are some of the ways in which you can test whether parallel installed instances work correctly.

**Installation**

Install three parallel instances `<snap>`, `<snap>_<key1>`, `<snap>_<key2>`: one instance without a key and two with different keys.

Example with local installation:

```sh
sudo snap install --dangerous ./<snap-file>.snap
sudo snap install --dangerous --name=<snap-name>_<instance-key> ./<snap-file>.snap
```

**Concurrent operation**

Run both instances and test the application's main workflows. Verify that ports, locks, sockets and single-instance detection do not conflict.

**Data isolation**

Write different settings and data through each instance. Confirm that neither reads or changes the other's state, including caches and external resources.

**Configuration and services**

Change a setting, restart a service and stop an instance. Confirm that the other instance remains unchanged and operational. Test missing configuration and resource conflicts, then recovery.

**Interfaces**

Inspect `snap connections` for each instance. Confirm correct hook execution and test manual connections through `snap connect`. If your snap acts as a provider on some interface, check that consumers are correctly receiving data.

**Refresh and revert**

Refresh one instance to a newer build, then revert. Confirm that hooks, data migrations and connections do not attempt to alter the other instance.

**Desktop integration**

Launch both instances in the same desktop session, including when one is already running.

**Removal**

Remove either instance and confirm that the other's data, services, launchers and shared-resource registrations still work.
