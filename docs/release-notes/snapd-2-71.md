---
myst:
  html_meta:
    description: Release notes for Snapd 2.71, released on 20 August 2025. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-71)=
# Snapd 2.71

*Released on 20 August 2025*

## Highlights

* Support for TPM backed Full Disk Encryption on Ubuntu 25.10

## Notable updates

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

## More about TPM backed FDE on Ubuntu Core and Ubuntu 25.10

To support hybrid Ubuntu 25.10+ systems, we’ve introduced a new key format. On Ubuntu Core this change is transparent to users, but it enables us to transition from file-based key storage to storing keys in the LUKS2 header (with header redundancy) on core26.

On previous versions of Ubuntu Core, once a reboot required a recovery key, the device would continue prompting for that key on every subsequent boot. This could be particularly problematic for unattended or remote devices. This behavior was improved so that after a firmware update, entering the recovery key triggers an automatic repair and restores normal unattended boot operation without further prompts.

The [fwupd](https://snapcraft.io/fwupd) tool is available both as a deb and as a snap providing a unified way to install and manage system firmware updates. Support has been added for updating the UEFI DBX (UEFI Secure Boot forbidden signatures database) without requiring a recovery key on reboot. This ensures that both hybrid Ubuntu 25.10+ and Ubuntu Core devices with Full Disk Encryption seamlessly apply DBX updates.

For an overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146)

## Changelog

* FDE: auto-repair when recovery key is used
* FDE: revoke keys on shim update
* FDE: revoke old TPM keys when `dbx` has been updated
* FDE: do not reseal FDE hook keys every time
* FDE: store keys in the kernel keyring when installing from initrd
* FDE: allow disabled DMA on Core
* FDE: snap-bootstrap: do not check for partition in scan-disk on CVM
* FDE: support secboot preinstall check for 25.10+ hybrid installs via the /v2/system/{label} endpoint
* FDE: support generating recovery key at install time via the /v2/systems/{label} endpoint
* FDE: update passphrase quality check at install time via the /v2/systems/{label} endpoint
* FDE: support replacing recovery key at runtime via the new /v2/system-volumes endpoint
* FDE: support checking recovery keys at runtime via the /v2/system-volumes endpoint
* FDE: support enumerating keyslots at runtime via the /v2/system-volumes endpoint
* FDE: support changing passphrase at runtime via the /v2/system-volumes endpoint
* FDE: support passphrase quality check at runtime via the /v2/system-volumes endpoint
* FDE: update secboot to revision 3e181c8edf0f
* Confdb: support lists and indexed paths on read and write
* Confdb: alias references must be wrapped in brackets
* Confdb: support indexed paths in confdb-schema assertion
* Confdb: make API errors consistent with options
* Confdb: fetch confdb-schema assertion on access
* Confdb: prevent \`--previous\` from being used in read-side hooks
* Components: fix snap command with multiple components
* Components: set revision of seed components to x1
* Components: unmount extra kernel-modules components mounts
* AppArmor Prompting: add lifespan "session" for prompting rules
* AppArmor Prompting: support restoring prompts after snapd restart
* AppArmor Prompting: limit the extra information included in probed AppArmor features and system key
* Notices: refactor notice state internals
* SELinux: look for restorecon/matchpathcon at all known locations rather than current PATH
* SELinux: update policy to allow watching cgroups (for RAA), and talking to user session agents (service mgmt/refresh)
* Refresh App Awareness: Fix unexpected inotify file descriptor cleanup
* snap-confine: workaround for `glibc` fchmodat() fallback and handle ENOSYS
* snap-confine: add support for host policy for limiting users able to run snaps
* LP: #2114923 Reject system key mismatch advise when not yet seeded
* Use separate lanes for essential and non-essential snaps during seeding and allow non-essential installs to retry
* Fix bug preventing remodel from core18 to core18 when snapd snap is unchanged
* LP: #2112551 Make removal of last active revision of a snap equal to snap remove
* LP: #2114779 Allow non-gpt in fallback mode to support RPi
* Switch from using systemd LogNamespace to manually controlled journal quotas
* Change snap command trace logging to only log the command names
* Grant desktop-launch access to /v2/snaps
* Update code for creating the snap journal stream
* Switch from using core to snapd snap for \`snap debug connectivity\`
* Fix offline remodel case where we switched to a channel without an actual refresh
* LP: #2112544 Fix \`snap debug connectivity\` check for RISC-V
* LP: #2112332 Exclude snap/snapd/preseeding when generating preseed tarball
* LP: #1952500 Fix snap command progress reporting
* LP: #1849346 Interfaces: kerberos-tickets |  add new interface
* Interfaces: u2f | add support for Thetis Pro
* Interfaces: u2f | add OneSpan device and fix older device
* Interfaces: pipewire, audio-playback | support pipewire as system daemon
* Interfaces: gpg-keys | allow access to GPG agent sockets
* Interfaces: usb-gadget | add new interface
* Interfaces: snap-fde-control, firmware-updater-support | add new interfaces to support FDE
* Interfaces: timezone-control | extend to support `timedatectl` `varlink`
* Interfaces: cpu-control | fix rules for accessing IRQ sysfs and `procfs` directories
* Interfaces: microstack-support | allow SR-IOV attachments
* Interfaces: modify AppArmor template to allow snaps to read their own systemd credentials
* Interfaces: posix-mq | allow stat on /dev/mqueue
* LP: #2098780 Interfaces: log-observe | add capability dac_read_search
* Interfaces: block-devices | allow access to ZFS pools and datasets
* LP: #2033883 Interfaces: block-devices | opt-in access to individual partitions
* Interfaces: accel | add new interface to support accel kernel subsystem
* Interfaces: shutdown | allow client to bind on its side of dbus socket
* Interfaces: modify seccomp template to allow pwritev2
* Interfaces: modify AppArmor template to allow reading /proc/sys/fs/nr_open
* Packaging: drop snap.failure service for openSUSE
* Packaging: add SELinux support for openSUSE
* Packaging: disable `optee` when using `nooptee` build tag
* Packaging: add support for static PIE builds in `snapd.mk`, drop pie.patch from openSUSE
* Packaging: add libcap2-bin runtime dependency for ubuntu-16.04
* Packaging: use `snapd.mk` for packaging on Fedora
* Packaging: exclude .git directory
* Packaging: fix DPKG_PARSECHANGELOG assignment
* Packaging: fix building on Fedora with `dpkg` installed
