(how-to-guides-manage-snaps-use-snapctl)=
# Use snapctl

The `snapctl` tool is bundled with _snapd_ to provide specific environmental feedback and a limited set of controls from **within the context** of a snap's execution environment in relation to snapd. It can be used, for example, to retrieve and set snap configuration options, check the status of a running snap, and reboot an Ubuntu Core 20 environment.

`snapctl` is typically run from a script _within a snap_, rather than on the host system. These scripts are used by snap developers to implement [hooks](/reference/development/supported-snap-hooks), or from within [snapcraft.yaml](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/snapcraft-yaml/), to augment a snap's execution environment.

For details on using _snapctl_ to add user options to a snap, see [Adding snap configuration](set-system-options).

## Configuration options

A snap's configuration options can be queried and altered with the `snapctl get`, `snapctl set` and `snapctl unset` commands. These work very similar to the analogous [`snap get/set/..` commands](/how-to-guides/manage-snaps/configure-snaps) outside the snap. The main difference is that using these commands from within a snap will *not* trigger [the `configure` hook](/reference/development/supported-snap-hooks).

The `snapctl` command uses the same get, set and unset syntax as the snap command:

```
snapctl get <configuration option>
```

For example, the following sets a value of `80` for *http*:

```sh
snapctl set ports.http=80
```

To unset a value, pass its name with `snapctl unset`, and more than one value can be passed at a time:

```sh
snapctl unset ports.http ports.https
```

For convenience, an option can also be unset by adding an exclamation mark (`!`) to the end of a value. For example, the following *unsets* `https`:

```sh
snapctl set ports.http=80 ports.https!
```

By using a dot in the key of an option, you create a nested configuration. You can retrieve multiple nested options by specifying their common key:

```
$ snapctl get ports
{
"http": "80",
"https": "443"
}
```

