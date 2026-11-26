---
myst:
  html_meta:
    description: Release notes for Snapd 2.61, released on 3 January 2024. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-61)=
# Snapd 2.61

*Released on 3 January 2024.*

This release included a lot of background work that will later be used by `confdb` (see Snapd 2.66), to help with  cross-snap configuration. This includes new rules for parsing assertions and a per-aspect field, plus a vital new ability to unset values from the command line.

We also got closer to finishing our opt-in AppArmor prompting support , with some important background improvements, and created a specification for the desktop user-experience flow. Our cross-distribution support also improved with this release, with a new repository and packages for Amazon Linux , and snapd 2.61.1 releases for Debian Sid and Fedora 38, 39, Rawhide and EPEL 7, 8 and 9.

## Snapd 2.61.1

*Released on 03 Jan 2024.*

* Stop requiring default provider snaps on image building and first boot if alternative providers are included and available
* Fix auth.json access for login as non-root group ID
* Fix incorrect remodelling conflict when changing track to older snapd version
* Improved check-rerefresh message
* Fix UC16/18 kernel/gadget update failure due volume mismatch with installed disk
* Stop auto-import of assertions during install modes
* Desktop interface exposes GetIdletime
* Polkit interface support for new polkit versions
* Fix not applying snapd snap changes in tracked channel when remodelling
* Fix control of activated services in 'snap start' and 'snap stop'
* Correctly reflect activated services in 'snap services'
* Disabled services are no longer enabled again when snap is refreshed
* Interfaces/builtin: added support for Token2 U2F keys
* Interfaces/u2f-devices: add Swissbit iShield Key
* Interfaces/builtin: update gpio apparmor to match pattern that contains multiple subdirectories under /sys/devices/platform
* Interfaces: add a polkit-agent interface
* Interfaces: add pcscd interface
* Kernel command-line can now be edited in the gadget.yaml
* Only track validation-sets in run-mode, fixes validation-set issues on first boot
* Added support for using store.access to disable access to snap store
* Support for fat16 partition in gadget
* Pre-seed authority delegation is now possible
* Support new system-user name *daemon*
* Several bug fixes and improvements around remodelling
* Offline remodelling support

## Snapd 2.61.2

*Released on 4 Mar 2024.*

* Fix to enable plug/slot sanitization for prepare-image
* Fix panic when device-service.access=offline
* Support offline remodeling
* Allow offline update only remodels without serial
* Fail early when remodeling to old model revision
* Fix to enable plug/slot sanitization for validate-seed
* Allow removal of core snap on classic systems
* Fix network-control interface denial for file lock on /run/netns
* Add well-known core24 snap-id
* Fix remodel snap installation order
* Prevent remodeling from UC18+ to UC16
* Fix cups auto-connect on classic with cups snap installed
* u2f-devices interface support for GoTrust Idem Key with USB-C
* Fix to restore services after unlink failure
* Add libcudnn.so to Nvidia libraries
* Fix skipping base snap download due to false snapd downgrade conflict
