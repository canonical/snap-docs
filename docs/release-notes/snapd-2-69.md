---
myst:
  html_meta:
    description: Release notes for Snapd 2.69 and 2.69.1, which did not reach stable. Their changes were included in Snapd 2.70 on 8 July 2025.
---

(release-notes_snapd-2-69)=
# Snapd 2.69

*Not released to stable; superseded by Snapd 2.69.1.*

* FDE: re-factor listing of the disks based on run mode model and model to correctly resolve paths
* FDE: run snapd from snap-failure with the correct keyring mode
* Snap components: allow remodeling back to an old snap revision that includes components
* Snap components: fix remodel to a kernel snap that is already installed on the system, but not the current kernel due to a previous remodel.
* Snap components: fix for snapctl inputs that can crash snapd
* Confdb (experimental): load ephemeral data when reading data via snapctl get
* Confdb (experimental): load ephemeral data when reading data via snap get
* Confdb (experimental): rename {plug}-view-changed hook to observe-view-{plug}
* Confdb (experimental): rename confdb assertion to confdb-schema
* Confdb (experimental): change operator grouping in confdb-control assertion
* Confdb (experimental): add confdb-control API
* AppArmor: extend the probed features to include the presence of files, as well as directories
* AppArmor prompting (experimental): simplify the listener
* AppArmor metadata tagging (disabled): probe parser support for tags
* AppArmor metadata tagging (disabled): implement notification protocol v5
* Confidential VMs: sysroot.mount is now dynamically created by snap-bootstrap instead of being a static file in the initramfs
* Confidential VMs: Add new implementation of snap integrity API
* Non-suid snap-confine: first phase to replace snap-confine `suid` with capabilities to achieve the required permissions
* Initial changes for dynamic security profiles updates
* Provide snap icon fallback for /v2/icons without requiring network access at runtime
* Add eMMC gadget update support
* Support reexec when using /usr/libexec/snapd on the host (Arch Linux, openSUSE)
* Auto detect snap mount dir location on unknown distributions
* Modify snap-confine AppArmor template to allow all `glibc` HWCAPS subdirectories to prevent launch errors
* LP: #2102456 update secboot to bf2f40ea35c4 and modify snap-bootstrap to remove usage of go templates to reduce size by 4MB
* Fix snap-bootstrap to mount kernel snap from /sysroot/writable/system-data
* LP: #2106121 fix snap-bootstrap busy loop
* Fix encoding of time.Time by using `omitzero` instead of `omitempty` (on go 1.24+)
* Fix setting snapd permissions through `permctl` for openSUSE
* Fix snap struct json tags typo
* Fix snap pack configure hook permissions check incorrect file mode
* Fix gadget snap reinstall to honor existing sizes of partitions
* Fix to update command line when re-executing a snapd tool
* Fix 'snap validate' of specific missing newline and add error on missed case of 'snap validate --refresh' without another action
* Workaround for snapd-confine time_t size differences between architectures
* Disallow pack and install of snapd, base and os with specific configure hooks
* Drop udev build dependency that is no longer required and add missing systemd-dev dependency
* Build snap-bootstrap with `nomanagers` tag to decrease size by 1MB
* Interfaces: polkit | support custom polkit rules
* Interfaces: opengl | LP: #2088456 fix GLX on nvidia when xorg is confined by AppArmor
* Interfaces: log-observe | add missing udev rule
* Interfaces: hostname-control | fix call to `hostnamectl` in core24
* Interfaces: network-control | allow removing created network namespaces
* Interfaces: scsi-generic | re-enable base declaration for scsi-generic plug
* Interfaces: u2f | add support for Arculus AuthentiKey

## Snapd 2.69.1

*Not released to stable; superseded by Snapd 2.70.*

The current release candidate for 2.69.1 requires a fix for [LP: #2109843](https://bugs.launchpad.net/snapd/+bug/2109843). To ensure we continue delivering the latest changes in a timely manner, we’ve decided to supersede the 2.69.1 candidate with 2.70. It will include the bug fix, additional improvements, and help align with our release plan for the 25.10 cycle.

* AppArmor prompting (experimental): avoid race between closing/reading socket fd
* Fix potential validation set deadlock due to bases waiting on snaps
* [LP: #2104066](https://bugs.launchpad.net/snapd/+bug/2104066) Only cancel notices requests on Stop/shutdown
* Run '`systemctl` start' for mount units to ensure they are run also when unchanged
* Interfaces: timeserver-control | allow `timedatectl` `timesync` commands
