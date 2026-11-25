---
myst:
  html_meta:
    description: Snapd release notes. Review new features, bug fixes, and changes across recent stable, beta, and earlier snapd releases.
---

(reference-release-notes)=
# Release notes

This page outlines the release notes of all recent versions of Snapd, summarising new features, bug fixes and changes in each version.

## Latest stable release

* **{ref}`Snapd 2.78 <ref-release-notes_snapd-2-78-release-notes>`** (3 November 2026)

## Next planned release

* {ref}`Snapd 2.79 <ref-release-notes_snapd-2-79-release-notes>` (delayed; stable planned for 6 January 2027)

## Older releases

* {ref}`Snapd 2.78 <ref-release-notes_snapd-2-78-release-notes>`
* {ref}`Snapd 2.77 <ref-release-notes_snapd-2-77-release-notes>`
* {ref}`Snapd 2.76 <ref-release-notes_snapd-2-76-release-notes>`
* {ref}`Snapd 2.75 <ref-release-notes_snapd-2-75-release-notes>`
* {ref}`Snapd 2.74 <ref-release-notes_snapd-2-74-release-notes>`
* {ref}`Snapd 2.73 <ref-release-notes_snapd-2-73-release-notes>`
* {ref}`Snapd 2.72 <ref-release-notes_snapd-2-72-release-notes>`
* {ref}`Snapd 2.71 <ref-release-notes_snapd-2-71-release-notes>`
* {ref}`Snapd 2.70 <ref-release-notes_snapd-2-70-release-notes>`
* {ref}`Snapd 2.69 <ref-release-notes_snapd-2-69-release-notes>` (not released; superseded by Snapd 2.70)
* {ref}`Snapd 2.68 <ref-release-notes_snapd-2-68-release-notes>`
* {ref}`Snapd 2.67 <ref-release-notes_snapd-2-67-release-notes>`
* {ref}`Snapd 2.66 <ref-release-notes_snapd-2-66-release-notes>`
* {ref}`Snapd 2.65 <ref-release-notes_snapd-2-65-release-notes>`
* {ref}`Snapd 2.64 <ref-release-notes_snapd-2-64-release-notes>`
* {ref}`Snapd 2.63 <ref-release-notes_snapd-2-63-release-notes>`
* {ref}`Snapd 2.62 <ref-release-notes_snapd-2-62-release-notes>`
* {ref}`Snapd 2.61 <ref-release-notes_snapd-2-61-release-notes>`
* {ref}`Snapd 2.60.3 <ref-release-notes_snapd-2-60-release-notes>`
* {ref}`Snapd 2.59 <ref-release-notes_snapd-2-59-release-notes>`
* {ref}`Snapd 2.58 <ref-release-notes_snapd-2-58-release-notes>`
* {ref}`Snapd 2.56 <ref-release-notes_snapd-2-56-release-notes>`
* {ref}`Snapd 2.55 <ref-release-notes_snapd-2-55-release-notes>`
* {ref}`Snapd 2.54.2 <ref-release-notes_snapd-2-54-release-notes>`
* {ref}`Snapd 2.51 <ref-release-notes_snapd-2-51-release-notes>`
* {ref}`Snapd 2.50 <ref-release-notes_snapd-2-50-release-notes>`
* {ref}`Snapd 2.49 <ref-release-notes_snapd-2-49-release-notes>`
* {ref}`Snapd 2.48 <ref-release-notes_snapd-2-48-release-notes>`
* {ref}`Snapd 2.47 <ref-release-notes_snapd-2-47-release-notes>`
* {ref}`Snapd 2.46 <ref-release-notes_snapd-2-46-release-notes>`
* {ref}`Snapd 2.45 <ref-release-notes_snapd-2-45-release-notes>`
* {ref}`Snapd 2.44 <ref-release-notes_snapd-2-44-release-notes>`
* {ref}`Snapd 2.43 <ref-release-notes_snapd-2-43-release-notes>`
* {ref}`Snapd 2.42 <ref-release-notes_snapd-2-42-release-notes>`
* {ref}`Snapd 2.34.3 <ref-release-notes_snapd-2-34-3-release-notes>`
* {ref}`Snapd 2.33 <ref-release-notes_snapd-2-33-release-notes>`
* {ref}`Snapd 2.32 <ref-release-notes_snapd-2-32-release-notes>`
* {ref}`Snapd 2.30 <ref-release-notes_snapd-2-30-release-notes>`
* {ref}`Snapd 2.28 <ref-release-notes_snapd-2-28-release-notes>`
* {ref}`Snapd 2.27 <ref-release-notes_snapd-2-27-release-notes>`
* {ref}`Snapd 2.24 <ref-release-notes_snapd-2-24-release-notes>`
* {ref}`Snapd 2.23.6 <ref-release-notes_snapd-2-23-6-release-notes>`

## Release policy and schedule

The snapd package updates automatically, and by default, checks for updates 4 times a day. To manually update or modify this process, see {ref}`Managing updates <how-to-guides-work-with-snaps-manage-updates>`.

{ref}`Channels <explanation-how-snaps-work-channels-and-tracks>` are used to distinguish between stable releases, which are always available from the stable channel, and beta and testing releases, which can be installed from the candidate, beta and edge channels.

To install snapd from the beta channel, for example, use the following command:

```
sudo snap refresh snapd --beta
```

To ensure you receive latest security updates and bug fixes, ensure you upgrade to a new release of Snapd shortly after it is released.

