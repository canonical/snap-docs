---
myst:
  html_meta:
    description: Release notes for Snapd 2.64, released to beta on 25 July 2024. Read about selected updates and improvements in this release.
---

(release-notes_snapd-2-64)=
# Snapd 2.64

*Released to beta on 25 July 2024*

For the 2.64 release, we updated the build process to use Ubuntu 22.04 instead of Ubuntu 16.04. This change only affected the snapd.snap, and had impact on builds for Debian, Fedora, Arch, openSUSE, or any other classic package

Users should see no changes or compatibility issues, and if you are a snapd developer, this change makes building snapd easier. The latest Snapcraft releases can now be used to build a local version of the snapd package. In the long term, this will also improve our iteration speed as we’ll require fewer snapd builds, providing developers with faster feedback on their changes.

As part of this release cycle, our `ubuntu-image` and validation-sets documentation also improved.

## Changelog

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
* Add missing `etelpmoc.sh` for shell completion
* Do not attempt to run snapd on classic when re-exec is disabled
* Packaging/build maintenance for Debian sid, Fedora, Arch, openSuse
* Add snap debug api command to enable running raw queries
* Enable snap-confine snap mount directory detection
* Replace global seccomp filter with deny rules in standard seccomp template
* Remove support for Ubuntu Core Launcher (superseded by snap-confine)
* Support creating pending serial bound users after serial assertion becomes available
* Support disabling cloud-init using kernel command-line
* In hybrid systems, apps can refresh without waiting for restarts required by essential snaps
* Ship `snap-debug-info.sh` script used for system diagnostics
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
* network-control interface: allow plug/slot access to `gnutls` config and systemd resolved cache flushing via D-Bus
