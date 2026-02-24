(tutorials-install-the-daemon-ubuntu)=
# Install snap on Ubuntu

Snap is pre-installed and ready to go on all recent releases of Ubuntu.

This means, if you're running [Ubuntu 16.04 LTS (Xenial Xerus)](https://www.ubuntu.com/) or later, including [Ubuntu 22.04 LTS (Jammy Jellyfish)](https://releases.ubuntu.com/22.04/) and [Ubuntu 23.04 (Lunar Lobster)](https://releases.ubuntu.com/lunar/), you don't need to do anything.

If you need to know which version of Ubuntu you're running, open **Settings** and select the **About** page. Alternatively, from the command line, type `lsb_release -a`.

For versions and flavours of Ubuntu that don't include *snap* by default, *snap* can be installed from the Ubuntu Software Centre by searching for `snapd`.

Alternatively, *snapd* can be installed from the command line:

```
sudo apt update
sudo apt install snapd
```

Either log out and back in again, or restart your system, to ensure snap’s paths are updated correctly.

To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```
$ sudo snap install hello-world
hello-world 6.4 from Canonical✓ installed
$ hello-world
Hello World!
```

Snap is now installed and ready to go.
