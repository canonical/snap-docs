(tutorials-install-the-daemon-index)=
# Install the daemon

Snaps are app packages for desktop, cloud and IoT that are easy to install, secure, cross-platform and dependency-free. 

The snap daemon, known as *snapd*, is the background service that manages and maintains your snaps. It needs to be  running before a snap can be installed.

Fortunately, the snap daemon is pre-installed and running on many distributions by default, and it's easy to install on most other distributions.

See [Troubleshooting](/how-to-guides/fix-common-issues/index) for help resolving installation issues.

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
| [AlmaLinux OS](/tutorials/install-the-daemon/almalinux-os) | [Arch Linux](/tutorials/install-the-daemon/arch-linux)|
| [CentOS](/tutorials/install-the-daemon/centos) | [Debian](/tutorials/install-the-daemon/debian)|
| [elementary OS](/tutorials/install-the-daemon/elementary-os) | [Fedora](/tutorials/install-the-daemon/fedora) |
| [GalliumOS](/tutorials/install-the-daemon/galliumos) | [Kali Linux](/tutorials/install-the-daemon/kali) |
| [KDE Neon*](/tutorials/install-the-daemon/neon) | [Linux Mint](/tutorials/install-the-daemon/linux-mint) | 
| [Manjaro*](/tutorials/install-the-daemon/manjaro-linux) | [openSUSE](/tutorials/install-the-daemon/opensuse) |
| [Parrot Security OS](/tutorials/install-the-daemon/parrot) | [Pop!_OS](/tutorials/install-the-daemon/pop-os) |
| [Raspberry Pi OS](/tutorials/install-the-daemon/raspberrypios) | | [Rocky Linux](/tutorials/install-the-daemon/rocky-linux) |
| [Ubuntu*](/tutorials/install-the-daemon/ubuntu) |  |

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
openSUSE <opensuse>
Parrot Security OS <parrot>
Pop!_OS <pop-os>
Raspberry Pi OS <raspberrypios>
Red Hat <red-hat>
Rocky Linux <rocky-linux>
Ubuntu <ubuntu>
