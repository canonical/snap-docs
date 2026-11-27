---
myst:
  html_meta:
    description: Release notes for Snapd 2.27, announced stable on 5 September 2017. Read about selected updates and improvements in this release.
---

(release-notes_snapd-2-27)=
# Snapd 2.27

The 2.27 release focuses on dynamic filesystem updates via `snap-update-ns`, Android boot support, and install/remove hooks. Updating the core snap is enough to use this release on a Linux distribution that allows snapd re-executions.

## Highlights

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

## New interfaces

* `broadcom-asic-control`
* `greengrass-support`
* `password-manager-service`

## Updated interfaces

Many pre-existing interfaces were updated with new rules: `alsa`, `browser-support`, `log-observe`, `mir`, `mount-observe`, `network-control`, `optical-drive`, `optical-observe`, `pulseaudio`, `screen-inhibit-control`, `system-observe`, `timezone-control`, `unity7`, `x11`.
