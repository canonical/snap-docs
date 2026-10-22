---
myst:
  html_meta:
    description: Understand parallel installs, which run isolated instances of the same snap with separate names, data, configuration, services, apps, aliases, and interfaces.
---

(interfaces-parallel-installs)=
# Parallel installs

Parallel installs enable you to run multiple instances of the same snap on the same system. Each instance is completely isolated from all other instances, including its name, configuration, interface connections, data locations, services, applications and aliases.

Parallel installs are enabled by default from snapd 2.79. Earlier versions of snapd treated them as an experimental feature that had to be enabled explicitly.

Not every snap can be installed as a parallel instance. Snaps that use unsupported interfaces or app properties are rejected when installed with an instance key. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-unsupported>` for details.

To disable parallel installs, set the `experimental.parallel-instances` system option to `false`:

```
sudo snap set system experimental.parallel-instances=false
```

With parallel installs disabled, `snap install` fails when given an instance key.

The native package of snapd 2.79 ships a new mount unit, crucial for the correct behavior of parallel instances of classic snaps. For systems that previously did not have the feature enabled and wish to use parallel instances of classic snaps, we recommend rebooting the system after updating the native package to a version >=2.79.

## Installing multiple instances

The process for installing multiple instances of a snap is identical to installing a single snap except you *must* provide a unique identifier, called an *instance key*, separated by an underscore (`_`) from the target snap name.

For example, the following command will install two instances of the [hello-world](https://snapcraft.io/hello-world) snap with the second given an instance key of `foo`:

```
sudo snap install hello-world hello-world_foo
```

To specify a specific {ref}`channel and track <explanation-how-snaps-work-channels-and-tracks>` for each instance, install each instance separately.

For example, to install [Juju](https://juju.is/) 2.9 alongside Juju 3.0, run the following commands:

```
sudo snap install --channel 2.9/stable juju_29 --classic
sudo snap install --channel 3.0/stable juju_30 --classic
```

When installing from snap file, the instance key is set by passing `--name=<snap>_<instance>` explicitly:

```
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

```
$ snap remove hello-world_foo
hello-world_foo removed
```

### Interfaces

{ref}`Interfaces <explanation-interfaces-all-about-interfaces>` work across multiple snap instances just as they do from any one snap to another. For example, *xkcd-webserver* includes a *network* plug, as will all of its instances, any of which can be connected to the system's *:network* slot:

```
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

Slots provided by a parallel instance are never used for automatic connections. If an instance provides a slot that another snap needs, connect it manually:

```
sudo snap connect <consumer-snap>:<plug> <provider-snap>_<instance-key>:<slot>
```

Some interfaces are not supported on parallel instances. See {ref}`Snaps that are unsupported as parallel instances  <interfaces-parallel-installs-unsupported>` for details.

### Services

As with Interfaces, {ref}`Services <how-to-guides-manage-snaps-control-services>` function the same with multiple instances of a snap as they do from any one snap to another.

However, with multiple instances, you're more likely to run into port allocation issues, such as two web servers needing access to port 80. In such cases, only the service from one instance will be active.

```
$ snap services
Service                            Startup  Current
xkcd-webserver.xkcd-webserver      enabled  active
xkcd-webserver_foo.xkcd-webserver  enabled  inactive
```

You can see why *xkcd-webserver_foo.xkcd-webserver* is inactive by looking at its logs:

```
$ sudo snap logs xkcd-webserver_foo.xkcd-webserver
2018-10-03T12:31:59Z xkcd-webserver_foo.xkcd-webserver[1760]: OSError: [Errno 98] Address already in use
(...)
```
As with single snap service collisions, the solution is to stop the service on one instance and start the service on the other: 

```
$ sudo snap stop xkcd-webserver.xkcd-webserver
Stopped.

$ sudo snap start xkcd-webserver_foo.xkcd-webserver
Started.

$ snap services
Service                            Startup  Current
xkcd-webserver.xkcd-webserver      enabled  inactive
xkcd-webserver_foo.xkcd-webserver  enabled  active
```

(interfaces-parallel-installs-aliases)=
## Application names and aliases

Snap application names for multiple instances are adjusted according to the following pattern:

`<instance-name>.<app>`

When an application name matches the snap name, a short alias is created to match the
instance name.

For example, with *hello-world* and *hello-world_foo* installed, *hello-world.env* has an alias of *hello-world_foo.env* in the *_foo* instance:

```
$ hello-world.env  |grep SNAP_INSTANCE_NAME
SNAP_INSTANCE_NAME=hello-world
$ hello-world_foo.env  |grep SNAP_INSTANCE_NAME
SNAP_INSTANCE_NAME=hello-world_foo
```

As with regular snaps, aliases can be added separately:

```
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

