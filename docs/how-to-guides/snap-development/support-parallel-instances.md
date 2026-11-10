---
myst:
  html_meta:
    description: Prepare a snap for parallel installs by using instance-aware paths, avoiding shared-resource conflicts, and checking unsupported features.
---

(how-to-guides-snap-development-support-parallel-instances)=
# Support parallel instances

Parallel installs let users install a snap more than once, with separate data, configuration, services and interface connections. Snapd enables them by default from version 2.79.

Snap developers should be aware of possible parallel instances of their snap and, if snapd considers their snap supported parallel instances, should work to ensure their snap will work properly with more than one installation on a system. To support parallel instances of the snap you develop, your application, its dependencies, and its hooks must work when another instance is running. Successful installation alone does not prove that a snap supports parallel instances.

For installation commands, instance management, and the full list of restrictions, see {ref}`Parallel installs <interfaces-parallel-installs>`.

Snap developers should first {ref}`check support for parallel instances of your snap <support-parallel-instances-check-support>`. If your snap is not supported for parallel instances, then you need perform no further action. Otherwise, ensure that you {ref}`use the snapd-provided environment variables <support-parallel-instances-use-environment-variables>` and {ref}`make shared resources configurable <support-parallel-instances-make-shared-resources-configurable>` in your snap. Finally, you can {ref}`test your snap for correct behavior with parallel instances <support-parallel-instances-test-snap>`.

(support-parallel-instances-check-support)=
## Check support for parallel instances of your snap

Inspect the {ref}`snap.yaml <reference-development-yaml-schemas-the-snap-format>` to determine your app's plugs, slots, and properties for compatibility with parallel installs. If your snap declares any unsupported plug, slot or app property, snapd refuses to install it as a parallel instance.

Compare your snap's declared plugs and slots against the table in {ref}`Unsupported interfaces <interfaces-parallel-installs-unsupported-table>`. Plugs and slots of the same interface can have different support coverage. For example, `dbus` plugs are supported, while `dbus` slots are not.

Two specific plugs are supported only under specific conditions:

* `desktop`
  : supported only when the `desktop-file-ids` attribute is **not** set.
* `shared-memory`
  : supported only when `private: true` is set.

Check whether any app declares one of the {ref}`unsupported app properties <interfaces-parallel-installs-unsupported-app-properties>`: `common-id`, `bus-name` or `activates-on`.

If your snap is not compatible with parallel instances, you need not worry about the rest of this guide since your snap will be unaffected by parallel instances support.

```{note}
Be aware that users have a mechanism to bypass the support checks; see {ref}`Installing an unsupported snap anyway <interfaces-parallel-installs-bypass>`.
```
(support-parallel-instances-use-environment-variables)=
## Use the snapd-provided environment variables

Ensure that all relevant references of your snap's name or paths in your snap's applications, hooks, or scripts use the proper environment variables. Users choose an instance key (`^[a-z0-9]{1,10}$`) when installing a parallel instance, giving the instance a name of the form `<snap>_<key>`. In all cases not referring specifically to the store name, developers should use `SNAP_INSTANCE_NAME` to refer to the name of their snap and should use the proper path environment variable for persisting data.

For the full list of runtime variables and example values, see {ref}`Snap environment, data and namespace <interfaces-parallel-installs-environment>` and {ref}`Environment variables <reference-development-environment-variables>`.

| Variable | Use case |
| --- | --- |
| `SNAP_NAME` | Use when you need the published snap name |
| `SNAP_INSTANCE_NAME` | Use always instead of `SNAP_NAME` except in cases where you need to refer to the published snap name |
| `SNAP_INSTANCE_KEY` | Use for determining if snap is running as an instance; it will be empty if the snap is not a parallel installed instance |

Use snap-provided paths instead of constructing them from the hard-coded snap name. Inside each instance's mount namespace, `$SNAP`, `$SNAP_DATA` and `$SNAP_COMMON` can have the same path strings as in the regular installation. Snapd maps them to that instance's files. Do not append the instance key to these variables.

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

For classic snaps, use the snap data variables for instance-local state and audit access to the user's real home directory and other host paths. See {ref}`Classic confinement <explanation-security-classic-confinement>` and {ref}`Parallel installs <interfaces-parallel-installs>` for the native-package and reboot requirements for classic instances.

(support-parallel-instances-make-shared-resources-configurable)=
## Make shared resources configurable

For each shared resource, either configure each instance to use a separate resource, provide explicit coordination between instances, or document that only one instance can run at a time. An interface being supported does not mean snapd coordinates access to its resources.

Review everything your application owns outside its snap data directories. Common areas of concern include:

* **Network services**: TCP and UDP listening addresses and ports.
* **Inter-process communication**: Unix sockets, abstract sockets, shared-memory paths, and semaphores.
* **External resources**: Databases, remote accounts, API queues, and service registrations that your application connects to.
* **System resources**: hardware devices, mounted filesystems, and firewall rules.

See {ref}`Current limitations<interfaces-parallel-installs-shared-resources>` for details on specific features.

(support-parallel-instances-test-snap)=
## Test your snap for correct behavior with parallel instances

To help ensure a positive experience for users, test your snap's behavior when installed as a parallel instance, for example with the following possible test steps. 

As a reminder, you can use `snap logs <instance-name>` to inspect logs when facing a failure.

**Installation**

Install a keyed instance both with and without the regular installation present.

Example with local installation:

```sh
sudo snap install --dangerous ./<snap-file>.snap
sudo snap install --dangerous --name=<snap-name>_<instance-key> ./<snap-file>.snap
```

**Concurrent operation**

Run both instances and exercise the application's main workflows. Verify that ports, locks, sockets and single-instance detection do not conflict.

**Data isolation**

Write different settings and data through each instance. Confirm that neither reads or changes the other's state, including caches and external resources.

**Configuration and services**

Change a setting, restart a service and stop an instance. Confirm that the other instance remains unchanged and operational. Test missing configuration and resource conflicts, then recovery.

**Interfaces**

Inspect `snap connections` for each instance. Test manual connections, disconnected plugs and any instance used as a provider.

**Refresh and revert**

Refresh one instance to a newer build, then revert where supported. Confirm that hooks, data migrations and connections do not attempt to alter the other instance.

**Desktop integration**

Launch both instances in the same desktop session, including when one is already running.

**Removal**

Remove either instance and confirm that the other's data, services, launchers and shared-resource registrations still work.
