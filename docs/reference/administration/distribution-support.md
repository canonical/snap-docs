(reference-administration-distribution-support)=
# Distribution support

Latest public release: 2.68 [github releases](https://github.com/canonical/snapd/releases). See [snapd roadmap](https://forum.snapcraft.io/t/the-snapd-roadmap/1973) for details.

## Repology overview

[![Packaging status](https://repology.org/badge/vertical-allrepos/snapd.svg?exclude_unsupported=1&columns=4&header=Overview+of+snapd+versions)](https://repology.org/project/snapd/versions)

We use a third-party tool called [Repology](https://repology.org/) to track snapd version numbers across various Linux distributions.

On some distributions, a non-snap package will install the snapd snap which will subsequently update itself. This process is called _re-execution_. On such systems, Repology can only detect the version number of the native non-snap package and not the updated snapd from the snap.

Distributions that have reached their end-of-life are excluded from the list.

## Ubuntu

[![Ubuntu 14.04 package](https://repology.org/badge/version-for-repo/ubuntu_14_04/snapd.svg)](https://repology.org/project/snapd/versions)
[![Ubuntu 16.04 package](https://repology.org/badge/version-for-repo/ubuntu_16_04/snapd.svg)](https://repology.org/project/snapd/versions)
[![Ubuntu 18.04 package](https://repology.org/badge/version-for-repo/ubuntu_18_04/snapd.svg)](https://repology.org/project/snapd/versions)
[![Ubuntu 20.04 package](https://repology.org/badge/version-for-repo/ubuntu_20_04/snapd.svg)](https://repology.org/project/snapd/versions)
[![Ubuntu 22.04 package](https://repology.org/badge/version-for-repo/ubuntu_22_04/snapd.svg)](https://repology.org/project/snapd/versions)
[![Ubuntu 24.04 package](https://repology.org/badge/version-for-repo/ubuntu_24_04/snapd.svg)](https://repology.org/project/snapd/versions)
[![Ubuntu 25.04 package](https://repology.org/badge/version-for-repo/ubuntu_25_04/snapd.svg)](https://repology.org/project/snapd/versions)

Due to distribution policy snapd is not regularly updated to the latest available version. Snapd re-execution is supported on Ubuntu. The versions listed above are usually only relevant before the installation of the first snap. Outside of unusual circumstances, the Ubuntu package is synchronized from Debian. This process stops once an upcoming Ubuntu release is entering feature freeze.

## Debian

[![Debian 11 package](https://repology.org/badge/version-for-repo/debian_11/snapd.svg)](https://repology.org/project/snapd/versions)
[![Debian 12 package](https://repology.org/badge/version-for-repo/debian_12/snapd.svg)](https://repology.org/project/snapd/versions)
[![Debian 13 package](https://repology.org/badge/version-for-repo/debian_13/snapd.svg)](https://repology.org/project/snapd/versions)
[![Debian Unstable package](https://repology.org/badge/version-for-repo/debian_unstable/snapd.svg)](https://repology.org/project/snapd/versions)

Due to distribution policy snapd is not regularly updated to the latest available version. Snapd re-execution is supported on Debian. The versions listed above are usually only relevant before the installation of the first snap.

Resources for developers:
 - [Salsa (Debian gitlab repository)](https://tracker.debian.org/pkg/snapd)
 - [Tracker (package status)](https://tracker.debian.org/pkg/snapd)
 - [Continuous integration](https://ci.debian.net/packages/s/snapd/) (requires authentication)
- [2.61.1 update thread](https://forum.snapcraft.io/t/debian-package-of-snapd-is-out-of-date-2-61-1/38515)

## Fedora

[![Fedora 40 package](https://repology.org/badge/version-for-repo/fedora_40/snapd.svg)](https://repology.org/project/snapd/versions)
[![Fedora 41 package](https://repology.org/badge/version-for-repo/fedora_41/snapd.svg)](https://repology.org/project/snapd/versions)

[![Fedora Rawhide package](https://repology.org/badge/version-for-repo/fedora_rawhide/snapd.svg)](https://repology.org/project/snapd/versions)

Fedora allows updating packages in stable distributions. You can expect all snapd releases to be updated within a week or two of the upstream release, following the usual testing and migration process. Due to ABI incompatibilities, differences in build configuration process and distribution policy snapd re-execution  is not supported on Fedora.

Resources for developers:
- [koschei (continuous integration)](https://koschei.fedoraproject.org/package/snapd)
- [koji (build farm)](https://koji.fedoraproject.org/koji/packageinfo?packageID=23242)
- [bodhi (updates)](https://bodhi.fedoraproject.org/updates/?packages=snapd)
- [source code](https://src.fedoraproject.org/rpms/snapd)

## EPEL (RHEL, CentOS, Alma Linux, Rocky Linux, etc)

[![EPEL 7 package](https://repology.org/badge/version-for-repo/epel_7/snapd.svg)](https://repology.org/project/snapd/versions)
[![EPEL 8 package](https://repology.org/badge/version-for-repo/epel_8/snapd.svg)](https://repology.org/project/snapd/versions)
[![EPEL 9 package](https://repology.org/badge/version-for-repo/epel_9/snapd.svg)](https://repology.org/project/snapd/versions)

Snapd is not directly available in the Red Hat family of *enterprise* distributions. It is freely available and maintained in the commonly used [EPEL (extra packages for enterprise linux) repository](https://docs.fedoraproject.org/en-US/epel/). You can expect all snapd releases to be updated within a week or two of the upstream release, following the usual testing and migration process. Due to ABI incompatibilities, differences in build configuration process and distribution policy snapd re-execution  is not supported on any of those systems.

## openSUSE, SUSE Enterprise Linux

Snapd is not directly available in the openSUSE or SUSE archive. Instead the package is maintained in the `system:snappy` project in Open Build Service (OBS), making it easily installable on the family of related SUSE distributions. You can expect all snapd releases to be updated within a week of the upstream release. Due to ABI incompatibilities, differences in build configuration process and distribution policy snapd re-execution  is not supported.

| Distro | Version |  Reexec |
|--|--|--|
| SLE 15 | 2.52 | n |
| Factory | 2.68 | n |
| Leap 15.5 | 2.68 | n |
| Leap 15.6 | 2.68 | n |
| Tumbleweed | 2.68 | n |

Resources for developers:
 - [system:snappy](https://build.opensuse.org/project/show/system:snappy)
 - [system:snappy/snapd source code](https://build.opensuse.org/package/show/system:snappy/snapd)
- [OSB#1127366 include snapd in Factory WIP](https://bugzilla.opensuse.org/show_bug.cgi?id=1127366)

## Arch Linux

[![AUR package](https://repology.org/badge/version-for-repo/aur/snapd.svg)](https://repology.org/project/snapd/versions)

Snapd is available in the [Arch User Repository (AUR)](https://wiki.archlinux.org/title/Arch_User_Repository). You can expect all snapd releases to be updated within a week of the upstream release. Due to ABI incompatibilities, differences in build configuration process, snapd re-execution  is not supported.

Resources for developers:
 - Package repo: [snapd in AUR](https://aur.archlinux.org/packages/snapd)

## Manjaro

[![Manjaro Stable package](https://repology.org/badge/version-for-repo/manjaro_stable/snapd.svg)](https://repology.org/project/snapd/versions)
[![Manjaro Testing package](https://repology.org/badge/version-for-repo/manjaro_testing/snapd.svg)](https://repology.org/project/snapd/versions)
[![Manjaro Unstable package](https://repology.org/badge/version-for-repo/manjaro_unstable/snapd.svg)](https://repology.org/project/snapd/versions)

Resources for developers:
- [packaging repository packages/extra](https://gitlab.manjaro.org/packages/extra/snapd)

## Gentoo

[![Gentoo package](https://repology.org/badge/version-for-repo/gentoo/snapd.svg)](https://repology.org/project/snapd/versions)

Resources for developers:
- [packaging repository app-containers/snapd](https://packages.gentoo.org/packages/app-containers/snapd)

## Solus

[![Solus package](https://repology.org/badge/version-for-repo/solus/snapd.svg)](https://repology.org/project/snapd/versions)

Snapd is available in the distribution archive. You may have to run extra commands to enable the `snapd.socket` and the `snapd.apparmor.service`. See TBD - installation instructions missing.

Resources for developers:
 - [packaging repository](https://github.com/getsolus/packages/tree/main/packages/s/snapd)

## Amazon Linux

Package repo: [snapd-amazon-linux](https://github.com/bboozzoo/snapd-amazon-linux) (unofficial)

Snapd upstream packaging: [snapd upstream](https://github.com/canonical/snapd/blob/master/packaging)

Instructions https://forum.snapcraft.io/t/unofficial-snapd-repositories-for-amazon-linux/38736

| Distro | Version |  Reexec| Notes |
|--|--|--|--|
| AL2 | 2.67 | n | unofficial |
| AL2023 | 2.67 |  n | unofficial |

## Yocto layer

A Yocto meta-layer called [meta-snapd](https://github.com/canonical/meta-snapd) exists, allowing the use of snapd and snaps on custom-build system images. Individual branches are named after Yocto release names.

| Snapd Release | Yocto Release | Kernel Recipe | Kernel Version | Confinement |
|--|--|--|--|--|
| 2.61.2 | kirkstone | linux-yocto | 5.10 | strict |
| 2.61.2 | kirkstone | linux-yocto | 5.15 | strict |
| 2.63 | nanbield | linux-yocto | - | partial |
| 2.63 | scarthgap| linux-yocto | - | partial |
| 2.63 | master | linux-yocto | - | partial |

At present master branch does not build as meta-security is being updated to support changes happening in Poky.

