(interfaces-installing-snap-on-centos)=
# Install snap on CentOS

Snap is available for [CentOS 9 Stream](https://www.centos.org/), CentOS 8 Stream, CentOS 8 and CentOS 7, from the 7.6 release onwards. It's also available for Red Hat Enterprise Linux (RHEL) 7.6+ (see [Installing snap on Red Hat Enterprise Linux](red-hat)).

The packages for CentOS 8/9 and CentOS 7 are in each distribution's respective [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) (EPEL) repository. The instructions for adding this repository diverge slightly between CentOS 8/9 and CentOS 7, which is why they're listed separately below.

```{tip}
If you need to know which version of CentOS you're running, type `cat /etc/centos-release`.
```

If you don't already have the EPEL repository added to your distribution, it can be added as follows:

## CentOS 8/9 Stream

The EPEL repository can be added to a CentOS 8/9 Stream system with the following command:

```bash
sudo dnf install epel-release
sudo dnf upgrade
```

## CentOS 7 Stream

The EPEL repository can be added to a CentOS 7 system with the following command:

```bash
sudo yum install epel-release
```

## Missing packages with EPEL

Packages in the EPEL repository are built against dependencies from the current RHEL release, and these packages are regularly imported from RHEL by the CentOS project.

Occasionally, however, the exact version of a specific package used to build the snapd RPM has yet to be imported into the base CentOS repositories. This can cause missing package errors similar to the following:

```no-highlight
Problem: package snapd-2.42.1-1.el8.x86_64 requires snapd-selinux = 2.42.1-1.el8,
but none of the providers can be installed.
```

In such an event, rather than waiting for EPEL packages to be updated, you can enable the [continuous release (CR)](https://wiki.centos.org/AdditionalResources(2f)Repositories(2f)CR.html) repository. This repository contains packages destined for the next point release of CentOS and should satisfy any missing version mismatch dependencies.

If you're interested in understanding how these packages are built, see  [Building a snap RPM for Red Hat Enterprise Linux](/explanation/snap-development/building-snap-rpms-on-rhel).

## Installing snapd

With the EPEL repository added to your CentOS installation, simply install the *snapd* package:

```bash
sudo yum install snapd
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
