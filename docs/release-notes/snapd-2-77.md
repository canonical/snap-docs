---
myst:
  html_meta:
    description: Release notes for Snapd 2.77, first released to stable as 2.77.1 on 2 October 2026. Read about selected updates and fixes.
---

(release-notes_snapd-2-77)=
# Snapd 2.77

*Released to candidate on 20 August 2026*

This release contains the 26.10 image content.

*We discovered a regression that was addressed in snapd 2.77.1: https://github.com/canonical/snapd/pull/17492.*

## Changelog

* Account for differences in names of the binaries in the snapd FIPS build
* Add code to calculate canonical subject name hash
* Add commands for debugging or accessing snap mount namespaces
* Add helpers for listing and iterating device mediation groups
* Add package ebpf with helpers wrapping eBPF exposed objects with dependency on github.com/cilium/ebpf
* Add secondary prerequisites task that acts as the synchronization point, which ensures that a snap's prerequisites are available before it's installed
* Add support for shell conditional syntax in envs
* Added /usr/share/{man,help,info} to system-packages-doc
* asserts: add validation-sets confdb-schema builtin
* asserts: ensure that compatibility labels are strings
* asserts: extend on-classic constraints to accept "distro/variant", "distro/*", and "distro/" under a new snap-declaration format 7
* asserts: validate serial in newDeviceIDFromString
* Bump github.com/canonical/go-efilib to v1.8.0 to include fixes for efivars probe
* confdb: add validation-sets handler and fix data loss when writing to new schemas or accounts
* confdb: fix bug on reading uneven lists
* confdb: literal subkeys are sorted after placeholders
* confdb: run observe-view-* hooks after commit
* confdb: support Encode/Decode for builtins
* confdb: support sign-only external keypair backends
* core-initrd: add missing libbpf and systemd dlopen dependencies, and increase mount burst
* Drop task logs for delayed effects
* During snap removal, clear-snap task errors early if there are user mounts in snap data dirs
* Enable reverts to trigger a seed refresh
* Ensure profiles are setup before running prepare-{slot, plug}* hooks
* Ensure that prereqs created by initial refresh run before create-recovery-system
* Exclude Georgian from translation linting
* experimental features: graduate layouts, classic-preserves-xdg-runtime-dir, refresh-app-awareness, and dbus-activation features
* experimental features: warn when setting graduated or default-enabled experimental features and do not store settings for graduated features
* Expose individual certs as well as c_rehash emulation
* Extend autogen with explicit --sysconfdir
* External keypair manager: add shared external key manager implementation
* External keypair manager: refactor GPG and external keypair managers to use extKeypairMgrImpl
* External keypair manager: support external OPENPGP signing in ExternalKeypairManager
* FDE: add post install actions API
* FDE: add reprovision API
* FDE: add reprovision recovery key generation API
* FDE: add reseal check after snapd refresh
* FDE: allow reprovision without factory reset
* FDE: change makebootable part of the boot package to not take install observers as parameters
* FDE: extend storage-encrypted system information
* FDE: make reprovision only seal
* FDE: remove all tmp keyslots on error
* FDE: remove check for unchanged authentication options
* FDE: run post install checks during auto repair
* Filter seed-refresh based on model and seed presence
* Fix failing snap remove when there are snapctl created mounts under snap global data dirs
* Fix postNotices to validate before locking state
* Guard the ensure check from running on classic
* Implement remodeling fully in terms of updates
* Implement ShutDown for HookManager
* Include variables SNAP_APP_NAME, and when applicable SNAP_APP_COMMON_ID, SNAP_APP_DESKTOP_FILE and SNAP_APP_BUS_NAME in snap application environments
* interfaces: add xdg-portal-permission-store interface
* interfaces: allow gtk css in subdirectories
* interfaces: allow systemd networkd link property changes via D-Bus
* interfaces: allow the systemd networkctl command
* interfaces: allow Wine to execute files accessed via the Document Portal
* interfaces: apparmor-observe | add interface
* interfaces: attempt to fix content with parallel installs
* interfaces: devlxd | fix access for LXD containers
* interfaces: docker | allow connecting to system-wide docker on classic
* interfaces: grant default access to memory.high in a snap's cgroup
* interfaces: iscsi-initiator | allow access to /var/lib/iscsi/nodes
* interfaces: kernel-sched-ext-control | add the kernel sched-ext control interface implementation
* interfaces: make polkit and upower implicit on Core systems only
* interfaces: open-iscsi | add missing state paths
* interfaces: opengl | expose wsl libraries
* interfaces: u2f-devices | add atkey PID and relative VID support
* List dir contents on failure to remove snap base data dir
* List non-snapctl mounts in snap data dirs
* LP: #2072331 Validate map keys in JSON config values
* LP: #2110510 Interfaces: allow reading of /proc/self/smaps_rollup
* LP: #2143934 Interfaces: network-control, network-manager | allow missing resolve1 link setters
* LP: #2160691 Security logging: strip trailing whitespace from audit netlink message payload
* LP: #2161982 Interfaces: vsock | add interface for VM guest services
* Make arguments of debug mount-namespace consistent with other debug commands
* Make bootloader logging less verbose
* Make cert manager garbage check run after symlink migration
* Make secondary prerequisite synchronization task handle same-change retries
* mkversion.sh: do describe in worktrees too
* multi-entry snapd: merge snap and snapd binaries
* multi-entry snapd: move debug device-cgroup implementation file under cmd/snapd/cli
* multi-entry snapd: move snap-gpio-helper sources around before transitioning to multi-entry dispatch
* multi-entry snapd: move snapd-apparmor sources to a dedicated tool location
* multi-entry snapd: move source files around in preparation for snapd/snap merge
* multi-entry snapd: move the snap-preseed sources around in preparation
* multi-entry snapd: move the sources of snapctl and snap-exec in preparation for the multi-entry dispatch
* Never create seed refresh tasks during a remodel
* packaging: assign a default label for /tmp/snap-private-tmp and set it during installation
* packaging: build deb with Go 1.23 for noble and jammy, Go 1.22 for focal
* packaging: drop SNAP_TAGS
* packaging: drop symlinks for opensuse 15.5/15.6 packaging
* packaging: fix service startup during install and session-agent socket handling on Ubuntu 26.04+
* packaging: fix stderr redirection
* packaging: restore gbp.conf output directory for Ubuntu 26.04 builds
* packaging: switch to apparmor 5.x with 5 ABI
* packaging: update bundled AppArmor to 5.0.2 and accept the 5.0 ABI when running as deb
* packaging: use a relative symlink for snapctl and update steam-support udev rules
* Preserve component in hook security tags
* Prevent removal of seed-refresh snaps when seed-refresh is enabled
* Refactor base-declaration into 1st class builtin assertion
* Refactor how the is-originating-from-snap-command advisory check works
* Refactor prerequisites task handler to enable proper seed-refresh integration
* Reintroduce fdstore helpers
* remote device management: add task to validate request messages
* remote device management: apply management messages, queue response messages, and improve sequencing and redelivery handling
* Remove osutil unused AtomicWriteFollow flag
* Remove xerrors dependency
* Reuse existing seed-refresh implementation for free during single-path installation
* Rework how SnapSetup.SnapPath is used
* seccomp: allow rseq_slice_yield
* security logging: add seclog API for administrative actions and token create/remove events
* security logging: add security logging for adding, updating and removing a snapd user
* Set target hostname from install-mode
* snap-confine: improve loading of BPF programs, retry on failures to collect verifier logs
* snap-confine: use profile and flags= in snap-confine and snap-update-ns' AppArmor profiles
* snap-confine: work around kernel mnt_ns_loop() ordering bug on 6.18.x
* snap: add debug command for listing currently mediated devices for a given snap
* snap: fix self-managed cgroup support checks
* snap: report hidden file access for paths allowed by home when prompting is active
* snap: report read-only file access for paths allowed by system-package-doc
* snapctl async support: add --format json to snap tasks to be consistent with snapctl
* snapctl async support: add snapctl tasks command
* snapctl async support: async feature negotiation between snap client and daemon
* snapctl async support: fix snapctl is-ready exit codes
* snapctl async support: re-enable snapctl async functionality
* snapshots: restore preserves snapctl created mounts
* snapshots: save excludes all mount points
* Support ca-certificate.crt only systems like core26
* Turn on quota-groups by default
* Use 0755 for certificate generation directories
* Use CreateTemp for NewAtomicFile tmp file creation
* Verify cached downloads in the do path and detect obvious corruption

