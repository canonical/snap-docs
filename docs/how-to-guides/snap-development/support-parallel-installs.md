---
myst:
  html_meta:
    description: Prepare a snap for parallel installs by using instance-aware paths, avoiding shared-resource conflicts, and checking unsupported features.
---

(how-to-guides-snap-development-support-parallel-installs)=
# Support parallel installs

Parallel installs let users install a snap more than once, with separate data, configuration, services and interface connections. Snapd enables them by default from version 2.79.

Snap developers should be aware of possible parallel instances of their snap and, if snapd deems their snap supported for parallel installs, should work to ensure their snap will work properly with more than one installation on a system. To support parallel instances of the snap you develop, your application, its dependencies, and its hooks must work when another instance is running. Successful installation alone does not prove that a snap supports parallel instances.

For installation commands, instance management, and the full list of restrictions, see {ref}`Parallel installs <interfaces-parallel-installs>`.

## Determine if your snap can be parallel installed

Not all snaps can be parallel installed. When installing a snap with an instance key, snapd checks every declared plug, slot and app property. If a snap declares an unsupported feature, installation fails with an error. For example:

```console
error: cannot install snap "my-snap_test" as parallel instance: plug "service" with
interface "bluez" is not supported for parallel instances: owning a unique global
resource cannot have parallel instances
```

Inspect the {ref}`snap.yaml <reference-development-yaml-schemas-the-snap-format>` to determine your app's plugs, slots, and properties for compatibility with parallel installs.

### Check your snap's plugs and slots

Compare your snap's declared plugs and slots against the table in {ref}`Unsupported interfaces <interfaces-parallel-installs-unsupported-table>`. Plugs and slots of the same interface can have different support coverage. For example, `dbus` plugs are supported, while `dbus` slots are not.

Two specific plugs are supported only under specific conditions:

* `desktop`
  : supported only when the `desktop-file-ids` attribute is **not** set.
* `shared-memory`
  : supported only when `private: true` is set.

### Check your snap's app properties

Check whether any app declares one of the {ref}`unsupported app properties <interfaces-parallel-installs-unsupported-app-properties>`: `common-id`, `bus-name` or `activates-on`. If your snap declares any unsupported plug, slot or app property, snapd refuses to install it as a parallel instance.

```{important}
If your snap is not compatible with parallel instances through either incompatible slots, plugs, or app properties, then snapd will block its parallel install. Correspondingly, such snaps need not worry about the rest of this guide since they will be unaffected by parallel instances support (however, be aware that users have a mechanism to bypass the checks; see {ref}`Installing an unsupported snap anyway <interfaces-parallel-installs-bypass>`).
```

## Use the instance name instead of the snap name

Users choose an instance key (`^[a-z0-9]{1,10}$`) when installing a parallel instance, giving the instance a name of the form `<snap>_<key>`. Your snap’s applications, hooks, or scripts might refer to the non-instanced snap name (`<snap>`), either as a hard-coded value or through `SNAP_NAME`. If they do, check whether those references need to identify a specific installation. In most cases, `SNAP_INSTANCE_NAME` should be used instead.

* For a regular installation, `SNAP_INSTANCE_NAME` equals `SNAP_NAME`, so code that uses `SNAP_INSTANCE_NAME` works identically in both regular and parallel installations.
* For a parallel installation, `SNAP_NAME` is still the installation name minus the instance key across every instance, so any lock file, socket, `/tmp` path or identifier built from `SNAP_NAME` will collide between instances.

| Variable | Use case |
| --- | --- |
| `SNAP_NAME` | Use when you need the published snap name |
| `SNAP_INSTANCE_NAME` | Use always instead of `SNAP_NAME` except in cases where you need to refer to the published snap name |
| `SNAP_INSTANCE_KEY` | Use for determining if snap is running as an instance; it will be empty if the snap is not a parallel installed instance |

