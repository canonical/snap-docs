---
myst:
  html_meta:
    description: Release notes for Snapd 2.76, released on 1 July 2026. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-76)=
# Snapd 2.76

*Released on 1 July 2026.*

## Overview

This release contains the remainder of the planned 26.04 content. It includes:

* Snap delta infrastructure, laying the groundwork for smaller snap updates
* Mount namespace and layout improvements for more robust and predictable snap confinement
* Performance improvements reducing overhead during snap operations and Ubuntu Core boot
* Improved snap component visibility and reliability
* Security hardening across snap-confine
* Continued progress on features in development, including snap deltas, [confdb](https://snapcraft.io/docs/confdb-configuration-management), [AppArmor prompting](https://snapcraft.io/install/prompting-client/ubuntu), remote device management, dm-verity, security logging and openshell
* FDE (Full Disk Encryption) maintenance updates and bug fixes
* New interfaces and interface improvements
* Packaging updates for cross-distro builds and Ubuntu 26.04 (Resolute)

## Components

Snapd 2.76 contains many enhancements to the components subsystem, providing greater transparency and stability for end users. Users can discover installed components directly through `snap info` and `snap list`, while several reliability fixes improve the experience around installation, refresh, and enable/disable workflows.

* Show hint in `snap list` that a snap has components
* List snap components in `snap-debug-info` via debug-tools
* Display detailed component information in `snap info`
* Fix download of private snap components by setting UserID ([LP: #2110368](https://bugs.launchpad.net/snapd/+bug/2110368))
* Fix snap enable/disable cycle forgetting components ([LP: #2147207](https://bugs.launchpad.net/snapd/+bug/2147207))
* Ensure existing snap confinement flags are not dropped when installing or removing components
* Improve `snapctl install` consistency when components are already installed
* Fix component installation for private snaps via `snapctl` ([LP: #2110368](https://bugs.launchpad.net/snapd/+bug/2110368))

## Mount namespace and layout

The 2.76 release continues to see improvements to how the mount namespace, the world view, of a snap is constructed and updated. Starting with 2.75, a mechanism was introduced for opportunistically discarding the mount namespace whenever a snap itself or one of its dependencies is updated. This ensures that snaps always start with the most up-to-date world view. In 2.76, this effort continued, ensuring that the mount namespace construction process itself is more robust and that snap features, such as content sharing and layouts, are applied in an orderly and predictable way, while squashing a number of bugs in the area.

* snap-update-ns: switch to a multi-pass process for constructing and updating mount namespaces
* Fix mount namespace updates with synthetic bind mounts on same target paths ([LP: #2144666](https://bugs.launchpad.net/snapd/+bug/2144666))

## Performance

Snapd 2.76 includes several targeted performance improvements that reduce overhead during common snap operations and speed up boot on Ubuntu Core devices.

* Reduce the number of AppArmor profile regenerations during snap operations
* Unroll CPU-heavy recursive function in snap state handlers
* Dispatch `systemctl` commands asynchronously when calling `Stop()`
* core-initrd: increase mount burst from 5 to 128 for faster boot
* core-initrd: add nfnetlink module to fix nf netlink socket speed regression ([LP: #2150773](https://bugs.launchpad.net/snapd/+bug/2150773))

## Security hardening

Snapd 2.76 hardens the snap-confine execution environment, addressing a memory safety issue and tightening security boundaries for BPF and mount operations.

* snap-confine: fix out-of-bounds read in mountinfo parser for partial escape sequences
* snap-confine: harden bpffs mount with `nosuid`, `nodev`, `noexec` flags
* snap-confine: set `FD_CLOEXEC` on file descriptors returned by BPF helpers
* snap-confine: remove experimental persistent per-user mount namespace feature

## Features in development

The following features are under active development and included in this release as building blocks for upcoming functionality. They are not yet considered stable for general use.

* **snap deltas:** introduces internal tooling for generating and applying binary deltas between snap revisions; supports the existing `xdelta3` format and adds the new `snap-1-1-xdelta3` format with improved compression of the squashfs artefact
* **[confdb](https://snapcraft.io/docs/confdb-configuration-management):** block concurrent confdb accesses; allow only API admin read access to confdb secrets; support `--wait-for` timeouts
* **[AppArmor prompting](https://snapcraft.io/install/prompting-client/ubuntu):** re-enable the prompting notice backend; validate permissions while unmarshalling; escape paths in prompt constraints; respond with full user-allowed permission set
* **remote device management:** support remote device management with the `dispatch-mgmt-messages` task with sequencing support
* **dm-verity:** add helper for validating integrity data; copy integrity data files during snap install
* **Security audit logging:** add security audit logging subsystem
* **openshell:** allow `openshell` snap to use experimental `daemon-scope: user`

## Other

* **mounts:** ensure `/tmp/.X11-unix` created inside mount namespace has correct permissions; allow configuring mount unit options based on filesystem type; `RemoveMountUnitFile` now unmounts even if mount unit file is missing
* **interfaces:** new `podman` interface for podman socket access; `docker` plug now implicit on classic systems; bluez: drop explicit `deny send_destination` in D-Bus configuration; disallow auto-connect to parallel installs; restore auto-connections on failed refresh undo; conditionally deny `/proc/self/mountinfo` to suppress Go 1.25+ denials; support deep SoC sysfs paths for LED brightness in bool-file ([LP: #2148544](https://bugs.launchpad.net/snapd/+bug/2148544)); stricter validation for content interface plugs and layout entries now applies to snaps using bases core26 (or later) and bare. For snaps using a content interface plug, or a layout entry (bind, bind-file or tmpfs) where the target path resides under `$SNAP`, the target path's presence is now mandatory and enforced during snap installation or refresh.
* **FDE:** deprecate `check-pin`/`passphrase` API actions; move auto-repair logic to `overlord/fdestate`; update secboot for TPM/FDE bug fixes including Intel HAP and recovery key parsing; give inactive state on classic ([LP: #2147606](https://bugs.launchpad.net/snapd/+bug/2147606))
* **snap CLI:** allow removing a snap and its base at the same time; avoid empty channel forwarding message ([LP: #2125344](https://bugs.launchpad.net/snapd/+bug/2125344)); clarify `snap install` help text for `--classic` and `--devmode` ([LP: #2150683](https://bugs.launchpad.net/snapd/+bug/2150683)); print complex attributes in `snap interface --attrs` output ([LP: #2152908](https://bugs.launchpad.net/snapd/+bug/2152908))
* **packaging:** FIPS bootstrap and dispatch via `snap-fips-dispatch`; add cross-distro build script; update bundled AppArmor to 4.1.7; drop transitional packages for Ubuntu 26.04; make Ubuntu 16.04 packaging dep17 compliant ([LP: #2139213](https://bugs.launchpad.net/snapd/+bug/2139213))
* Update seccomp syscalls list for kernel 7.1.0
* Improve handling of failed downloads and retain partial files for resume ([LP: #2146337](https://bugs.launchpad.net/snapd/+bug/2146337))
* Skip redundant xdg-settings confirmation prompt when setting is already correct ([LP: #1966067](https://bugs.launchpad.net/snapd/+bug/1966067))

## Test Feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

## Changelog

* assertions: add helper for validating integrity data
* assertions: drop incorrect/non-standard Ed25519 support
* confdb: allow only API admin read access to confdb secrets
* confdb: block concurrent confdb accesses
* confdb: block concurrent snapctl accesses to configuration database
* confdb: check for ephemeral data when missing `save-view` hook on commit
* confdb: ignore not-found errors in confdb-schema refreshes
* confdb: support `--wait-for` timeouts when accessing confdb
* core-initrd: add group referenced in udev rules
* core-initrd: add libbpf dependency to initramfs
* core-initrd: add missing libbpf dependency in 24.04 packaging
* core-initrd: ensure audio is a system group
* core-initrd: fix `/boot/uboot` mount with u-boot env in dedicated partition
* core-initrd: increase mount burst from 5 to 128 for faster boot
* core-initrd: sync partition udev rules with the ones in core-base
* core-initrd: sync with latest upload to snappy-dev PPA
* core-initrd: synchronize changelogs with latest PPA upload
* core-initrd: update changelog with latest PPA upload
* LP: #2150773 core-initrd: add nfnetlink module to fix nf netlink socket speed regression (Ubuntu Core only)
* cross-distro: allow snapd to manipulate systemd unit files in SELinux policy
* cross-distro: FIPS bootstrap and dispatch via `snap-fips-dispatch`
* desktop: fix common ID selection with multiple desktop plugs
* FDE: allow user mode on core in secboot TPM handling
* FDE: bump go-efilib dependency
* FDE: bump secboot to rev cdcb64992e54 for FDE fixes
* FDE: deprecate `check-pin`/`passphrase` API endpoints
* LP: #2147606 FDE: give inactive state on classic
* FDE: improve tracing for OP-TEE probing
* FDE: move auto-repair logic to `overlord/fdestate` and provide state
* FDE: update secboot for TPM/FDE bug fixes including Intel HAP and recovery key parsing
* FDE: use any primary key matching digest when adding a keyslot
* FDE: use ignore action for preinstall check in VM
* interfaces: bluez | drop explicit `deny send_destination` in D-Bus configuration
* interfaces: conditionally deny `/proc/self/mountinfo` to suppress Go 1.25+ denials
* interfaces: custom-device | fix `for-device` validation panic on non-string value
* interfaces: disallow auto-connect to parallel installs
* interfaces: docker | make plug implicit on classic systems
* interfaces: ignore errors in disconnect hooks during explicit snap disconnect
* interfaces: mediatek-accel | add plug interface base declaration
* interfaces: microceph-support | suppress noisy sudo denial audit logs
* interfaces: podman | add new interface for podman socket access
* interfaces: pulseaudio | fix security tag syntax inconsistency
* interfaces: raw-usb | allow USB device enumeration on Fairphone 5 with NexDock
* interfaces: restore auto-connections on failed refresh undo
* LP: #2148544 interfaces: bool-file | support deep SoC sysfs paths for LED brightness
* LP: #2139213 packaging: make Ubuntu 16.04 packaging dep17 compliant
* packaging: add cross-distro build script and instructions
* packaging: add openSUSE 16.0 spread support
* packaging: Debian build improvements
* packaging: default openSUSE to `/var/lib/snapd/snap` and sync from downstream
* packaging: drop transitional packages only for Ubuntu 26.04 (Resolute)
* packaging: fix Launchpad FIPS build detection for `snapd-fips` job
* packaging: refactor and clean up `snapd.mk`, standardize test-data directories
* packaging: switch to `golang-github-chai2010-gettext-go-dev`
* packaging: update bundled AppArmor 4.1.7 (snapd snap only)
* prompting: escape paths in prompt constraints
* prompting: improve API error handling and validation
* prompting: improve error message when no handler service is present
* prompting: re-enable the prompting notice backend
* prompting: respond with full user-allowed permission set
* prompting: validate permissions while unmarshalling
* remote device management: implement `dispatch-mgmt-messages` task with sequencing support
* LP: #2125344 snap: avoid empty channel forwarding message
* LP: #2150683 snap: clarify `snap install` help text for `--classic` and `--devmode`
* LP: #2152908 snap: print complex attributes in `snap interface --attrs` output
* snap: add run-inhibit hint and inhibit info when a snap is disabled
* snap: allow removing a snap and its base at the same time
* snap: display detailed component information in `snap info`
* snap: extend `AlreadyInstalledError` to multiple snaps and components
* snap: extend `set-quota` command options description with accepted value formats
* snap: implement `snap delta` command for computing snap deltas
* snap: improve consistency for `snap install` when some snaps are already installed
* snap: show hint in `snap list` that a snap has components
* snap-confine: allow inheriting unix sockets from snaps
* snap-confine: allow linking to `libm` in AppArmor profile
* snap-confine: fix out-of-bounds read in mountinfo parser for partial escape sequences
* snap-confine: harden bpffs mount with `nosuid`, `nodev`, `noexec` flags
* snap-confine: remove experimental persistent per-user mount namespace feature
* snap-confine: set `FD_CLOEXEC` on file descriptors returned by BPF helpers
* snap-confine: support `transparent_hugepage` in AppArmor profile
* snap-confine: use `strchr` after NUL-terminating in infofile parser
* snap-update-ns: switch to a multi-pass process for constructing and updating mount namespaces
* `RemoveMountUnitFile` now unmounts even if mount unit file is missing
* Add explicit mount phase during single-reboot refresh to fix undo of kernel refreshes
* Add security audit logging subsystem
* Add base prioritized AppArmor snippets for strictly confined or jailed snaps
* Allow `openshell` snap to use experimental `daemon-scope: user`
* Allow configuring mount unit options based on filesystem type
* Allow equals signs in uevent values in netlink parser
* Also bind-mount directories modified by kmod backend during preseed
* Clean up potentially corrupted files during snap download undo
* Complete the bootloader environment implementation
* Copy integrity data files during snap install
* Create hook for seed refresh mode
* Create removal tasks for old seed-refresh seeds
* Dispatch `systemctl` commands asynchronously when calling `Stop()`
* Ensure `/tmp/.X11-unix` created inside mount namespace has correct permissions
* Ensure exclusive changes conflict with refresh/revert
* Ensure existing snap confinement flags are not dropped when installing or removing components
* Export ubuntu-boot-state filename constant from bootloader package
* Fix duplicate removal of apps under `$SNAP_MOUNT_DIR/bin`
* Fix integration between prerequisites task and seed-refresh mode
* Fix split-refresh overwriting provided lane
* Fix use of umask in `GetListener` for socket activation
* Ignore `net.ErrClosed` during daemon shutdown
* Implement `ResolveValidationSetsEnforcementError` in terms of one call
* Improve `snapctl install` consistency when components are already installed
* Inject seed creation tasks into snap refresh flow
* Introduce system options for custom certificates on Ubuntu Core
* Keep idle services with activation units stopped on reload
* List snap components in `snap-debug-info` via debug-tools
* Look at gadget.yaml instead of marker file to determine ubootpart usage
* LP: #1966067 Skip redundant xdg-settings confirmation prompt when setting is already correct
* LP: #2110368 Fix component installation for private snaps via `snapctl`
* LP: #2110368 Fix download of private snap components by setting UserID
* LP: #2144666 Fix mount namespace updates with synthetic bind mounts on same target paths
* LP: #2146337 Improve handling of failed downloads and retain partial files for resume
* LP: #2147207 Fix snap enable/disable cycle forgetting components
* Make run-inhibit hint for kill-snap-apps task based on kill reason
* Merge content-provider prerequisite updates into seed-refresh
* Move `SortServices` into `Backend.StartServices`
* Move state to client change conversion to ctlcmd package
* Omit misleading "try to refresh snapd" suggestion for ISA-related errors
* Only create `link-component` tasks when needed during refresh to existing revision
* Reconfigure piboot bootloader on gadget refreshes to preserve `os_prefix`
* Reduce the number of AppArmor profile regenerations during snap operations
* Refactor seed-refresh ownership to `devicestate`
* Regenerate certificate database on remodels
* Remove obsolete FIXME comment in `VersionCompare`
* Remove unused `GenerateDmVerityData` helper from snap/integrity
* Rename and document error type for ISA assumes flags
* Restart snapd from `daemon.Stop` to improve restart reliability
* Restart stopped services on error in `stopSnapServices` for transactionality
* Simplify certificate-db updates on model-base refresh/installs
* Support racing `Loop` and `Stop` correctly in overlord
* Support sending file descriptors to systemd via `sd_notify`
* Unroll CPU-heavy recursive function in snap state handlers
* Update seccomp syscalls list for kernel 7.1.0
* Use change ID to prevent nested seed-refresh spawned by prerequisites
* Validate content interface plug target directories exist for core26+ snaps
* Validate layout paths exist in snap tree for snaps using bare or core26+

## Snapd 2.76.1 (Security Release)

*Released on 23 July 2026.*

* CVE-2024-5300
* CVE-2026-8933
* CVE-2026-15226

## Snapd 2.76.2

*Released on 11 August 2026.*

* interfaces: steam-support, docker-support | fix mountinfo denial

## Snapd 2.76.3

*Released to candidate on 20 August 2026.*

The snapd 2.76.3 Debian packages were released to Jammy, Noble and Resolute.

### Overview

Snapd 2.76.3 delivers the final 26.04.1 content. It includes the 2.76.2 mountinfo regression fix that was previously released as a snap only. It includes:

* FDE (Full Disk Encryption) install-time passphrase/PIN support, first-boot keyboard configuration, and a requirement for volume authentication when a hardware root of trust is missing
* The 2.76.2 mountinfo regression fix for Steam and Docker snaps
* Packaging and hook-ordering fixes

### FDE

Snapd 2.76.3 completes the remaining 26.04.1 FDE objectives for install and first boot. It adds passphrase and PIN support for volume authentication, allowing installation to continue when a hardware root of trust is missing. It also adds support for applying the selected keyboard layout on first boot so Plymouth uses the correct layout before snapd is running.

### Other

* Cross-distro: modify SELinux policy to use `init_named_socket_activation()` for allowing systemd to start snapd through socket activation; packaging: make sure that `usr/bin/snap` is built with correct build tags on debian sid
* Ensure profiles are set up before running `prepare-{slot,plug}*` hooks

### Test feedback

Feel free to provide your test feedback here or directly in Launchpad. To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

### Changelog

* FDE: support keyboard configuration at install-time for first-boot
* FDE: re-enable passphrases/PINs at install-time
* FDE: require volumes authentication if HWROT is missing
* FDE: bump secboot to rev 457b03a16d19
* FDE: use new secboot API for reprovision TPM
* Cross-distro: modify SELinux policy to use init_named_socket_activation() for allowing systemd to start snapd through socket activation
* packaging: make sure that usr/bin/snap is built with correct build tags on debian sid
* Ensure profiles are setup before running prepare-{slot, plug}* hooks
