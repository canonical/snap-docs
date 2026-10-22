---
myst:
  html_meta:
    description: Reference documentation for snapd's experimental features, including the feature flag mechanism, graduation process, and current and previous feature lists.
---

(ref-experimental-features_experimental-features)=
# Experimental features

Experimental features are part of the _snapd_ development process. They allow engineering teams to test both the viability of an idea and its implementation.

If an experimental feature is considered unstable or likely to change, they are demarcated by an experimental feature flag, such as the following for 
{ref}`Confdb <explanation-how-snaps-work-confdb-configuration-mechanism>`

```
sudo snap set system experimental.confdb=true
```
## Request for feedback

We'd be grateful for any feedback users of these experimental features may have. Please leave a comment beneath this forum post, chat to us on [Matrix.org](https://matrix.to/#/#snapd:ubuntu.com), or file an issue in the [snapd GitHub repository](https://github.com/canonical/snapd). Thank you!

## Feature graduation process

When a feature graduates from experimental status, it is first set as default enabled. When the feature flag is set/changed, a warning stating that the feature is enabled by default and will be permanently enabled in a future release will be presented. 

In a future release, the experimental feature is graduated to be permanently enabled. At this point, it is impossible to disable the feature. Attempting to set/change its feature flag will present a warning stating that the feature is no longer experimental and is always enabled.

## Experimental features being removed

Currently, [gate-auto-refresh-hook](https://documentation.ubuntu.com/core/explanation/refresh-control) is planned to be removed. Please share your use case for the feature at [forum](https://forum.snapcraft.io/t/planned-updates-to-snapd-experimental-features) so we can consider it prior to removal.

## Previous experimental features

The following table lists features that were previously experimental.

| Name | Feature Flag | Graduated/Removed | Release | Notes |
| :--- | :----------- | :---------------- | :------ | :---- |
| RobustMountNamespaceUpdates | robust-mount-namespace-updates | Graduated | 2.68 | It controlled how snap-update-ns updates existing mount namespaces. |
| [SnapdSnap](https://snapcraft.io/snapd) | snapd-snap | Graduated | 2.68 | It controlled the possibility of installing the snapd snap. |
| {ref}`GPIOChardevInterface <interfaces-gpio-chardev>`| gpio-chardev-interface | Removed | 2.70 | It controlled the availability of the interface allowing access to specific GPIO chardev lines.|
| PerUserMountNamespace | per-user-mount-namespace | Removed | 2.76 | It controlled the persistence of per-user mount namespaces. |
| [Layouts](https://ubuntu.com/docs/snapcraft/9/how-to/crafting/use-layouts/) | layouts | Graduated | 2.77 | It controlled availability of snap layouts. |
| ClassicPreservesXdgRuntimeDir | classic-preserves-xdg-runtime-dir | Graduated | 2.77 | It controlled XDG_RUNTIME_DIR in snaps with classic confinement. |
| {ref}`DbusActivation <interfaces-dbus-interface>` | dbus-activation | Graduated | 2.77 | It controlled whether snaps daemons can be activated via D-Bus. |
| {ref}`RefreshAppAwareness <explanation-how-snaps-work-refresh-awareness>` | refresh-app-awareness | Graduated | 2.77 | It controlled refresh being aware of running applications. |
| {ref}`QuotaGroups <how-to-guides-manage-snaps-use-resource-quotas>` | quota-groups | Graduated | 2.78 | It enabled experimental journal log quotas for quota groups. |
| [GateAutoRefreshHook](https://documentation.ubuntu.com/core/explanation/refresh-control) | gate-auto-refresh-hook | Removed | 2.79 | It enables refresh control from snaps via the gate-auto-refresh hook. |
| {ref}`CheckDiskSpaceInstall, CheckDiskSpaceRemove, and CheckDiskSpaceRefresh <how-to-guides-manage-snaps-disk-space-awareness>` | check-disk-space-install, check-disk-space-remove, check-disk-space-refresh | Graduated | 2.79 | Disk space awareness controls free disk space checks on snap install, remove, and refresh. |
| {ref}`RefreshAppAwarenessUX <explanation-how-snaps-work-refresh-awareness>` | refresh-app-awareness-ux | Graduated | 2.79 | It enables experimental UX improvements for refresh-app-awareness. |

## Current experimental features

The following table lists all the features considered experimental.

| Name | Feature Flag | Date Introduced | Enabled by Default | Notes |
| :--- | :----------- | :-------------- | :----------------- | :---- |
| {ref}`Hotplug <interfaces-hotplug-support>` | hotplug | Jul 2018 (snapd 2.34) | NO | It controls the availability of dynamically creating slots based on system hardware. Currently only serial ports are supported (serial-port interface). |
| {ref}`ParallelInstances <interfaces-parallel-installs>` | parallel-instances | Jun 2018 (snapd 2.34) | NO | It controls the availability installing a snap multiple times. Layouts are not working properly with parallel installs due to problems with persistent mounts. |
| HiddenSnapDataHomeDir | hidden-snap-folder | Aug 2020 (snapd 2.46) | NO | It controls whether snap data is stored in ~/.snap/data instead of ~/snap. |
| UserDaemons | user-daemons | Aug 2020 (snapd 2.46)   | NO | It controls the availability of user mode service support. Snapcraft needs to enable the `daemon-scope` setting. |
| MoveSnapHomeDir | move-snap-home-dir | Jul 2022 (snapd 2.57) | NO | It controls whether snap user data under ~/snap (or ~/.snap/data) can be moved to ~/Snap.|
| {ref}`Confdb <explanation-how-snaps-work-confdb-configuration-mechanism>` | confdb | Apr 2024 (snapd 2.62) | NO | It enables experimental configuration via confdb views. |
| AppArmorPrompting | apparmor-prompting | Apr 2024 (snapd 2.62) | NO | It enables AppArmor to prompt the user for permission when apps perform certain operations. Currently under active development. |
| ContentCompatLabel | content-compatibility-label | Oct 2025 (snapd 2.72) | NO | It enables compatibility labels for the content interface. |
| RemoteDeviceManagement | remote-device-management | Apr 2026 (snapd 2.75) | NO | It enables experimental remote management of the device via the Store, including delegating control of confdb views to operators. Currently under active development. |
| {ref}`SnapDeltaFormat <how-to-guides-manage-snaps-snap-deltas>` | snap-delta-format | Apr 2026 (snapd 2.75) | NO | It enables deltas that use the "snap delta" format. |