For the full list of runtime variables and example values, see {ref}`Snap environment, data and namespace <interfaces-parallel-installs-environment>` and {ref}`Environment variables <reference-development-environment-variables>`.

## Keep data and runtime files instance-local

Use snap-provided paths instead of constructing them from the hard-coded snap name.

| Purpose | Use |
| --- | --- |
| Read-only files shipped in the snap | `$SNAP` |
| System data for this revision only | `$SNAP_DATA` |
| System data shared across all revisions and all instances | `$SNAP_COMMON` |
| User data for this revision only | `$SNAP_USER_DATA` |
| User data shared across all revisions of this instance only | `$SNAP_USER_COMMON` |
| Per-user runtime files (instance-specific) | `$XDG_RUNTIME_DIR` |

For example, a user application can keep its database in:

```sh
mkdir -p "$SNAP_USER_COMMON"
exec "$SNAP/bin/my-app" --database "$SNAP_USER_COMMON/state.db"
```

```{note}
Inside each instance's mount namespace, `$SNAP`, `$SNAP_DATA` and `$SNAP_COMMON` can have the same path strings as in the regular installation. Snapd maps them to that instance's files. Do not append the instance key to these variables.

User data paths are not remapped in the same way and include the instance name. Paths observed inside a snap are not necessarily the paths that a host application should use. See {ref}`Snap environment, data and namespace <interfaces-parallel-installs-environment>`.
```

For classic snaps, use the snap data variables for instance-local state and audit access to the user's real home directory and other host paths. See {ref}`Classic confinement <explanation-security-classic-confinement>` and {ref}`Parallel installs <interfaces-parallel-installs>` for the native-package and reboot requirements for classic instances.

Apply the same rules to PID files, locks, caches and generated configuration. Review your snaps hooks; they must operate on their own state and resources, not those of another instance.

## Make shared resources configurable

For each shared resource, either configure each instance to use a separate resource, provide explicit coordination between instances, or document that only one instance can run at a time. An interface being supported does not mean snapd coordinates access to its resources.

Review everything your application owns outside its snap data directories. Common areas of concern include:

* **Network services**: TCP and UDP listening addresses and ports.
* **Inter-process communication**: Unix sockets, abstract sockets, shared-memory paths, and semaphores.
* **External resources**: Databases, remote accounts, API queues, and service registrations that your application connects to.
* **System resources**: hardware devices, mounted filesystems, and firewall rules.

See {ref}`Current limitations<interfaces-parallel-installs-shared-resources>` for details on specific features.

## Test your snap for correct behavior with parallel instances

To secure a positive experience for users, ensure your snap behaves properly when installed as a parallel instance. Test that you don't have wayward hard-coded instance-specific values by performing the following suggested steps.

#### Installation

Install a keyed instance both with and without the regular installation present.

Example with local installation:

```sh
sudo snap install --dangerous ./<snap-file>.snap
sudo snap install --dangerous --name=<snap-name>_<instance-key> ./<snap-file>.snap
```

#### Concurrent operation

Run both instances and exercise the application's main workflows. Verify that ports, locks, sockets and single-instance detection do not conflict.

#### Data isolation
Write different settings and data through each instance. Confirm that neither reads or changes the other's state, including caches and external resources.

#### Configuration and services
Change a setting, restart a service and stop an instance. Confirm that the other instance remains unchanged and operational. Test missing configuration and resource conflicts, then recovery.

#### Interfaces
Inspect `snap connections` for each instance. Test manual connections, disconnected plugs and any instance used as a provider.

#### Refresh and revert

Refresh one instance to a newer build, then revert where supported. Confirm that hooks, data migrations and connections do not alter the other instance.

#### Desktop integration
Launch both instances in the same desktop session, including when one is already running.

#### Removal
Remove either instance and confirm that the other's data, services, launchers and shared-resource registrations still work.

Use `snap services`, `snap logs <instance-name>` and `snap connections <instance-name>` to investigate failures.
