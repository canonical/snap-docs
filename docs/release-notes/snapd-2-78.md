---
myst:
  html_meta:
    description: Release notes for Snapd 2.78, released on 3 November 2026. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-78)=
# Snapd 2.78

*Released on 3 November 2026.*

This release contains the 26.10 update content.

## FDE

* Update the keyring and state after reprovision, and complete the decision flow for auto-repair and reprovision.
* Add memfd-secret-backed state for secrets.
* Update secboot to support Thunderbolt security level 0 on Ubuntu Core.

## Components and seed refresh

* Account for components when deciding whether a seed refresh is needed, and prevent seeded components from being removed.
* Set `SNAP_COMPONENTS` in snap application environments.
* Support sharing content from components with the `$SNAP_COMPONENT(...)` syntax.
* Improve seed-refresh prerequisites and disk-space checks, and attempt to refresh only essential snaps when a disk-space check fails.

## Interfaces

* Add the `ubuntu-drivers-observe` interface.
* `content`: support sharing content from components.
* `shutdown`: allow `RebootWithFlags`.
* `daemon-notify`: allow the disconnected `/systemd/notify` path.
* `microceph-support`: add the `user-identity-switching` plug attribute.
* `u2f-devices`: add the Gemalto eToken Fusion to the fallback list.
* `power-control`: allow standardized charge-threshold sysfs attributes.
* Fix system-key comparisons and AppArmor profile generation for paths containing spaces.

## Confdb

* Improve error messages for map keys in JSON config values.
* Support reading and writing to builtin confdbs.
* Enforce validation-set constraints before changing state.

## Packaging and security

* Add a downstream version suffix that can be manipulated independently of the full version.
* Work around `dh_golang` behavior and remove `prepare-debian-build-tree`.
* Optimize Perl and Python rules in the AppArmor template for core24+ snaps.
* Update security logging APIs to specify who performed an action, what happened, and why or why not.

## Other

* Add the `disk-reservation.size` option and migrate experimental disk-space checks.
* Remove unloaded mount units during snap removal and pass subsystem triggers to udev.
* Fix handling of kernels that occupy multiple boot partitions with the Little Kernel bootloader.
* Ensure recovery-mode reboots are always oneshots, hide recovery entries in hybrid GRUB menus, and improve hybrid remodeling.
* Add a seed allowlist when creating recovery systems.
* Merge selected internal tools into the multi-entry snapd binary.

## Experimental features

### Graduated

- **quota-groups:** resource limits for snaps are now available without setting the experimental flag.

### Enabled by default

- **refresh-app-awareness-ux:** enabled by default.

For the release plan and complete list of changes, please refer to the [full release notes](https://forum.snapcraft.io/t/the-snapd-roadmap/1973).

## Test feedback

Feel free to share your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast-track investigations, please include details about your system, the snapd version(s), and steps to reproduce the issue.

## Security reports

Please report security vulnerabilities in private. The [snapd security policy](https://github.com/canonical/snapd/blob/master/SECURITY.md) describes what qualifies and how to report it.

## Changelog

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
