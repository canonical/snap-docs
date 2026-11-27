---
myst:
  html_meta:
    description: Release notes for Snapd 2.67, released on 11 January 2025. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-67)=
# Snapd 2.67

*Released on 11 January 2025.*

## Highlights:

* **Registry views**
   
   This feature has evolved beyond cross-snap configuration, now enabling custodian snaps to validate changes and store registry data outside of snapd.

* **Components**

  Standard components are now broadly usable, after the addition of the `snap components` command, support for joint install of snaps and components from local files, and tab completion.

   Building on standard components, kernel components have been enhanced with support for the `snapctl model` command for kernel snaps as well as other improvements to enable kernel drivers for proprietary hardware on Ubuntu Core.

## Notable bug fixes:

* AppArmor Prompting: Fixed an issue with overlapping rules ([bug report](https://github.com/canonical/desktop-security-center/issues/74))
* Resolved a deadlock edge case related to app awareness during refresh operations ([LP2084730](https://bugs.launchpad.net/snapd/+bug/2084730))
* Addressed issues with reloading service activation units to prevent systemd errors ([LP2083961](https://bugs.launchpad.net/snapd/+bug/2083961))
* Fixed the generation of AppArmor profiles with incorrect revisions during concurrent refreshes of snaps using the content interface
* Fix AppArmor permissions to allow snaps access to kernel modules and firmware on UC24, which also fixes the kernel-modules-control interface on UC24
* Fix ‘snap run’ getent based user lookup in case of bad PATH (LP2090938 2)
* Fix snapd using the incorrect AppArmor version during undo of an refresh
* Extended hardware-observe interface to allow support riscv_hwprobe syscall and mount-observe interface to allow listmount and statmount syscalls

## Changelog

* AppArmor prompting (experimental): allow overlapping rules
* Registry view (experimental): Changes to registry data (from both users and snaps) can be validated and saved by custodian snaps
* Registry view (experimental): Support 'snapctl get --pristine' to read the registry data excluding staged transaction changes
* Registry view (experimental): Put registry commands behind experimental feature flag
* Components: Make modules shipped/created by kernel-modules components available right after reboot
* Components: Add tab completion for local component files
* Components: Allow installing snaps and components from local files jointly on the CLI
* Components: Allow 'snapctl model' command for gadget and kernel snaps
* Components: Add 'snap components' command
* Components: Bug fixes
* eMMC gadget updates (WIP): add syntax support in gadget.yaml for eMMC schema
* Support for ephemeral recovery mode on hybrid systems
* Support for dm-verity options in snap-bootstrap
* Support for `overlayfs` options and allow empty what argument for `tmpfs`
* Enable ubuntu-image to determine the size of the disk image to create
* Expose 'snap debug' commands 'validate-seed' and 'seeding'
* Add debug API option to use dedicated snap socket /run/snapd-snap.socket 
* Hide experimental features that are no longer required (accepted/rejected)
* Mount ubuntu-save partition with no{exec,dev,`suid`} at install, run and factory-reset
* Improve memory controller support with cgroup v2
* Support ssh socket activation configurations (used by ubuntu 22.10+)
* Fix generation of AppArmor profile with incorrect revision during multi snap refresh 
* Fix refresh app awareness related deadlock edge case
* Fix not caching delta updated snap download
* Fix passing non root uid, guid to initial `tmpfs` mount
* Fix ignoring snaps in try mode when amending
* Fix reloading of service activation units to avoid systemd errors
* Fix snapd snap FIPS build on Launchpad to use Advantage Pro FIPS updates PPA
* Make killing of snap apps best effort to avoid possibility of malicious failure loop
* Alleviate impact of auto-refresh failure loop with progressive delay
* Dropped `timedatex` in selinux-policy to avoid runtime issue
* Fix missing syscalls in seccomp profile
* Modify AppArmor template to allow using SNAP_REEXEC on arch systems
* Modify AppArmor template to allow using vim.tiny (available in base snaps)
* Modify AppArmor template to add read-access to debian_version
* Modify AppArmor template to allow owner to read @{PROC}/@{pid}/sessionid
* {common,personal,system}-files interface: prohibit trailing @ in filepaths
* {desktop,shutdown,system-observe,upower-observe} interface: improve for Ubuntu Core Desktop
* custom-device interface: allow @ in custom-device filepaths
* desktop interface: improve launch entry and systray integration with session
* desktop-legacy interface: allow DBus access to com.canonical.dbusmenu
* fwupd interface: allow access to `nvmem` for thunderbolt plugin
* mpris interface: add `plasmashell` as label
* mount-control interface: add support for nfs mounts
* network-{control,manager} interface: add missing dbus link rules
* network-manager-observe interface: add `getDevices` methods
* opengl interface: add Kernel Fusion Driver access to opengl
* screen-inhibit-control interface: improve screen inhibit control for use on core
* udisks2 interface: allow ping of the UDisks2 service
* u2f-devices interface: add Nitrokey Passkey


## Snapd 2.67.1

*Released on 7 March 2025.*

### Notable updates

* Fix AppArmor permissions to allow snaps access to kernel modules and firmware on UC24, which also fixes the kernel-modules-control interface on UC24
* Fix 'snap run' getent based user lookup in case of bad PATH ([LP: #2090938](https://launchpad.net/bugs/2090938))
* Fix snapd using the incorrect AppArmor version during undo of a refresh
* Extended hardware-observe interface to allow the riscv_hwprobe syscall, and mount-observe interface to allow the listmount and statmount syscalls

### Changelog

* Fix apparmor permissions to allow snaps access to kernel modules and firmware on UC24, which also fixes the kernel-modules-control interface on UC24
* AppArmor prompting (experimental): disallow /./ and /../ in path patterns
* [LP: #2090938](https://bugs.launchpad.net/snapd/+bug/2090938) Fix 'snap run' getent based user lookup in case of bad PATH
* Fix snapd using the incorrect AppArmor version during undo of an refresh for regenerating snap profiles
* Add new syscalls to base templates
* hardware-observe interface: allow riscv_hwprobe syscall
* mount-observe interface: allow listmount and statmount syscalls
