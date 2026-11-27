---
myst:
  html_meta:
    description: Release notes for Snapd 2.75, whose changes were released as 2.75.2 on 23 April 2026. Read about selected updates and fixes.
---

(release-notes_snapd-2-75)=
# Snapd 2.75

*Not released, superseded by 2.75.1.*

* FDE: run early boot check only once per boot
* FDE: update secboot to revision 77bc2457cc76
* FDE: add degraded state for status API
* FDE: prevent resealing tasks from running together
* FDE: enable using keyslot tokens to store protected keys for UC26+
* FDE: early commit `kcmdline` config transaction in update-gadget-cmdline to mitigate possible race condition
* FDE: ensure extra snapd `kcmdline` fragments are applied
* FDE: remove old secboot activation API calls
* LP: #2142130 update apparmor parser to 4.1.7
* LP: #2137543 disable translations in formatted output for snapctl services
* LP: #2142655 improve snap size reporting precision in `snap info` output
* LP: #2139664 snap-confine: remove race condition triggered by hat profile
* LP: #2139065 skip 70-snap.*.rules when building `dracut` initramfs
* LP: #2002697 error early on removal without purge if home is in NFS mount
* LP: #2141461 Interfaces: allow snap-update-ns to read /proc/pid/auxv
* LP: #2138268 Interfaces: kerberos-tickets| new interface allow access to kerberos tickets stored in /tmp
* Interfaces: block-devices| allow Xen block devices
* Interfaces: u2f-devices| add Tokey 3 FIDO
* Interfaces: `devlxd`| new interface allowing access to LXD `devlxd` socket and APIs
* Interfaces: browser-support| allow reading pressure stall info information
* Interfaces: network-setup-control| allow additional netplan files access
* Interfaces: desktop| allow access `kvantum`, `lxqt`, and gtk4 configuration files
* Interfaces: system-observe| allow `fdinfo` access for GPU monitoring
* Interfaces: ubuntu-pro-control| allow access to Ubuntu Advantage client configuration
* Prompting: add API endpoint to ask whether application should have access
* Prompting: add support for audio-record prompting via API endpoint
* Prompting: store snap name instead of apparmor label in requests
* Prompting: respond with 503 to API requests when prompting subsystem is shutting down
* Prompting: generalize prompting subsystem to support requests from outside AppArmor
* Confdb: unset data for missing paths in set request
* Confdb: return 400 for API requests with missing filter constraints
* Confdb: return 400 for API requests with unmatched filter constraints
* Confdb: support typed constraints in confdb filtering
* Confdb: fixed unmarshalling transaction with placeholder path in deltas
* Confdb: refresh confdb-schema assertions during manual refresh
* Remote device management (experimental): add skeleton device management manager
* Remote device management (experimental): add message exchange loop
* Components: add `snap component` command, include component summary in `snap info` output
* Components: enforce validation sets when installing components
* Configuration: add `system.motd` configuration option to customize message of the day (motd)
* packaging: remove dependencies libbrotli1, libfreetype6, and libpng16-16 from snap
* snap-bootstrap: use `libblkid` for disk information to speed up boot
* snap-confine: improve data handling error
* snap-confine: use `ld` cache from the app base for core26+
* snap: add riscv ISA detection for snaps
* squashfs: reduce memory footprint of single file extraction
* Add experimental snap delta format
* Enable early download of seed snaps during refresh
* Enable parallel downloads of essential snaps during refresh
* Disallow removing components required by validation sets
* Make `snap prepare-image` fail on --validation=ignore if model has enforced validation-sets
* Fix correctly handling interrupted snap downloads
* Fix handling of store throttling for refresh-app-awareness monitored snaps
* Stop removed "endure" services on refresh
* Install by default from the initramfs for UC26+, removing the need for a reboot after installation
* Keep `minidebuginfo` in snapd snap
* Make snap-specific systemd cgroup mandatory for snaps using core26 and later, improve messaging for failure scenarios
* Preserve stale connections of broken snaps
* Remove enforce-validation-sets need for network
* Opportunistic discarding of mount namespace when updating slot providers
* Support for delaying updates of snap mount namespaces when refreshing slot providers
* Use application CommonID as default source for desktop ID

## Snapd 2.75.1

*Not released, superseded by 2.75.2.*

* FDE: limit number of boot check log entries
* Allow a logged in user to refresh private snaps during a refresh with multiple snaps
* Use precise prune pattern for `tmpfiles` (CVE-2026-3888)

## Snapd 2.75.2

*Released on 23 April 2026.*

### Overview

Snapd 2.75.2 includes the content of 2.75 and 2.75.1, which were not released.

* Bug fixes and robustness improvements
* [Permissions Prompting](https://snapcraft.io/install/prompting-client/ubuntu) support for audio-record prompting via the snapd API

### Notable updates

* Use precise prune pattern for `tmpfiles` (CVE-2026-3888)
* AppArmor parser updated to 4.1.7 ([LP: #2142130](https://bugs.launchpad.net/snapd/+bug/2142130))
* Disable translations in formatted output for snapctl services ([LP: #2137543](https://bugs.launchpad.net/snapd/+bug/2137543))
* Improve snap size reporting precision in `snap info` output ([LP: #2142655](https://bugs.launchpad.net/snapd/+bug/2142655))
* snap-confine: remove race condition triggered by hat profile ([LP: #2139664](https://bugs.launchpad.net/snapd/+bug/2139664))
* Skip 70-snap.*.rules when building `dracut` initramfs ([LP: #2139065](https://bugs.launchpad.net/snapd/+bug/2139065))
* Error early on removal without purge if home is in NFS mount ([LP: #2002697](https://bugs.launchpad.net/snapd/+bug/2002697))
* Interfaces: allow snap-update-ns to read /proc/pid/auxv ([LP: #2141461](https://bugs.launchpad.net/snapd/+bug/2141461))
* Interfaces: kerberos-tickets | new interface allowing access to kerberos tickets stored in /tmp ([LP: #2138268](https://bugs.launchpad.net/snapd/+bug/2138268))
* Keep `minidebuginfo` in the snapd snap
* squashfs: reduce memory footprint of single file extraction
* Add `snap component` command

### Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

### Changelog

* Interfaces: network-setup-*| allow running python binaries from the base on UC26+
* Cross-distro: modify SELinux policy to allow mounting on `/var/snap/<snap>/<rev>`
* Fix potential task deadlock by considering all tasks in a lane that might be waiting for a reboot when processing delayed security backend effects
