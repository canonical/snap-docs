---
myst:
  html_meta:
    description: Release notes for Snapd 2.74, whose changes were released as 2.74.1 on 19 March 2026. Read about selected updates and fixes.
---

(release-notes_snapd-2-74)=
# Snapd 2.74

*Not released, superseded by 2.74.1*

* FDE: use new activation API from secboot
* FDE: use activation API also with non keydata keys
* FDE: ignore internal recovery key expiration during install
* FDE: support adding/removing PINs post-installation
* FDE: support changing PINs post-installation
* FDE: support adding a recovery key post-installation
* FDE: provide activation status via new endpoint v2/system-info/storage-encrypted
* FDE: support sealing and resealing using the preinstall check result
* FDE: disable passphrase support during install
* FDE: add keyboard configuration helpers
* FDE: lazily inject keyboard layout configuration in kernel cmdline
* FDE: enable pin tries and limits PIN entry attempts to 3
* FDE: extend secureboot endpoint to accept DB, KEK, and PK
* FDE: simplify /v2/system-volumes keyslots handling by allowing name-only entries, implicitly expanding to all system containers
* FDE: support extra non-system key slot names to support agents such as Landscape to set dedicated recovery keys
* FDE: initialize fde state after device state
* FDE: use device node to find the storage container and keys
* FDE: provide user visible name for disk based on ID_MODEL
* FDE: update secboot in snapd with latest additions and fixes
* core-initrd: add systemd service for setting plymouth keyboard layout and X11 keyboard layouts
* core-initrd: set plymouth cleartext toggle option
* core-initrd: fix plymouth missing font issue
* core-initrd: update dependency from libteec1 to libteec2
* core-initrd: add new dlopened libs
* LP: #2116949 Preseeding: add support for preseeding of hybrid systems via the installer API$
* Preseeding: check whether a path is a mount point before remounting
* Confdb: support tagging paths as secret in storage schemas
* Confdb: support filtering on placeholder sub-keys
* Confdb: support filtering in API and confdbstate
* Confdb: support field filtering on reads
* Confdb: support "parameters" stanza and check filters against them
* Confdb: add support for '--with' constraints
* Confdb: parsing fixes and error handling improvements
* Assertions: restrict serials to new format in confdb-control
* Assertions: add verify signature function
* Remote device management: modify request-message assertion to expose its time constraints for remote device management
* Remote device management: support polling of store messages
* Remote device management: add signing of response messages with device key
* Prompting: enable notify protocol v5 and test prompt restoration after snapd restart
* snap: change malformed '--channel=' warning to error
* snap: add 'snap report-issue' command to get the available contact details for the specified snap
* snap: add 'snap version --verbose' flag to include information on snap binaries origin
* snap: create the XDG_RUNTIME_DIR folder
* LP: #2068493 snap: add support for 'snap refresh --tracking'
* snapctl: add '--tracking' flag to 'snapctl refresh'
* Reexec: include the info filepath in the version compare debug log
* Reexec: add support for forcing reexec into and older snapd snap by setting SNAP_REEXEC=force in the environment
* snap-confine: correct error message related to snap-confine group policy validation
* snap-confine: ensure we only mount existing directories
* LP: #2134364 snap-confine: handle potential race when creating /tmp/snap-private-tmp when lacking systemd-tmpfiles support
* snap-confine: filter plus characters from security tags
* Desktop: use desktop file IDs as desktop IDs
* Desktop: store the common ID in the desktop file
* Desktop: allow graphical daemons to show icons in the dock
* Desktop: change user daemons with desktop plug defined to depend on graphical-session.target
* dm-verity for essential snaps: made change to prerequisite struct
* Cross-distro: modify SELinux profile to allow connecting to squid proxy
* Cross-distro: add support for migrating snap mount directory
* Packaging: drop ubuntu-14.04 packaging
* Packaging: drop ubuntu-{14.04,16.04} transitional binary packages
* Packaging: remove desktop files and state lock file during snapd purge
* Packaging: fix inhibition hint file being left behind on failed unlink-current-snap
* Disallow timeouts < 1us in systemd units
* Add snap-store to the user-daemons support overrides
* Support for `SuccessExitStatus=` generation for systemd daemon
* Make standby output more verbose
* Add prepare-serial-request hook
* Try to discard snap mount namespaces when no processes are running during snap updates
* Improve handling of snap downloads cache by introducing periodic cleanup with more aggressive policy
* Interfaces: mediatek-accel | create new interface
* Interfaces: nvidia-video-driver-libs | create new interface
* Interfaces: *-driver-libs | accept component paths
* Interfaces: desktop-legacy, unity7 | remove workaround for slash filtering in ibus address
* Interfaces: fwupd | allow writing reboot notification in /run
* Interfaces: add 'install' coreutils to base AppArmor template
* Interfaces: u2f-devices | add apparmor permissions to allow the use of the libfido2 library in snaps
* Interfaces: u2f-devices | add support for Thetis security key
* Interfaces: add AppArmor workaround for mmap MAP_HUGETLB
* Interfaces: timeserver-control | manage per-link ntp settings via systemd-networkd

