(tutorials-install-the-daemon-opensuse)=
# Install snap on openSUSE

Snap can be installed from the command line on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/) and [openSUSE Leap 15.x](https://get.opensuse.org/leap/).


```{admonition} Older openSUSE releases

The snap daemon, snapd, is only built for currently supported openSUSE releases. See [Support lifetime](https://en.opensuse.org/Lifetime) for details about which releases are currently within the support timeframe.

```

## Add the repository

You need first add the *snappy* repository from the terminal. Tumbleweed users, for example, can do this with the following command:

```
sudo zypper addrepo --refresh \
  https://download.opensuse.org/repositories/system:/snappy/openSUSE_Tumbleweed \
  snappy
```

Swap out `openSUSE_Tumbleweed` for your chosen openSUSE distribution, such as `openSUSE_Leap_15.6`.

With the repository added, import its GPG key:

```
sudo zypper --gpg-auto-import-keys refresh
```

Finally, upgrade the package cache to include the new *snappy* repository:

```
sudo zypper dup --from snappy
```

## Install snapd

Snap can now be installed with the following:

```
sudo zypper install snapd
```

You then need to either reboot, logout/login or `source /etc/profile` to have /snap/bin added to PATH.

Now enable and start the *snapd* service with the following command:

```
sudo systemctl enable --now snapd
```

Run the following to enable and start the _snapd.apparmor_ service:

```
sudo systemctl enable --now snapd.apparmor
```

At this point, we recommend restarting your machine. You now have *snapd* installed and ready to go.

## Troubleshooting

If you don’t see the *snapd* update on your system, make sure the repository is refreshing correctly.

If it's not, remove and re-add the repository with the following two commands (`--refresh` is important), replacing *openSUSE_Tumbleweed* with your specific version of openSUSE:

```
sudo zypper removerepo snappy
sudo zypper addrepo --refresh \
    https://download.opensuse.org/repositories/system:/snappy/openSUSE_Tumbleweed \
    snappy
```

