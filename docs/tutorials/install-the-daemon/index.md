---
myst:
  html_meta:
    description: Installation instructions for the snap daemon (snapd) - the background service that manages and maintains your snaps. Snapd is pre-installed on many Linux distributions, and easy to install on most others. Find installation instructions for your distribution here.
---

(tutorials-install-the-daemon-index)=
# Install the daemon

Snaps are app packages for desktop, cloud and IoT that are easy to install, secure, cross-platform and dependency-free. 

The snap daemon, known as *snapd*, is the background service that manages and maintains your snaps. It needs to be  running before a snap can be installed.

Fortunately, the snap daemon is pre-installed and running on many distributions by default, and it's easy to install on most other distributions.

See {ref}`Troubleshooting <how-to-guides-fix-common-issues-index>` for help resolving installation issues.

## Snap pre-installed

The snap daemon (snapd) is pre-installed and ready to go on the following:

| | |
|--|--|
| [KDE Neon](https://neon.kde.org/) | [Manjaro](https://manjaro.org/) |
[Solus](https://getsol.us/) | [Ubuntu](https://ubuntu.com/) 18.04 and above |
 | Most [Ubuntu flavours](https://wiki.ubuntu.com/DerivativeTeam/Derivatives#Official_Ubuntu_Flavors) | [Zorin OS](https://zorinos.com/) |


## Without snap

For distributions without the snap daemon pre-installed, use the links below for specific installation instructions:

| | |
|--|--|
| {ref}`AlmaLinux OS <tutorials-install-the-daemon-almalinux-os>` | {ref}`Arch Linux <tutorials-install-the-daemon-arch-linux>`|
| {ref}`CentOS <interfaces-installing-snap-on-centos>` | {ref}`Debian <tutorials-install-the-daemon-debian>`|
| {ref}`elementary OS <tutorials-install-the-daemon-elementary-os>` | {ref}`Fedora <tutorials-install-the-daemon-fedora>` |
| {ref}`GalliumOS <interfaces-installing-snap-on-galliumos>` | {ref}`Kali Linux <interfaces-installing-snap-on-kali>` |
| {ref}`KDE Neon* <interfaces-installing-snap-on-kde-neon>` | {ref}`Linux Mint <tutorials-install-the-daemon-linux-mint>` | 
| {ref}`Manjaro* <tutorials-install-the-daemon-manjaro-linux>` | {ref}`OpenMandriva <tutorials-install-the-daemon-openmandriva>` |
| {ref}`openSUSE <tutorials-install-the-daemon-opensuse>` | {ref}`Parrot Security OS <interfaces-installing-snap-on-parrot-security-os>` |
| {ref}`Pop!_OS <tutorials-install-the-daemon-pop-os>`  | {ref}`Raspberry Pi OS <interfaces-installing-snap-on-raspbian>` |
| {ref}`Rocky Linux <tutorials-install-the-daemon-rocky-linux>` | {ref}`Ubuntu* <tutorials-install-the-daemon-ubuntu>` |

**\*** While snapd is pre-installed on these systems, installation instructions can help if you're using older versions, or want to re-install snap after removing it.

```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

AlmaLinux OS <almalinux-os>
Arch Linux <arch-linux>
CentOS <centos>
Debian <debian>
Elementary OS <elementary-os>
Fedora <fedora>
GalliumOS <galliumos>
Kali Linux <kali>
Linux Mint <linux-mint>
Manjaro Linux <manjaro-linux>
KDE Neon <neon>
openMandriva <openmandriva>
openSUSE <opensuse>
Parrot Security OS <parrot>
Pop!_OS <pop-os>
Raspberry Pi OS <raspberrypios>
Red Hat <red-hat>
Rocky Linux <rocky-linux>
Ubuntu <ubuntu>