## Snapd 2.74.1

*Released on 19 March 2026.*

### Overview

Snapd 2.74.1 delivers TPM-backed Full Disk Encryption (FDE) to Resolute (26.04). It includes the content of 2.74, which was not released.

* Delivers TPM-backed full-disk encryption (FDE) with support for third-party NVIDIA kernel modules in Resolute for Classic Hybrid systems (Classic Ubuntu with Kernel and Gadget snaps)
* Bug fixes and robustness improvements
* Interface additions supporting new and emerging use cases
* Additions for other work-in-progress features, including:
  * [Confdb](https://snapcraft.io/docs/confdb-configuration-management) and related remote device-management capabilities
  * [AppArmor prompting](https://snapcraft.io/install/prompting-client/ubuntu) for camera access

### Notable updates

* FDE: reuse preinstall check context during install to account for user-ignored errors ([LP: #2141328](https://bugs.launchpad.net/snapd/+bug/2141328))
* FDE: fix db updates by allowing multiple payloads ([LP: #2139611](https://bugs.launchpad.net/snapd/+bug/2139611))
* snap-confine: add CAP_SYS_RESOURCE to allow raising memory lock limit when required ([LP: #2139300](https://bugs.launchpad.net/snapd/+bug/2139300))
* snap-confine: bump the max element count of the BPF map used to store IDs of allowed/matched devices to 1000 ([LP: #2139099](https://bugs.launchpad.net/snapd/+bug/2139099))
* Desktop: revert change that caused user daemons declaring the desktop plug to implicitly depend on graphical-session.target ([LP: #2141607](https://bugs.launchpad.net/snapd/+bug/2141607))
* Preseeding: add support for preseeding of hybrid systems via the installer API ([LP: #2116949](https://bugs.launchpad.net/ubuntu/+source/snapd/+bug/2116949))
* snap: add support for `snap refresh --tracking` ([LP: #2068493](https://bugs.launchpad.net/snapd/+bug/2068493))
* snap-confine: handle potential race when creating /tmp/snap-private-tmp when lacking systemd-tmpfiles support ([LP: #2134364](https://bugs.launchpad.net/snapd/+bug/2134364))

For an overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146). You are welcome to try it out for yourself using the [Resolute Daily Installer Image](https://cdimage.ubuntu.com/daily-live/current/resolute-desktop-amd64.iso).

### Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

### Changelog

* FDE: measure DeployedMode and AuditMode variables if they appear as disabled in the event log to avoid a potential reseal-failure boot loop
* LP: #2141328 FDE: reuse preinstall check context during install to account for user-ignored errors
* LP: #2139611 FDE: fix db updates by allowing multiple payloads
* LP: #2139300 snap-confine: add CAP_SYS_RESOURCE to allow raising memory lock limit when required
* LP: #2139099 snap-confine: bump the max element count of the BPF map used to store IDs of allowed/matched devices to 1000
* LP: #2141607 Desktop: revert change that caused user daemons declaring the desktop plug to implicitly depend on graphical-session.target
* Interfaces: Added pidfd_open and memfd_secret to seccomp template
* Interfaces: camera | add locking permission for /dev/video
