---
myst:
  html_meta:
    description: Release notes for Snapd 2.73, released on 9 January 2026. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-73)=
# Snapd 2.73

*Released on 9 January 2026.*

## Overview
Snapd 2.73 does not introduce new user-facing features. Instead, it provides:

* Bug fixes and robustness improvements
* Interface additions supporting new and emerging use cases
* Building blocks for several work-in-progress features, including:
  * [TPM-backed Full Disk Encryption](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146) (FDE)
  * [Confdb](https://snapcraft.io/docs/confdb-configuration-management) and related remote device-management capabilities
  * [AppArmor prompting](https://snapcraft.io/install/prompting-client/ubuntu) for camera access

These changes are intended to improve reliability today while preparing the ground for upcoming releases.

## Notable updates

* FDE: On Ubuntu Core systems using UEFI ≥ 2.5, when Deployed Mode is disabled, both AuditMode and DeployedMode are now measured and must be permitted to ensure that autorepair continues to function correctly.
* Fix scenario where multiple snaps refreshed together skips refresh control
* Prevent disabling base snaps to ensure dependent snaps can be removed
* Protect the per-snap tmp directory against being reaped by age
* Avoid race between store download stream and cache cleanup executing in parallel when invoked by `snap download`
* Use "current" instead of revision number for icons ([LP: #1851490](https://bugs.launchpad.net/snapd/+bug/1851490))
* Add `snapctl version` command ([LP: #2121853](https://bugs.launchpad.net/snapd/+bug/2121853))
* Ensure no more than one partition on disk can match a gadget partition ([LP: #2127214](https://bugs.launchpad.net/snapd/+bug/2127214))
* Prompting: Do not record notices for unchanged rules on snapd startup ([LP: #2127189](https://bugs.launchpad.net/snapd/+bug/2127189))
* snap-confine: Update AppArmor profile to allow read/write to journal as workaround for snap-confine fd inheritance prevented by newer AppArmor ([LP: #2127244](https://bugs.launchpad.net/snapd/+bug/2127244))

For an overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146)

## Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

## Changelog

* FDE: do not save incomplete FDE state when resealing was skipped
* FDE: warn of inconsistent primary or policy counter
* Confdb: document confdb in snapctl help messages
* Confdb: only confdb hooks wait if snaps are disabled
* Confdb: relax confdb change conflict checks
* Confdb: remove empty parent when removing last leaf
* Confdb: support parsing field filters
* Confdb: wrap confdb write values under "values" key
* dm-verity for essential snaps: add new naming convention for verity files
* dm-verity for essential snaps: add snap integrity discovery
* dm-verity for essential snaps: fix verity salt calculation
* Assertions: add hardware identity assertion
* Assertions: add integrity stanza in snap resources revisions
* Assertions: add request message assertion required for remote device management
* Assertions: add response-message assertion for secure remote device management
* Assertions: expose WithStackedBackstore in RODatabase
* Packaging: cross-distro | install upstream NEWS file into relevant snapd package doc directory
* Packaging: cross-distro | tweak how the blocks injecting $SNAP_MOUNT_DIR/bin are generated as required for openSUSE
* Packaging: remove deprecated snap-gdb-shim and all references now that snap run --gdb is unsupported and replaced by --gdbserver
* Preseed: call systemd-tmpfiles instead handle-writable-paths on uc26
* Preseed: do not remove the /snap dir but rather all its contents during reset
* snap-confine: attach name derived from security tag to BPF maps and programs
* snap-confine: ensure permitted capabilities match expectation
* snap-confine: fix cached snap-confine profile cleanup to report the correct error instead of masking backend setup failures
* snap-confine: Improve validation of user controlled paths
* snap-confine: tighten snap cgroup checks to ensure a snap cannot start another snap in the same cgroup, preventing incorrect device-filter installation
* core-initrd: add 26.04 ubuntu-core-initramfs package
* core-initrd: add missing order dependency for setting default system files
* core-initrd: avoid scanning loop and mmc boot partitions as the boot disk won't be any of these
* core-initrd: make cpio a Depends and remove from Build-Depends
* core-initrd: start plymouth sooner and reload when gadget is available
* Cross-distro: modify syscheck to account for differences in openSUSE 16.0+
* Validation sets: use in-flight validation sets when calling 'snapctl install' from hook
* Prompting: enable prompting for the camera interface
* Prompting: remove polkit authentication when modifying/deleting prompting rules
* LP: #2127189 Prompting: do not record notices for unchanged rules on snapd startup
* AppArmor: add free and pidof to the template
* AppArmor: adjust interfaces/profiles to cope with coreutils paths
* Interfaces: add support for compatibility expressions
* Interfaces: checkbox-support | complete overhaul
* Interfaces: define vulkan-driver-libs, cuda-driver-libs, egl-driver-libs, gbm-driver-libs, opengl-driver-libs, and opengles-driver-libs
* Interfaces: allow snaps on classic access to nvidia graphics libraries exported by *-driver-libs interfaces
* Interfaces: fwupd | broaden access to /boot/efi/EFI
* Interfaces: gsettings | set dconf-service as profile for ca.desrt.dconf.Writer
* Interfaces: iscsi-initiator, dm-multipath, nvme-control | add new interfaces
* Interfaces: opengl | grant read/write permission to /run/nvidia-persistenced/socket
* interfaces: ros-snapd-support | add access to /v2/changes/
* Interfaces: system-observe | read access to btrfs/ext4/zfs filesystem information
* Interfaces: system-trace | allow /sys/kernel/tracing/** rw
* Interfaces: usb-gadget | add support for ffs mounts in attributes
* Add autocompletion to run command
* Introduce option for disallowing auto-connection of a specific interface
* Only log errors for user service operations performed as a part of snap removal
* Patch snap names in service requests for parallel installed snaps
* Simplify traits for eMMC special partitions
* Strip apparmor_parser from debug symbols shrinking snapd size by ~3MB
* Fix InstallPathMany skipping refresh control
* Fix waiting for GDB helper to stop before attaching gdbserver
* Protect the per-snap tmp directory against being reaped by age
* Prevent disabling base snaps to ensure dependent snaps can be removed
* Modify API endpoint /v2/logs to reject n <= 0 (except for special case -1 meaning all)
* Avoid potential deadlock when task is injected after the change was aborted
* Avoid race between store download stream and cache cleanup executing in parallel when invoked by snap download task
* LP: #1851490 Use "current" instead of revision number for icons
* LP: #2121853 Add snapctl version command
* LP: #2127214 Ensure no more than one partition on disk can match a gadget partition
* LP: #2127244 snap-confine: update AppArmor profile to allow read/write to journal as workaround for snap-confine fd inheritance prevented by newer AppArmor  
* LP: #2127766 Add new tracing mechanism with independently running strace and shim synchronization
