---
myst:
  html_meta:
    description: Release notes for Snapd 2.51, released on 7 June 2021. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-51)=
# Snapd 2.51

*Released on June 7 2021.*

* New `swap.size` system config setting for Ubuntu Core devices
* Full kernel command line customization for UC20 pc/grub gadgets
* REST API support for creating recovery systems on UC20
* New `raw-input` interface
* New `dsp` interface
* New `sd-control` interface (2.51.3)
* New `netlink-driver` interface (2.51.1)
* New `install-device` gadget hook to be executed during install mode on UC20
* New `snapctl reboot --poweroff|--halt` command to be used in `install-device` hook to shut device off after install mode (but before first boot seeding in run mode)
* New `snapctl reboot system-mode` command to be report what mode a UC20 system is in.
* New kernel FDE hook V2 for UC20 devices
* Experimental quota resource groups support
