---
myst:
  html_meta:
    description: Release notes for Snapd 2.24, confirmed stable on 1 May 2017. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-24)=
# Snapd 2.24

The 2.24 release focuses on new features after several 2.23 maintenance releases.

## Highlights

* Remove snap config values when a snap is removed
* Fix potential transition issue from ubuntu-core to core
* Work towards improved aliases
* Many cross-distro improvements
* Fixes to work better with gnome-software
* Enable large file support
* Handle missing `snap-confine` gracefully
* Rework internal interface API to be more flexible and extensible
* Detect devmode by inspecting AppArmor support in the kernel
* Allow `chroot` in the base template
* Fix `pi-config` and add new `sdtv_aspect`, `config_hdmi_boost`, `hdmi_force_hotplug` options
* Interface updates: `browser-support`, `unity7`, `framebuffer`, `location-observe`, `location-control`, `mir`, `opengl`, `unity8`
* New interfaces: `joystick`, `maliit`, `autopilot`
