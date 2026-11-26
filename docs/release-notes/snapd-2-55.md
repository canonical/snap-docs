---
myst:
  html_meta:
    description: Release notes for Snapd 2.55, released as 2.55.3 on 20 April 2022. Read about the layout regression fix and selected updates.
---

(release-notes_snapd-2-55)=
# Snapd 2.55

## Snapd 2.55.2

A regression was discovered in the snapd 2.55.2 release after it became available in the stable channel, so the stable release was reverted back to 2.54.4.

The bug was that when "layouts" are applied to content snap content, those layouts could be mounted in the wrong way, resulting in missing files for the snap. This caused, for example, the `newsflash` snap to fail to start. The fix shipped in 2.55.3.

## Snapd 2.55.3

*Released on Apr 20 2022.*

* Fix refresh layout construction (fixes Firefox crash)
* Support for the "piboot" bootloader
* Interface operations are faster by using more batched operations
* New mount-control interface ([topic](https://forum.snapcraft.io/t/the-mount-control-interface/28953))
* New polkit interface ([topic](https://forum.snapcraft.io/t/the-polkit-interface/28408))
