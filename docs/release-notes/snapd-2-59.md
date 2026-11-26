---
myst:
  html_meta:
    description: Release notes for Snapd 2.59, released on 27 March 2023. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-59)=
# Snapd 2.59

*Released on Mar 27 2023.*

* Support setting extra kernel command line parameters via snap configuration and under a gadget allow-list
* Support for Full-Disk-Encryption using ICE
* Support for arbitrary home dir locations via snap configuration
* New nvidia-drivers-support interface
* Support for udisks2 snap
* Pre-download of snaps ready for refresh and automatic refresh of the snap when all apps are closed
* New microovn interface
* Support uboot with `CONFIG_SYS_REDUNDAND_ENV=n`
* Make "snap-preseed --reset" re-exec when needed
* Update the fwupd interface to support fully confined fwupd
* The memory,cpu,thread quota options are no longer experimental
* Support debugging snap client requests via the `SNAPD_CLIENT_DEBUG_HTTP` environment variable
* Support ssh listen-address via snap configuration
* Support for quotas on single services
* prepare-image now takes into account snapd versions going into the image, including in the kernel initrd, to fetch supported assertion formats
