(interfaces-installing-snap-on-raspbian)=
# Install snap on Raspberry Pi OS

Snap can be installed on a [Raspberry Pi](https://www.raspberrypi.org/) running the latest version of [Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) by opening a terminal and typing a couple of commands.


Enter the following into the terminal:

```
sudo apt update
sudo apt install snapd
```
You will also need to reboot your device. This can be accomplished from the terminal (and from the desktop), but make sure you save any open documents first:

```
sudo reboot
```

After this, install the `core` snap in order to get the latest `snapd`.

```
$ sudo snap install core
core 16-2.45.2 from Canonical✓ installed
```

> ⓘ  Note: some snaps require new snapd features and will show an error such as `snap "lxd" assumes unsupported features"` during install. You can solve this issue by making sure the core snap is installed (`snap install core`) and it's the latest version (`snap refresh core`).


To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```
$ snap install hello-world
hello-world 6.3 from Canonical✓ installed
$ hello-world
Hello World!
```

Snap is now installed and ready to go!  If you're using a desktop, a great next step is to [install the Snap Store app](/reference/interfaces/installing-snap-store-app).


```{tip}
Snap is an integral part of [Ubuntu Core](https://ubuntu.com/core), which can be installed as the native Raspberry Pi operating system. Ubuntu Core provides more permissive access to the Raspberry Pi, and may enable functionality not easily mirrored when snap is installed from Raspberry Pi OS. A good example of this is low-level access to a Raspberry Pi's GPIO pins.
```

