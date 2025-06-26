(snap-tutorials-install-the-daemon-almalinux-os)=
# AlmaLinux OS

Snap is available for [AlmaLinux OS](https://almalinux.org/), a Linux distribution that’s being actively developed to provide binary compatibility with Red Hat Enterprise Linux (RHEL) and 
_pre-Stream_ CentOS.

The snap packages for AlmaLinux OS can be found in the [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) (EPEL) repository.  The EPEL repository is added to a AlmaLinux OS system with the following commands:

```bash
sudo dnf install epel-release
sudo dnf upgrade
```

If you use a root user rather than _sudo_ to handle security privileges, run `su` first and remove _sudo_ from subsequent commands.

### Installing snapd

With the EPEL repository added to your AlmaLinux OS installation, simply install the *snapd* package (as root/or with _sudo_):

```no-highlight
sudo dnf install snapd
```

Once installed, the *systemd* unit that manages the main snap communication socket needs to be enabled:

```bash
sudo systemctl enable --now snapd.socket
```

To enable *classic* snap support, enter the following to create a symbolic link between `/var/lib/snapd/snap` and `/snap`:

```bash
sudo ln -s /var/lib/snapd/snap /snap
```

Either log out and back in again or restart your system to ensure snap’s paths are updated correctly.

Snap is now installed and ready to go!  If you're using a desktop, a great next step is to [install the Snap Store app](/).

