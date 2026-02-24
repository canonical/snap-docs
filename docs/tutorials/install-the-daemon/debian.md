(tutorials-install-the-daemon-debian)=
# Install snap on Debian

On Debian, snap can be installed directly from the command line:

```
sudo apt update
sudo apt install snapd
```
If the *sudo* command isn't installed (usually because a root password was provided at install time), you can install *snap* by first switching to the *root* account:

```
$ su root
# apt update
# apt install snapd
```

**Either log out and back in again, or restart your system, to ensure snap’s paths are updated correctly.**

After this, install the `snapd` snap in order to get the latest `snapd`.

```
sudo snap install snapd
```

> ⓘ  Note: some snaps require new snapd features and will show an error such as `snap "lxd" assumes unsupported features"` during install. You can solve this issue by making sure the core snap is installed (`snap install core`) and it's the latest version (`snap refresh core`).

To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```
$ sudo snap install hello-world
hello-world 6.3 from Canonical✓ installed
$ hello-world
Hello World!
```

Snap is now installed and ready to go!
