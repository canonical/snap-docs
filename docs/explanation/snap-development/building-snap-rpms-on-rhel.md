(interfaces-building-snap-rpms-on-rhel)=
# Building snap rpms on RHEL

Snap is  currently available for  [Red Hat Enterprise Linux (RHEL) 8](https://www.redhat.com/en/enterprise-linux-8) and RHEL 7.6+. See [Installing snap on Red Hat Enterprise Linux (RHEL)](/tutorials/install-the-daemon/red-hat) for installation instructions.

However, if you are an advanced user and wish to see how *snap* is built, its RPMs can be built and manually installed relatively easily, as outlined below.

## Building the RPM manually

First, both the new developer-centric [CodeReady Linux Builder](https://developers.redhat.com/blog/2018/11/15/introducing-codeready-linux-builder/) and the [AppStream](https://developers.redhat.com/blog/2018/11/15/rhel8-introducing-appstreams/) additional user space application repositories need to be added, followed by the [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) repository:

```
$ sudo subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
$ sudo subscription-manager repos --enable rhel-8-for-x86_64-appstream-rpms
$ sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

Next, refresh the package list and install a few dependencies:

```
$ sudo dnf upgrade
$ sudo dnf module install go-toolset
$ sudo dnf install rpmdevtools
```

The snapd code base includes an [RPM SPEC file](https://rpm-packaging-guide.github.io/#what-is-a-spec-file), which [contains the recipe](https://github.com/canonical/snapd/blob/2.42/packaging/fedora/snapd.spec) used to build the RPM packages. To setup the RPM build environment, first prepare the RPM tree in your home directory, fetch the source tarballs and extract the RPM spec:

```
$ rpmdev-setuptree
$ cd ~/rpmbuild/SOURCES
$ curl -L \
    https://github.com/canonical/snapd/releases/download/2.42/snapd_2.42.no-vendor.tar.xz \
    -o snapd_2.42.no-vendor.tar.xz
$ tar -xvJ -C ~/rpmbuild/SPECS --strip-components=3 \
    -f snapd_2.42.no-vendor.tar.xz \
    snapd-2.42/packaging/fedora/
```

Then, while still in `~/rpmbuild/SOURCES`, fetch the remaining release packages and install the build dependencies:

```
$ spectool -g ~/rpmbuild/SOURCES/snapd.spec
$ sudo dnf builddep ~/rpmbuild/SPECS/snapd.spec -y
```

Three RPMs form the complete snapd installation, and these are built as follows:

```
$ rpmbuild -bb ~/rpmbuild/SPECS/snapd.spec
```

Finally, all three RPM packages can be installed:

```
$ sudo dnf localinstall \
   ~/rpmbuild/RPMS/x86_64/snap-confine-2.42-0.el8.x86_64.rpm \
   ~/rpmbuild/RPMS/x86_64/snapd-2.42-0.el8.x86_64.rpm \
   ~/rpmbuild/RPMS/noarch/snapd-selinux-2.42-0.el8.noarch.rpm
```

Once installed, the *systemd* unit that manages the main snap communication socket needs to be enabled:

```
$ sudo systemctl enable --now snapd.socket
```

The snapd environment can now be tested, and hopefully, used productively:

```
$ snap install hello-world
```
A reboot/logout/login should put hello-world in the path.

