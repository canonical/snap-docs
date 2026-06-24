(interfaces-installing-snap-on-red-hat)=
# Install snap on Red Hat 

Snap is available for [Red Hat Enterprise Linux (RHEL) 9.x](https://developers.redhat.com/products/rhel/overview), RHEL 8 and RHEL 7, from the 7.6 release onwards. It's also available for CentOS 7.6+ (see {ref}`Installing snap on CentOS <interfaces-installing-snap-on-centos>`).

The packages for RHEL are in the distribution's respective [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) (EPEL) repository. The instructions for adding this repository diverge slightly between RHEL9, RHEL 8 and RHEL 7, which is why they're listed separately below.

If you need to know which version of Red Hat you're running, type `cat /etc/redhat-release`.

If you don't already have the EPEL repository added to your distribution, it can be added as follows:

## Add EPEL to RHEL 9

The EPEL repository can be added to a RHEL 9 system with the following command:

```
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo dnf upgrade
```

## Add EPEL to RHEL 8

The EPEL repository can be added to a RHEL 8 system with the following command:

```
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo dnf upgrade
```

## Installing snapd

With the EPEL repository added to your RHEL installation, the next step is to install the *snapd* package:

```
sudo yum install snapd
```

Once installed, the *systemd* unit that manages the main snap communication socket needs to be enabled:

```
sudo systemctl enable --now snapd.socket
```

To enable *classic* snap support, enter the following to create a symbolic link between `/var/lib/snapd/snap` and `/snap`:

```
sudo ln -s /var/lib/snapd/snap /snap
```

**Either log out and back in again or restart your system** to ensure snap’s paths are updated correctly.

Snap is now installed and ready to go.

