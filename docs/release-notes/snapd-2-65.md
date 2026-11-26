---
myst:
  html_meta:
    description: Release notes for Snapd 2.65, released to beta on 23 August 2024. Read about selected updates and fixes in this release.
---

(release-notes_snapd-2-65)=
# Snapd 2.65

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
* power-control interface: support for battery charging thresholds, type/status and AC type/status
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

## Snapd 2.65.1

*Released to beta on 24 August 2024.*

* Fix snapd riscv64 build

## Snapd 2.65.3

*Released to beta on 24 August 2024.*

* Fix missing aux info from store on snap setup
* Bump squashfuse from version 0.5.0 to 0.5.2 (used in snapd deb only)
