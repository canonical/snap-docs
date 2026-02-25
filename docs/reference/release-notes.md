(reference-release-notes)=
# Release notes

This page outlines the release notes of all recent versions of Snapd, summarising new features, bug fixes and changes in each version.

## Recent releases

### Latest stable release

* **[Snapd 2.73](#snapd-2-73-release-notes)** (27th November 2025)

### Latest beta release
* [Snapd 2.74](#snapd-2-74-release-notes) (21st January 2026)

### Older releases
* [Snapd 2.73](#snapd-2-73-release-notes) (27th November 2025)
* [Snapd 2.72](#snapd-2-72-release-notes) (30th September 2025)
* [Snapd 2.71](#snapd-2-71-release-notes) (14th August 2025)
* [Snapd 2.70](#snapd-2-70-release-notes) (31th June 2025)
* [Snapd 2.68](#snapd-2-68-release-notes) (31st March 2025)
* [Snapd 2.67](#snapd-2-67-release-notes) (13th January 2025)
* [Snapd 2.66](#snapd-2-66-release-notes) (26th November 2024)
* [Snapd 2.65](#snapd-2-65-release-notes) (8th October 2024)
* [Snapd 2.64](#snapd-2-64-release-notes) (25th July 2024)
* [Snapd 2.63](#snapd-2-63-release-notes) (6th June 2024)
* [Snapd 2.62](#snapd-2-62-release-notes) (15th April 2024)
* [Snapd 2.61](#snapd-2-61-release-notes) (3rd January 2024)

## Release policy and schedule

The snapd package updates automatically, and by default, checks for updates 4 times a day. To manually update or modify this process, see [Managing updates](/how-to-guides/work-with-snaps/manage-updates).

[Channels](/explanation/how-snaps-work/channels-and-tracks) are used to distinguish between stable releases, which are always available from the stable channel, and beta and testing releases, which can be installed from the candidate, beta and edge channels.

To install snapd from the beta channel, for example, use the following command:

```
sudo snap refresh snapd --beta
```

To ensure you receive latest security updates and bug fixes, ensure you upgrade to a new release of Snapd shortly after it is released.

For the release plan and complete list of changes, please refer to the [snapd roadmap](/). Feel free to provide your test feedback on the [forum](https://forum.snapcraft.io/c/snapd/5), or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug).

We greatly appreciate your contributions and support!

---

## Snapd 2.74 release notes

We’re pleased to share that Snapd 2.74 snap is available for testing in the beta channel.

# New in snapd 2.74
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
* Preseeding: check whether a path is a mountpoint before remounting
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

## Snapd 2.73 release notes

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

## Snapd 2.72 release notes

### **Highlights**

* Enable the gpio-chardev interface now with the more robust gpio-aggregator configfs kernel interface ([LP: #1916244](https://bugs.launchpad.net/snapd/+bug/1916244))
* FDE enhancements and additions: add generic reseal function and correct sealing with kernel command line defaults, support replacing TPM protected keys at runtime, secboot preinstall check fix actions and using OPTEE (Ubuntu Core & arm) for protecting keys, as an alternative to existing fde-setup hooks.

### **Notable updates**

* snap-confine: fix non-suid limitation by switching to root:root to operate v1 freezer
* Fix preseeding failure due to scan-disk issue on RPi
* Snap installation: skip snap icon download when running in a cloud or using a proxy store ([LP: #2122054](https://bugs.launchpad.net/snapd/+bug/2122054))
* snap-confine: fix error message with /root/snap not accessible ([LP: #2117558](https://bugs.launchpad.net/snapd/+bug/2117558))
* Interfaces: do not expose Kerberos tickets for classic snaps ([LP: #2121238](https://bugs.launchpad.net/snapd/+bug/2121238))
* Cleanly support socket activation for classic snap ([LP: #2117121](https://bugs.launchpad.net/snapd/+bug/2117121))
* Improve progress reporting for snap install/refresh ([LP: #2112626](https://bugs.launchpad.net/snapd/+bug/2112626))
* Extend output to indicate when snap data snapshot was created during remove ([LP: #2114704](https://bugs.launchpad.net/snapd/+bug/2114704))

For the release plan and complete list of changes, please refer to the [full release notes](https://forum.snapcraft.io/t/the-snapd-roadmap/1973).

### **More about GPIO Chardev**

This release supports the kernel GPIO character device API with specific GPIO lines mediation through the new gpio-chardev interface which offers more fine-grained control over the gpio-control interface that allowed unrestricted access to all GPIO chips when needed.

For historical context: traditionally Snapd supported mediation of the sysfs interface for GPIO access. This sysfs kernel interface is considered legacy by upstream kernel developers (and will be removed from UC26+ kernels) and it has been replaced by a new character device API, commonly referred to as gpiod.

The new kernel GPIO APIs are typically consumed through the libgpiod library (C or various bindings) or a set of command line utilities provided by said library.

For more information on how to use the new interface (and migration from the older gpio interface), please check the official documentation for the gpio-chardev interface:[ https://forum.snapcraft.io/t/the-gpio-chardev-interface/46411](https://forum.snapcraft.io/t/the-gpio-chardev-interface/46411).

### **More about our FDE journey**

***The previous release***, 2.71, concluded the Snapd contribution to TPM FDE for the 25.10 [install image](https://cdimage.ubuntu.com/daily-live/current/questing-desktop-amd64.iso).

Progression through the 25.10 cycle up to 2.71:
* 2.68.* - introduced a new key format, added support for passphrases during installation, and included various fixes.
* 2:70 - set roles in TPM keys and fixed resealing with the v1 hook key format.
* 2.71 - added recovery key auto-repair, delivered many additional APIs needed to support installation and use of TPM-backed FDE on hybrid Ubuntu 25.10, and included further fixes.

As part of this work, secboot has been improved to more extensively check whether the platform can support secure boot, which is used by one of the new Snapd APIs introduced in 2.71 and used by the installer to determine TPM FDE availability during hybrid Ubuntu installation.

***This release***, along with releases 2.73 and 2.74 planned for next cycle, will extend and refine the TPM FDE hybrid Ubuntu installation and overall user experience for the Ubuntu 26.04 LTS release.

A lot of care goes into continually ensuring compatibility with Ubuntu Core, previous versions of Snapd and targeted hardware. Each release must pass extensive testing, including test suites for certified hardware. In addition to our own rigorous testing, we strongly advise all users to also thoroughly test all their hardware variations and inform us of potential issues or concerns as soon as possible.

For a broader overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146)

### **Test Feedback**

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) Snapd version(s) and (3) steps to reproduce the issue.

## Snapd 2.71 release notes

## **Highlights**

* Support for TPM backed Full Disk Encryption on Ubuntu 25.10

## **Notable updates**
* Fix offline remodel case where we switched to a channel without an actual refresh
* Reject system key mismatch advice when not yet seeded ([LP: #2114923](https://bugs.launchpad.net/ubuntu-desktop-provision/+bug/2114923))
* Make removal of last active revision of a snap equal to snap remove ([LP: #2112551](https://bugs.launchpad.net/bugs/2112551))
* Allow non-gpt in fallback mode to support RPi ([LP: #2114779](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/2114779))
* Fix \`snap debug connectivity\` check for RISC-V ([LP: #2112544](https://bugs.launchpad.net/ubuntu/+source/snapd/+bug/2112544))
* Exclude snap/snapd/preseeding when generating preseed tarball ([LP: #2112332](https://bugs.launchpad.net/snapd/+bug/2112332))
* Fix snap command progress reporting ([LP: #1952500](https://bugs.launchpad.net/bugs/1952500))
* Interfaces: kerberos-tickets | add new interface ([LP: #1849346](https://bugs.launchpad.net/ubuntu/+source/chromium-browser/+bug/1849346))
* Interfaces: log-observe | add capability dac_read_search ([LP: #2098780](https://bugs.launchpad.net/bugs/2098780))
* Interfaces: block-devices | opt-in access to individual partitions ([LP: #2033883](https://bugs.launchpad.net/snapd/+bug/2033883))

## **More about TPM backed FDE on Ubuntu Core and Ubuntu 25.10**

To support hybrid Ubuntu 25.10+ systems, we’ve introduced a new key format. On Ubuntu Core this change is transparent to users, but it enables us to transition from file-based key storage to storing keys in the LUKS2 header (with header redundancy) on core26.

On previous versions of Ubuntu Core, once a reboot required a recovery key, the device would continue prompting for that key on every subsequent boot. This could be particularly problematic for unattended or remote devices. This behavior was improved so that after a firmware update, entering the recovery key triggers an automatic repair and restores normal unattended boot operation without further prompts.

The [fwupd](https://snapcraft.io/fwupd) tool is available both as a deb and as a snap providing a unified way to install and manage system firmware updates. Support has been added for updating the UEFI DBX (UEFI Secure Boot forbidden signatures database) without requiring a recovery key on reboot. This ensures that both hybrid Ubuntu 25.10+ and Ubuntu Core devices with Full Disk Encryption seamlessly apply DBX updates.

For an overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146)

## Snapd 2.70 release notes

### Highlights

* `snap-confine` no longer requires to be `setuid` root, now uses file capabilities and executes in the security context of the user who invokes it.
* snapd.apparmor is now enabled on Fedora, so that a Fedora container running on an apparmor-capable kernel works correctly.

### Notable updates

* Reset SHELL to /bin/bash in non-classic snaps ([LP: #2107443](https://bugs.launchpad.net/snapd/+bug/2107443))
* Only cancel notices requests on stop/shutdown ([LP: #2104066](https://bugs.launchpad.net/snapstore-server/+bug/2104066))
* Fix GLX on nvidia when xorg is confined by AppArmor ([LP: #2088456](https://bugs.launchpad.net/canonical-kernel-snaps/+bug/2102456))
* Fix snap-bootstrap busy loop ([LP: #2106121](https://bugs.launchpad.net/snapd/+bug/2106121))
* Update secboot and modify snap-bootstrap to remove usage of go templates to reduce size by 4MB ([LP: #2102456](https://bugs.launchpad.net/canonical-kernel-snaps/+bug/2102456))

### More about no-setuid snap confine

In an effort to increase the security and have better control over the execution of privileged binaries, the snap application bootstrapping helper, snap-confine, no longer requires to be setuid root. Instead it relies on file capabilities and executes in the security context of the user who invoked it. The required capabilities are effectively a subset of all the capabilities which were previously obtained immediately when executing the privileged binary. The effective capabilities are dynamically switched at runtime, such that the helper executes with the least set of effective privileges at any given time.

For the release plan and complete list of changes, please refer to the [full release notes](https://forum.snapcraft.io/t/the-snapd-roadmap/1973). Please note that 2.70 includes all the changes in the superseded 2.69 and 2.69.1 releases.

## Snapd 2.68 release notes

The official release for this version was Snapd 2.68.4.

### Highlights

* [FDE](https://ubuntu.com/core/docs/full-disk-encryption): Add support for a new and more extensible key format and passphrases for encrypted partitions can now be specified during installation
* [Components](https://snapcraft.io/docs/components): Support online/offline [remodeling](https://ubuntu.com/core/docs/remodelling) and the creation of new recovery systems for models that contain components, on Ubuntu Core as well as Hybrid systems. Components are useful for distributing optional resources for a snap, such as debug symbols alongside snap binaries, and kernel modules alongside a kernel snap.
* [Kernel Components](https://canonical-snapcraft.readthedocs-hosted.com/en/stable/reference/components.html): Make kernel components and modules available in early boot
* Interfaces: Added [auditd-support interface](https://snapcraft.io/docs/auditd-support-interface) that allows a snap to ship auditd as part of a snap and `checkbox-support` interface that allows unrestricted access to devices when testing with checkbox

### Notable updates
* Fix issue preventing hybrid systems from being seeded on first boot
* Modify AppArmor template to allow using setpriv to run ([LP: #20729871](https://bugs.launchpad.net/snapd/+bug/2072987))
* Disable udev backend when inside a container ([LP: #1712808](https://bugs.launchpad.net/snapd/+bug/1712808)
* Remove auto-import udev rules not required by deb package to avoid unwanted syslog errors ([LP: #1966203](https://bugs.launchpad.net/snapd/+bug/1966203))
* Fix progress reporting when stdout is on a tty, but stdin is not ([LP: #1886414](https://bugs.launchpad.net/ubuntu/+source/chromium-browser/+bug/1886414))

### Experimental Features
* Removed stale `robust-mount-namespace-updates` experimental flag
* Removed rejected `snapd-snap` experimental feature and its feature flag

### Impact on Ubuntu Core using Full Disk Encryption

If you are planning to test or use this snapd release and you are using full disk encryption (with both hooks and TPM), some updates to your kernel snap are needed:
* If you maintain your own kernel snap, you will need to include the new snap-bootstrap.
* If you are using a kernel snap maintained by Canonical, all our kernel snaps will be updated to the new version of snap-bootstrap in due course.

Until all kernel snaps are updated, snapd from latest/edge cannot be used for installation or remodeling if you are using FDE. If you have not updated the kernel snap, do not report bugs you encountered when:
* Remodeling with a snapd from latest/edge, then doing factory reset.
* Installing fresh images with snapd from latest/edge

## Snapd 2.67 release notes

*Released 13th January 2025*

### Highlights:

* **Registry views**
   
   This feature has evolved beyond cross-snap configuration, now enabling custodian snaps to validate changes and store registry data outside of snapd.

* **Components**

  Standard components are now broadly usable, after the addition of the `snap components` command, support for joint install of snaps and components from local files, and tab completion.

   Building on standard components, kernel components have been enhanced with support for the `snapctl model` command for kernel snaps as well as other improvements to enable kernel drivers for proprietary hardware on Ubuntu Core.

### Notable bug fixes:

* AppArmor Prompting: Fixed an issue with overlapping rules ([bug report](https://github.com/canonical/desktop-security-center/issues/74))
* Resolved a deadlock edge case related to app awareness during refresh operations ([LP2084730](https://bugs.launchpad.net/snapd/+bug/2084730))
* Addressed issues with reloading service activation units to prevent systemd errors ([LP2083961](https://bugs.launchpad.net/snapd/+bug/2083961))
* Fixed the generation of AppArmor profiles with incorrect revisions during concurrent refreshes of snaps using the content interface
* Fix AppArmor permissions to allow snaps access to kernel modules and firmware on UC24, which also fixes the kernel-modules-control interface on UC24
* Fix ‘snap run’ getent based user lookup in case of bad PATH (LP2090938 2)
* Fix snapd using the incorrect AppArmor version during undo of an refresh
* Extended hardware-observe interface to allow support riscv_hwprobe syscall and mount-observe interface to allow listmount and statmount syscalls


For the release plan and the complete list of changes, please refer to the [Snapd roadmap](/).

## Snapd 2.66 release notes

*Released 26th November 2024*

This release added the ability for Snapcraft 8.x to build snapd using with core22 base, and support for building a snapd variant that's [FIPS](https://en.wikipedia.org/wiki/FIPS_140-3) compliant. 

Other highlights include:

*  **AppArmor prompting**

   In collaboration with the security and desktop teams at Canonical, this release of snapd includes the functionality required for snaps to request interface access from the user. 

   For more information on this feature, including design details and how it can be tested in Ubuntu 24.10, see [Introducing Permissions Prompting](https://discourse.ubuntu.com/t/ubuntu-desktop-s-24-10-dev-cycle-part-5-introducing-permissions-prompting/47963).

* **Experimental confdb support**

   This release includes many updates to support _confdb_, formerly known as Registry, which will significantly improve how we handle configuration data and share that data between snaps and devices.

## Snapd 2.64 release notes

*Released 26th November 2024*

For the 2.64 release, we updated the build process to use Ubuntu 22.04 instead of Ubuntu 16.04. This change only affected the snapd.snap, and had impact on builds for Debian, Fedora, Arch, openSUSE, or any other classic package

Users should see no changes or compatibility issues, and if you are a snapd developer, this change makes building snapd easier. The latest Snapcraft releases can now be used to build a local version of the snapd package. In the long term, this will also improve our iteration speed as we’ll require fewer snapd builds, providing developers with faster feedback on their changes.

As part of this release cycle, our `ubuntu-image` and validation-sets documentation also improved.

## Snapd 2.63 release notes

*Released 6th June 2024*

Snap-based [Ubuntu Core](https://ubuntu.com/core) devices will benefit from many of our the features for this release, including support for [Offline remodelling](https://ubuntu.com/core/docs/uc20/remodelling#heading--offline), the use of [Validation sets](https://snapcraft.io/docs/validation-sets) in the [model assertion](https://ubuntu.com/core/docs/reference/assertions/model) and setting a custom port for SSH. 

There’s also a new `snap sign` [`--chain`](https://ubuntu.com/core/docs/system-user#heading--generating-auto) argument in this release, that can be used to aggregate all the assertions required to create a new system user.

## Snapd 2.62 release notes

*Released 15th April 2024*

The functionality to add custom device interfaces to an app is now complete, as is our create and removal functionality for Ubuntu Core recovery systems. We’ve also finally made a commitment on what minimum [system requirements](https://ubuntu.com/core/docs/system-requirements) might actually be for Ubuntu Core, even if you can’t actually buy a device with less than several gigabytes of on-board RAM.

This release also included two significant additions to our documentation. Firstly, the Docker interface now includes a fully realised example implementation, and secondly, we’ve completed a new page on recovery system via the REST API, thanks to Andrew.

Finally, this release included new packages for Arch Linux, Amazon Linux, Debian, Fedora, openSUSE and Solus.

## Snapd 2.61 release notes

*Released 3rd January 2024*

This release included a lot of background work that will later be used by `confdb` (see Snapd 2.66), to help with  cross-snap configuration. This includes new rules for parsing assertions and a per-aspect field, plus a vital new ability to unset values from the command line.

We also got closer to finishing our opt-in AppArmor prompting support , with some important background improvements, and created a specification for the desktop user-experience flow. Our cross-distribution support also improved with this release, with a new repository and packages for Amazon Linux , and snapd 2.61.1 releases for Debian Sid and Fedora 38, 39, Rawhide and EPEL 7, 8 and 9.

