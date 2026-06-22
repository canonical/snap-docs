(ref-experimental-features_experimental-features)=
# Experimental features

Experimental features are part of the _snapd_ development process. They allow engineering teams to test both the viability of an idea and its implementation.

If an experimental feature is considered unstable or likely to change, they are demarcated by an experimental feature flag, such as the following for {ref}`Quota groups <how-to-guides-manage-snaps-use-resource-quotas>`.

```
sudo snap set system experimental.quota-groups=true
```
## Request for feedback

We'd be grateful for any feedback users of these experimental features may have. Please leave a comment beneath this forum post, chat to us on [Matrix.org](https://matrix.to/#/#snapd:ubuntu.com), or file an issue in the [snapd GitHub repository](https://github.com/canonical/snapd). Thank you!

## Current experimental features

The following table lists all the features considered experimental.

| Name                                                                              | Date Introduced         | Enabled by Default | Notes                                                                                        |
| :-------------------------------------------------------------------------------- | :---------------------- | :----------------- | :------------------------------------------------------------------------------------------- |
| [Layouts](https://documentation.ubuntu.com/snapcraft/9.0/how-to/crafting/use-layouts/)                                      | Jun 2018 (snapd 2.33)   | YES                | Widely used by graphical snaps as they depend on files in the gnome content snaps.           |
| {ref}`Hotplug support <interfaces-hotplug-support>`                                                       | Jul 2018 (snapd 2.34)   | NO                 | Currently only serial ports are supported (serial-port interface).                           |
| {ref}`Parallel installs <interfaces-parallel-installs>`                                                      | Jun 2018 (snapd 2.34)   | NO                 | Layouts are not working properly with parallel installs due problems with persistent mounts. |
| {ref}`Refresh app awareness <explanation-how-snaps-work-refresh-awareness>`                                                 | Mar 2019 (snapd 2.38)   | YES                | There are some bugs that need to be addressed.                                               |
| [classic-preserves-xdg-runtime-dir](https://github.com/canonical/snapd/pull/7659) | Jan 2020 (snapd 2.43)   | YES                | No longer considered experimental.                                                           |
| {ref}`The dbus interface <interfaces-dbus-interface>`                                                     | Aug 2020 (snapd 2.46)   | YES                | dbus-activation is now supported.                                                            |
| hidden-snap-folder                                                    | Aug 2020 (snapd 2.46)   | NO                 |                                                                                              |
| user-daemons                                                          | Aug 2020 (snapd 2.46)   | NO                 | Snapcraft needs to enable daemon-scope setting.                                              |
| {ref}`Disk space awareness <how-to-guides-manage-snaps-disk-space-awareness>`                                                  | Sept 2020 (snapd 2.47)  | NO                 | Needs better testing.                                                                        |
| [gate-auto-refresh-hook](https://documentation.ubuntu.com/core/explanation/refresh-control)                                                | Apr 2021 (snapd 2.50)   | NO                 | Functionality has mostly been replaced by Validation sets.                                   |
| {ref}`Quota groups <how-to-guides-manage-snaps-use-resource-quotas>`                                                          | May 2021 (snapd 2.51)   | NO                 | Memory, CPU and thread quotas have moved out of experimental.                                |
| move-snap-home-dir                                                    | Jul 2022 (snapd 2.57)   | NO                 |                                                                                              |
| {ref}`Confdb <explanation-how-snaps-work-confdb-configuration-mechanism>`          | Apr 2024 (snapd 2.62)   | NO                 | Configuration via confdb views.                                                              |
| [apparmor-prompting](https://github.com/canonical/snapd/pull/13693)                | Apr 2024 (snapd 2.62)   | NO                 | Currently under active development.                                                          |
| [refresh-app-awareness-ux](https://github.com/canonical/snapd/pull/13479)         | Apr 2024 (snapd 2.62)   | NO                 | There are some bugs that need to be addressed and some work on the desktop side.             |
| confdb-control                                                                     | Mar 2025 (snapd 2.68)   | NO                 | Delegate control of confdb views to operators. Full end-to-end use requires remote-device-management, which is still under development. |
| content-compatibility-label                                                        | Oct 2025 (snapd 2.72)   | NO                 |                                                                                              |
| clustering                                                                         | Dec 2025 (snapd 2.73)   | NO                 |                                                                                              |
| remote-device-management                                                           | Apr 2026 (snapd 2.75) | NO                 | Remote device management via the Store. Currently under active development.                  |
| seed-refresh                                                                       | Apr 2026 (snapd 2.75) | NO                 |                                                                                              |
| snap-delta-format                                                                  | Apr 2026 (snapd 2.75) | NO                 |                                                                                              |
