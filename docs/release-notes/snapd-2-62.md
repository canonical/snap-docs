---
myst:
  html_meta:
    description: Release notes for Snapd 2.62, released on 15 April 2024. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-62)=
# Snapd 2.62

*Released on 15 April 2024.*

The functionality to add custom device interfaces to an app is now complete, as is our create and removal functionality for Ubuntu Core recovery systems. We’ve also finally made a commitment on what minimum [system requirements](https://ubuntu.com/core/docs/system-requirements) might actually be for Ubuntu Core, even if you can’t actually buy a device with less than several gigabytes of on-board RAM.

This release also included two significant additions to our documentation. Firstly, the Docker interface now includes a fully realised example implementation, and secondly, we’ve completed a new page on recovery system via the REST API, thanks to Andrew.

Finally, this release included new packages for Arch Linux, Amazon Linux, Debian, Fedora, openSUSE and Solus.

## Changelog

* Aspects based configuration schema support (experimental)
* Refresh app awareness support for UI (experimental)
* Support for user daemons by introducing new control switches --user/--system/--users for service start/stop/restart (experimental)
* Add AppArmor prompting experimental flag (feature currently unsupported)
* Installation of local snap components of type test
* Packaging of components with snap pack
* Expose experimental features supported/enabled in snapd REST API endpoint /v2/system-info
* Support creating and removing recovery systems for use by factory reset
* Enable API route for creating and removing recovery systems using /v2/systems with action create and /v2/systems/{label} with action remove
* Lift requirements for fde-setup hook for single boot install
* Enable single reboot gadget update for UC20+
* Allow core to be removed on classic systems
* Support for remodeling on hybrid systems
* Install desktop files on Ubuntu Core and update after snapd upgrade
* Upgrade sandbox features to account for cgroup v2 device filtering
* Support snaps to manage their own cgroups
* Add support for AppArmor 4.0 unconfined profile mode
* Add AppArmor based read access to /etc/default/keyboard
* Upgrade to squashfuse 0.5.0
* Support useradd utility to enable removing Perl dependency for UC24+
* Support for recovery-chooser to use console-conf snap
* Add support for --uid/--gid using strace-static
* Add support for notices (from pebble) and expose via the snapd REST API endpoints /v2/notices and /v2/notice
* Add polkit authentication for snapd REST API endpoints /v2/snaps/{snap}/conf and /v2/apps
* Add refresh-inhibit field to snapd REST API endpoint /v2/snaps
* Add refresh-inhibited select query to REST API endpoint /v2/snaps
* Take into account validation sets during remodeling
* Improve offline remodeling to use installed revisions of snaps to fulfill the remodel revision requirement
* Add rpi configuration option sdtv_mode
* When snapd snap is not installed, pin policy ABI to 4.0 or 3.0 if present on host
* Fix gadget zero-sized disk mapping caused by not ignoring zero sized storage traits
* Fix gadget install case where size of existing partition was not correctly taken into account
* Fix trying to unmount early kernel mount if it does not exist
* Fix restarting mount units on snapd start
* Fix call to udev in preseed mode
* Fix to ensure always setting up the device cgroup for base bare and core24+
* Fix not copying data from newly set homedirs on revision change
* Fix leaving behind empty snap home directories after snap is removed (resulting in broken symlink)
* Fix to avoid using libzstd from host by adding to snapd snap
* Fix autorefresh to correctly handle forever refresh hold
* Fix username regex allowed for system-user assertion to not allow '+'
* Fix incorrect application icon for notification after autorefresh completion
* Fix to restart mount units when changed
* Fix to support AppArmor running under incus
* Fix case of snap-update-ns dropping synthetic mounts due to failure to match  desired mount dependencies
* Fix parsing of base snap version to enable pre-seeding of Ubuntu Core Desktop
* Fix packaging and tests for various distributions
* Add remoteproc interface to allow developers to interact with Remote Processor Framework which enables snaps to load firmware to ARM Cortex microcontrollers
* Add kernel-control interface to enable controlling the kernel firmware search path
* Add nfs-mount interface to allow mounting of NFS shares
* Add ros-opt-data interface to allow snaps to access the host /opt/ros/ paths
* Add snap-refresh-observe interface that provides refresh-app-awareness clients access to relevant snapd API endpoints
* steam-support interface: generalize Pressure Vessel root paths and allow access to driver information, features and container versions
* steam-support interface: make implicit on Ubuntu Core Desktop
* desktop interface: improved support for Ubuntu Core Desktop and limit autoconnection to implicit slots
* cups-control interface: make autoconnect depend on presence of cupsd on host to ensure it works on classic systems
* opengl interface: allow read access to /usr/share/nvidia
* personal-files interface: extend to support automatic creation of missing parent directories in write paths
* network-control interface: allow creating /run/resolveconf
* network-setup-control and network-setup-observe interfaces: allow busctl bind as required for systemd 254+
* libvirt interface: allow r/w access to /run/libvirt/libvirt-sock-ro and read access to /var/lib/libvirt/dnsmasq/**
* fwupd interface: allow access to IMPI devices (including locking of device nodes), sysfs attributes needed by amdgpu and the COD capsule update directory
* uio interface: allow configuring UIO drivers from userspace libraries
* serial-port interface: add support for NXP Layerscape SoC
* lxd-support interface: add attribute enable-unconfined-mode to require LXD to opt-in to run unconfined
* block-devices interface: add support for ZFS volumes
* system-packages-doc interface: add support for reading jquery and sphinx documentation
* system-packages-doc interface: workaround to prevent autoconnect failure for snaps using base bare
* microceph-support interface: allow more types of block devices to be added as an OSD
* mount-observe interface: allow read access to /proc/{pid}/task/{tid}/mounts and proc/{pid}/task/{tid}/mountinfo
* polkit interface: changed to not be implicit on core because installing policy files is not possible
* upower-observe interface: allow stats refresh
* gpg-public-keys interface: allow creating lock file for certain gpg operations
* shutdown interface: allow access to SetRebootParameter method
* media-control interface: allow device file locking
* u2f-devices interface: support for Trustkey G310H, JaCarta U2F, Kensington VeriMark Guard, RSA DS100, Google Titan v2
