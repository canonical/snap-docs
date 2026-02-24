(interfaces-installing-snap-on-kali)=
# Install snap on Kali Linux

```{important}
Installing snap from a _live_ Kali Linux environment is not currently supported. These instructions only work when Kali Linux is installed.
```
From a Kali Linux installation, snap can be installed directly from the command line:

```
sudo apt update
sudo apt install snapd
```
If the *sudo* command isn't installed (usually because a root password was provided at install time), you can install *snap* by first switching to the *root* account:

```
su root
apt update
apt install snapd
```

Additionally, enable and start both the snapd and the snapd.apparmor services with the following command:

```
systemctl enable --now snapd apparmor
```

**Either log out and back in again, or restart your system, to ensure snap’s paths are updated correctly.**

To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```
$ snap install hello-world
hello-world 6.3 from Canonical✓ installed
$ hello-world
Hello World!
```

See [Missing binaries](/how-to-guides/fix-common-issues/index.md#missing-binaries-command-not-found) if snaps are not added to the system path.
