(tutorials-install-the-daemon-manjaro-linux)=
# Install snap on Manjaro Linux

Snap is often installed by default on Manjaro, especially if you're using a KDE Plasma desktop. If not, or if it's been removed,  it can easily be  installed.

The easiest way to install Snap is from Manjaro's *Add/Remove Software* application (Pamac), found in the launch menu. From the application, search for `snapd`, select the result, and click *Apply*.

An optional dependency is *bash completion support*, which we recommend leaving enabled when prompted.

Alternatively, *snapd* can be installed from the command line:

```
sudo pacman -S snapd
```

Once installed, the *systemd* unit that manages the main snap communication socket needs to be enabled:

```
sudo systemctl enable --now snapd.socket
```

To enable *classic* snap support, enter the following to create a symbolic link between `/var/lib/snapd/snap` and `/snap`:

```
sudo ln -s /var/lib/snapd/snap /snap
```

Restart your system to ensure snap’s paths and AppArmor are initialised and updated correctly.

To test your system, install the [hello-world](https://snapcraft.io/hello-world) snap and make sure it runs correctly:

```
$ sudo snap install hello-world
hello-world 6.3 from Canonical✓ installed
$ hello-world
Hello World!
```

Snap is now installed and ready to go!
