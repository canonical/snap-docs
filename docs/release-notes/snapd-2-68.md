---
myst:
  html_meta:
    description: Release notes for Snapd 2.68, released as 2.68.4 on 28 April 2025. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-68)=
# Snapd 2.68

The official release for this version was Snapd 2.68.4.

## Highlights

* [FDE](https://ubuntu.com/core/docs/full-disk-encryption): Add support for a new and more extensible key format and passphrases for encrypted partitions can now be specified during installation
* {ref}`Components <how-to-guides-manage-snaps-using-components>`: Support online/offline [remodeling](https://ubuntu.com/core/docs/remodelling) and the creation of new recovery systems for models that contain components, on Ubuntu Core as well as Hybrid systems. Components are useful for distributing optional resources for a snap, such as debug symbols alongside snap binaries, and kernel modules alongside a kernel snap.
* [Kernel Components](https://documentation.ubuntu.com/snapcraft/stable/reference/components/): Make kernel components and modules available in early boot
* Interfaces: Added {ref}`auditd-support interface <interfaces-auditd-support>` that allows a snap to ship auditd as part of a snap and `checkbox-support` interface that allows unrestricted access to devices when testing with checkbox

## Notable updates
* Fix issue preventing hybrid systems from being seeded on first boot
* Modify AppArmor template to allow using setpriv to run ([LP: #2072987](https://bugs.launchpad.net/snapd/+bug/2072987))
* Disable udev backend when inside a container ([LP: #1712808](https://bugs.launchpad.net/snapd/+bug/1712808))
* Remove auto-import udev rules not required by deb package to avoid unwanted syslog errors ([LP: #1966203](https://bugs.launchpad.net/snapd/+bug/1966203))
* Fix progress reporting when stdout is on a tty, but stdin is not ([LP: #1886414](https://bugs.launchpad.net/ubuntu/+source/chromium-browser/+bug/1886414))

## Experimental Features
* Removed stale `robust-mount-namespace-updates` experimental flag
* Removed rejected `snapd-snap` experimental feature and its feature flag

## Impact on Ubuntu Core using Full Disk Encryption

If you are planning to test or use this snapd release and you are using full disk encryption (with both hooks and TPM), some updates to your kernel snap are needed:
* If you maintain your own kernel snap, you will need to include the new snap-bootstrap.
* If you are using a kernel snap maintained by Canonical, all our kernel snaps will be updated to the new version of snap-bootstrap in due course.

Until all kernel snaps are updated, snapd from latest/edge cannot be used for installation or remodeling if you are using FDE. If you have not updated the kernel snap, do not report bugs you encountered when:
* Remodeling with a snapd from latest/edge, then doing factory reset.
* Installing fresh images with snapd from latest/edge

## Changelog

* FDE: add support for new and more extensible key format that is unified between TPM and FDE hook
* FDE: add support for adding passphrases during installation
* FDE: update secboot to 30317622bbbc
* Snap components: make kernel components available on firstboot after either initramfs or ephemeral rootfs style install
* Snap components: mount drivers tree from initramfs so kernel modules are available in early boot stages
* Snap components: support remodeling to models that contain components
* Snap components: support offline remodeling to models that contain components
* Snap components: support creating new recovery systems with components
* Snap components: support downloading components with 'snap download' command
* Snap components: support sideloading asserted components
* AppArmor Prompting(experimental): improve version checks and handling of listener notification protocol for communication with kernel AppArmor
* AppArmor Prompting(experimental): make prompt replies idempotent, and have at most one rule for any given path pattern, with potentially mixed outcomes and lifespans
* AppArmor Prompting(experimental): timeout unresolved prompts after a period of client inactivity
* AppArmor Prompting(experimental): return an error if a patch request to the API would result in a rule without any permissions
* AppArmor Prompting(experimental): warn if there is no prompting client present but prompting is enabled, or if a prompting-related error occurs during snapd startup
* AppArmor Prompting(experimental): do not log error when converting empty permissions to AppArmor permissions
* Confdb(experimental): rename registries to confdbs (including API /v2/registries => /v2/confdb)
* Confdb(experimental): support marking confdb schemas as ephemeral
* Confdb(experimental): add confdb-control assertion and feature flag
* Refresh App Awareness(experimental): LP: #2089195 prevent possibility of incorrect notification that snap will quit and update
* Confidential VMs: snap-bootstrap support for loading partition information from a manifest file for cloudimg-rootfs mode
* Confidential VMs: snap-bootstrap support for setting up cloudimg-rootfs as an overlayfs with integrity protection
* dm-verity for essential snaps: add support for snap-integrity assertion
* Interfaces: modify AppArmor template to allow owner read on @{PROC}/@{pid}/fdinfo/*
* Interfaces: [LP: #2072987](https://bugs.launchpad.net/snapd/+bug/2072987) modify AppArmor template to allow using setpriv to run daemon as non-root user
* Interfaces: add configfiles backend that ensures the state of configuration files in the filesystem
* Interfaces: add ldconfig backend that exposes libraries coming from snaps to either the rootfs or to other snaps
* Interfaces: [LP: #1712808](https://bugs.launchpad.net/snapd/+bug/1712808) [LP: 1865503](https://bugs.launchpad.net/snapd/+bug/1865503) disable udev backend when inside a container
* Interfaces: add auditd-support interface that grants audit_control capability and required paths for auditd to function
* Interfaces: add checkbox-support interface that allows unrestricted access to all devices
* Interfaces: fwupd | allow access to dell bios recovery
* Interfaces: fwupd | allow access to shim and fallback shim
* Interfaces: mount-control | add mount option validator to detect mount option conflicts early
* Interfaces: cpu-control | add read access to /sys/kernel/irq/<IRQ>
* Interfaces: locale-control | changed to be implicit on Ubuntu Core Desktop
* Interfaces: microstack-support | support for utilizing of AMD SEV capabilities
* Interfaces: u2f | added missing OneSpan device product IDs
* Interfaces: auditd-support | grant seccomp setpriority
* Interfaces: opengl interface | enable parsing of nvidia driver information files
* Interfaces:  [LP: #2095009](https://bugs.launchpad.net/stuttgart/+bug/2095009) mount-control interface | add CIFS support
* Allow mksquashfs 'xattrs' when packing snap types os, core, base and snapd as part of work to support non-root snap-confine
* Upstream/downstream packaging changes and build updates
* Improve error logs for malformed desktop files to also show which desktop file is at fault
* Provide more precise error message when overriding channels with grade during seed creation
* Expose 'snap prepare-image' validation parameter
* Add snap-seccomp 'dump' command that dumps the filter rules from a compiled profile
* Add fallback release info location /etc/initrd-release
* Added core-initrd to snapd repo and fixed issues with ubuntu-core-initramfs deb builds
* Remove stale robust-mount-namespace-updates experimental feature flag
* Remove snapd-snap experimental feature (rejected) and it's feature flag
* Changed snap-bootstrap to mount base directly on /sysroot
* Mount ubuntu-seed mounted as no-{suid,exec,dev}
* Mapping volumes to disks: add support for volume-assignments in gadget
* Fix silently broken binaries produced by distro patchelf 0.14.3 by using locally build patchelf 0.18
* Fix mismatch between listed refresh candidates and actual refresh due to outdated validation sets
* Fix 'snap get' to produce compact listing for tty
* Fix missing store-url by keeping it as part of auxiliary store info
* Fix snap-confine attempting to retrieve device cgroup setup inside container where it is not available
* Fix 'snap set' and 'snap get' panic on empty strings with early error checking
* Fix logger debug entries to show correct caller and file information
* Fix issue preventing hybrid systems from being seeded on first boot
* [LP: #1966203](https://bugs.launchpad.net/snapd/+bug/1966203) remove auto-import udev rules not required by deb package to avoid unwanted syslog errors
* [LP: #1886414](https://bugs.launchpad.net/ubuntu/+source/chromium-browser/+bug/1886414) fix progress reporting when stdout is on a tty, but stdin is nots

## Snapd 2.68.1

*Released to beta on 24 February 2025.*

* Fix snap-confine type specifier type mismatch on armhf

## Snapd 2.68.2

*Released to candidate on 12 March 2025.*

* FDE: use boot mode for FDE hooks
* FDE: add snap-bootstrap compatibility check to prevent image~19 March 2025 creation with incompatible snapd and kernel snap
* FDE: add argon2 out-of-process KDF support
* FDE: have separate mutex for the sections writing a fresh modeenv
* FDE: [LP: #2099709](https://bugs.launchpad.net/snapd/+bug/2099709) update secboot to e07f4ae48e98
* Confdb: support pruning ephemeral data and process alternative types in order
* core-initrd: look at env to mount directly to /sysroot
* core-initrd: prepare for Plucky build and split out 24.10 (Oracular)
* Fix missing primed packages in snapd snap manifest
* Interfaces: posix-mq | fix incorrect clobbering of global variable and make interface more precise
* Interfaces: opengl | add more kernel fusion driver files

## Snapd 2.68.3

*Released to candidate on 29 March 2025.*

### Highlights

* [FDE](https://ubuntu.com/core/docs/full-disk-encryption): Add support for a new and more extensible key format and passphrases for encrypted partitions can now be specified during installation.
* [Components](https://snapcraft.io/docs/components): Support online/offline [remodeling](https://ubuntu.com/core/docs/remodelling) and the creation of new recovery systems for models that contain components, on Ubuntu Core as well as Hybrid systems. Components are useful for distributing optional resources for a snap, such as debug symbols alongside snap binaries, and kernel modules alongside a kernel snap.
* [Kernel Components](https://canonical-snapcraft.readthedocs-hosted.com/en/stable/reference/components.html): Make kernel components and modules available in early boot.
* Interfaces: Added the [auditd-support interface](https://snapcraft.io/docs/auditd-support-interface), which allows a snap to ship auditd as part of a snap, and the `checkbox-support` interface, which allows unrestricted access to devices when testing with checkbox.

### Notable updates

* Fix issue preventing hybrid systems from being seeded on first boot
* Modify AppArmor template to allow using setpriv to run ([LP: #2072987](https://bugs.launchpad.net/snapd/+bug/2072987))
* Disable udev backend when inside a container ([LP: #1712808](https://bugs.launchpad.net/snapd/+bug/1712808))
* Remove auto-import udev rules not required by the deb package to avoid unwanted syslog errors ([LP: #1966203](https://bugs.launchpad.net/snapd/+bug/1966203))
* Fix progress reporting when stdout is on a tty, but stdin is not ([LP: #1886414](https://bugs.launchpad.net/ubuntu/+source/chromium-browser/+bug/1886414))

### Experimental features

* Removed the stale `robust-mount-namespace-updates` experimental flag
* Removed the rejected `snapd-snap` experimental feature and its feature flag

### Impact on Ubuntu Core using Full Disk Encryption

If you are planning to test or use this snapd release and you are using full disk encryption (with both hooks and TPM), some updates to your kernel snap are needed:

* If you maintain your own kernel snap, you will need to include the new snap-bootstrap.
* If you are using a kernel snap maintained by Canonical, all Canonical kernel snaps will be updated to the new version of snap-bootstrap in due course.

Until all kernel snaps are updated, snapd from latest/edge cannot be used for installation or remodeling if you are using FDE. If you have not updated the kernel snap, do not report bugs you encountered when:
* Remodeling with a snapd from latest/edge, then doing factory reset.
* Installing fresh images with snapd from latest/edge

However, please do report bugs if you find issues when:
* You updated to snapd to the latest/edge.
* You reverted from a snapd coming from latest/edge.

### Changelog

* FDE: [LP: #2101834](https://bugs.launchpad.net/snapd/+bug/2101834) snapd 2.68+ and snap-bootstrap <2.68 fallback to old keyring path
* Fix Plucky snapd deb build issue related to /var/lib/snapd/void permissions
* Fix snapd deb build complaint about ifneq with extra bracket

## Snapd 2.68.4

*Released on 28 April 2025.*

The release process for snapd 2.68.4 took significant time to stabilize. This update was prompted by a mistake in classic 24.XX models that required a workaround in snapd.

This release includes the exact content of snapd 2.68.3, along with a couple of additional changes:

* Workaround for classic 24.04/24.10 models that incorrectly specify core22 instead of core24 ([LP: #2072987](https://bugs.launchpad.net/snapd/+bug/2072987))
* Updated build dependencies

During the 2.68.4 rollout, Ubuntu Core 24 images built with Snapd 2.68.4 and the then-current 24/stable `pc-kernel` would not function correctly until kernel version 6.8.0-58.60+1 was promoted to the stable channel. See the [original release notice](https://forum.snapcraft.io/t/snapd-2-68-4-release-update/46738/4) for the rollout context.

### Changelog

* Snap components: [LP: #2104933](https://bugs.launchpad.net/snapd/+bug/2104933) workaround for classic 24.04/24.10 models that incorrectly specify core22 instead of core24
* Update build dependencies

## Snapd 2.68.5

*Released on 17 June 2025.*

Snapd 2.68.5 addresses an issue where preseed files may be missing when running inside a container ([LP: #2109843](https://bugs.launchpad.net/snapd/+bug/2109843)).

### Changelog

* [LP: #2109843](https://bugs.launchpad.net/snapd/+bug/2109843) fix missing preseed files when running in a container
