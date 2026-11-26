---
myst:
  html_meta:
    description: Release notes for Snapd 2.66 and 2.66.1, released on 26 November 2024. Read about selected updates and fixes in these releases.
---

(release-notes_snapd-2-66)=
# Snapd 2.66

*Released on 26 November 2024.*

This release added the ability for Snapcraft 8.x to build snapd using with core22 base, and support for building a snapd variant that's [FIPS](https://en.wikipedia.org/wiki/FIPS_140-3) compliant. 

Other highlights include:

*  **AppArmor prompting**

   In collaboration with the security and desktop teams at Canonical, this release of snapd includes the functionality required for snaps to request interface access from the user. 

   For more information on this feature, including design details and how it can be tested in Ubuntu 24.10, see [Introducing Permissions Prompting](https://discourse.ubuntu.com/t/ubuntu-desktop-s-24-10-dev-cycle-part-5-introducing-permissions-prompting/47963).

* **Experimental confdb support**

   This release includes many updates to support _confdb_, formerly known as Registry, which will significantly improve how we handle configuration data and share that data between snaps and devices.

## Snapd 2.66.1

*Released on 26 November 2024.*

This is the first release of the snapd snap built against core22. It includes important fixes and features worked on over the preceding months.

It also comes with new AppArmor version 4.0.2, which supports AppArmor prompting and includes a security update that impacts rare and specific mount-control plug definitions.

### Changelog

* AppArmor prompting (experimental): expand kernel support checks
* AppArmor prompting (experimental): consolidate error messages and add error kinds
* AppArmor prompting (experimental): grant /v2/snaps/{name} via snap-interfaces-requests-control
* AppArmor prompting (experimental): add checks for duplicate pattern variants
* Registry views (experimental): add handlers that commit (and cleanup) registry transactions
* Registry views (experimental): add a snapctl fail command for rejecting registry transactions
* Registry views (experimental): allow custodian snaps to implement registry hooks that modify and save registry data
* Registry views (experimental): run view-changed hooks only for snaps plugging views affected by modified paths
* Registry views (experimental): make registry transactions serialisable
* Snap components: handle refreshing components to revisions that have been on the system before
* Snap components: enable creating Ubuntu Core images that contain components
* Snap components: handle refreshing components independently of snaps
* Snap components: handle removing components when refreshing a snap that no longer defines them
* Snap components: extend snapd Ubuntu Core installation API to allow for picking optional snaps and components to install
* Snap components: extend kernel.yaml with "dynamic-modules", allowing kernel to define a location for kmods from component hooks
* Snap components: renamed component type "test" to "standard"
* Desktop IDs: support installing desktop files with custom names based on desktop-file-ids desktop interface plug attr
* Auto-install snapd on classic systems as prerequisite for any non-essential snap install
* Support loading AppArmor profiles on WSL2 with non-default kernel and securityfs mounted
* Debian/Fedora packaging updates
* Add snap debug command for investigating execution aspects of the snap toolchain
* Improve snap pack error for easier parsing
* Add support for user services when refreshing snaps
* Add snap remove --terminate flag for terminating running snap processes
* Support building FIPS complaint snapd deb and snap
* Fix to not use nss when looking up for users/groups from snapd snap
* Fix ordering in which layout changes are saved
* Patch snapd snap dynamic linker to ignore LD_LIBRARY_PATH and related variables
* Fix libexec dir for openSUSE Slowroll
* Fix handling of the shared snap directory for parallel installs
* Allow writing to /run/systemd/journal/dev-log by default
* Avoid state lock during snap removal to avoid delaying other snapd operations
* Add nomad-support interface to enable running Hashicorp Nomad
* Add intel-qat interface
* u2f-devices interface: add u2f trustkey t120 product id and fx series fido u2f devices
* desktop interface: improve integration with xdg-desktop-portal
* desktop interface: add desktop-file-ids plug attr to desktop interface
* unity7 interface: support desktop-file-ids in desktop files rule generation
* desktop-legacy interface: support desktop-file-ids in desktop files rule generation
* desktop-legacy interface: grant access to gcin socket location
* login-session-observe interface: allow introspection
* custom-device interface: allow to explicitly identify matching device in udev tagging block
* system-packages-doc interface: allow reading /usr/share/javascript
* modem-manager interface: add new format of WWAN ports
* pcscd interface: allow pcscd to read opensc.conf
* cpu-control interface: add IRQ affinity control to cpu_control
* opengl interface: add support for cuda workloads on Tegra iGPU in opengl interface
