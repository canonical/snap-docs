(snap-tutorials-install-the-daemon-pop-os)=
# Install snap on Pop!\_OS

Snap can be installed on Pop!_OS from the command line. Open *Terminal* from the Applications launcher and type the following:

```bash
$ sudo apt update
$ sudo apt install snapd
```

Either log out and back in again, or restart your system, to ensure snap’s paths are updated correctly.

To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```bash
$ sudo snap install hello-world
hello-world 6.3 from Canonical✓ installed
$ hello-world
Hello World!
```

Snap is now installed and ready to go!  If you're using a desktop, a great next step is to [install the Snap Store app](/).

