---
myst:
  html_meta:
    description: Release notes for Snapd 2.63, released on 23 May 2024. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-63)=
# Snapd 2.63

*Released on 23 May 2024.*

Snap-based [Ubuntu Core](https://ubuntu.com/core) devices will benefit from many of our the features for this release, including support for [Offline remodelling](https://documentation.ubuntu.com/core/explanation/remodeling/#offline-remodeling), the use of {ref}`Validation sets <explanation-how-snaps-work-validation-sets>` in the [model assertion](https://ubuntu.com/core/docs/reference/assertions/model) and setting a custom port for SSH.

There’s also a new `snap sign` [`--chain`](https://documentation.ubuntu.com/core/how-to-guides/manage-ubuntu-core/add-a-system-user/#generating-auto-import-assert) argument in this release, that can be used to aggregate all the assertions required to create a new system user.

## Changelog

* Support for snap services to show the current status of user services (experimental)
* Refresh app awareness: record snap-run-inhibit notice when starting app from snap that is busy with refresh (experimental)
* Refresh app awareness: use warnings as fallback for desktop notifications (experimental)
* Aspect based configuration: make request fields in the aspect-bundle's rules optional (experimental)
* Aspect based configuration: make map keys conform to the same format as path sub-keys (experimental)
* Aspect based configuration: make unset and set behaviour similar to configuration options (experimental)
* Aspect based configuration: limit nesting level for setting value (experimental)
* Components: use symlinks to point active snap component revisions
* Components: add model assertion support for components
* Components: fix to ensure local component installation always gets a new revision number
* Add basic support for a CIFS remote filesystem-based home directory
* Add support for AppArmor profile kill mode to avoid snap-confine error
* Allow more than one interface to grant access to the same API endpoint or notice type
* Allow all snapd service's control group processes to send systemd notifications to prevent warnings flooding the log
* Enable not preseeded single boot install
* Update secboot to handle new `sbatlevel`
* Fix to not use cgroup for non-strict confined snaps (devmode, classic)
* Fix two race conditions relating to freedesktop notifications
* Fix missing tunables in snap-update-ns AppArmor template
* Fix rejection of snapd snap udev command line by older host snap-device-helper
* Rework seccomp allow/deny list
* Clean up files removed by gadgets
* Remove non-viable boot chains to avoid secboot failure
* posix_mq interface: add support for missing time64 `mqueue` syscalls mq_timedreceive_time64 and mq_timedsend_time64
* password-manager-service interface: allow `kwalletd` version 6
* kubernetes-support interface: allow SOCK_SEQPACKET sockets
* system-observe interface: allow listing systemd units and their properties
* opengl interface: enable use of nvidia container toolkit CDI config generation