```
$ sudo snap alias hello-world_foo bar_env
error: cannot perform the following tasks:
- Setup manual alias "bar_env" => "hello-world" for snap "hello-world_foo"
(cannot enable alias "bar_env" for "hello-world_foo", already enabled for "hello-world_bar")
```

When aliases trigger a conflict during snap installation, try passing `--unaliased` with the command to disable automatic alias generation:

```
$ sudo snap install snap-with-conflicting-alias_foo --unaliased
```

(interfaces-parallel-installs-environment)=
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

(interfaces-parallel-installs-unsupported)=
## Snaps that are unsupported as parallel instances

Certain snaps, due to their nature, can never be parallel installed:
- snapd
- core base
- kernel
- gadget

All other snaps are subject to feature checking. Snapd checks every snap installed with an instance key and rejects it if it uses a feature that cannot work with more than one instance.

### Unsupported interfaces

Some interfaces give the snap exclusive ownership of a system-wide resource, such as a well-known D-Bus name. Others allow operations on shared hardware or kernel state that would conflict if performed by more than one instance. A snap cannot be installed as a parallel instance (unless specified with an explicit bypass flag; see {ref}`Installing an unsupported snap anyway <interfaces-parallel-installs-bypass>`) if it declares a plug or slot for one of these interfaces on an unsupported side:

| Interface | Plug supported | Slot supported |
|-----------|----------------|----------------|
| {ref}`acrn-support <interfaces-acrn-support-interface>` | No | Yes |
| {ref}`adb-support <interfaces-adb-support-interface>` | No | Yes |
| {ref}`audio-playback <interfaces-audio-playback-interface>` | Yes | No |
| {ref}`auditd-support <interfaces-auditd-support>` | No | Yes |
| {ref}`avahi-control <interfaces-avahi-control-interface>` | Yes | No |
| {ref}`avahi-observe <interfaces-avahi-observe-interface>` | Yes | No |
| {ref}`bluez <interfaces-bluez-interface>` | Yes | No |
| {ref}`checkbox-support <ref-checkbox-support-interface_checkbox-support-interface>` | No | Yes |
| {ref}`classic-support <interfaces-classic-support-interface>` | No | Yes |
| {ref}`core-support <interfaces-core-support-interface>` | No | No |
| {ref}`cuda-driver-libs <interfaces-cuda-driver-libs>` | Yes | No |
| {ref}`dbus <interfaces-dbus-interface>` | Yes | No |
| {ref}`desktop <interfaces-desktop-interface>` | Only without `desktop-file-ids` | No |
| {ref}`dm-crypt <interfaces-dm-crypt-interface>` | No | Yes |
| {ref}`docker <interfaces-docker-interface>` | Yes | No |
| {ref}`docker-support <interfaces-docker-support-interface>` | No | Yes |
| {ref}`dsp <interfaces-dsp-interface>` | No | Yes |
| {ref}`egl-driver-libs <interfaces-egl-driver-libs>` | Yes | No |
| {ref}`firmware-updater-support <ref-firmware-updater-support-interface_firmware-updater-support-interface>` | No | Yes |
| {ref}`fpga <interfaces-fpga-interface>` | No | Yes |
| {ref}`fwupd <interfaces-fwupd-interface>` | Yes | No |
| {ref}`gbm-driver-libs <ref-gbm-driver-libs-interface_gbm-driver-libs-interface>` | Yes | No |
| {ref}`greengrass-support <interfaces-greengrass-support-interface>` | No | Yes |
| {ref}`kubernetes-support <interfaces-kubernetes-support-interface>` | No | Yes |
| {ref}`location-control <interfaces-location-control-interface>` | Yes | No |
| {ref}`location-observe <interfaces-location-observe-interface>` | Yes | No |
| {ref}`lxd-support <interfaces-lxd-support-interface>` | No | Yes |
| {ref}`maliit <interfaces-maliit-interface>` | Yes | No |
| {ref}`media-hub <interfaces-media-hub-interface>` | Yes | No |
| {ref}`microceph-support <interfaces-microceph-support>` | No | Yes |
| {ref}`microstack-support <interfaces-microstack-support-interface>` | No | Yes |
| {ref}`mir <interfaces-mir-interface>` | Yes | No |
| {ref}`modem-manager <interfaces-modem-manager-interface>` | Yes | No |
| {ref}`multipass-support <interfaces-multipass-support-interface>` | No | Yes |
| {ref}`network-manager <interfaces-network-manager-interface>` | Yes | No |
| {ref}`nomad-support <interfaces-nomad-support>` | No | Yes |
| {ref}`nvidia-drivers-support <interfaces-nvidia-drivers-support-interface>` | No | Yes |
| `nvidia-video-driver-libs` | Yes | No |
| {ref}`ofono <interfaces-ofono-interface>` | Yes | No |
| {ref}`online-accounts-service <interfaces-online-accounts-service-interface>` | Yes | No |
| {ref}`opengl-driver-libs <ref-opengl-driver-libs-interface_opengl-driver-libs-interface>` | Yes | No |
| {ref}`opengles-driver-libs <ref-opengles-driver-libs-interface_opengles-driver-libs-interface>` | Yes | No |
| {ref}`openvswitch-support <interfaces-openvswitch-support-interface>` | No | Yes |
| {ref}`physical-memory-control <interfaces-physical-memory-control-interface>` | No | Yes |
| {ref}`pipewire <interfaces-pipewire-interface>` | Yes | No |
| {ref}`pkcs11 <interfaces-pkcs11>` | Yes | No |
| {ref}`posix-mq <interfaces-posix-mq-interface>` | No | No |
| {ref}`pulseaudio <interfaces-pulseaudio-interface>` | Yes | No |
| {ref}`ros-snapd-support <interfaces-ros-snapd-support>` | No | Yes |
| {ref}`shared-memory <interfaces-shared-memory-interface>` | Only with `private: true` | No |
| {ref}`steam-support <interfaces-steam-support-interface>` | No | Yes |
| {ref}`storage-framework-service <interfaces-storage-framework-service-interface>` | Yes | No |
| {ref}`thumbnailer-service <interfaces-thumbnailer-service-interface>` | Yes | No |
| {ref}`ubuntu-download-manager <interfaces-ubuntu-download-manager-interface>` | Yes | No |
| {ref}`udisks2 <interfaces-udisks2-interface>` | Yes | No |
| {ref}`unity8 <interfaces-unity8-interface>` | Yes | No |
| {ref}`unity8-calendar <interfaces-unity8-calendar-interface>` | Yes | No |
| {ref}`unity8-contacts <interfaces-unity8-contacts-interface>` | Yes | No |
| {ref}`upower-observe <interfaces-upower-observe-interface>` | Yes | No |
| `vulkan-driver-libs` | Yes | No |
| {ref}`wayland <interfaces-wayland-interface>` | Yes | No |
| {ref}`x11 <interfaces-x11-interface>` | Yes | No |
| {ref}`xilinx-dma <interfaces-xilinx-dma>` | No | Yes |

