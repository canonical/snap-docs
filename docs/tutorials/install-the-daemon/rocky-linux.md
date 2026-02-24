(tutorials-install-the-daemon-rocky-linux)=
# Rocky Linux

Snap is available for [Rocky Linux 8](https://rockylinux.org/), a Linux distribution that's being actively developed to provide binary compatibility with Red Hat Enterprise Linux (RHEL).

See also [Installing snap on Red Hat Enterprise Linux](/).

The snap packages for Rocky Linux can be found in the [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) (EPEL) repository.  The EPEL repository can be added to a Rocky Linux system with the following command:

```
$ sudo dnf install epel-release
$ sudo dnf upgrade
```

If you use a root user rather than _sudo_ to handle security privileges, run `su` first and remove _sudo_ from subsequent commands.

 > ⓘ  If you're interested in understanding how these packages are built, see  [Building a snap RPM for Red Hat Enterprise Linux (RHEL) 8](/).

## Installing snapd

With the EPEL repository added to your Rocky Linux installation, simply install the *snapd* package (as root/or with _sudo_):

```
$ sudo yum install snapd
```

Once installed, the *systemd* unit that manages the main snap communication socket needs to be enabled:

```
$ sudo systemctl enable --now snapd.socket
```

To enable *classic* snap support, enter the following to create a symbolic link between `/var/lib/snapd/snap` and `/snap`:

```
$ sudo ln -s /var/lib/snapd/snap /snap
```

Either log out and back in again or restart your system to ensure snap’s paths are updated correctly.

Snap is now installed and ready to go!  If you're using a desktop, a great next step is to [install the Snap Store app](/).

