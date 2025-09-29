(interfaces-installing-snap-on-red-hat)=
# installing-snap-on-red-hat

Snap is available for [Red Hat Enterprise Linux (RHEL) 9.x](https://developers.redhat.com/products/rhel/overview), RHEL 8 and RHEL 7, from the 7.6 release onwards. It's also available for CentOS 7.6+ (see [Installing snap on CentOS](/interfaces/installing-snap-on-centos)).

The packages for RHEL are in the distribution's respective [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) (EPEL) repository. The instructions for adding this repository diverge slightly between RHEL9, RHEL 8 and RHEL 7, which is why they're listed separately below.

> ⓘ  If you need to know which version of Red Hat you're running, type `cat /etc/redhat-release`.

If you don't already have the EPEL repository added to your distribution, it can be added as follows:

[details=Adding EPEL to RHEL 9]

The EPEL repository can be added to a RHEL 9 system with the following command:

```bash
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo dnf upgrade
```
 > ⓘ  If you're interested in understanding how these packages are built, see  [Building a snap RPM for Red Hat Enterprise Linux (RHEL) 8](/interfaces/building-snap-rpms-on-rhel).

[/details]

[details=Adding EPEL to RHEL 8]

The EPEL repository can be added to a RHEL 8 system with the following command:

```bash
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo dnf upgrade
```
 > ⓘ  If you're interested in understanding how these packages are built, see  [Building a snap RPM for Red Hat Enterprise Linux (RHEL) 8](/interfaces/building-snap-rpms-on-rhel).

[/details]

[details=Adding EPEL to RHEL 7]

The EPEL repository can be added to a  RHEL 7 system with the following command:

```bash
sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```
Adding the *optional* and *extras* repositories is also recommended:

```bash
sudo subscription-manager repos --enable "rhel-*-optional-rpms" --enable "rhel-*-extras-rpms"
sudo yum update
```
[/details]


### Installing snapd

With the EPEL repository added to your RHEL installation, the next step is to install the *snapd* package:

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

**Either log out and back in again or restart your system** to ensure snap’s paths are updated correctly.

Snap is now installed and ready to go!  If you're using a desktop, a great next step is to [install the Snap Store app](/interfaces/installing-snap-store-app).