When an instance cannot be installed, the error names the plug or slot responsible and the reason, for example:

```
cannot install snap "network-manager_foo" as parallel instance: slot "service" with interface "network-manager" is not supported for parallel instances: owning a unique global resource cannot have parallel instances
```

### Unsupported app properties

A snap is unsupported as a parallel instance if any of its apps set one of the following properties in `snap.yaml`:

* `common-id`: the desktop file ID referenced by AppStream metadata is unique on the system.
* `bus-name`: the well-known D-Bus name the app claims is unique on the system.
* `activates-on`: D-Bus activation requires a `dbus` slot, which is not supported on parallel instances.

(interfaces-parallel-installs-bypass)=
### Installing an unsupported snap anyway

Users who understand and accept the risks of conflicts between instances may bypass these checks with `--allow-unsupported-instances`:

```
sudo snap install --allow-unsupported-instances <snap>_<instance-key>
```

Snapd remembers this choice for the instance, so later refreshes are not blocked.

If a refresh introduces an unsupported plug, slot or app property to an instance that is already installed and was fully supported, snapd blocks the refresh and adds a warning visible with `snap warnings`. To refresh the instance anyway, run:

```
sudo snap refresh --allow-unsupported-instances <snap>_<instance-key>
```

`--allow-unsupported-instances` can only be used with snaps installed with an instance key.

(interfaces-parallel-installs-shared-resources)=
### Interfaces that control shared system resources

Some supported interfaces grant control over a resource that is shared by the whole system, such as block devices or network ports. Each instance of a snap that uses one of these interfaces acts on the same system resource, and snapd does not coordinate between them. Before running more than one instance of a snap that uses such an interface, make sure that the instances are configured to manage different resources, or that only one instance is active at a time.

## Classic confinement

