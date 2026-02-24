(tutorials-install-the-daemon-arch-linux)=
# Install snap on Arch Linux

On Arch Linux, *snap* can be installed from the [Arch User Repository (AUR)](https://aur.archlinux.org/packages/snapd/).

The [manual build process](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages) is the Arch-supported install method for AUR packages, and you'll need the [prerequisites](https://wiki.archlinux.org/index.php/Arch_User_Repository#Prerequisites) installed before you can install any AUR package. You can then install snap with the following:

```
git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si
```

Once installed, the *systemd* unit that manages the main snap communication socket needs to be enabled:

```
sudo systemctl enable --now snapd.socket
```

## Confinement

To take advantage of [Snap confinement](/explanation/security/snap-confinement) and application sandboxing, ensure [AppArmor](https://wiki.archlinux.org/title/AppArmor#Installation) is install and enabled on your system, then run the following:

```
sudo systemctl enable --now snapd.apparmor.service
```

To test whether confinement is running correctly, install the [hello-world](https://snapcraft.io/hello-world) snap and run `hello-world.evil`. If confinement is working, you will see a permission denied error:

```
$ hello-world.evil 
Hello Evil World!
This example demonstrates the app confinement
You should see a permission denied error next
/snap/hello-world/29/bin/evil: 9: /snap/hello-world/29/bin/evil: cannot create /var/tmp/myevil.txt: Permission denied
```

## Classic support

To enable *classic* snap support, enter the following to create a symbolic link between `/var/lib/snapd/snap` and `/snap`:

```
sudo ln -s /var/lib/snapd/snap /snap
```

Either log out and back in again, or restart your system, to ensure snap’s paths are updated correctly.

To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```
$ sudo snap install hello-world
hello-world 6.3 from Canonical✓ installed
$ hello-world
Hello World!
```
