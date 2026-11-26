---
myst:
  html_meta:
    description: Release notes for Snapd 2.34.3, announced on 8 August 2018. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-34-3)=
# Snapd 2.34.3

* **Interface connection via gadget** ([topic](https://forum.snapcraft.io/t/1431)): This allows defining interface connections on the gadget snap so that on first boot the given plugs and slots get connected.
* **New interfaces**: New `dvb` interface ([topic](https://forum.snapcraft.io/t/3497)), `can-bus` interface, and new `{contacts,calendar}-service` interfaces are now available.
* **New system configuration**: A new system config option to configure the hardware watchdog on Ubuntu Core ([topic](https://forum.snapcraft.io/t/5695)). A new option to disable/enable IPv6 on the system is also available via `snap set system network.disable-ipv6`.