Snaps with {ref}`classic confinement <explanation-security-classic-confinement>` can be installed as parallel instances, but may require some setup on the part of the user, depending on the snap. Check the relevant snap's documentation for more details.

As mentioned in {ref}`the beginning description of parallel instances <interfaces-parallel-installs>`, for correct behavior of parallel instances of classic snaps, systems that previously did not have parallel instances enabled yet had at least one snap installed should reboot their system after updating the native package to snapd >=2.79. 

## Current limitations

There are a few limitations with parallel installs that will be addressed in subsequent `snapd` releases.

### User data and runtime locations

The user data locations are kept separate across multiple instances. Applications that hard code paths to either user data directories or the XDG runtime directory may not function correctly as the AppArmor profile has been updated to allow accessing instance specific paths only.

Applications need to use `SNAP_USER_DATA`, `SNAP_USER_COMMON` or fallback to using `HOME`.

Applications built using most popular frameworks, such as Gtk/glib or Qt, and that are already capable of observing both `HOME` and `XDG_RUNTIME_DIR`, should continue to work.

### Ports, DBus names, shared memory and socket activation

Snaps may provide APIs consumed by other snaps or the host system at some well known locations or addresses, such as DBus service names, /dev/shm objects or semaphores, abstract socket addresses. While the default AppArmor template has been updated to allow only instance specific access, connecting interfaces may allow a wider access capabilities that can lead to conflicts between instances of the same snap.

(interfaces-parallel-installs-ports)=
#### Ports

When snapd installs a snap with services, the services are automatically started. Services trying to bind to the same port may fail or function incorrectly. Such snaps should deliver means for configuration of the service via configure hooks.

A demo snap https://github.com/bboozzoo/parallel-installs-demo provides an example of reconfiguration via configure hooks.

Repeated failed starts of a service due to a port already in use can trigger systemd start-rate limiting and suppress further restarts. To avoid restart suppression:

1. Identify the service name:

  ```
  snap services <snap-instance-name>
  ```

2. Clear the failed state before applying the new port configuration:

  ```
  sudo systemctl reset-failed snap.<snap-instance-name>.<service-name>.service
  ```

3. Apply the port configuration (this restarts the service through the configure hook):

  ```
  sudo snap set <snap-instance-name> <key>=<port>
  ```

#### DBus names

Snaps that own a well-known D-Bus name, through a `dbus` slot or the `bus-name` app property, are not supported as parallel instances. See {ref}`interfaces-parallel-installs-unsupported`.

Snaps with plug-side `dbus` interface declarations are supported.

#### `/dev/shm`

The default AppArmor profile allows instance specific access only. Applications hardcoding paths can break.

The `shared-memory` interface is only supported on parallel instances for plugs with the `private` attribute set to `true`, which gives each instance its own private `/dev/shm`. Slot-side parallel installations with `shared-memory` are not supported. Note that some interfaces such as `mir` allow a wider access to `/dev/shm`. Such a snap would need to be updated to made instance aware.

#### Socket activation

Snaps can use `listen-stream` socket definitions of three kinds: a network address, or an `AF_UNIX` socket addressed by either a filesystem path or an abstract name. Each behaves differently with parallel installs:

* **Network sockets** (for example a bare `<port>`) are not adjusted for parallel installs. Instances trying to bind to the same address and port collide in the same way described above under Ports. Since the address is hard-coded, using `AF_INET`/`AF_INET6` socket activation is not recommended for snaps that want to support parallel installs.
* **`AF_UNIX` filesystem-path sockets** using `$SNAP_DATA`, `$SNAP_COMMON` or `$XDG_RUNTIME_DIR` for system daemons, or `$SNAP_USER_DATA`, `$SNAP_USER_COMMON` or `$XDG_RUNTIME_DIR` for user daemons, are automatically expanded to instance-specific locations, so the clients can use the appropriate path, for example `/var/snap/hello-world_foo/common/name.socket`.
* **`AF_UNIX` abstract sockets** must be declared with a `@snap.<snap-name>.` prefix. When generating the systemd socket unit for a snap instance, snapd automatically remaps this prefix to `@snap.<instance-name>.`, so each instance listens on its own abstract address without colliding with other instances. Clients must connect using the instance-qualified address, for example `@snap.hello-world_foo.socket` rather than `@snap.hello-world.socket`.

If, after any variable expansion or instance remapping, the resulting socket address exceeds the maximum length of 108 bytes allowed for a [Unix domain socket](https://man7.org/linux/man-pages/man7/unix.7.html) address, snapd fails to generate the socket unit and reports an error.
