---
myst:
  html_meta:
    description: Release notes for Snapd 2.60.3, released on 2 September 2023. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-60-3)=
# Snapd 2.60.3

*Released on Sep 02 2023.*

* Bugfixes
* Use "aes-cbc-essiv:sha256" in `cryptsetup` on arm 32bit devices to increase speed on devices with CAAM support
* Stop using `-O no-expr-simplify` in apparmor_parser to avoid  potential exponential memory use. This can lead to slower   policy complication in some cases but it is much safer on  low memory devices.
* Support for dynamic snapshot data exclusions
* Apparmor userspace is vendored inside the snapd snap
* Added a default-configure hook that exposes gadget default configuration  options to snaps during first install before services are started
* Allow install from initrd to speed up the initial installation for  systems that do not have a install-device hook
* New `snap sign --chain` flag that appends the account and account-key  assertions
* Support validation-sets in the model assertion
* Support new "min-size" field in gadget.yaml
* New interface: "userns"