To see this in action, look at the [NextCloud snap](https://github.com/nextcloud/nextcloud-snap). It uses `snapctl` within its [various hooks](https://github.com/nextcloud/nextcloud-snap/blob/master/src/hooks/utilities/configuration-utilities) to set configuration options such as `snapctl get private.mode` and `snapctl set private.mode="$1"`.

## Confdb

The `snapctl get`, `snapctl set` and `snapctl unset` commands can also be used to access and modify [confdb configurations](/explanation/how-snaps-work/confdb-configuration-mechanism.md). To use `snapctl` to access confdb, you can include the `--view` flag as well as the name of the snap's [interface plug](/explanation/how-snaps-work/confdb-configuration-mechanism.md/#interface-plugs) that refers to the [confdb view](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/) being accessed, prefixed with a colon.

```sh
$ snapctl get --view :setup-wifi ssid
foo
```

When using `snapctl get` in [confdb hooks](/explanation/how-snaps-work/confdb-configuration-mechanism.md#hooks), the data returned will reflect the changes being committed as part of the ongoing transaction that resulted in the hooks being invoked. To read the state of the confdb without the uncommitted changes, you can use the `--previous` flag.

```sh
$ snapctl get --view --previous :setup-wifi ssid
bar
```

You can also use the `--default` flag to provide a default value to be returned if no data is stored under the requested configuration path.

For further information on confdb, see [Configure snaps with confdb](/how-to-guides/manage-snaps/configure-snaps-with-confdb.md) and [Confdb configuration mechanism](/explanation/how-snaps-work/confdb-configuration-mechanism.md).

## Components

Component support requires *snapd 2.67+* .

[Components](/explanation/how-snaps-work/snap-components) are exposed in the snap mountspace under `/snap/<snap_name>/components/<snap_revision>/<component_name>`. This is a symlink to `/snap/<snap_name>/components/mnt/<component_name>/<component_revision>`.

There is only one component revision active for a snap revision at a given time.

From within a snap, the _snapctl_ command can be used to install and remove components from an application, including snap hooks and component hooks. The syntax for both commands are as follows:

```sh
snapctl install +<comp_name>
snapctl remove +<comp_name>
```

If these commands are run from a [hook](/reference/development/supported-snap-hooks), the components will be installed/removed after the hook itself has run if it ended successfully.

## snapctl commands

From within a snap, the [snapctl](https://snapcraft.io/docs/using-snapctl) command can be used to install and remove components from an application, including snap hooks and component hooks. The commands for this are:

$ snapctl install +<comp_name>

$ snapctl remove +<comp_name>

If these commands are run from a hook, the components will be installed/removed after the hook itself has run if it ended successfully.

## Health state

> ⓘ  Health reporting is under development and its capabilities and syntax may change.

Snap developers can use `snapctl set-health` to provide feedback on the operational state, or health, of a snap.

It uses the following syntax:

```
snapctl set-health [--code=<error code>] <status> [<message>]
```

`status` can be one of the following:

* `okay`: which takes no message and no code
* `waiting`: some resource the snap needs isn't ready yet, and there's nothing for the user to do but wait. A message (+code) must explain what it's waiting for
* `blocked`: the user needs to do something for the snap to do something. A message (+code) must say what
* `error`: something went wrong; a message (+code) must explain what has broken

Outside the snap, health status in included as a note in the output to `snap list`, and as a category in `snap info` for a specific snap:

```
$ snap info nextcloud
name:    nextcloud
summary: Nextcloud Server - A safe home for all your data
health:
  status:  blocked
  message: Backing up database.
  checked: today at 10:44 GMT
```

For more comprehensive information on using `snapctl set-health`, see [Health checks](https://forum.snapcraft.io/t/health-checks/10605).

## Interface connections<

(from _snapd 2.43+_)

The state of a specific snap interface can be probed with the `snapctl is-connected` sub-command by supplying either a slot or plug name as an argument:

```
snapctl is-connected <plug|slot>
```

The plug or slot is always the name of the plug/slot from the calling snap.

If the given plug or slot is connected, the command returns the standard exit code for success, which is `0` on POSIX systems. A non-zero exit code is returned in all other cases.

For example, the following indicates the camera interface **is not** connected:

```
$ snapctl is-connected camera; echo $?
1
```

This behaviour can be easily used within a hook, for example:

```
if snapctl is-connected camera; then
  # exit status=0. logic when connected
  echo "connected"
else
  # logic when not connected; note if this is run from hooks.
  # printing to stdout/stderr is not visible to the user
  # (unless the hook fails entirely with exit status > 0)
  echo "not connected"
fi
```

Snaps can only query their own plugs and slots because the snap name is implicit and implied by the snapctl execution context.

See [Snapcraft interfaces](/) for more details on manipulating interfaces from a snap.

## Model information

(from _snapd 2.56+_ onwards)

A [model assertion](https://ubuntu.com/core/docs/reference/assertions/model) contains the
fundamental definition of a snap-based device, such as a device running [Ubuntu Core](https://ubuntu.com/core/).

The _snap model_ command can be used to return to the active model identification for the device, and `snapctl model` returns the equivalent to `snap model --verbose` from within a snap. However, for this to work, the requesting snap needs to meet _one_ of the following criteria:

The requesting snap must be either:
1. a [gadget snap](/reference/development/yaml-schemas/the-gadget-snap)
1. published from the same brand as the device model assertion 
1. have the [snapd-control](/) plug

By default, the output model identification information is presented in a structured yaml-like format:

```yaml
brand-id:      canonical
model:         ubuntu-core-22-amd64
grade:         signed
[...]
```

This can be changed to JSON with the `--json` flag:

```
{
  "architecture": "amd64",
  "base": "core22",
  "brand-id": "canonical",
  "grade": "signed",
  "model": "ubuntu-core-22-amd64",
  "serial": "5f1ee168-ee21-4c38-b03c-5ff9bef64c1e",
  "snaps": [
    {
      "default-channel": "22/stable",
      "id": "UqFziVZDHLSyO3TqSWgNBoAdHbLI4dAH",
      "name": "pc",
      "type": "gadget"
    },
    [...]
```

The raw assertion can also be requested with the `--assertion` flag.

## Mount control

When the [mount-control interface](/) is connected, a snapped application or service can use the _mount_ command to mount transient (non-persistent) and persistent filesystem mount points:

```
snapctl mount -o <options> -t <fstype> </path/to/device> </target/mount/point>
```

To mount a persistent mount point, add the `--persistent` option:

```
$ snapctl mount --persistent -o bind,rw /usr/share /media/mount
```

A corresponding _umount_ command can be used to remove a mount point:

```
snapctl umount </path/to/mount/point>
```

See [mount-control interface](/) for further details on permitted filesystems and mount options.


##  Reboot control (from the UC20+ install-device hook)

The `snapctl reboot` command can be used to control reboot behaviour from the gadget `install-device hook` during UC20+ **install mode**.

See the [UC20+ installation process](https://ubuntu.com/core/docs/uc20/installation-process#heading--install-device) documentation for further details.

## Refresh control (from the UC20+ gate-auto-refresh hook)

The gate-auto-refresh hook is executed by snapd for every snap that will be updated with the next automatic refresh. It's also executed for every snap that is dependent on a snap that will be updated.

This hook is capable of executing the _snapctl refresh_ command with 3 specific arguments, `hold`, `proceed` and `pending`:

This feature is currently considered experimental. See [Refresh control](/) for further details.

### snapctl refresh --hold

Requests that snapd does not refresh the calling snap, nor the snaps it depends upon, during the current automatic refresh. A snap can hold its own refresh for up to 90 days and other snaps for up to 48 hours. The command prints an error and returns a non-zero exit status if these deadlines are reached and the refresh can no longer be held.

### snapctl refresh --proceed

Signals to snapd that a refresh can proceed for both the calling snap and the snaps it depends upon. This does not necessarily mean the update will happen, because they may be held by other snaps, and snapd only proceeds with auto-refresh after consulting gate-auto-refresh hooks of all potentially affected snaps.

### snapctl refresh --pending

Checks whether the executing snap has a pending refresh, or will be affected by the refresh of its base snap.

The output from `snapctl refresh --pending` includes the following details:

- **pending**: none, inhibited or ready
- **channel**: tracking-channel
- **version**: version (only if there is a pending refresh for the snap itself)
- **revision**: revision (only if there is a pending refresh for the snap itself)
- **base**: true or false (true if the snap is affected by refresh of its base snap)
- **restart**: true or false (true if refresh will cause system restart)

The pending output value is set to "none" if there is no pending refresh for the snap and the value is "ready" if there is a pending refresh. A pending value of "inhibited" indicates that the next refresh is inhibited because one or more of the snap's applications are running. This currently requires the experimental refresh app awareness feature to be enabled (see below).

### snapctl refresh --tracking

Checks which channel the snap is currently tracking.

The output from `snapctl refresh --tracking` includes the following details:

- **channel**: tracking-channel

## The snap-refresh-control interface

The `snapctl refresh --proceed` command can be executed by a snapped application outside of the gate-auto-refresh hook if the snap has the `snap-refresh-control` interface and the interface is connected. This enables the snap to trigger an auto-refresh outside of the normal auto-refresh schedule and should be used cautiously.

Please note that the  "snapctl refresh" commands cannot be used from hooks other than gate-auto-refresh hook.

If the gate-auto-refresh hook doesn't invoke "snapctl refresh --proceed" or "snapctl refresh --hold" commands and exits with exit code 0, the refresh proceeds normally as if the hook didn't exist (except for respecting "inhibited" status if refresh app awareness is in use).

If the hook fails with an error, snapd assumes "hold" as long as the maximum deadline hasn't been reached.

## Services

As with configuration options (see above), snapctl sub-commands for managing services are the same as those used by the snap command. See [Services and daemons](/) for further details.

To query the startup and running state of a service, for example, use `snapctl services <service-name>`:

```
$ snapctl services nextcloud.mysql
Service          Startup  Current  Notes
nextcloud.mysql  enabled  active   -
```

The `start`, `stop` and `restart` snapctl commands can be used to start, stop and restart services:

```
$ snapctl stop nextcloud.mysql
$ snapctl services nextcloud.mysql
Service          Startup  Current   Notes
nextcloud.mysql  enabled  inactive  -
```

Services can be enabled and disabled by adding the `--enable` argument to _snapctl start_ and `--disable` to _snapctl stop_ respectively:

```
$ snapctl start nextcloud.myql --enable
$ snapctl stop nextcloud.mysql --disable
```

Snaps can only query their own services.

## System mode

The `snapctl system-mode` command returns YAML-formatted details about specific system states:

```
$ snapctl system-mode
system-mode: install
seed-loaded: true
factory: true
```

The following keys and values can potentially be returned:

- **system-mode**: `install`, `factory-reset`, `recover`, `run`</br>
   The current (operational) system mode:
   - `install`: denotes the system is installing
   - `factory-reset`: a factory reset has been triggered
   - `recover`: the system is in _recovery mode_  
   - `run`: indicates the system has booted normally.</br>This is the only reported system mode on UC16/UC18 system.

   See [Recovery modes](https://ubuntu.com/core/docs/recovery-modes) for more details on each mode.

- **seed-loaded**: `true` </br>
    Set when the installation of seeded snaps for the model has finished.
- **factory**: `true`</br>
   Only possible on a [UC20+](https://ubuntu.com/core/docs/uc20) system in install mode (`system-mode: install`) with the factory image hint set. This  value can be used to govern whether factory-only resources may be available. See [Factory image hint](  https://ubuntu.com/core/docs/uc20/installation-process#heading--factory) for more details.
