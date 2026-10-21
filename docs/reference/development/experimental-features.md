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

| Name     | Graduated/Removed       | Release            | Notes        |
| :-------- | :---------------------- | :----------------- | :----------- |
| robust-mount-namespace-updates | Graduated | 2.67 | RobustMountNamespaceUpdates controlled how snap-update-ns updates existing mount namespaces. |
| [snapd-snap](https://snapcraft.io/snapd) | Graduated | 2.67 | SnapdSnap controlled possibility of installing the snapd snap. |
| {ref}`gpio-chardev-interface <interfaces-gpio-chardev>`| Removed | 2.69 | GpioChardevInterface controlled the availability of the interface allowing access to specific GPIO chardev lines.|
| per-user-mount-namespace | Removed | 2.76 | PerUserMountNamespace controlled the persistence of per-user mount namespaces. |
| [layouts](https://ubuntu.com/docs/snapcraft/9/how-to/crafting/use-layouts/) | Graduated | 2.77 | Layouts controlled availability of snap layouts. |
| classic-preserves-xdg-runtime-dir | Graduated | 2.77 | ClassicPreservesXdgRuntimeDir controlled XDG_RUNTIME_DIR in snaps with classic confinement. |
| {ref}`dbus-activation <interfaces-dbus-interface>` | Graduated | 2.77 | DbusActivation controlled whether snaps daemons can be activated via D-Bus. |
| {ref}`refresh-app-awareness <explanation-how-snaps-work-refresh-awareness>` | Graduated | 2.77 | RefreshAppAwareness controlled refresh being aware of running applications. |
| {ref}`quota-groups <how-to-guides-manage-snaps-use-resource-quotas>` | Graduated | 2.78 | QuotaGroups enabled experimental journal log quotas for quota groups. |

## Current experimental features

The following table lists all the features considered experimental.

| Name                                                                              | Date Introduced         | Enabled by Default | Notes                                                                                        |
| :-------------------------------------------------------------------------------- | :---------------------- | :----------------- | :------------------------------------------------------------------------------------------- |
| {ref}`hotplug <interfaces-hotplug-support>` | Jul 2018 (snapd 2.34)   | NO                 | Hotplug controls availability of dynamically creating slots based on system hardware. Currently only serial ports are supported (serial-port interface). |
| {ref}`parallel-installs <interfaces-parallel-installs>` | Jun 2018 (snapd 2.34)   | NO                 | ParallelInstances controls availability installing a snap multiple times. Layouts are not working properly with parallel installs due problems with persistent mounts. |
| hidden-snap-folder | Aug 2020 (snapd 2.46)   | NO                 | HiddenSnapDataHomeDir controls whether snap data is stored in ~/.snap/data instead of ~/snap. |
| user-daemons | Aug 2020 (snapd 2.46)   | NO                 | UserDaemons controls availability of user mode service support. Snapcraft needs to enable daemon-scope setting. |
| {ref}`Disk space awareness <how-to-guides-manage-snaps-disk-space-awareness>` | Sept 2020 (snapd 2.47)  | NO                 | CheckDiskSpaceInstall, CheckDiskSpaceRemove, CheckDiskSpaceRefresh control free disk space check on snap install, remove and refresh respectively. Needs better testing. |
| [gate-auto-refresh-hook](https://documentation.ubuntu.com/core/explanation/refresh-control) | Apr 2021 (snapd 2.50)   | NO                 | GateAutoRefreshHook enables refresh control from snaps via gate-auto-refresh hook. Functionality has mostly been replaced by Validation sets. |
| move-snap-home-dir | Jul 2022 (snapd 2.57)   | NO                 |                                                                                              |
| {ref}`Confdb <explanation-how-snaps-work-confdb-configuration-mechanism>` | Apr 2024 (snapd 2.62)   | NO                 | Confdb enables experimental configuration via confdb views. |
| apparmor-prompting | Apr 2024 (snapd 2.62)   | NO                 | AppArmorPrompting enables AppArmor to prompt the user for permission when apps perform certain operations. Currently under active development. |
| {ref}`refresh-app-awareness-ux <explanation-how-snaps-work-refresh-awareness>`       | Apr 2024 (snapd 2.62)   | YES                 | RefreshAppAwarenessUX enables experimental UX improvements for refresh-app-awareness. There are some bugs that need to be addressed and some work on the desktop side. |
| content-compatibility-label | Oct 2025 (snapd 2.72)   | NO                 | ContentCompatLabel enables compatibility labels for the content interface. |
| remote-device-management | Apr 2026 (snapd 2.75) | NO                 | RemoteDeviceManagement enables experimental remote management of the device via the Store, including delegating control of confdb views to operators. Currently under active development. |
| {ref}`snap-delta-format <how-to-guides-manage-snaps-snap-deltas>`   | Apr 2026 (snapd 2.75) | NO                 | SnapDeltaFormat enables deltas that use the "snap delta" format. |