For the release plan and complete list of changes, please refer to the {ref}`snapd roadmap <reference-release-notes>`. Feel free to provide your test feedback on the [forum](https://forum.snapcraft.io/c/snapd/5), or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug).

We greatly appreciate your contributions and support!

---

(ref-release-notes_snapd-2-79-release-notes)=
## Snapd 2.79

This release contains the 26.10 final content.

**Content targeting this release must be ready by 16 October 2026.**

**Update:**

This release was delayed because snapd was updated to the core26 base. That base inherited [Resolute's s390x jump to z15](https://bugs.launchpad.net/ubuntu-z-systems/+bug/2126577), which breaks snapd support for s390x z13. As a temporary solution, we are dropping snapd's move to the core26 base while we work on a solution. The beta and candidate dates have moved. The stable date is unchanged.

| Milestone | Status | Date |
|---|---|---|
| Beta | Pending | 17 November 2026 |
| Candidate | Pending | 26 November 2026 |
| Stable | Pending | 6 January 2027 |

(ref-release-notes_snapd-2-78-release-notes)=
## Snapd 2.78

*Released on 3 November 2026.*

This release contains the 26.10 update content.

### FDE

* Update the keyring and state after reprovision, and complete the decision flow for auto-repair and reprovision.
* Add memfd-secret-backed state for secrets.
* Update secboot to support Thunderbolt security level 0 on Ubuntu Core.

### Components and seed refresh

* Account for components when deciding whether a seed refresh is needed, and prevent seeded components from being removed.
* Set `SNAP_COMPONENTS` in snap application environments.
* Support sharing content from components with the `$SNAP_COMPONENT(...)` syntax.
* Improve seed-refresh prerequisites and disk-space checks, and attempt to refresh only essential snaps when a disk-space check fails.

### Interfaces

* Add the `ubuntu-drivers-observe` interface.
* `content`: support sharing content from components.
* `shutdown`: allow `RebootWithFlags`.
* `daemon-notify`: allow the disconnected `/systemd/notify` path.
* `microceph-support`: add the `user-identity-switching` plug attribute.
* `u2f-devices`: add the Gemalto eToken Fusion to the fallback list.
* `power-control`: allow standardized charge-threshold sysfs attributes.
* Fix system-key comparisons and AppArmor profile generation for paths containing spaces.

### Confdb

* Improve error messages for map keys in JSON config values.
* Support reading and writing to builtin confdbs.
* Enforce validation-set constraints before changing state.

### Packaging and security

* Add a downstream version suffix that can be manipulated independently of the full version.
* Work around `dh_golang` behavior and remove `prepare-debian-build-tree`.
* Optimize Perl and Python rules in the AppArmor template for core24+ snaps.
* Update security logging APIs to specify who performed an action, what happened, and why or why not.

### Other

* Add the `disk-reservation.size` option and migrate experimental disk-space checks.
* Remove unloaded mount units during snap removal and pass subsystem triggers to udev.
* Fix handling of kernels that occupy multiple boot partitions with the Little Kernel bootloader.
* Ensure recovery-mode reboots are always oneshots, hide recovery entries in hybrid GRUB menus, and improve hybrid remodeling.
* Add a seed allowlist when creating recovery systems.
* Merge selected internal tools into the multi-entry snapd binary.

### Experimental features

#### Graduated

- **quota-groups:** resource limits for snaps are now available without setting the experimental flag.

#### Enabled by default

- **refresh-app-awareness-ux:** enabled by default.

For the release plan and complete list of changes, please refer to the [full release notes](https://forum.snapcraft.io/t/the-snapd-roadmap/1973).

### Test feedback

Feel free to share your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast-track investigations, please include details about your system, the snapd version(s), and steps to reproduce the issue.

### Security reports

Please report security vulnerabilities in private. The [snapd security policy](https://github.com/canonical/snapd/blob/master/SECURITY.md) describes what qualifies and how to report it.

### Changelog

* FDE: update keyring after reprovision
* FDE: set new state after reprovision
* FDE: complete the decision for auto-repair/reprovision
* FDE: add memfd-secret backed state for secrets
* FDE: update secboot to rev dd95d85 - support thunderbolt security level 0 on UC
* components: account for components in seed refresh triggering
* components: prevent components in the seed from being removed
* components: set $SNAP_COMPONENTS in the application's environment, with the path to the snap's own components directory
* confdb: make error message on map keys for JSON config values more specific
* confdb: support reading/writing to builtin confdbs
* confdb: enforce validation set constraints before changing state
* remote device management: update the prepare-serial-request registration body to use hardware-id-key-sha3-384 field name
* packaging: introduce a downstream version suffix to manipulate rather than the full version
* packaging: workaround dh_golang, drop prepare-debian-build-tree
* security logging: change LogAdminActivity and LogUnauthorizedAccess api and structs to specify Who, What and Why/-Not
* interfaces: content | support for sharing content from components using the $SNAP_COMPONENT(...) syntax
* interfaces: shutdown | allow RebootWithFlags
* interfaces: daemon-notify | allow disconnected path /systemd/notify
* interfaces: microceph-support | add user-identity-switching plug attribute
* interfaces: u2f-devices | add Gemalto eToken Fusion to fallback list
* interfaces: ubuntu-drivers-observe | add new interface
* interfaces: power-control | allow standardized charge threshold sysfs attributes
* LP: #2161845 interfaces: fix snapd system-key comparison always failing
* LP: #2161950 interfaces: unity7 | allow Chromium StatusNotifierItem object paths
* LP: #2164382 interfaces: u2f-devices | use fido-id udev builtin to identify devices
* LP: #2164689 interfaces: {personal,system}-files | fix profile if path has spaces
* LP: #2106306 check user before deleting snap user data during snap removal
* LP: #2082384 Remove sequence file during snap removal
* Pass subsystem triggers to udev during snap removal
* Remove unloaded mount units during snap removal
* Attempt to refresh just essential snaps when disk space check fails
* Properly consider new and existing revisions during disk space checks
* Add disk-reservation.size option and migrate experimental disk space checks
* Optimize perl and python rules in apparmor template for core24+ snaps
* Fix same kernel occupying multiple boot partitions for Little Kernel bootloader
* Graduate quota-groups feature
* Enable by default refresh-app-awareness-ux feature
* Ensure that reboots into recovery mode are always oneshots
* Hide recovery mode entries in hybrid grub menu
* Fix hybrid remodeling when gadget defines a partition with a system-seed role
* Add seed allowlist to recovery-system creation
* Improve robustness of seed refresh prerequisites by properly merging them
* Merge selected internal tools into the multi-entry snapd binary

(ref-release-notes_snapd-2-77-release-notes)=
## Snapd 2.77

*Released to candidate on 20 August 2026*

This release contains the 26.10 image content.

*We discovered a regression that was addressed in snapd 2.77.1: https://github.com/canonical/snapd/pull/17492.*

### Changelog

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

### Snapd 2.77.1

*Released on 2 October 2026.*


Snapd 2.77.1 is the first stable release in the 2.77.x series, since the following blocking issue was found in 2.77:

* Fix undo of `unlink-component` after its snap revision was discarded. This is the regression that kept 2.77 from release. A refresh or removal that had to undo unlinking a component could fail once that revision was already gone.
* `power-control`: allow reading battery state files (low impact)

#### FDE

Snapd 2.77.1 carries the 26.10 FDE work for reprovision and post-install handling.

* A device can be reprovisioned without a factory reset. The release adds APIs for reprovision, for generating a recovery key as part of reprovision, and for post-install actions.
* Storage-encrypted system information is extended.
* Perform a reseal dry-run check after a snapd refresh
* Improve cleanup robustness of FDE tasks

#### Packaging and AppArmor

* Update the bundled AppArmor to 5.0.2, and accept the 5.0 ABI when snapd is running as a deb
* Build the deb with Go 1.23 on Noble and Jammy, and Go 1.22 on Focal
* Fix service startup during install, and session-agent socket handling, on Ubuntu 26.04 and later
* Use a relative symlink for `snapctl`, and update the steam-support udev rules

#### Interfaces

* New interfaces: `apparmor-observe`, `kernel-sched-ext-control`, `vsock` ([LP: #2161982](https://bugs.launchpad.net/snapd/+bug/2161982)), and `xdg-portal-permission-store`
* `content`: a plug now mounts the parallel instance that provides the slot ([LP: #1915709](https://bugs.launchpad.net/snapd/+bug/1915709))
* `docker`: allow connecting to the system-wide Docker socket on classic
* Make `polkit` and `upower` implicit on Ubuntu Core only
* `opengl`: expose WSL libraries
* Allow Wine to execute files opened through the Document Portal
* Allow `networkctl` and systemd-networkd link property changes
* Allow reading `/proc/self/smaps_rollup` ([LP: #2110510](https://bugs.launchpad.net/snapd/+bug/2110510))
* `network-control` and `network-manager`: allow a missing resolve1 link ([LP: #2143934](https://bugs.launchpad.net/snapd/+bug/2143934))

#### Other

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

#### Experimental features

##### Graduated

These experimental features have graduated. They are now always enabled.

- **layouts:** a snap can bind-mount, symlink, or place a tmpfs inside its mount namespace
- **classic-preserves-xdg-runtime-dir:** on classic, a snap keeps the session `XDG_RUNTIME_DIR` and can reach user-session services there
- **refresh-app-awareness:** snapd holds a refresh while that snap’s apps are running
- **dbus-activation:** a snap app or service can be started by D-Bus activation

##### Enabled by default

- **quota-groups:** resource limits for snaps are available without setting the experimental flag

##### In development

The following are still under active development and are not yet considered stable for general use.

- **confdb:** validation-sets support; fix data loss when writing to a new schema or account; run `observe-view-*` hooks after commit; sign-only external keypair backends; validate map keys in JSON config values ([LP: #2072331](https://bugs.launchpad.net/snapd/+bug/2072331))
- **Security logging:** log administrative actions, token create and remove events, and adding, updating, or removing a snapd user; strip trailing whitespace from audit message payloads ([LP: #2160691](https://bugs.launchpad.net/snapd/+bug/2160691))
- **Remote device management:** validate request messages, apply management messages, queue responses, and improve sequencing and redelivery

#### Test Feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

#### Security reports

Please report security vulnerabilities in private. The [snapd security policy](https://github.com/canonical/snapd/blob/master/SECURITY.md) describes what qualifies and how to report it.

#### Known issues

The bundled AppArmor update to 5.0.2 can cause issues on some outdated kernels. If you see issues related to network access, update your kernel to the latest version provided by your system. If you are using the EOL 25.04 version of Ubuntu, you cannot use 2.77.1 or any later version of the snapd snap. Add `SNAP_REEXEC=0` to `/etc/environment` to force using the deb package.

#### Changelog

* Fix undo of unlink-component after its snap revision was discarded
* interfaces: power-control | allow reading all battery state files

(ref-release-notes_snapd-2-76-release-notes)=
## Snapd 2.76

*Released on 1 July 2026.*

### Overview

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

### Components

Snapd 2.76 contains many enhancements to the components subsystem, providing greater transparency and stability for end users. Users can discover installed components directly through `snap info` and `snap list`, while several reliability fixes improve the experience around installation, refresh, and enable/disable workflows.

* Show hint in `snap list` that a snap has components
* List snap components in `snap-debug-info` via debug-tools
* Display detailed component information in `snap info`
* Fix download of private snap components by setting UserID ([LP: #2110368](https://bugs.launchpad.net/snapd/+bug/2110368))
* Fix snap enable/disable cycle forgetting components ([LP: #2147207](https://bugs.launchpad.net/snapd/+bug/2147207))
* Ensure existing snap confinement flags are not dropped when installing or removing components
* Improve `snapctl install` consistency when components are already installed
* Fix component installation for private snaps via `snapctl` ([LP: #2110368](https://bugs.launchpad.net/snapd/+bug/2110368))

### Mount namespace and layout

The 2.76 release continues to see improvements to how the mount namespace, the world view, of a snap is constructed and updated. Starting with 2.75, a mechanism was introduced for opportunistically discarding the mount namespace whenever a snap itself or one of its dependencies is updated. This ensures that snaps always start with the most up-to-date world view. In 2.76, this effort continued, ensuring that the mount namespace construction process itself is more robust and that snap features, such as content sharing and layouts, are applied in an orderly and predictable way, while squashing a number of bugs in the area.

* snap-update-ns: switch to a multi-pass process for constructing and updating mount namespaces
* Fix mount namespace updates with synthetic bind mounts on same target paths ([LP: #2144666](https://bugs.launchpad.net/snapd/+bug/2144666))

### Performance

Snapd 2.76 includes several targeted performance improvements that reduce overhead during common snap operations and speed up boot on Ubuntu Core devices.

* Reduce the number of AppArmor profile regenerations during snap operations
* Unroll CPU-heavy recursive function in snap state handlers
* Dispatch `systemctl` commands asynchronously when calling `Stop()`
* core-initrd: increase mount burst from 5 to 128 for faster boot
* core-initrd: add nfnetlink module to fix nf netlink socket speed regression ([LP: #2150773](https://bugs.launchpad.net/snapd/+bug/2150773))

### Security hardening

Snapd 2.76 hardens the snap-confine execution environment, addressing a memory safety issue and tightening security boundaries for BPF and mount operations.

* snap-confine: fix out-of-bounds read in mountinfo parser for partial escape sequences
* snap-confine: harden bpffs mount with `nosuid`, `nodev`, `noexec` flags
* snap-confine: set `FD_CLOEXEC` on file descriptors returned by BPF helpers
* snap-confine: remove experimental persistent per-user mount namespace feature

### Features in development

The following features are under active development and included in this release as building blocks for upcoming functionality. They are not yet considered stable for general use.

* **snap deltas:** introduces internal tooling for generating and applying binary deltas between snap revisions; supports the existing `xdelta3` format and adds the new `snap-1-1-xdelta3` format with improved compression of the squashfs artefact
* **[confdb](https://snapcraft.io/docs/confdb-configuration-management):** block concurrent confdb accesses; allow only API admin read access to confdb secrets; support `--wait-for` timeouts
* **[AppArmor prompting](https://snapcraft.io/install/prompting-client/ubuntu):** re-enable the prompting notice backend; validate permissions while unmarshalling; escape paths in prompt constraints; respond with full user-allowed permission set
* **remote device management:** support remote device management with the `dispatch-mgmt-messages` task with sequencing support
* **dm-verity:** add helper for validating integrity data; copy integrity data files during snap install
* **Security audit logging:** add security audit logging subsystem
* **openshell:** allow `openshell` snap to use experimental `daemon-scope: user`

### Other

* **mounts:** ensure `/tmp/.X11-unix` created inside mount namespace has correct permissions; allow configuring mount unit options based on filesystem type; `RemoveMountUnitFile` now unmounts even if mount unit file is missing
* **interfaces:** new `podman` interface for podman socket access; `docker` plug now implicit on classic systems; bluez: drop explicit `deny send_destination` in D-Bus configuration; disallow auto-connect to parallel installs; restore auto-connections on failed refresh undo; conditionally deny `/proc/self/mountinfo` to suppress Go 1.25+ denials; support deep SoC sysfs paths for LED brightness in bool-file ([LP: #2148544](https://bugs.launchpad.net/snapd/+bug/2148544)); stricter validation for content interface plugs and layout entries now applies to snaps using bases core26 (or later) and bare. For snaps using a content interface plug, or a layout entry (bind, bind-file or tmpfs) where the target path resides under `$SNAP`, the target path's presence is now mandatory and enforced during snap installation or refresh.
* **FDE:** deprecate `check-pin`/`passphrase` API actions; move auto-repair logic to `overlord/fdestate`; update secboot for TPM/FDE bug fixes including Intel HAP and recovery key parsing; give inactive state on classic ([LP: #2147606](https://bugs.launchpad.net/snapd/+bug/2147606))
* **snap CLI:** allow removing a snap and its base at the same time; avoid empty channel forwarding message ([LP: #2125344](https://bugs.launchpad.net/snapd/+bug/2125344)); clarify `snap install` help text for `--classic` and `--devmode` ([LP: #2150683](https://bugs.launchpad.net/snapd/+bug/2150683)); print complex attributes in `snap interface --attrs` output ([LP: #2152908](https://bugs.launchpad.net/snapd/+bug/2152908))
* **packaging:** FIPS bootstrap and dispatch via `snap-fips-dispatch`; add cross-distro build script; update bundled AppArmor to 4.1.7; drop transitional packages for Ubuntu 26.04; make Ubuntu 16.04 packaging dep17 compliant ([LP: #2139213](https://bugs.launchpad.net/snapd/+bug/2139213))
* Update seccomp syscalls list for kernel 7.1.0
* Improve handling of failed downloads and retain partial files for resume ([LP: #2146337](https://bugs.launchpad.net/snapd/+bug/2146337))
* Skip redundant xdg-settings confirmation prompt when setting is already correct ([LP: #1966067](https://bugs.launchpad.net/snapd/+bug/1966067))

### Test Feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

### Changelog

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
* Add base prioritized AppArmmor snippets for strictly confined or jailed snaps
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

### Snapd 2.76.1 (Security Release)

*Released on 23 July 2026.*

* CVE-2024-5300
* CVE-2026-8933
* CVE-2026-15226

### Snapd 2.76.2

*Released on 11 August 2026.*

* interfaces: steam-support, docker-support | fix mountinfo denial

### Snapd 2.76.3

*Released to candidate on 20 August 2026.*

The snapd 2.76.3 Debian packages were released to Jammy, Noble and Resolute.

#### Overview

Snapd 2.76.3 delivers the final 26.04.1 content. It includes the 2.76.2 mountinfo regression fix that was previously released as a snap only. It includes:

* FDE (Full Disk Encryption) install-time passphrase/PIN support, first-boot keyboard configuration, and a requirement for volume authentication when a hardware root of trust is missing
* The 2.76.2 mountinfo regression fix for Steam and Docker snaps
* Packaging and hook-ordering fixes

#### FDE

Snapd 2.76.3 completes the remaining 26.04.1 FDE objectives for install and first boot. It adds passphrase and PIN support for volume authentication, allowing installation to continue when a hardware root of trust is missing. It also adds support for applying the selected keyboard layout on first boot so Plymouth uses the correct layout before snapd is running.

#### Other

* Cross-distro: modify SELinux policy to use `init_named_socket_activation()` for allowing systemd to start snapd through socket activation; packaging: make sure that `usr/bin/snap` is built with correct build tags on debian sid
* Ensure profiles are set up before running `prepare-{slot,plug}*` hooks

#### Test feedback

Feel free to provide your test feedback here or directly in Launchpad. To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

#### Changelog

* FDE: support keyboard configuration at install-time for first-boot
* FDE: re-enable passphrases/PINs at install-time
* FDE: require volumes authentication if HWROT is missing
* FDE: bump secboot to rev 457b03a16d19
* FDE: use new secboot API for reprovision TPM
* Cross-distro: modify SELinux policy to use init_named_socket_activation() for allowing systemd to start snapd through socket activation
* packaging: make sure that usr/bin/snap is built with correct build tags on debian sid
* Ensure profiles are setup before running prepare-{slot, plug}* hooks

(ref-release-notes_snapd-2-75-release-notes)=
## Snapd 2.75

*Not released, superseded by 2.75.1.*

* FDE: run early boot check only once per boot
* FDE: update secboot to revision 77bc2457cc76
* FDE: add degraded state for status API
* FDE: prevent resealing tasks from running together
* FDE: enable using keyslot tokens to store protected keys for UC26+
* FDE: early commit kcmdline config transaction in update-gadget-cmdline to mitigate possible race condition
* FDE: ensure extra snapd kcmdline fragments are applied
* FDE: remove old secboot activation API calls
* LP: #2142130 update apparmor parser to 4.1.7
* LP: #2137543 disable translations in formatted output for snapctl services
* LP: #2142655 improve snap size reporting precision in `snap info` output
* LP: #2139664 snap-confine: remove race condition triggered by hat profile
* LP: #2139065 skip 70-snap.*.rules when building dracut initramfs
* LP: #2002697 error early on removal without purge if home is in NFS mount
* LP: #2141461 Intefaces: allow snap-update-ns to read /proc/pid/auxv
* LP: #2138268 Interfaces: kerberos-tickets| new interface allow access to kerberos tickets stored in /tmp
* Interfaces: block-devices| allow Xen block devices
* Interfaces: u2f-devices| add Tokey 3 FIDO
* Interfaces: devlxd| new interface allowing acccess to LXD devlxd socket and APIs
* Interfaces: browser-support| allow reading pressure stall info information
* Interfaces: network-setup-control| allow additional netplan files access
* Interfaces: desktop| allow access kvantum, lxqt, and gtk4 configuration files
* Interfaces: system-observe| allow fdinfo access for GPU monitoring
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
* snap-bootstrap: use libblkid for disk information to speed up boot
* snap-confine: improve data handling error
* snap-confine: use ld cache from the app base for core26+
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
* Keep minidebuginfo in snapd snap
* Make snap-specific systemd cgroup mandatory for snaps using core26 and later, improve messaging for failure scenarios
* Preserve stale connections of broken snaps
* Remove enforce-validation-sets need for network
* Opportunistic discarding of mount namespace when updating slot providers
* Support for delaying updates of snap mount namespaces when refreshing slot providers
* Use application CommonID as default source for desktop ID

### Snapd 2.75.1

*Not released, superseded by 2.75.2.*

* FDE: limit number of boot check log entries
* Allow a logged in user to refresh private snaps during a refresh with multiple snaps
* Use precise prune pattern for tmpfiles (CVE-2026-3888)

### Snapd 2.75.2

*Released on 23 April 2026.*

#### Overview

Snapd 2.75.2 includes the content of 2.75 and 2.75.1, which were not released.

* Bug fixes and robustness improvements
* [Permissions Prompting](https://snapcraft.io/install/prompting-client/ubuntu) support for audio-record prompting via the snapd API

#### Notable updates

* Use precise prune pattern for tmpfiles (CVE-2026-3888)
* AppArmor parser updated to 4.1.7 ([LP: #2142130](https://bugs.launchpad.net/snapd/+bug/2142130))
* Disable translations in formatted output for snapctl services ([LP: #2137543](https://bugs.launchpad.net/snapd/+bug/2137543))
* Improve snap size reporting precision in `snap info` output ([LP: #2142655](https://bugs.launchpad.net/snapd/+bug/2142655))
* snap-confine: remove race condition triggered by hat profile ([LP: #2139664](https://bugs.launchpad.net/snapd/+bug/2139664))
* Skip 70-snap.*.rules when building dracut initramfs ([LP: #2139065](https://bugs.launchpad.net/snapd/+bug/2139065))
* Error early on removal without purge if home is in NFS mount ([LP: #2002697](https://bugs.launchpad.net/snapd/+bug/2002697))
* Interfaces: allow snap-update-ns to read /proc/pid/auxv ([LP: #2141461](https://bugs.launchpad.net/snapd/+bug/2141461))
* Interfaces: kerberos-tickets | new interface allowing access to kerberos tickets stored in /tmp ([LP: #2138268](https://bugs.launchpad.net/snapd/+bug/2138268))
* Keep minidebuginfo in the snapd snap
* squashfs: reduce memory footprint of single file extraction
* Add `snap component` command

#### Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

#### Changelog

* Interfaces: network-setup-*| allow running python binaries from the base on UC26+
* Cross-distro: modify SELinux policy to allow mounting on `/var/snap/\<snap\>/\<rev\>`
* Fix potential task deadlock by considering all tasks in a lane that might be waiting for a reboot when processing delayed security backend effects

(ref-release-notes_snapd-2-74-release-notes)=
## Snapd 2.74

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

### Snapd 2.74.1

*Released on 19 March 2026.*

#### Overview

Snapd 2.74.1 delivers TPM-backed Full Disk Encryption (FDE) to Resolute (26.04). It includes the content of 2.74, which was not released.

* Delivers TPM-backed full-disk encryption (FDE) with support for third-party NVIDIA kernel modules in Resolute for Classic Hybrid systems (Classic Ubuntu with Kernel and Gadget snaps)
* Bug fixes and robustness improvements
* Interface additions supporting new and emerging use cases
* Additions for other work-in-progress features, including:
  * [Confdb](https://snapcraft.io/docs/confdb-configuration-management) and related remote device-management capabilities
  * [AppArmor prompting](https://snapcraft.io/install/prompting-client/ubuntu) for camera access

#### Notable updates

* FDE: reuse preinstall check context during install to account for user-ignored errors ([LP: #2141328](https://bugs.launchpad.net/snapd/+bug/2141328))
* FDE: fix db updates by allowing multiple payloads ([LP: #2139611](https://bugs.launchpad.net/snapd/+bug/2139611))
* snap-confine: add CAP_SYS_RESOURCE to allow raising memory lock limit when required ([LP: #2139300](https://bugs.launchpad.net/snapd/+bug/2139300))
* snap-confine: bump the max element count of the BPF map used to store IDs of allowed/matched devices to 1000 ([LP: #2139099](https://bugs.launchpad.net/snapd/+bug/2139099))
* Desktop: revert change that caused user daemons declaring the desktop plug to implicitly depend on graphical-session.target ([LP: #2141607](https://bugs.launchpad.net/snapd/+bug/2141607))
* Preseeding: add support for preseeding of hybrid systems via the installer API ([LP: #2116949](https://bugs.launchpad.net/ubuntu/+source/snapd/+bug/2116949))
* snap: add support for `snap refresh --tracking` ([LP: #2068493](https://bugs.launchpad.net/snapd/+bug/2068493))
* snap-confine: handle potential race when creating /tmp/snap-private-tmp when lacking systemd-tmpfiles support ([LP: #2134364](https://bugs.launchpad.net/snapd/+bug/2134364))

For an overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146). You are welcome to try it out for yourself using the [Resolute Daily Installer Image](https://cdimage.ubuntu.com/daily-live/current/resolute-desktop-amd64.iso).

#### Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

#### Changelog

* FDE: measure DeployedMode and AuditMode variables if they appear as disabled in the event log to avoid a potential reseal-failure boot loop
* LP: #2141328 FDE: reuse preinstall check context during install to account for user-ignored errors
* LP: #2139611 FDE: fix db updates by allowing multiple payloads
* LP: #2139300 snap-confine: add CAP_SYS_RESOURCE to allow raising memory lock limit when required
* LP: #2139099 snap-confine: bump the max element count of the BPF map used to store IDs of allowed/matched devices to 1000
* LP: #2141607 Desktop: revert change that caused user daemons declaring the desktop plug to implicitly depend on graphical-session.target
* Interfaces: Added pidfd_open and memfd_secret to seccomp template
* Interfaces: camera | add locking permission for /dev/video

(ref-release-notes_snapd-2-73-release-notes)=
## Snapd 2.73

*Released on 9 January 2026.*

### Overview
Snapd 2.73 does not introduce new user-facing features. Instead, it provides:

* Bug fixes and robustness improvements
* Interface additions supporting new and emerging use cases
* Building blocks for several work-in-progress features, including:
  * [TPM-backed Full Disk Encryption](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146) (FDE)
  * [Confdb](https://snapcraft.io/docs/confdb-configuration-management) and related remote device-management capabilities
  * [AppArmor prompting](https://snapcraft.io/install/prompting-client/ubuntu) for camera access

These changes are intended to improve reliability today while preparing the ground for upcoming releases.

### Notable updates

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

### Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) snapd version(s) and (3) steps to reproduce the issue.

### Changelog

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

(ref-release-notes_snapd-2-72-release-notes)=
## Snapd 2.72

*Released on 21 October 2025*

### Highlights

* Enable the gpio-chardev interface now with the more robust gpio-aggregator configfs kernel interface ([LP: #1916244](https://bugs.launchpad.net/snapd/+bug/1916244))
* FDE enhancements and additions: add generic reseal function and correct sealing with kernel command line defaults, support replacing TPM protected keys at runtime, secboot preinstall check fix actions and using OPTEE (Ubuntu Core & arm) for protecting keys, as an alternative to existing fde-setup hooks.

### Notable updates

* snap-confine: fix non-suid limitation by switching to root:root to operate v1 freezer
* Fix preseeding failure due to scan-disk issue on RPi
* Snap installation: skip snap icon download when running in a cloud or using a proxy store ([LP: #2122054](https://bugs.launchpad.net/snapd/+bug/2122054))
* snap-confine: fix error message with /root/snap not accessible ([LP: #2117558](https://bugs.launchpad.net/snapd/+bug/2117558))
* Interfaces: do not expose Kerberos tickets for classic snaps ([LP: #2121238](https://bugs.launchpad.net/snapd/+bug/2121238))
* Cleanly support socket activation for classic snap ([LP: #2117121](https://bugs.launchpad.net/snapd/+bug/2117121))
* Improve progress reporting for snap install/refresh ([LP: #2112626](https://bugs.launchpad.net/snapd/+bug/2112626))
* Extend output to indicate when snap data snapshot was created during remove ([LP: #2114704](https://bugs.launchpad.net/snapd/+bug/2114704))

For the release plan and complete list of changes, please refer to the [full release notes](https://forum.snapcraft.io/t/the-snapd-roadmap/1973).

### More about GPIO Chardev

This release supports the kernel GPIO character device API with specific GPIO lines mediation through the new gpio-chardev interface which offers more fine-grained control over the gpio-control interface that allowed unrestricted access to all GPIO chips when needed.

For historical context: traditionally Snapd supported mediation of the sysfs interface for GPIO access. This sysfs kernel interface is considered legacy by upstream kernel developers (and will be removed from UC26+ kernels) and it has been replaced by a new character device API, commonly referred to as gpiod.

The new kernel GPIO APIs are typically consumed through the libgpiod library (C or various bindings) or a set of command line utilities provided by said library.

For more information on how to use the new interface (and migration from the older gpio interface), please check the official documentation for the {ref}`gpio-chardev interface <interfaces-gpio-chardev>`.

### More about our FDE journey

***The previous release***, 2.71, concluded the Snapd contribution to TPM FDE for the 25.10 [install image](https://releases.ubuntu.com/25.10/ubuntu-25.10-desktop-amd64.iso).

Progression through the 25.10 cycle up to 2.71:
* 2.68.* - introduced a new key format, added support for passphrases during installation, and included various fixes.
* 2:70 - set roles in TPM keys and fixed resealing with the v1 hook key format.
* 2.71 - added recovery key auto-repair, delivered many additional APIs needed to support installation and use of TPM-backed FDE on hybrid Ubuntu 25.10, and included further fixes.

As part of this work, secboot has been improved to more extensively check whether the platform can support secure boot, which is used by one of the new Snapd APIs introduced in 2.71 and used by the installer to determine TPM FDE availability during hybrid Ubuntu installation.

***This release***, along with releases 2.73 and 2.74 planned for next cycle, will extend and refine the TPM FDE hybrid Ubuntu installation and overall user experience for the Ubuntu 26.04 LTS release.

A lot of care goes into continually ensuring compatibility with Ubuntu Core, previous versions of Snapd and targeted hardware. Each release must pass extensive testing, including test suites for certified hardware. In addition to our own rigorous testing, we strongly advise all users to also thoroughly test all their hardware variations and inform us of potential issues or concerns as soon as possible.

For a broader overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146)

### Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) Snapd version(s) and (3) steps to reproduce the issue.

### Changelog

* FDE: support replacing TPM protected keys at runtime via the /v2/system-volumes endpoint
* FDE: support secboot preinstall check fix actions for 25.10+ hybrid installs via the /v2/system/{label} endpoint
* FDE: tweak polkit message to remove jargon
* FDE: ensure proper sealing with kernel command line defaults
* FDE: provide generic reseal function
* FDE: support using OPTEE for protecting keys, as an alternative to existing fde-setup hooks (Ubuntu Core only)
* Confdb: 'snapctl get --view' supports passing default values
* Confdb: content sub-rules in confdb-schemas inherit their parent rule's "access"
* Confdb: make confdb error kinds used in API more generic
* Confdb: fully support lists and indexed paths (including unset)
* Prompting: add notice backend for prompting types (unused for now)
* Prompting: include request cgroup in prompt
* Prompting: handle unsupported xattrs
* Prompting: add permission mapping for the camera interface
* Notices: read notices from state without state lock
* Notices: add methods to get notice fields and create, reoccur, and deepcopy notice
* Notices: add notice manager to coordinate separate notice backends
* Notices: support draining notices from state when notice backend registered as producer of a particular notice type
* Notices: query notice manager from daemon instead of querying state for notices directly
* Packaging: Ubuntu | ignore .git directory
* Packaging: FIPS | bump deb Go FIPS to 1.23
* Packaging: snap | bump FIPS toolchain to 1.23
* Packaging: debian | sync most upstream changes
* Packaging: debian-sid | depends on libcap2-bin for postint
* Packaging: Fedora | drop fakeroot
* Packaging: snap | modify snapd.mk to pass build tags when running unit tests
* Packaging: snap | modify snapd.mk to pass nooptee build tag
* Packaging: modify Makefile.am to fix snap-confine install profile with 'make hack'
* Packaging: modify Makefile.am to fix out-of-tree use of 'make hack'
* LP: #2122054 Snap installation: skip snap icon download when running in a cloud or using a proxy store
* Snap installation: add timeout to http client when downloading snap icon
* Snap installation: use http(s) proxy for icon downloads
* LP: #2117558 snap-confine: fix error message with /root/snap not accessible
* snap-confine: fix non-suid limitation by switching to root:root to operate v1 freezer
* core-initrd: do not use writable-paths when not available
* core-initrd: remove debian folder
* LP: #1916244 Interfaces: gpio-chardev | re-enable the gpio-chardev interface now with the more robust gpio-aggregator configfs kernel interface
* Interfaces: gpio-chardev | exclusive snap connections, raise a conflict when both gpio-chardev and gpio are connected
* Interfaces: gpio-chardev | fix gpio-aggregator module load order
* Interfaces: ros-snapd-support | grant access to /v2/changes
* Interfaces: uda-driver-libs, egl-driver-libs, gbm-driver-libs, opengl-driver-libs, opengles-driver-libs | new interfaces to support nvidia driver components
* Interfaces: microstack-support | allow DPDK (hugepage related permissions)
* Interfaces: system-observe | allow reading additional files in /proc, needed by node-exporter
* Interfaces: u2f | add Cano Key, Thesis FIDO2 BioFP+ Security Key and Kensington VeriMark DT Fingerprint Key to device list
* Interfaces: snap-interfaces-requests-control | allow shell API control
* Interfaces: fwupd | allow access to Intel CVS sysfs
* Interfaces: hardware-observe | allow read access to Kernel Samepage Merging (KSM)
* Interfaces: xilinx-dma | support Multi Queue DMA (QDMA) IP
* Interfaces: spi | relax sysfs permission rules to allow access to SPI device node attributes
* Interfaces: content | introduce compatibility label
* LP: #2121238 Interfaces: do not expose Kerberos tickets for classic snaps
* Interfaces: ssh-public-keys | allow ro access to public host keys with ssh-key
* Interfaces: Modify AppArmor template to allow listing systemd credentials and invoking systemd-creds
* Interfaces: modify AppArmor template with workarounds for Go 1.35 cgroup aware GOMAXPROCS
* Interfaces: modify seccomp template to allow landlock_*
* Prevent snap hooks from running while relevant snaps are unlinked
* Make refreshes wait before unlinking snaps if running hooks can be affected
* Fix systemd unit generation by moving "WantedBy=" from section "unit" to "install"
* Add opt-in logging support for snap-update-ns
* Unhide 'snap help' sign and export-key under Development category
* LP: #2117121 Cleanly support socket activation for classic snap
* Add architecture to 'snap version' output
* Add 'snap debug api' option to disable authentication through auth.json
* Show grade in notes for 'snap info --verbose'
* Fix preseeding failure due to scan-disk issue on RPi
* Support 'snap debug api' queries to user session agents
* LP: #2112626 Improve progress reporting for snap install/refresh
* Drop legacy BAMF_DESKTOP_FILE_HINT in desktop files
* Fix /v2/apps error for root user when user services are present
* LP: #2114704 Extend output to indicate when snap data snapshot was created during remove
* Improve how we handle emmc volumes
* Improve handling of system-user extra assertions

(ref-release-notes_snapd-2-71-release-notes)=
## Snapd 2.71

*Released on 20 August 2025*

### Highlights

* Support for TPM backed Full Disk Encryption on Ubuntu 25.10

### Notable updates

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

### More about TPM backed FDE on Ubuntu Core and Ubuntu 25.10

To support hybrid Ubuntu 25.10+ systems, we’ve introduced a new key format. On Ubuntu Core this change is transparent to users, but it enables us to transition from file-based key storage to storing keys in the LUKS2 header (with header redundancy) on core26.

On previous versions of Ubuntu Core, once a reboot required a recovery key, the device would continue prompting for that key on every subsequent boot. This could be particularly problematic for unattended or remote devices. This behavior was improved so that after a firmware update, entering the recovery key triggers an automatic repair and restores normal unattended boot operation without further prompts.

The [fwupd](https://snapcraft.io/fwupd) tool is available both as a deb and as a snap providing a unified way to install and manage system firmware updates. Support has been added for updating the UEFI DBX (UEFI Secure Boot forbidden signatures database) without requiring a recovery key on reboot. This ensures that both hybrid Ubuntu 25.10+ and Ubuntu Core devices with Full Disk Encryption seamlessly apply DBX updates.

For an overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146)

### Changelog

* FDE: auto-repair when recovery key is used
* FDE: revoke keys on shim update
* FDE: revoke old TPM keys when dbx has been updated
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
* snap-confine: workaround for glibc fchmodat() fallback and handle ENOSYS
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
* Interfaces: timezone-control | extend to support timedatectl varlink
* Interfaces: cpu-control | fix rules for accessing IRQ sysfs and procfs directories
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
* Packaging: disable optee when using nooptee build tag
* Packaging: add support for static PIE builds in snapd.mk, drop pie.patch from openSUSE
* Packaging: add libcap2-bin runtime dependency for ubuntu-16.04
* Packaging: use snapd.mk for packaging on Fedora
* Packaging: exclude .git directory
* Packaging: fix DPKG_PARSECHANGELOG assignment
* Packaging: fix building on Fedora with dpkg installed

(ref-release-notes_snapd-2-70-release-notes)=
## Snapd 2.70

*Released on 8 July 2025*

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

Please note that 2.70 includes all the changes in the superseded 2.69 and 2.69.1 releases.

### Changelog

* FDE: Fix reseal with v1 hook key format
* FDE: set role in TPM keys
* AppArmor prompting (experimental): add handling for expired requests or listener in the kernel
* AppArmor prompting: log the notification protocol version negotiated with the kernel
* AppArmor prompting: implement notification protocol v5 (manually disabled for now)
* AppArmor prompting: register listener ID with the kernel and resend notifications after snapd restart (requires protocol v5+)
* AppArmor prompting: select interface from metadata tags and set request interface accordingly (requires protocol v5+)
* AppArmor prompting: include request PID in prompt
* AppArmor prompting: move the max prompt ID file to a subdirectory of the snap run directory
* AppArmor prompting: avoid race between closing/reading socket fd
* Confdb (experimental): make save/load hooks mandatory if affecting ephemeral
* Confdb: clear tx state on failed load
* Confdb: modify 'snap sign' formats JSON in assertion bodies (e.g. confdb-schema)
* Confdb: add NestedEphemeral to confdb schemas
* Confdb: add early concurrency checks
* Simplify building Arch package
* Enable snapd.apparmor on Fedora
* Build snapd snap with libselinux
* Emit snapd.apparmor warning only when using apparmor backend
* When running snap, on system key mismatch e.g. due to network attached HOME, trigger and wait for a security profiles regeneration
* Avoid requiring state lock to get user, warnings, or pending restarts when handling API requests
* Start/stop ssh.socket for core24+ when enabling/disabling the ssh service
* Allow providing a different base when overriding snap
* Modify snap-bootstrap to mount snapd snap directly to /snap
* Modify snap-bootstrap to mount /lib/{modules,firmware} from snap as fallback
* Modify core-initrd to use systemctl reboot instead of /sbin/reboot
* Copy the initramfs 'manifest-initramfs.yaml' to initramfs file creation directory so it can be copied to the kernel snap
* Build the early initrd from installed ucode packages
* Create drivers tree when remodeling from UC20/22 to UC24
* Load gpio-aggregator module before the helper-service needs it
* Run 'systemctl start' for mount units to ensure they are run also when unchanged
* Update godbus version to 'v5 v5.1.0'
* Add support for POST to /v2/system-info with system-key-mismatch indication from the client
* Add 'snap sign --update-timestamp' flag to update timestamp before signing
* Add vfs support for snap-update-ns to use to simulate and evaluate mount sequences
* Add refresh app awareness debug logging
* Add snap-bootstrap scan-disk subcommand to be called from udev
* Add feature to inject proxy store assertions in build image
* Add OP-TEE bindings, enable by default in ARM and ARM64 builds
* Fix systemd dependency options target to go under 'unit' section
* Fix snap-bootstrap reading kernel snap instead of base resulting in bad modeenv
* Fix a regression during seeding when using early-config
* LP: #2107443 reset SHELL to /bin/bash in non-classic snaps
* Make Azure kernels reboot upon panic
* Fix snap-confine to not drop capabilities if the original user is already root
* Fix data race when stopping services
* Fix task dependency issue by temporarily disable re-refresh on prerequisite updates
* Fix compiling against op-tee on armhf
* Fix dbx update when not using FDE
* Fix potential validation set deadlock due to bases waiting on snaps
* LP: #2104066 Only cancel notices requests on stop/shutdown
* Interfaces: bool-file | fix gpio glob pattern as required for '[XXXX]*' format
* Interfaces: system-packages-doc | allow access to /usr/local/share/doc
* Interfaces: ros-snapd-support interface | added new interface
* Interfaces: udisks2 | allow chown capability
* Interfaces: system-observe | allow reading cpu.max
* Interfaces: serial-port | add ttyMAXX to allowed list
* Interfaces: modified seccomp template to disallow 'O_NOTIFICATION_PIPE'
* Interfaces: fwupd | add support for modem-manager plugin
* Interfaces: gpio-chardev | make unsupported and remove experimental flag to hide this feature until gpio-aggregator is available
* Interfaces: hardware-random | fix udev match rule
* Interfaces: timeserver-control | extend to allow timedatectl timesync commands
* Interfaces: add symlinks backend

(ref-release-notes_snapd-2-69-release-notes)=
## Snapd 2.69

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
* Non-suid snap-confine: first phase to replace snap-confine suid with capabilities to achieve the required permissions
* Initial changes for dynamic security profiles updates
* Provide snap icon fallback for /v2/icons without requiring network access at runtime
* Add eMMC gadget update support
* Support reexec when using /usr/libexec/snapd on the host (Arch Linux, openSUSE)
* Auto detect snap mount dir location on unknown distributions
* Modify snap-confine AppArmor template to allow all glibc HWCAPS subdirectories to prevent launch errors
* LP: #2102456 update secboot to bf2f40ea35c4 and modify snap-bootstrap to remove usage of go templates to reduce size by 4MB
* Fix snap-bootstrap to mount kernel snap from /sysroot/writable/system-data
* LP: #2106121 fix snap-bootstrap busy loop
* Fix encoding of time.Time by using omitzero instead of omitempty (on go 1.24+)
* Fix setting snapd permissions through permctl for openSUSE
* Fix snap struct json tags typo
* Fix snap pack configure hook permissions check incorrect file mode
* Fix gadget snap reinstall to honor existing sizes of partitions
* Fix to update command line when re-executing a snapd tool
* Fix 'snap validate' of specific missing newline and add error on missed case of 'snap validate --refresh' without another action
* Workaround for snapd-confine time_t size differences between architectures
* Disallow pack and install of snapd, base and os with specific configure hooks
* Drop udev build dependency that is no longer required and add missing systemd-dev dependency
* Build snap-bootstrap with nomanagers tag to decrease size by 1MB
* Interfaces: polkit | support custom polkit rules
* Interfaces: opengl | LP: #2088456 fix GLX on nvidia when xorg is confined by AppArmor
* Interfaces: log-observe | add missing udev rule
* Interfaces: hostname-control | fix call to hostnamectl in core24
* Interfaces: network-control | allow removing created network namespaces
* Interfaces: scsi-generic | re-enable base declaration for scsi-generic plug
* Interfaces: u2f | add support for Arculus AuthentiKey

### Snapd 2.69.1

*Not released to stable; superseded by Snapd 2.70.*

The current release candidate for 2.69.1 requires a fix for [LP: #2109843](https://bugs.launchpad.net/snapd/+bug/2109843). To ensure we continue delivering the latest changes in a timely manner, we’ve decided to supersede the 2.69.1 candidate with 2.70. It will include the bug fix, additional improvements, and help align with our release plan for the 25.10 cycle.

* AppArmor prompting (experimental): avoid race between closing/reading socket fd
* Fix potential validation set deadlock due to bases waiting on snaps
* [LP: #2104066](https://bugs.launchpad.net/snapd/+bug/2104066) Only cancel notices requests on Stop/shutdown
* Run 'systemctl start' for mount units to ensure they are run also when unchanged
* Interfaces: timeserver-control | allow timedatectl timesync commands

(ref-release-notes_snapd-2-68-release-notes)=
## Snapd 2.68

The official release for this version was Snapd 2.68.4.

### Highlights

* [FDE](https://ubuntu.com/core/docs/full-disk-encryption): Add support for a new and more extensible key format and passphrases for encrypted partitions can now be specified during installation
* {ref}`Components <how-to-guides-manage-snaps-using-components>`: Support online/offline [remodeling](https://ubuntu.com/core/docs/remodelling) and the creation of new recovery systems for models that contain components, on Ubuntu Core as well as Hybrid systems. Components are useful for distributing optional resources for a snap, such as debug symbols alongside snap binaries, and kernel modules alongside a kernel snap.
* [Kernel Components](https://documentation.ubuntu.com/snapcraft/stable/reference/components/): Make kernel components and modules available in early boot
* Interfaces: Added {ref}`auditd-support interface <interfaces-auditd-support>` that allows a snap to ship auditd as part of a snap and `checkbox-support` interface that allows unrestricted access to devices when testing with checkbox

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

### Changelog

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

### Snapd 2.68.1

*Released to beta on 24 February 2025.*

* Fix snap-confine type specifier type mismatch on armhf

### Snapd 2.68.2

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

### Snapd 2.68.3

*Released to candidate on 29 March 2025.*

#### Highlights

* [FDE](https://ubuntu.com/core/docs/full-disk-encryption): Add support for a new and more extensible key format and passphrases for encrypted partitions can now be specified during installation.
* [Components](https://snapcraft.io/docs/components): Support online/offline [remodeling](https://ubuntu.com/core/docs/remodelling) and the creation of new recovery systems for models that contain components, on Ubuntu Core as well as Hybrid systems. Components are useful for distributing optional resources for a snap, such as debug symbols alongside snap binaries, and kernel modules alongside a kernel snap.
* [Kernel Components](https://canonical-snapcraft.readthedocs-hosted.com/en/stable/reference/components.html): Make kernel components and modules available in early boot.
* Interfaces: Added the [auditd-support interface](https://snapcraft.io/docs/auditd-support-interface), which allows a snap to ship auditd as part of a snap, and the `checkbox-support` interface, which allows unrestricted access to devices when testing with checkbox.

#### Notable updates

* Fix issue preventing hybrid systems from being seeded on first boot
* Modify AppArmor template to allow using setpriv to run ([LP: #2072987](https://bugs.launchpad.net/snapd/+bug/2072987))
* Disable udev backend when inside a container ([LP: #1712808](https://bugs.launchpad.net/snapd/+bug/1712808))
* Remove auto-import udev rules not required by the deb package to avoid unwanted syslog errors ([LP: #1966203](https://bugs.launchpad.net/snapd/+bug/1966203))
* Fix progress reporting when stdout is on a tty, but stdin is not ([LP: #1886414](https://bugs.launchpad.net/ubuntu/+source/chromium-browser/+bug/1886414))

#### Experimental features

* Removed the stale `robust-mount-namespace-updates` experimental flag
* Removed the rejected `snapd-snap` experimental feature and its feature flag

#### Impact on Ubuntu Core using Full Disk Encryption

If you are planning to test or use this snapd release and you are using full disk encryption (with both hooks and TPM), some updates to your kernel snap are needed:

* If you maintain your own kernel snap, you will need to include the new snap-bootstrap.
* If you are using a kernel snap maintained by Canonical, all Canonical kernel snaps will be updated to the new version of snap-bootstrap in due course.

Until all kernel snaps are updated, snapd from latest/edge cannot be used for installation or remodeling if you are using FDE. If you have not updated the kernel snap, do not report bugs you encountered when:
* Remodeling with a snapd from latest/edge, then doing factory reset.
* Installing fresh images with snapd from latest/edge

However, please do report bugs if you find issues when:
* You updated to snapd to the latest/edge.
* You reverted from a snapd coming from latest/edge.

#### Changelog

* FDE: [LP: #2101834](https://bugs.launchpad.net/snapd/+bug/2101834) snapd 2.68+ and snap-bootstrap <2.68 fallback to old keyring path
* Fix Plucky snapd deb build issue related to /var/lib/snapd/void permissions
* Fix snapd deb build complaint about ifneq with extra bracket

### Snapd 2.68.4

*Released on 28 April 2025.*

The release process for snapd 2.68.4 took significant time to stabilize. This update was prompted by a mistake in classic 24.XX models that required a workaround in snapd.

This release includes the exact content of snapd 2.68.3, along with a couple of additional changes:

* Workaround for classic 24.04/24.10 models that incorrectly specify core22 instead of core24 ([LP: #2072987](https://bugs.launchpad.net/snapd/+bug/2072987))
* Updated build dependencies

During the 2.68.4 rollout, Ubuntu Core 24 images built with Snapd 2.68.4 and the then-current 24/stable `pc-kernel` would not function correctly until kernel version 6.8.0-58.60+1 was promoted to the stable channel. See the [original release notice](https://forum.snapcraft.io/t/snapd-2-68-4-release-update/46738/4) for the rollout context.

#### Changelog

* Snap components: [LP: #2104933](https://bugs.launchpad.net/snapd/+bug/2104933) workaround for classic 24.04/24.10 models that incorrectly specify core22 instead of core24
* Update build dependencies

### Snapd 2.68.5

*Released on 17 June 2025.*

Snapd 2.68.5 addresses an issue where preseed files may be missing when running inside a container ([LP: #2109843](https://bugs.launchpad.net/snapd/+bug/2109843)).

#### Changelog

* [LP: #2109843](https://bugs.launchpad.net/snapd/+bug/2109843) fix missing preseed files when running in a container

(ref-release-notes_snapd-2-67-release-notes)=
## Snapd 2.67

*Released on 11 January 2025.*

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

### Changelog

* AppArmor prompting (experimental): allow overlapping rules
* Registry view (experimental): Changes to registry data (from both users and snaps) can be validated and saved by custodian snaps
* Registry view (experimental): Support 'snapctl get --pristine' to read the registry data excluding staged transaction changes
* Registry view (experimental): Put registry commands behind experimental feature flag
* Components: Make modules shipped/created by kernel-modules components available right after reboot
* Components: Add tab completion for local component files
* Components: Allow installing snaps and components from local files jointly on the CLI
* Components: Allow 'snapctl model' command for gadget and kernel snaps
* Components: Add 'snap components' command
* Components: Bug fixes
* eMMC gadget updates (WIP): add syntax support in gadget.yaml for eMMC schema
* Support for ephemeral recovery mode on hybrid systems
* Support for dm-verity options in snap-bootstrap
* Support for overlayfs options and allow empty what argument for tmpfs
* Enable ubuntu-image to determine the size of the disk image to create
* Expose 'snap debug' commands 'validate-seed' and 'seeding'
* Add debug API option to use dedicated snap socket /run/snapd-snap.socket 
* Hide experimental features that are no longer required (accepted/rejected)
* Mount ubuntu-save partition with no{exec,dev,suid} at install, run and factory-reset
* Improve memory controller support with cgroup v2
* Support ssh socket activation configurations (used by ubuntu 22.10+)
* Fix generation of AppArmor profile with incorrect revision during multi snap refresh 
* Fix refresh app awareness related deadlock edge case
* Fix not caching delta updated snap download
* Fix passing non root uid, guid to initial tmpfs mount
* Fix ignoring snaps in try mode when amending
* Fix reloading of service activation units to avoid systemd errors
* Fix snapd snap FIPS build on Launchpad to use Advantage Pro FIPS updates PPA
* Make killing of snap apps best effort to avoid possibility of malicious failure loop
* Alleviate impact of auto-refresh failure loop with progressive delay
* Dropped timedatex in selinux-policy to avoid runtime issue
* Fix missing syscalls in seccomp profile
* Modify AppArmor template to allow using SNAP_REEXEC on arch systems
* Modify AppArmor template to allow using vim.tiny (available in base snaps)
* Modify AppArmor template to add read-access to debian_version
* Modify AppArmor template to allow owner to read @{PROC}/@{pid}/sessionid
* {common,personal,system}-files interface: prohibit trailing @ in filepaths
* {desktop,shutdown,system-observe,upower-observe} interface: improve for Ubuntu Core Desktop
* custom-device interface: allow @ in custom-device filepaths
* desktop interface: improve launch entry and systray integration with session
* desktop-legacy interface: allow DBus access to com.canonical.dbusmenu
* fwupd interface: allow access to nvmem for thunderbolt plugin
* mpris interface: add plasmashell as label
* mount-control interface: add support for nfs mounts
* network-{control,manager} interface: add missing dbus link rules
* network-manager-observe interface: add getDevices methods
* opengl interface: add Kernel Fusion Driver access to opengl
* screen-inhibit-control interface: improve screen inhibit control for use on core
* udisks2 interface: allow ping of the UDisks2 service
* u2f-devices interface: add Nitrokey Passkey


### Snapd 2.67.1

*Released on 7 March 2025.*

#### Notable updates

* Fix AppArmor permissions to allow snaps access to kernel modules and firmware on UC24, which also fixes the kernel-modules-control interface on UC24
* Fix 'snap run' getent based user lookup in case of bad PATH ([LP: #2090938](https://launchpad.net/bugs/2090938))
* Fix snapd using the incorrect AppArmor version during undo of a refresh
* Extended hardware-observe interface to allow the riscv_hwprobe syscall, and mount-observe interface to allow the listmount and statmount syscalls

#### Changelog

* Fix apparmor permissions to allow snaps access to kernel modules and firmware on UC24, which also fixes the kernel-modules-control interface on UC24
* AppArmor prompting (experimental): disallow /./ and /../ in path patterns
* [LP: #2090938](https://bugs.launchpad.net/snapd/+bug/2090938) Fix 'snap run' getent based user lookup in case of bad PATH
* Fix snapd using the incorrect AppArmor version during undo of an refresh for regenerating snap profiles
* Add new syscalls to base templates
* hardware-observe interface: allow riscv_hwprobe syscall
* mount-observe interface: allow listmount and statmount syscalls

(ref-release-notes_snapd-2-66-release-notes)=
## Snapd 2.66

*Released on 26 November 2024.*

This release added the ability for Snapcraft 8.x to build snapd using with core22 base, and support for building a snapd variant that's [FIPS](https://en.wikipedia.org/wiki/FIPS_140-3) compliant. 

Other highlights include:

*  **AppArmor prompting**

   In collaboration with the security and desktop teams at Canonical, this release of snapd includes the functionality required for snaps to request interface access from the user. 

   For more information on this feature, including design details and how it can be tested in Ubuntu 24.10, see [Introducing Permissions Prompting](https://discourse.ubuntu.com/t/ubuntu-desktop-s-24-10-dev-cycle-part-5-introducing-permissions-prompting/47963).

* **Experimental confdb support**

   This release includes many updates to support _confdb_, formerly known as Registry, which will significantly improve how we handle configuration data and share that data between snaps and devices.

### Snapd 2.66.1

*Released on 26 November 2024.*

This is the first release of the snapd snap built against core22. It includes important fixes and features worked on over the preceding months.

It also comes with new AppArmor version 4.0.2, which supports AppArmor prompting and includes a security update that impacts rare and specific mount-control plug definitions.

#### Changelog

* AppArmor prompting (experimental): expand kernel support checks
* AppArmor prompting (experimental): consolidate error messages and add error kinds
* AppArmor prompting (experimental): grant /v2/snaps/{name} via snap-interfaces-requests-control
* AppArmor prompting (experimental): add checks for duplicate pattern variants
* Registry views (experimental): add handlers that commit (and cleanup) registry transactions
* Registry views (experimental): add a snapctl fail command for rejecting registry transactions
* Registry views (experimental): allow custodian snaps to implement registry hooks that modify and save registry data
* Registry views (experimental): run view-changed hooks only for snaps plugging views affected by modified paths
* Registry views (experimental): make registry transactions serialisable
* Snap components: handle refreshing components to revisions that have been on the system before
* Snap components: enable creating Ubuntu Core images that contain components
* Snap components: handle refreshing components independently of snaps
* Snap components: handle removing components when refreshing a snap that no longer defines them
* Snap components: extend snapd Ubuntu Core installation API to allow for picking optional snaps and components to install
* Snap components: extend kernel.yaml with "dynamic-modules", allowing kernel to define a location for kmods from component hooks
* Snap components: renamed component type "test" to "standard"
* Desktop IDs: support installing desktop files with custom names based on desktop-file-ids desktop interface plug attr
* Auto-install snapd on classic systems as prerequisite for any non-essential snap install
* Support loading AppArmor profiles on WSL2 with non-default kernel and securityfs mounted
* Debian/Fedora packaging updates
* Add snap debug command for investigating execution aspects of the snap toolchain
* Improve snap pack error for easier parsing
* Add support for user services when refreshing snaps
* Add snap remove --terminate flag for terminating running snap processes
* Support building FIPS complaint snapd deb and snap
* Fix to not use nss when looking up for users/groups from snapd snap
* Fix ordering in which layout changes are saved
* Patch snapd snap dynamic linker to ignore LD_LIBRARY_PATH and related variables
* Fix libexec dir for openSUSE Slowroll
* Fix handling of the shared snap directory for parallel installs
* Allow writing to /run/systemd/journal/dev-log by default
* Avoid state lock during snap removal to avoid delaying other snapd operations
* Add nomad-support interface to enable running Hashicorp Nomad
* Add intel-qat interface
* u2f-devices interface: add u2f trustkey t120 product id and fx series fido u2f devices
* desktop interface: improve integration with xdg-desktop-portal
* desktop interface: add desktop-file-ids plug attr to desktop interface
* unity7 interface: support desktop-file-ids in desktop files rule generation
* desktop-legacy interface: support desktop-file-ids in desktop files rule generation
* desktop-legacy interface: grant access to gcin socket location
* login-session-observe interface: allow introspection
* custom-device interface: allow to explicitly identify matching device in udev tagging block
* system-packages-doc interface: allow reading /usr/share/javascript
* modem-manager interface: add new format of WWAN ports
* pcscd interface: allow pcscd to read opensc.conf
* cpu-control interface: add IRQ affinity control to cpu_control
* opengl interface: add support for cuda workloads on Tegra iGPU in opengl interface

(ref-release-notes_snapd-2-65-release-notes)=
## Snapd 2.65

*Released to beta on 23 August 2024.*

* Support building snapd using base Core22 (Snapcraft 8.x)
* FIPS: support building FIPS complaint snapd variant that switches to FIPS mode when the system boots with FIPS enabled
* AppArmor: update to latest 4.0.2 release
* AppArmor: enable using ABI 4.0 from host parser
* AppArmor: fix parser lookup
* AppArmor: support AppArmor snippet priorities
* AppArmor: allow reading cgroup memory.max file
* AppArmor: allow using snap-exec coming from the snapd snap when starting a confined process with jailmode
* AppArmor prompting (experimental): add checks for prompting support, include prompting status in system key, and restart snapd if prompting flag changes
* AppArmor prompting (experimental): include prompt prefix in AppArmor rules if prompting is supported and enabled
* AppArmor prompting (experimental): add common types, constraints, and mappings from AppArmor permissions to abstract permissions
* AppArmor prompting (experimental): add path pattern parsing and matching
* AppArmor prompting (experimental): add path pattern precedence based on specificity
* AppArmor prompting (experimental): add packages to manage outstanding request prompts and rules
* AppArmor prompting (experimental): add prompting API and notice types, which require snap-interfaces-requests-control interface
* AppArmor prompting (experimental): feature flag can only be enabled if prompting is supported, handler service connected, and the service can be started
* Registry views (experimental): rename from aspects to registries
* Registry views (experimental): support reading registry views and setting/unsetting registry data using snapctl
* Registry views (experimental): fetch and refresh registry assertions as needed
* Registry views (experimental): restrict view paths from using a number as first character and view names to storage path style patterns
* Snap components: support installing snaps and components from files at the same time (no REST API/CLI)
* Snap components: support downloading components related assertions from the store
* Snap components: support installing components from the store
* Snap components: support removing components individually and during snap removal
* Snap components: support kernel modules as components
* Snap components: support for component install, pre-refresh and post-refresh hooks
* Snap components: initial support for building systems that contain components
* Refresh app awareness (experimental): add data field for /v2/changes REST API to allow associating each task with affected snaps
* Refresh app awareness (experimental): use the app name from .desktop file in notifications
* Refresh app awareness (experimental): give snap-refresh-observe interface access to /v2/snaps/{name} endpoint
* Improve snap-confine compatibility with nvidia drivers
* Allow re-exec when SNAP_REEXEC is set for unlisted distros to simplify testing
* Allow mixing revision and channel on snap install
* Generate GNU build ID for Go binaries
* Add missing etelpmoc.sh for shell completion
* Do not attempt to run snapd on classic when re-exec is disabled
* Packaging/build maintenance for Debian sid, Fedora, Arch, openSuse
* Add snap debug API command to enable running raw queries
* Enable snap-confine snap mount directory detection
* Replace global seccomp filter with deny rules in standard seccomp template
* Remove support for Ubuntu Core Launcher (superseded by snap-confine)
* Support creating pending serial bound users after serial assertion becomes available
* Support disabling cloud-init using kernel command-line
* In hybrid systems, apps can refresh without waiting for restarts required by essential snaps
* Ship snap-debug-info.sh script used for system diagnostics
* Improve error messages when attempting to run non-existent snap
* Switch to -u UID:GID for strace-static
* Support enabling snapd logging with snap set system debug.snapd.{log,log-level}
* Add options system.coredump.enable and system.coredump.maxuse to support using systemd-coredump on Ubuntu Core
* Provide documentation URL for 'snap interface <iface-name>'
* Fix restarting activated services instead of their activator units (i.e. sockets, timers)
* Fix potential unexpected auto-refresh of snap on managed schedule
* Fix potential segfault by guarding against kernel command-line changes on classic system
* Fix proxy entries in /etc/environment with missing newline that caused later manual entries to not be usable
* Fix offline remodelling by ignoring prerequisites that will otherwise be downloaded from store
* Fix devmode seccomp deny regression that caused spamming the log instead of actual denies
* Fix snap lock leak during refresh
* Fix not re-pinning validation sets that were already pinned when enforcing new validation sets
* Fix handling of unexpected snapd runtime failure
* Fix /v2/notices REST API skipping notices with duplicate timestamps
* Fix comparing systemd versions that may contain pre-release suffixes
* Fix udev potentially starting before snap-device-helper is made available
* Fix race in snap seed metadata loading
* Fix treating cloud-init exit status 2 as error
* Fix to prevent sending refresh complete notification if snap snap-refresh-observe interface is connected
* Fix to queue snapctl service commands if run from the default-configure hook to ensure they get up-to-date config values
* Fix stop service failure when the service is not actually running anymore
* Fix parsing /proc/PID/mounts with spaces
* Add registry interface that provides snaps access to a particular registry view
* Add snap-interfaces-requests-control interface to enable prompting client snaps
* steam-support interface: remove all AppArmor and seccomp restrictions to improve user experience
* opengl interface: improve compatibility with nvidia drivers
* home interface: autoconnect home on Ubuntu Core Desktop
* serial-port interface: support RPMsg tty
* display-control interface: allow changing LVDS backlight power and brightness
* power-control interface: support for battery charging thesholds, type/status and AC type/status
* cpu-control interface: allow CPU C-state control
* raw-usb interface: support RPi5 and Thinkpad x13s
* custom-device interface: allow device file locking
* lxd-support interface: allow LXD to self-manage its own cgroup
* network-manager interface: support MPTCP sockets
* network-control interface: allow plug/slot access to gnutls config and systemd resolved cache flushing via D-Bus
* network-control interface: allow wpa_supplicant dbus api
* gpio-control interface: support gpiochip* devices
* polkit interface: fix "rw" mount option check
* u2f-devices interface: enable additional security keys
* desktop interface: enable kde theming support

### Snapd 2.65.1

*Released to beta on 24 August 2024.*

* Fix snapd riscv64 build

### Snapd 2.65.3

*Released to beta on 24 August 2024.*

* Fix missing aux info from store on snap setup
* Bump squashfuse from version 0.5.0 to 0.5.2 (used in snapd deb only)

(ref-release-notes_snapd-2-64-release-notes)=
## Snapd 2.64

*Released to beta on 25 July 2024*

For the 2.64 release, we updated the build process to use Ubuntu 22.04 instead of Ubuntu 16.04. This change only affected the snapd.snap, and had impact on builds for Debian, Fedora, Arch, openSUSE, or any other classic package

Users should see no changes or compatibility issues, and if you are a snapd developer, this change makes building snapd easier. The latest Snapcraft releases can now be used to build a local version of the snapd package. In the long term, this will also improve our iteration speed as we’ll require fewer snapd builds, providing developers with faster feedback on their changes.

As part of this release cycle, our `ubuntu-image` and validation-sets documentation also improved.

### Changelog

* Support building snapd using base Core22 (Snapcraft 8.x)
* FIPS: support building FIPS complaint snapd variant that switches to FIPS mode when the system boots with FIPS enabled
* AppArmor: update to AppArmor 4.0.1
* AppArmor: support AppArmor snippet priorities
* AppArmor prompting: add checks for prompting support, include prompting status in system key, and restart snapd if prompting flag changes
* AppArmor prompting: include prompt prefix in AppArmor rules if prompting is supported and enabled
* AppArmor prompting: add common types, constraints, and mappings from AppArmor permissions to abstract permissions
* AppArmor prompting: add path pattern parsing and matching
* Registry views (experimental): rename from aspects to registries
* Registry views (experimental): support reading registry views using snapctl
* Registry views (experimental): restrict view paths from using a number as first character and view names to storage path style patterns
* Snap components: support installing snaps and components from files at the same time (no REST API/CLI)
* Snap components: support downloading components related assertions from the store
* Snap components: support installing components from the store (no REST API/CLI)
* Snap components: support removing components (REST API, no CLI)
* Snap components: started support for component hooks
* Snap components: support kernel modules as components
* Refresh app awareness (experimental): add data field for /v2/changes REST API to allow associating each task with affected snaps
* Refresh app awareness (experimental): use the app name from .desktop file in notifications
* Refresh app awareness (experimental): give snap-refresh-observe interface access to /v2/snaps/{name} endpoint
* Allow re-exec when SNAP_REEXEC is set for unlisted distros to simplify testing
* Generate GNU build ID for Go binaries
* Add missing etelpmoc.sh for shell completion
* Do not attempt to run snapd on classic when re-exec is disabled
* Packaging/build maintenance for Debian sid, Fedora, Arch, openSuse
* Add snap debug api command to enable running raw queries
* Enable snap-confine snap mount directory detection
* Replace global seccomp filter with deny rules in standard seccomp template
* Remove support for Ubuntu Core Launcher (superseded by snap-confine)
* Support creating pending serial bound users after serial assertion becomes available
* Support disabling cloud-init using kernel command-line
* In hybrid systems, apps can refresh without waiting for restarts required by essential snaps
* Ship snap-debug-info.sh script used for system diagnostics
* Improve error messages when attempting to run non-existent snap
* Switch to -u UID:GID for strace-static
* Support enabling snapd logging with snap set system debug.snapd.{log,log-level}
* Fix restarting activated services instead of their activator units (i.e. sockets, timers)
* Fix potential unexpected auto-refresh of snap on managed schedule
* Fix potential segfault by guarding against kernel command-line changes on classic system
* Fix proxy entries in /etc/environment with missing newline that caused later manual entries to not be usable
* Fix offline remodelling by ignoring prerequisites that will otherwise be downloaded from store
* Fix devmode seccomp deny regression that caused spamming the log instead of actual denies
* Fix snap lock leak during refresh
* Fix not re-pinning validation sets that were already pinned when enforcing new validation sets
* Fix handling of unexpected snapd runtime failure
* Fix /v2/notices REST API skipping notices with duplicate timestamps
* Fix comparing systemd versions that may contain pre-release suffixes
* Fix udev potentially starting before snap-device-helper is made available
* Fix race in snap seed metadata loading
* Fix treating cloud-init exit status 2 as error
* Fix to prevent sending refresh complete notification if snap snap-refresh-observe interface is connected
* Fix to queue snapctl service commands if run from the default-configure hook to ensure they get up-to-date config values
* Fix stop service failure when the service is not actually running anymore
* Add registry interface that provides snaps access to a particular registry view
* steam-support interface: relaxed AppArmor and seccomp restrictions to improve user experience
* home interface: autoconnect home on Ubuntu Core Desktop
* serial-port interface: support RPMsg tty
* display-control interface: allow changing LVDS backlight power and brightness
* power-control interface: support for battery charging thesholds, type/status and AC type/status
* cpu-control interface: allow CPU C-state control
* raw-usb interface: support RPi5 and Thinkpad x13s
* custom-device interface: allow device file locking
* lxd-support interface: allow LXD to self-manage its own cgroup
* network-manager interface: support MPTCP sockets
* network-control interface: allow plug/slot access to gnutls config and systemd resolved cache flushing via D-Bus

(ref-release-notes_snapd-2-63-release-notes)=
## Snapd 2.63

*Released on 23 May 2024.*

Snap-based [Ubuntu Core](https://ubuntu.com/core) devices will benefit from many of our the features for this release, including support for [Offline remodelling](https://documentation.ubuntu.com/core/explanation/remodeling/#offline-remodeling), the use of {ref}`Validation sets <explanation-how-snaps-work-validation-sets>` in the [model assertion](https://ubuntu.com/core/docs/reference/assertions/model) and setting a custom port for SSH.

There’s also a new `snap sign` [`--chain`](https://documentation.ubuntu.com/core/how-to-guides/manage-ubuntu-core/add-a-system-user/#generating-auto-import-assert) argument in this release, that can be used to aggregate all the assertions required to create a new system user.

### Changelog

* Support for snap services to show the current status of user services (experimental)
* Refresh app awareness: record snap-run-inhibit notice when starting app from snap that is busy with refresh (experimental)
* Refresh app awareness: use warnings as fallback for desktop notifications (experimental)
* Aspect based configuration: make request fields in the aspect-bundle's rules optional (experimental)
* Aspect based configuration: make map keys conform to the same format as path sub-keys (experimental)
* Aspect based configuration: make unset and set behaviour similar to configuration options (experimental)
* Aspect based configuration: limit nesting level for setting value (experimental)
* Components: use symlinks to point active snap component revisions
* Components: add model assertion support for components
* Components: fix to ensure local component installation always gets a new revision number
* Add basic support for a CIFS remote filesystem-based home directory
* Add support for AppArmor profile kill mode to avoid snap-confine error
* Allow more than one interface to grant access to the same API endpoint or notice type
* Allow all snapd service's control group processes to send systemd notifications to prevent warnings flooding the log
* Enable not preseeded single boot install
* Update secboot to handle new sbatlevel
* Fix to not use cgroup for non-strict confined snaps (devmode, classic)
* Fix two race conditions relating to freedesktop notifications
* Fix missing tunables in snap-update-ns AppArmor template
* Fix rejection of snapd snap udev command line by older host snap-device-helper
* Rework seccomp allow/deny list
* Clean up files removed by gadgets
* Remove non-viable boot chains to avoid secboot failure
* posix_mq interface: add support for missing time64 mqueue syscalls mq_timedreceive_time64 and mq_timedsend_time64
* password-manager-service interface: allow kwalletd version 6
* kubernetes-support interface: allow SOCK_SEQPACKET sockets
* system-observe interface: allow listing systemd units and their properties
* opengl interface: enable use of nvidia container toolkit CDI config generation

(ref-release-notes_snapd-2-62-release-notes)=
## Snapd 2.62

*Released on 15 April 2024.*

The functionality to add custom device interfaces to an app is now complete, as is our create and removal functionality for Ubuntu Core recovery systems. We’ve also finally made a commitment on what minimum [system requirements](https://ubuntu.com/core/docs/system-requirements) might actually be for Ubuntu Core, even if you can’t actually buy a device with less than several gigabytes of on-board RAM.

This release also included two significant additions to our documentation. Firstly, the Docker interface now includes a fully realised example implementation, and secondly, we’ve completed a new page on recovery system via the REST API, thanks to Andrew.

Finally, this release included new packages for Arch Linux, Amazon Linux, Debian, Fedora, openSUSE and Solus.

### Changelog

* Aspects based configuration schema support (experimental)
* Refresh app awareness support for UI (experimental)
* Support for user daemons by introducing new control switches --user/--system/--users for service start/stop/restart (experimental)
* Add AppArmor prompting experimental flag (feature currently unsupported)
* Installation of local snap components of type test
* Packaging of components with snap pack
* Expose experimental features supported/enabled in snapd REST API endpoint /v2/system-info
* Support creating and removing recovery systems for use by factory reset
* Enable API route for creating and removing recovery systems using /v2/systems with action create and /v2/systems/{label} with action remove
* Lift requirements for fde-setup hook for single boot install
* Enable single reboot gadget update for UC20+
* Allow core to be removed on classic systems
* Support for remodeling on hybrid systems
* Install desktop files on Ubuntu Core and update after snapd upgrade
* Upgrade sandbox features to account for cgroup v2 device filtering
* Support snaps to manage their own cgroups
* Add support for AppArmor 4.0 unconfined profile mode
* Add AppArmor based read access to /etc/default/keyboard
* Upgrade to squashfuse 0.5.0
* Support useradd utility to enable removing Perl dependency for UC24+
* Support for recovery-chooser to use console-conf snap
* Add support for --uid/--gid using strace-static
* Add support for notices (from pebble) and expose via the snapd REST API endpoints /v2/notices and /v2/notice
* Add polkit authentication for snapd REST API endpoints /v2/snaps/{snap}/conf and /v2/apps
* Add refresh-inhibit field to snapd REST API endpoint /v2/snaps
* Add refresh-inhibited select query to REST API endpoint /v2/snaps
* Take into account validation sets during remodeling
* Improve offline remodeling to use installed revisions of snaps to fulfill the remodel revision requirement
* Add rpi configuration option sdtv_mode
* When snapd snap is not installed, pin policy ABI to 4.0 or 3.0 if present on host
* Fix gadget zero-sized disk mapping caused by not ignoring zero sized storage traits
* Fix gadget install case where size of existing partition was not correctly taken into account
* Fix trying to unmount early kernel mount if it does not exist
* Fix restarting mount units on snapd start
* Fix call to udev in preseed mode
* Fix to ensure always setting up the device cgroup for base bare and core24+
* Fix not copying data from newly set homedirs on revision change
* Fix leaving behind empty snap home directories after snap is removed (resulting in broken symlink)
* Fix to avoid using libzstd from host by adding to snapd snap
* Fix autorefresh to correctly handle forever refresh hold
* Fix username regex allowed for system-user assertion to not allow '+'
* Fix incorrect application icon for notification after autorefresh completion
* Fix to restart mount units when changed
* Fix to support AppArmor running under incus
* Fix case of snap-update-ns dropping synthetic mounts due to failure to match  desired mount dependencies
* Fix parsing of base snap version to enable pre-seeding of Ubuntu Core Desktop
* Fix packaging and tests for various distributions
* Add remoteproc interface to allow developers to interact with Remote Processor Framework which enables snaps to load firmware to ARM Cortex microcontrollers
* Add kernel-control interface to enable controlling the kernel firmware search path
* Add nfs-mount interface to allow mounting of NFS shares
* Add ros-opt-data interface to allow snaps to access the host /opt/ros/ paths
* Add snap-refresh-observe interface that provides refresh-app-awareness clients access to relevant snapd API endpoints
* steam-support interface: generalize Pressure Vessel root paths and allow access to driver information, features and container versions
* steam-support interface: make implicit on Ubuntu Core Desktop
* desktop interface: improved support for Ubuntu Core Desktop and limit autoconnection to implicit slots
* cups-control interface: make autoconnect depend on presence of cupsd on host to ensure it works on classic systems
* opengl interface: allow read access to /usr/share/nvidia
* personal-files interface: extend to support automatic creation of missing parent directories in write paths
* network-control interface: allow creating /run/resolveconf
* network-setup-control and network-setup-observe interfaces: allow busctl bind as required for systemd 254+
* libvirt interface: allow r/w access to /run/libvirt/libvirt-sock-ro and read access to /var/lib/libvirt/dnsmasq/**
* fwupd interface: allow access to IMPI devices (including locking of device nodes), sysfs attributes needed by amdgpu and the COD capsule update directory
* uio interface: allow configuring UIO drivers from userspace libraries
* serial-port interface: add support for NXP Layerscape SoC
* lxd-support interface: add attribute enable-unconfined-mode to require LXD to opt-in to run unconfined
* block-devices interface: add support for ZFS volumes
* system-packages-doc interface: add support for reading jquery and sphinx documentation
* system-packages-doc interface: workaround to prevent autoconnect failure for snaps using base bare
* microceph-support interface: allow more types of block devices to be added as an OSD
* mount-observe interface: allow read access to /proc/{pid}/task/{tid}/mounts and proc/{pid}/task/{tid}/mountinfo
* polkit interface: changed to not be implicit on core because installing policy files is not possible
* upower-observe interface: allow stats refresh
* gpg-public-keys interface: allow creating lock file for certain gpg operations
* shutdown interface: allow access to SetRebootParameter method
* media-control interface: allow device file locking
* u2f-devices interface: support for Trustkey G310H, JaCarta U2F, Kensington VeriMark Guard, RSA DS100, Google Titan v2

(ref-release-notes_snapd-2-61-release-notes)=
## Snapd 2.61

*Released on 3 January 2024.*

This release included a lot of background work that will later be used by `confdb` (see Snapd 2.66), to help with  cross-snap configuration. This includes new rules for parsing assertions and a per-aspect field, plus a vital new ability to unset values from the command line.

We also got closer to finishing our opt-in AppArmor prompting support , with some important background improvements, and created a specification for the desktop user-experience flow. Our cross-distribution support also improved with this release, with a new repository and packages for Amazon Linux , and snapd 2.61.1 releases for Debian Sid and Fedora 38, 39, Rawhide and EPEL 7, 8 and 9.

### Snapd 2.61.1

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

### Snapd 2.61.2

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

(ref-release-notes_snapd-2-60-release-notes)=
## Snapd 2.60.3

*Released on Sep 02 2023.*

* Bugfixes
* Use "aes-cbc-essiv:sha256" in cryptsetup on arm 32bit devices to increase speed on devices with CAAM support
* Stop using `-O no-expr-simplify` in apparmor_parser to avoid  potential exponential memory use. This can lead to slower   policy complication in some cases but it is much safer on  low memory devices.
* Support for dynamic snapshot data exclusions
* Apparmor userspace is vendored inside the snapd snap
* Added a default-configure hook that exposes gadget default configuration  options to snaps during first install before services are started
* Allow install from initrd to speed up the initial installation for  systems that do not have a install-device hook
* New `snap sign --chain` flag that appends the account and account-key  assertions
* Support validation-sets in the model assertion
* Support new "min-size" field in gadget.yaml
* New interface: "userns"

(ref-release-notes_snapd-2-59-release-notes)=
## Snapd 2.59

*Released on Mar 27 2023.*

* Support setting extra kernel command line parameters via snap configuration and under a gadget allow-list
* Support for Full-Disk-Encryption using ICE
* Support for arbitrary home dir locations via snap configuration
* New nvidia-drivers-support interface
* Support for udisks2 snap
* Pre-download of snaps ready for refresh and automatic refresh of the snap when all apps are closed
* New microovn interface
* Support uboot with `CONFIG_SYS_REDUNDAND_ENV=n`
* Make "snap-preseed --reset" re-exec when needed
* Update the fwupd interface to support fully confined fwupd
* The memory,cpu,thread quota options are no longer experimental
* Support debugging snap client requests via the `SNAPD_CLIENT_DEBUG_HTTP` environment variable
* Support ssh listen-address via snap configuration
* Support for quotas on single services
* prepare-image now takes into account snapd versions going into the image, including in the kernel initrd, to fetch supported assertion formats

(ref-release-notes_snapd-2-58-release-notes)=
## Snapd 2.58

*Released on Jan 09 2023.*

* `snap refresh --hold` support (https://forum.snapcraft.io/t/refresh-control/27213)
* new `users.lockout` configuration option
* support auto import assertions on first boot (https://github.com/snapcore/snapd/pull/11797)

(ref-release-notes_snapd-2-56-release-notes)=
## Snapd 2.56

*Released on Jun 06 2022.*

* support "starred" developers
* factory reset support for unencrypted devices

(ref-release-notes_snapd-2-55-release-notes)=
## Snapd 2.55

### Snapd 2.55.2

A regression was discovered in the snapd 2.55.2 release after it became available in the stable channel, so the stable release was reverted back to 2.54.4.

The bug was that when "layouts" are applied to content snap content, those layouts could be mounted in the wrong way, resulting in missing files for the snap. This caused, for example, the `newsflash` snap to fail to start. The fix shipped in 2.55.3.

### Snapd 2.55.3

*Released on Apr 20 2022.*

* Fix refresh layout construction (fixes Firefox crash)
* Support for the "piboot" bootloader
* Interface operations are faster by using more batched operations
* New mount-control interface ([topic](https://forum.snapcraft.io/t/the-mount-control-interface/28953))
* New polkit interface ([topic](https://forum.snapcraft.io/t/the-polkit-interface/28408))

(ref-release-notes_snapd-2-54-release-notes)=
## Snapd 2.54.2

*Released on Jan 24 2022.*

* New `shared-memory` interface ([topic](https://forum.snapcraft.io/t/the-shared-memory-interface/28382))
* Allow sideload of multiple snaps via the API
* riscv64 support for snap-seccomp
* fixes/improvements for various interfaces

(ref-release-notes_snapd-2-51-release-notes)=
## Snapd 2.51

*Released on June 7 2021.*

* New `swap.size` system config setting for Ubuntu Core devices
* Full kernel command line customization for UC20 pc/grub gadgets
* REST API support for creating recovery systems on UC20
* New `raw-input` interface
* New `dsp` interface
* New `sd-control` interface (2.51.3)
* New `netlink-driver` interface (2.51.1)
* New `install-device` gadget hook to be executed during install mode on UC20
* New `snapctl reboot --poweroff|--halt` command to be used in `install-device` hook to shut device off after install mode (but before first boot seeding in run mode)
* New `snapctl reboot system-mode` command to be report what mode a UC20 system is in.
* New kernel FDE hook V2 for UC20 devices
* Experimental quota resource groups support

(ref-release-notes_snapd-2-50-release-notes)=
## Snapd 2.50

*Released on June 2 2021.*

* Make /etc/ssl available for snaps on Ubuntu classic ([PR](https://github.com/snapcore/snapd/pull/9819))
* Support for DTBs from the kernel snap
* Snap service units are now re-written when snapd is refreshed as necessary
* New `dsp` interface

(ref-release-notes_snapd-2-49-release-notes)=
## Snapd 2.49

*Released on Mar 04 2021.*

* Express encryption preferences for UC20
* Devmode snaps in dangerous model UC20 seeds
* Support for LK bootloader for UC20
* Detection/abort of very slow downloads 
* Fix `snap try` inside lxd containers
* Add "Tegra" and RPi "MMAL"   support
* Add new "install-mode: disable" option  

(ref-release-notes_snapd-2-48-release-notes)=
## Snapd 2.48

*Released on Nov 30 2020.*

* Support for the "ubuntu-save" partition
* More versatile UC20 recovery booting in "degraded" situations
* Bulk assertion refresh for snap-declarations
* New `snap recovery --show-keys` command
* Improve notification UI for app-refresh-awareness
* New PTP hardware clock interface
* New `snap import-snapshot` command

(ref-release-notes_snapd-2-47-release-notes)=
## Snapd 2.47

*Released on Oct 21 2020.*

* better portal support with GLib ([PR](https://github.com/snapcore/snapd/pull/8301))
* add cups interface and update cups-control for cups as a strict snap ([PR](https://github.com/snapcore/snapd/pull/8920))
* disable console-conf from gadget with core setting ([PR](https://github.com/snapcore/snapd/pull/9272))
* Improve disk-space awareness of snapd ([topic](https://forum.snapcraft.io/t/20007))
* New "snap reboot" command

(ref-release-notes_snapd-2-46-release-notes)=
## Snapd 2.46

*Released on Sep 14 2020.*

* uinput interface ([PR](https://github.com/snapcore/snapd/pull/8867))
* system-source-code interface ([PR](https://github.com/snapcore/snapd/pull/8868))
* system-packages-doc interface ([PR](https://github.com/snapcore/snapd/pull/8578))
* snaps can now set default-url-scheme-handler
* system-user assertions can be limited to specific serial assertions
* experimental user session daemons with `daemon-scope` ([PR](https://github.com/snapcore/snapd/pull/5822))
* experimental gdbserver support with snaps ([topic](https://forum.snapcraft.io/t/new-experimental-snap-run-experimental-gdbserver-option/18227))

(ref-release-notes_snapd-2-45-release-notes)=
## Snapd 2.45

*Released on Jul 15 2020.*

* Ubuntu Core 20 beta
* Generic serials for third parties
* Use xdg desktop portal from `snapctl user-open`
* Custom SSL cert support for store interactions ([topic](https://forum.snapcraft.io/t/custom-ssl-certs-for-snapd-to-the-snap-store-communication/17446)).

(ref-release-notes_snapd-2-44-release-notes)=
## Snapd 2.44

*Released on March 31 2020.*

* Switch within tracks with risk-only channel specification ([old topic](https://forum.snapcraft.io/t/11769), [new topic](https://forum.snapcraft.io/t/14970))
* Support for default tracks ([topic](https://forum.snapcraft.io/t/14970))
* Plug/slot rules: plug-names/slot-names constraints ([topic](https://forum.snapcraft.io/t/plug-slot-rules-plug-names-slot-names-constraints/12439))
* `snap remove-user` support

(ref-release-notes_snapd-2-43-release-notes)=
## Snapd 2.43

*Released on Feb 19 2020.*

* snapctl is-connected plug|slot ([topic](https://forum.snapcraft.io/t/14144))
* Remodel: gadget support
* Plug/slot declaration rules: greedy plugs ([topic](https://forum.snapcraft.io/t/12438))
* `system-backup` interface ([PR](https://github.com/snapcore/snapd/pull/6436))
* Speedup seccomp backend setup ([PR](https://github.com/snapcore/snapd/pull/7821))

(ref-release-notes_snapd-2-42-release-notes)=
## Snapd 2.42

*Released on Oct 10 2019.*

* Little-Kernel bootloader support
* Improve performance in lxd when snapfuse is used ([topic](https://forum.snapcraft.io/t/10747/6))
* Work with cgroup v2 only systems
* Improved icon-theme support ([topic](https://forum.snapcraft.io/t/10676))

(ref-release-notes_snapd-2-34-3-release-notes)=
## Snapd 2.34.3

### Highlights

* **Interface connection via gadget** ([topic](https://forum.snapcraft.io/t/1431)): This allows defining interface connections on the gadget snap so that on first boot the given plugs and slots get connected.
* **New interfaces**: New `dvb` interface ([topic](https://forum.snapcraft.io/t/3497)), `can-bus` interface, and new `{contacts,calendar}-service` interfaces are now available.
* **New system configuration**: A new system config option to configure the hardware watchdog on Ubuntu Core ([topic](https://forum.snapcraft.io/t/5695)). A new option to disable/enable IPv6 on the system is also available via `snap set system network.disable-ipv6`.

(ref-release-notes_snapd-2-33-release-notes)=
## Snapd 2.33

The beta channel now contains a new "core" snap with the 2.33~rc1 release. This is the first test-release for the coming 2.33 version of snapd. It contains a lot of tweaks and fixes but relatively little in terms of big new features. The recent weeks were very focused on stabilizing for the 18.04 Ubuntu release and many of the 2.33 fixes were backported into the 2.32 release.

(ref-release-notes_snapd-2-32-release-notes)=
## Snapd 2.32

The beta channel contains a new "core" with the snapd 2.32~pre1 release. This is the first prerelease for the coming 2.32 snapd. It contains some exciting new features like layouts, auto-connect tasks and system-key based profile re-generation and auto install of default content providers and more. 

(ref-release-notes_snapd-2-30-release-notes)=
## Snapd 2.30

### Highlights

* **Service control on snapctl (start/stop/etc)** ([topic](https://forum.snapcraft.io/t/1908)): Allows a snap to control its services from inside a hook. This is useful, for example, to restart a service in the configure hook when a configuration item has changed.
* **Support for socket activation** ([topic](https://forum.snapcraft.io/t/2050)): Some daemons use systemd's "socket activation" feature, where the daemon is started on demand when a socket is connected to. This is now supported via the new `snapcraft.yaml` `sockets:` key.
* **Pre-refresh hook support** ([topic](https://forum.snapcraft.io/t/478)): Provides a way for a snap to do things before it is refreshed, such as storing state before a refresh.
* **Allow configuring core before it is installed**: Allows setting, for example, a proxy for snapd even before the core snap is installed.
* **Run configuration of core internally**: The code to configure core moved from an external script to internal Go code, allowing better and earlier error checking and making things faster.
* **Support for Nvidia Vulkan/32-bit NVIDIA drivers**.

Complete details are available in the [project's commit history](https://github.com/snapcore/snapd/commits/release/2.30).

(ref-release-notes_snapd-2-28-release-notes)=
## Snapd 2.28

### Highlights

* **New "post-refresh" hook** ([topic](https://forum.snapcraft.io/t/478/10/)): A new hook, `post-refresh`, runs after the snap is refreshed but before services are started, useful for refresh-related housekeeping.
* **Initial base snap support** ([topic](https://forum.snapcraft.io/t/381/)): The new "base" snap allows snaps to select which base filesystem they require, rather than always using the `core` snap. This release adds support for bases and provides an example base snap called `bare`, which is empty and useful for minimal, statically linked snaps. New bases are not automatically downloaded in this release; that capability came in 2.29.
* **Polkit integration** ([topic](https://forum.snapcraft.io/t/1206)): Provides integration with the "polkit" mechanism of the GUI environment, making it possible to download and install snaps from graphical package management interfaces without logging into the store, as was previously required when operating as root or via sudo in the terminal.
* **Full xdg-open support via `snap userd`** ([topic](https://forum.snapcraft.io/t/1420)): Allows opening `http`, `https`, and `mailto` links directly from confined snaps without installing extra software.
* **Full bash-completion** ([topic](https://forum.snapcraft.io/t/2261)): Bash-completion support was added in 2.27, requiring an extra step to enable it in the shell. That step is now eliminated and is fully automatic. Completion of aliases is not yet supported.
* **New `snap switch` command** ([topic](https://forum.snapcraft.io/t/1418)): A convenient way to switch the channel of a snap without refreshing it right away, useful when offline or on a high-cost connection.
* **Proxy configuration on Core devices** ([topic](https://forum.snapcraft.io/t/467)): Core devices can now have their system-wide proxies configured via `snap set core proxy.{http,https,ftp}=<url>`.
* **Snap service management** ([topic](https://forum.snapcraft.io/t/262)): The new `snap services <snap>` command shows a snap's services and their status, also summarized in `snap info <snap>`. Services can be started/stopped via the new `snap start/stop/restart <snap.app>` commands, with logs available via `snap logs <snap.app>`. All of these are also exposed via the API.
* **Classic confinement on distributions that do not use the `/snap` directory** ([topic](https://forum.snapcraft.io/t/1732)): Classic-confinement snaps, which may refer to paths under `/snap`, now also work on distributions that use a different directory layout, once a symlink from `/snap` to the non-standard snap directory (usually `/var/lib/snapd/snap`) is created. The related error message was also improved.

Complete details are available in the project's commit history.

(ref-release-notes_snapd-2-27-release-notes)=
## Snapd 2.27

The 2.27 release focuses on dynamic filesystem updates via `snap-update-ns`, Android boot support, and install/remove hooks. Updating the core snap is enough to use this release on a Linux distribution that allows snapd re-executions.

### Highlights

* **Dynamic filesystem updates**: The `snap-update-ns` tool is available, enabling changes to be performed dynamically in the filesystem available inside the snap mount namespace. In practice, connections performed with the `content` interface are immediately available for the snap software to consume, even while it's still running. This is the foundation for [layouts](https://forum.snapcraft.io/t/1471), which will allow arbitrary mappings inside the snap namespace.
* **Android boot support**: The snapd boot sequence can now handle Android-style boot management, opening up a new range of devices for snapd that support transactional updates of the OS and kernel with automatic reverts on boot failures.
* **Install and remove hooks**: The new `install` and `remove` hooks allow a snap to implement logic activated only when the snap is first installed or removed from the system.
* **General snapctl support**: The `snapctl` tool, previously usable only inside hooks, can now be used outside of hooks as well, becoming a general mechanism for snap software to communicate with snapd at any point.
* **New `title` field**: Supported across the entire pipeline (snapd, API, store, snapcraft, etc), holding a high-level, usually uppercased name for the application (e.g. "Heroku CLI" for the application named "heroku"), as distinct from `summary`.
* **Install `--unaliased` parameter**: Allows installing a snap without its aliases being enabled, so its commands are only observable under names prefixed with the snap name.
* **`--last` in abort and watch**: The `snap abort` and `snap watch` commands now accept `--last=<kind>`, previously only available in the `changes` command, to operate on the last change of a particular kind, e.g. `snap watch --last=install`.
* **Seccomp argument filtering**: Re-enabled, so systems with working seccomp support see stricter rules when operating with the relevant interfaces.
* **Command `change` is now `tasks`**: The `snap change` command was renamed `tasks`, as a better counterpart to `snap changes`. The old name remains available as an alias.
* **New `search` alias**: `search` is an alias for `snap find`, addressing a common source of confusion with the `apt search` command.
* **Types in `snap list`**: The `snap list` command now displays the snap type under the Notes column for snaps which are not of type `app`.
* **More info in `info`**: The `snap info` command now displays the snap's unique ID, and shows the sha3-384 hash in verbose mode when given a snap filename.
* **Configuration defaults on first boot**: Devices managed entirely by snapd now also apply the default configuration specified by the gadget snap during first boot.
* **Auto-import assertions only on vfat and ext4**: The auto-import of assertions performed when media is plugged into managed devices now only happens on ext4 and vfat filesystems.

### New interfaces

* `broadcom-asic-control`
* `greengrass-support`
* `password-manager-service`

### Updated interfaces

Many pre-existing interfaces were updated with new rules: `alsa`, `browser-support`, `log-observe`, `mir`, `mount-observe`, `network-control`, `optical-drive`, `optical-observe`, `pulseaudio`, `screen-inhibit-control`, `system-observe`, `timezone-control`, `unity7`, `x11`.

(ref-release-notes_snapd-2-24-release-notes)=
## Snapd 2.24

The 2.24 release focuses on new features after several 2.23 maintenance releases.

### Highlights

* Remove snap config values when a snap is removed
* Fix potential transition issue from ubuntu-core to core
* Work towards improved aliases
* Many cross-distro improvements
* Fixes to work better with gnome-software
* Enable large file support
* Handle missing `snap-confine` gracefully
* Rework internal interface API to be more flexible and extensible
* Detect devmode by inspecting AppArmor support in the kernel
* Allow chroot in the base template
* Fix `pi-config` and add new `sdtv_aspect`, `config_hdmi_boost`, `hdmi_force_hotplug` options
* Interface updates: `browser-support`, `unity7`, `framebuffer`, `location-observe`, `location-control`, `mir`, `opengl`, `unity8`
* New interfaces: `joystick`, `maliit`, `autopilot`

(ref-release-notes_snapd-2-23-6-release-notes)=
## Snapd 2.23.6

The 2.23.6 release focuses on improving the robustness of the configuration hook system.

### Highlights

* tests: fix `interfaces-cups-control` for zesty
* configstate,hookstate: timeout the configure hook after 5 minutes, report failures
* packaging: rename the file shipping the snap-confine AppArmor profile to work around dpkg bug #858004
* many: ignore configure hook failures on core refresh to ensure upgrades are always possible
* snapstate: restart as needed if we undid unlinking, i.e. relinked core or kernel snap
* Support for `snap core set pi-config.framebuffer_{width,height}` (and more config.txt settings; see the [configuration options for core snap](https://forum.snapcraft.io/t/configuration-options-for-core-snap/87) topic)

The source is available at the [2.23.6 release tag](https://github.com/snapcore/snapd/releases/tag/2.23.6).
