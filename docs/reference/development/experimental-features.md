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

Currently, {ref}`Hotplug support <interfaces-hotplug-support>` and [gate-auto-refresh-hook](https://documentation.ubuntu.com/core/explanation/refresh-control) are planned to be removed. Please share your use case for these features at [forum](https://forum.snapcraft.io/t/planned-updates-to-snapd-experimental-features) so we can consider it prior to removal

## Current experimental features

The following table lists all the features considered experimental.

| Name                                                                              | Date Introduced         | Enabled by Default | Notes                                                                                        |
| :-------------------------------------------------------------------------------- | :---------------------- | :----------------- | :------------------------------------------------------------------------------------------- |
| {ref}`Hotplug support <interfaces-hotplug-support>`                                                       | Jul 2018 (snapd 2.34)   | NO                 | Currently only serial ports are supported (serial-port interface).                           |
| {ref}`Parallel installs <interfaces-parallel-installs>`                                                      | Jun 2018 (snapd 2.34)   | NO                 | Layouts are not working properly with parallel installs due problems with persistent mounts. |
| hidden-snap-folder                                                    | Aug 2020 (snapd 2.46)   | NO                 |                                                                                              |
| user-daemons                                                          | Aug 2020 (snapd 2.46)   | NO                 | Snapcraft needs to enable daemon-scope setting.                                              |
| {ref}`Disk space awareness <how-to-guides-manage-snaps-disk-space-awareness>`                                                  | Sept 2020 (snapd 2.47)  | NO                 | Needs better testing.                                                                        |
| [gate-auto-refresh-hook](https://documentation.ubuntu.com/core/explanation/refresh-control)                                                | Apr 2021 (snapd 2.50)   | NO                 | Functionality has mostly been replaced by Validation sets.                                   |
| move-snap-home-dir                                                    | Jul 2022 (snapd 2.57)   | NO                 |                                                                                              |
| {ref}`Confdb <explanation-how-snaps-work-confdb-configuration-mechanism>`          | Apr 2024 (snapd 2.62)   | NO                 | Configuration via confdb views.                                                              |
| [apparmor-prompting](https://github.com/canonical/snapd/pull/13693)                | Apr 2024 (snapd 2.62)   | NO                 | Currently under active development.                                                          |
| [refresh-app-awareness-ux](https://github.com/canonical/snapd/pull/13479)         | Apr 2024 (snapd 2.62)   | NO                 | There are some bugs that need to be addressed and some work on the desktop side.             |
| content-compatibility-label                                                        | Oct 2025 (snapd 2.72)   | NO                 |                                                                                              |
| clustering                                                                         | Dec 2025 (snapd 2.73)   | NO                 |                                                                                              |
| remote-device-management                                                           | Apr 2026 (snapd 2.75) | NO                 | Remote device management via the Store, including delegating control of confdb views to operators. Currently under active development.                  |
| seed-refresh                                                                       | Apr 2026 (snapd 2.75) | NO                 |                                                                                              |
| snap-delta-format                                                                  | Apr 2026 (snapd 2.75) | NO                 |                                                                                              |
