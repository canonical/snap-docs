(tutorials-install-the-daemon-linux-mint)=
# Install snap on Linux Mint

Snap is available for the latest release of Linux Mint, 22.1 (Xia), and for older releases from Linux Mint 18.2 (Sonya) onwards.

You can find out which version of Linux Mint you're running by opening *System info* from the *Preferences* menu.

From Linux Mint 20 onwards, installing Snap is blocked by a file called `nosnap.pref` in the directory `/etc/apt/preferences.d/`; this file needs to be either moved or removed from the directory, or renamed with an extension other than `.pref` before Snap can be installed.

This can be accomplished from the command line, and the following command (for example) renames `nosnap.pref` to `nosnap.backup`:

```
sudo mv /etc/apt/preferences.d/nosnap.pref /etc/apt/preferences.d/nosnap.backup
```

With the file renamed, the package database needs to be updated next:

```
sudo apt update
```

To now install snap from the Software Manager application, search for *snapd* and click **Install**.

Alternatively, *snapd* can be installed from the command line:

```
sudo apt install snapd
```

To complete the installation, either restart your machine, or log out and in again.

To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```
$ snap install hello-world
hello-world 6.4 from Canonical✓ installed
$ hello-world
Hello World!
```

Snap is now installed and ready to go! 
