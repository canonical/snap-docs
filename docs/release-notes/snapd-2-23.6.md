---
myst:
  html_meta:
        description: Release notes for Snapd 2.23.6, announced in beta on 29 March 2017. Read about selected fixes and improvements to configuration hooks.
---

(release-notes_snapd-2-23-6)=
# Snapd 2.23.6

The 2.23.6 release focuses on improving the robustness of the configuration hook system.

## Highlights

- tests: fix `interfaces-cups-control` for zesty
- configstate,hookstate: timeout the configure hook after 5 minutes, report failures
- packaging: rename the file shipping the snap-confine AppArmor profile to work around dpkg bug #858004
- many: ignore configure hook failures on core refresh to ensure upgrades are always possible
- snapstate: restart as needed if we undid unlinking, i.e. relinked core or kernel snap
- Support for `snap core set pi-config.framebuffer_{width,height}` (and more config.txt settings; see the [configuration options for core snap](https://forum.snapcraft.io/t/configuration-options-for-core-snap/87) topic)

The source is available at the [2.23.6 release tag](https://github.com/snapcore/snapd/releases/tag/2.23.6).
