---
myst:
  html_meta:
    description: Release notes for Snapd 2.72, released on 21 October 2025. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-72)=
# Snapd 2.72

*Released on 21 October 2025*

## Highlights

* Enable the gpio-chardev interface now with the more robust gpio-aggregator configfs kernel interface ([LP: #1916244](https://bugs.launchpad.net/snapd/+bug/1916244))
* FDE enhancements and additions: add generic reseal function and correct sealing with kernel command line defaults, support replacing TPM protected keys at runtime, secboot preinstall check fix actions and using OPTEE (Ubuntu Core & arm) for protecting keys, as an alternative to existing fde-setup hooks.

## Notable updates

* snap-confine: fix non-suid limitation by switching to root:root to operate v1 freezer
* Fix preseeding failure due to scan-disk issue on RPi
* Snap installation: skip snap icon download when running in a cloud or using a proxy store ([LP: #2122054](https://bugs.launchpad.net/snapd/+bug/2122054))
* snap-confine: fix error message with /root/snap not accessible ([LP: #2117558](https://bugs.launchpad.net/snapd/+bug/2117558))
* Interfaces: do not expose Kerberos tickets for classic snaps ([LP: #2121238](https://bugs.launchpad.net/snapd/+bug/2121238))
* Cleanly support socket activation for classic snap ([LP: #2117121](https://bugs.launchpad.net/snapd/+bug/2117121))
* Improve progress reporting for snap install/refresh ([LP: #2112626](https://bugs.launchpad.net/snapd/+bug/2112626))
* Extend output to indicate when snap data snapshot was created during remove ([LP: #2114704](https://bugs.launchpad.net/snapd/+bug/2114704))

For the release plan and complete list of changes, please refer to the [full release notes](https://forum.snapcraft.io/t/the-snapd-roadmap/1973).

## More about GPIO Chardev

This release supports the kernel GPIO character device API with specific GPIO lines mediation through the new gpio-chardev interface which offers more fine-grained control over the gpio-control interface that allowed unrestricted access to all GPIO chips when needed.

For historical context: traditionally Snapd supported mediation of the sysfs interface for GPIO access. This sysfs kernel interface is considered legacy by upstream kernel developers (and will be removed from UC26+ kernels) and it has been replaced by a new character device API, commonly referred to as gpiod.

The new kernel GPIO APIs are typically consumed through the libgpiod library (C or various bindings) or a set of command line utilities provided by said library.

For more information on how to use the new interface (and migration from the older gpio interface), please check the official documentation for the {ref}`gpio-chardev interface <interfaces-gpio-chardev>`.

## More about our FDE journey

***The previous release***, 2.71, concluded the Snapd contribution to TPM FDE for the 25.10 [install image](https://releases.ubuntu.com/25.10/ubuntu-25.10-desktop-amd64.iso).

Progression through the 25.10 cycle up to 2.71:
* 2.68.* - introduced a new key format, added support for passphrases during installation, and included various fixes.
* 2:70 - set roles in TPM keys and fixed resealing with the v1 hook key format.
* 2.71 - added recovery key auto-repair, delivered many additional APIs needed to support installation and use of TPM-backed FDE on hybrid Ubuntu 25.10, and included further fixes.

As part of this work, secboot has been improved to more extensively check whether the platform can support secure boot, which is used by one of the new Snapd APIs introduced in 2.71 and used by the installer to determine TPM FDE availability during hybrid Ubuntu installation.

***This release***, along with releases 2.73 and 2.74 planned for next cycle, will extend and refine the TPM FDE hybrid Ubuntu installation and overall user experience for the Ubuntu 26.04 LTS release.

A lot of care goes into continually ensuring compatibility with Ubuntu Core, previous versions of Snapd and targeted hardware. Each release must pass extensive testing, including test suites for certified hardware. In addition to our own rigorous testing, we strongly advise all users to also thoroughly test all their hardware variations and inform us of potential issues or concerns as soon as possible.

For a broader overview on TPM backed FDE for hybrid Ubuntu 25.10, see: [TPM/FDE progress for Ubuntu 25.10](https://discourse.ubuntu.com/t/tpm-fde-progress-for-ubuntu-25-10/65146)

## Test feedback

Feel free to provide your test feedback here or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug). To help fast track investigations please provide (1) details about the system, (2) Snapd version(s) and (3) steps to reproduce the issue.

## Changelog

* FDE: support replacing TPM protected keys at runtime via the /v2/system-volumes endpoint
* FDE: support secboot preinstall check fix actions for 25.10+ hybrid installs via the /v2/system/{label} endpoint
* FDE: tweak polkit message to remove jargon
* FDE: ensure proper sealing with kernel command line defaults
* FDE: provide generic reseal function
* FDE: support using OPTEE for protecting keys, as an alternative to existing fde-setup hooks (Ubuntu Core only)
* Confdb: 'snapctl get --view' supports passing default values
* Confdb: content sub-rules in confdb-schemas inherit their parent rule's "access"
* Confdb: make confdb error kinds used in API more generic
* Confdb: fully support lists and indexed paths (including unset)
* Prompting: add notice backend for prompting types (unused for now)
* Prompting: include request cgroup in prompt
* Prompting: handle unsupported `xattrs`
* Prompting: add permission mapping for the camera interface
* Notices: read notices from state without state lock
* Notices: add methods to get notice fields and create, reoccur, and `deepcopy` notice
* Notices: add notice manager to coordinate separate notice backends
* Notices: support draining notices from state when notice backend registered as producer of a particular notice type
* Notices: query notice manager from daemon instead of querying state for notices directly
* Packaging: Ubuntu | ignore .git directory
* Packaging: FIPS | bump deb Go FIPS to 1.23
* Packaging: snap | bump FIPS toolchain to 1.23
* Packaging: debian | sync most upstream changes
* Packaging: debian-sid | depends on libcap2-bin for `postint`
* Packaging: Fedora | drop `fakeroot`
* Packaging: snap | modify `snapd.mk` to pass build tags when running unit tests
* Packaging: snap | modify `snapd.mk` to pass `nooptee` build tag
* Packaging: modify `Makefile.am` to fix snap-confine install profile with 'make hack'
* Packaging: modify `Makefile.am` to fix out-of-tree use of 'make hack'
* LP: #2122054 Snap installation: skip snap icon download when running in a cloud or using a proxy store
* Snap installation: add timeout to http client when downloading snap icon
* Snap installation: use http(s) proxy for icon downloads
* LP: #2117558 snap-confine: fix error message with /root/snap not accessible
* snap-confine: fix non-suid limitation by switching to root:root to operate v1 freezer
* core-initrd: do not use writable-paths when not available
* core-initrd: remove debian folder
* LP: #1916244 Interfaces: gpio-chardev | re-enable the gpio-chardev interface now with the more robust gpio-aggregator configfs kernel interface
* Interfaces: gpio-chardev | exclusive snap connections, raise a conflict when both gpio-chardev and gpio are connected
* Interfaces: gpio-chardev | fix gpio-aggregator module load order
* Interfaces: ros-snapd-support | grant access to /v2/changes
* Interfaces: uda-driver-libs, egl-driver-libs, gbm-driver-libs, opengl-driver-libs, opengles-driver-libs | new interfaces to support nvidia driver components
* Interfaces: microstack-support | allow DPDK (hugepage related permissions)
* Interfaces: system-observe | allow reading additional files in /proc, needed by node-exporter
* Interfaces: u2f | add Cano Key, Thesis FIDO2 BioFP+ Security Key and Kensington VeriMark DT Fingerprint Key to device list
* Interfaces: snap-interfaces-requests-control | allow shell API control
* Interfaces: fwupd | allow access to Intel CVS sysfs
* Interfaces: hardware-observe | allow read access to Kernel Samepage Merging (KSM)
* Interfaces: xilinx-dma | support Multi Queue DMA (QDMA) IP
* Interfaces: spi | relax sysfs permission rules to allow access to SPI device node attributes
* Interfaces: content | introduce compatibility label
* LP: #2121238 Interfaces: do not expose Kerberos tickets for classic snaps
* Interfaces: ssh-public-keys | allow ro access to public host keys with ssh-key
* Interfaces: Modify AppArmor template to allow listing systemd credentials and invoking systemd-creds
* Interfaces: modify AppArmor template with workarounds for Go 1.35 cgroup aware GOMAXPROCS
* Interfaces: modify seccomp template to allow landlock_*
* Prevent snap hooks from running while relevant snaps are unlinked
* Make refreshes wait before unlinking snaps if running hooks can be affected
* Fix systemd unit generation by moving "WantedBy=" from section "unit" to "install"
* Add opt-in logging support for snap-update-ns
* Unhide 'snap help' sign and export-key under Development category
* LP: #2117121 Cleanly support socket activation for classic snap
* Add architecture to 'snap version' output
* Add 'snap debug api' option to disable authentication through auth.json
* Show grade in notes for 'snap info --verbose'
* Fix preseeding failure due to scan-disk issue on RPi
* Support 'snap debug api' queries to user session agents
* LP: #2112626 Improve progress reporting for snap install/refresh
* Drop legacy BAMF_DESKTOP_FILE_HINT in desktop files
* Fix /v2/apps error for root user when user services are present
* LP: #2114704 Extend output to indicate when snap data snapshot was created during remove
* Improve how we handle `emmc` volumes
* Improve handling of system-user extra assertions