## Snapd 2.77.1

*Released on 2 October 2026.*


Snapd 2.77.1 is the first stable release in the 2.77.x series, since the following blocking issue was found in 2.77:

* Fix undo of `unlink-component` after its snap revision was discarded. This is the regression that kept 2.77 from release. A refresh or removal that had to undo unlinking a component could fail once that revision was already gone.
* `power-control`: allow reading battery state files (low impact)

### FDE

Snapd 2.77.1 carries the 26.10 FDE work for reprovision and post-install handling.

* A device can be reprovisioned without a factory reset. The release adds APIs for reprovision, for generating a recovery key as part of reprovision, and for post-install actions.
* Storage-encrypted system information is extended.
* Perform a reseal dry-run check after a snapd refresh
* Improve cleanup robustness of FDE tasks

### Packaging and AppArmor

* Update the bundled AppArmor to 5.0.2, and accept the 5.0 ABI when snapd is running as a deb
* Build the deb with Go 1.23 on Noble and Jammy, and Go 1.22 on Focal
* Fix service startup during install, and session-agent socket handling, on Ubuntu 26.04 and later
* Use a relative symlink for `snapctl`, and update the steam-support udev rules

### Interfaces

* New interfaces: `apparmor-observe`, `kernel-sched-ext-control`, `vsock` ([LP: #2161982](https://bugs.launchpad.net/snapd/+bug/2161982)), and `xdg-portal-permission-store`
* `content`: a plug now mounts the parallel instance that provides the slot ([LP: #1915709](https://bugs.launchpad.net/snapd/+bug/1915709))
* `docker`: allow connecting to the system-wide Docker socket on classic
* Make `polkit` and `upower` implicit on Ubuntu Core only
* `opengl`: expose WSL libraries
* Allow Wine to execute files opened through the Document Portal
* Allow `networkctl` and systemd-networkd link property changes
* Allow reading `/proc/self/smaps_rollup` ([LP: #2110510](https://bugs.launchpad.net/snapd/+bug/2110510))
* `network-control` and `network-manager`: allow a missing resolve1 link ([LP: #2143934](https://bugs.launchpad.net/snapd/+bug/2143934))

### Other

* Seed refresh and remodel: express remodeling as updates; let reverts trigger a seed refresh; make a snap's prerequisites available before it is installed; keep snaps required by seed refresh from being removed
* Snap applications receive `SNAP_APP_NAME` and, when applicable, `SNAP_APP_COMMON_ID`, `SNAP_APP_DESKTOP_FILE`, and `SNAP_APP_BUS_NAME`. Environment entries may use shell conditional syntax
* Snapshots: restore keeps mounts created with snapctl; save skips mount points
* Removal: fail early when user mounts are still present under snap data; snapctl mounts under global data no longer make `snap remove` fail
* Verify cached downloads and detect obvious corruption
* Support systems that ship only `ca-certificate.crt`, such as core26
* snap-confine: retry BPF program loading when verifier logs cannot be collected; set AppArmor profile flags; work around a kernel mount-namespace ordering bug on 6.18 ([LP: #2161539](https://bugs.launchpad.net/snapd/+bug/2161539))
* Set the target hostname from install mode
* Prompting: report hidden-file access for paths allowed by `home`, and read-only access for paths allowed by `system-packages-doc`
* Option names with underscores are no longer permitted

### Experimental features

#### Graduated

These experimental features have graduated. They are now always enabled.

- **layouts:** a snap can bind-mount, symlink, or place a tmpfs inside its mount namespace
- **classic-preserves-xdg-runtime-dir:** on classic, a snap keeps the session `XDG_RUNTIME_DIR` and can reach user-session services there
- **refresh-app-awareness:** snapd holds a refresh while that snap’s apps are running
- **dbus-activation:** a snap app or service can be started by D-Bus activation

#### Enabled by default

- **quota-groups:** resource limits for snaps are available without setting the experimental flag

#### In development

The following are still under active development and are not yet considered stable for general use.

- **confdb:** validation-sets support; fix data loss when writing to a new schema or account; run `observe-view-*` hooks after commit; sign-only external keypair backends; validate map keys in JSON config values ([LP: #2072331](https://bugs.launchpad.net/snapd/+bug/2072331))
- **Security logging:** log administrative actions, token create and remove events, and adding, updating, or removing a snapd user; strip trailing whitespace from audit message payloads ([LP: #2160691](https://bugs.launchpad.net/snapd/+bug/2160691))
- **Remote device management:** validate request messages, apply management messages, queue responses, and improve sequencing and redelivery

### Test Feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

### Security reports

Please report security vulnerabilities in private. The [snapd security policy](https://github.com/canonical/snapd/blob/master/SECURITY.md) describes what qualifies and how to report it.

### Known issues

The bundled AppArmor update to 5.0.2 can cause issues on some outdated kernels. If you see issues related to network access, update your kernel to the latest version provided by your system. If you are using the EOL 25.04 version of Ubuntu, you cannot use 2.77.1 or any later version of the snapd snap. Add `SNAP_REEXEC=0` to `/etc/environment` to force using the deb package.

### Changelog

* Fix undo of unlink-component after its snap revision was discarded
* interfaces: power-control | allow reading all battery state files
