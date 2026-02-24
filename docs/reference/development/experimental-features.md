# Experimental features

Experimental features are part of the _snapd_ development process. They allow engineering teams to test both the viability of an idea and its implementation.

If an experimental feature is considered unstable or likely to change, they are demarcated by an experimental feature flag, such as the following for [Quota groups](/t/25553).

```
sudo snap set system experimental.quota-groups=true
```
## Request for feedback

We'd be grateful for any feedback users of these experimental features may have. Please leave a comment beneath this forum post, chat to us on [Matrix.org](https://matrix.to/#/#snapd:ubuntu.com), or file an issue in the [snapd GitHub repository](https://github.com/canonical/snapd). Thank you!

## Current experimental features

The following table lists all the features considered experimental.

| Name                                                                              | Date Introduced         | Enabled by Default | Notes                                                                                        |
| :-------------------------------------------------------------------------------- | :---------------------- | :----------------- | :------------------------------------------------------------------------------------------- |
| [Layouts](/t/7207)                                                                | Jun 2018 (snapd 2.33)   | YES                | Widely used by graphical snaps as they depend on files in the gnome content snaps.           |
| [Hotplug support](/t/10750)                                                       | Jul 2018 (snapd 2.34)   | NO                 | Currently only serial ports are supported (serial-port interface).                           |
| [Parallel installs](/t/7679)                                                      | Jun 2018 (snapd 2.34)   | NO                 | Layouts are not working properly with parallel installs due problems with persistent mounts. |
| [snapd-snap](https://github.com/canonical/snapd/pull/6404)                        | Oct 2018 (snapd 2.36)   | NO                 | Used for triggering the snapd snap install change.                                           |
| [per-user-mount-namespace](https://github.com/canonical/snapd/pull/6149)          | Jan 2019 (snapd 2.37)   | NO                 |                                                                                              |
| [Refresh app awareness](/t/31152)                                                 | Mar 2019 (snapd 2.38)   | YES                | There are some bugs that need to be addressed.                                               |
| [robust-mount-namespace-updates](https://github.com/canonical/snapd/pull/7773)     | Nov 2019 (snapd 2.42.3) | YES                | No longer considered experimental.                                                           |
| [classic-preserves-xdg-runtime-dir](https://github.com/canonical/snapd/pull/7659) | Jan 2020 (snapd 2.43)   | YES                | No longer considered experimental.                                                           |
| [The dbus interface](/t/2038)                                                     | Aug 2020 (snapd 2.46)   | YES                | dbus-activation is now supported.                                                            |
| [hidden-snap-folder](/t/28509)                                                    | Aug 2020 (snapd 2.46)   | NO                 |                                                                                              |
| [user-daemons](/t/22318)                                                          | Aug 2020 (snapd 2.46)   | NO                 | Snapcraft needs to enable daemon-scope setting.                                              |
| [Disk space awareness](/t/20007)                                                  | Sept 2020 (snapd 2.47)  | NO                 | Needs better testing.                                                                        |
| [gate-auto-refresh-hook](/t/27213)                                                | Apr 2021 (snapd 2.50)   | NO                 | Functionality has mostly been replaced by Validation sets.                                   |
| [Quota groups](/t/25553)                                                          | May 2021 (snapd 2.51)   | NO                 | Memory, CPU and thread quotas have moved out of experimental.                                |
| [move-snap-home-dir](/t/28509)                                                    | Jul 2022 (snapd 2.57)   | NO                 |                                                                                              |
| [apparmor-prompting](https://github.com/canonical/snapd/pull/13693)                | Mar 2024 (snapd 2.62)   | NO                 | Currently under active development.                                                          |
| [refresh-app-awareness-ux](https://github.com/canonical/snapd/pull/13479)         | Mar 2024 (snapd 2.62)   | NO                 | There are some bugs that need to be addressed and some work on the desktop side.             |
