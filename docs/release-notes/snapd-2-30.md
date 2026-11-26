---
myst:
  html_meta:
    description: Release notes for Snapd 2.30, announced stable on 5 January 2018. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-30)=
# Snapd 2.30

* **Service control on snapctl (start/stop/etc)** ([topic](https://forum.snapcraft.io/t/1908)): Allows a snap to control its services from inside a hook. This is useful, for example, to restart a service in the configure hook when a configuration item has changed.
* **Support for socket activation** ([topic](https://forum.snapcraft.io/t/2050)): Some daemons use systemd's "socket activation" feature, where the daemon is started on demand when a socket is connected to. This is now supported via the new `snapcraft.yaml` `sockets:` key.
* **Pre-refresh hook support** ([topic](https://forum.snapcraft.io/t/478)): Provides a way for a snap to do things before it is refreshed, such as storing state before a refresh.
* **Allow configuring core before it is installed**: Allows setting, for example, a proxy for snapd even before the core snap is installed.
* **Run configuration of core internally**: The code to configure core moved from an external script to internal Go code, allowing better and earlier error checking and making things faster.
* **Support for Nvidia Vulkan/32-bit NVIDIA drivers**.

Complete details are available in the [project's commit history](https://github.com/snapcore/snapd/commits/release/2.30).
