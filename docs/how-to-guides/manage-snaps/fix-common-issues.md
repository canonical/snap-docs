(how-to-guides-fix-common-issues-index)=
# Fix common issues

Snaps run on, and are built for, a diverse and constantly evolving set of [operating systems](/tutorials/install-the-daemon/index) and [embedded devices](https://ubuntu.com/core/docs/supported-platforms#heading--supported).

The vast majority of our users and developers experience very few issues, but any technology this complex and diverse will likely encounter some issues and incompatibilities.

This page attempts to guide users to either an appropriate solution to their issues, or the correct forum/thread where they can get help.

## Network access

The snap daemon (snapd) requires network access to install, update, build and publish snaps. Local network and port configurations can affect their access.

See [Network requirements](/reference/administration/network-requirements) for which hosts and ports are required to ensure consistent communication.

## Cannot communicate with the server / connection refused

To perform most actions, the snap client needs to communicate with the snap daemon. If this isn't possible, the snap command fails and outputs a connection refused error.

There are various causes for this error.  Try the following steps, and if the problem persists, see the next section on generating and sharing debugging details.

1. Restart snapd:

   ```bash
   sudo systemctl restart snapd snapd.socket
   ```

1. Reload systemd's daemon state:

    ```bash
   sudo systemctl daemon-reload
    ```

1. Reboot the machine:
    
    ```bash
    sudo reboot
    ```

See [cannot communicate with server connection refused ](https://forum.snapcraft.io/t/snap-d-error-cannot-communicate-with-server-connection-refused/6093) for discussions on this issue.

## Slow snap downloads

When a snap is installed, it's downloaded and authenticated against one or more servers attached to the [Snap Store](https://snapcraft.io/store) (or a local proxy). If a server is unavailable, or suffering bandwidth issues, installation progress will be slow.

You can check on the operational status of the servers attached to the Snap Store from the Snap Store status page: [https://status.snapcraft.io/](https://status.snapcraft.io/). 

![Snap Store status](https://assets.ubuntu.com/v1/dd75734c-image+%282%29.png) 

The Snap Store Status page also includes a status history for the servers over the last week and an incident history.

![iSnap Store incident report](https://assets.ubuntu.com/v1/5af8a398-image.png) 

See [Extremely slow snap downoads](https://forum.snapcraft.io/t/extremely-slow-snap-downloads/4668/38) for further discussions on snap download speeds.

## Missing binaries / command not found

When the snap daemon is installed, its executable components are added to the system path ($PATH). If this doesn't happen correctly, a warning is issued stating that snapd cannot be found.

The first thing to do is check installation instructions for the specific operating system. See [Installing snapd](/tutorials/install-the-daemon/index) for further details.

Linux distributions differ, but most will need a restart after snapd has been installed to refresh paths and system security profiles. 

Executables from installed snaps can usually be found in `/snap/bin/`, and this should also be in your path. You can check this by typing `echo $PATH | grep "snap/bin"` on the command line, or by using the _which_ command to see where the executable binary:

```bash
$ which spotify
/snap/bin/spotify
```

If an executable isn't in your path, try using the `snap run` command, such as `snap run spotify`.

You can also manually add `/snap/bin` to your system $PATH. This is typically accomplished by adding a line similar to the following in your shell environment's configuration file (such as `~/.bashrc` or `~/.zshrc`):

```bash
export PATH="/snap/bin:$PATH"
```

You will need to restart your shell for the changes to take effect.

## Home directories outside of /home

The snap daemon (snapd) requires a user’s home directory ($HOME) to be located under  `/home`  on the local filesystem. This requirement cannot currently be changed. However, it is possible to  *bind mount*  an alternative $HOME location to  `/home`  to allow other locations to be found by snapd. This process is outlined below.

See [Home directories outside of ‘/home’](https://forum.snapcraft.io/t/home-directories-outside-of-home/19224) for further details.

## Domain served /home directories

Domain-mounted home directories beneath `/home/<DOMAIN-NAME>` may require extra AppArmor permissions.

These can be granted by running `sudo dpkg-reconfigure apparmor` and entering `/home/<DOMAIN-NAME>/`, replacing <DOMAIN-NAME> with your domain, as an additional home directory location at the prompt.

## chmod errors

There is a known [issue](https://bugs.launchpad.net/snapd/+bug/1914786) affecting some Debian 10 users, alongside some other Linux distributions users.

Snaps that depend on a _browser-sandbox_, such as Teams and Chromium, may inadvertently exit without an error, although logs should reveal an _incorrect chmod (4755)_ error caused by the following system call:

`clone(child_stack=0x7ffc0ea30060, flags=CLONE_NEWUSER|SIGCHLD) = -1 EPERM (Operation not permitted)`

As a temporary solution, the issues can be bypassed with the following command:

```bash
sudo sysctl kernel.unprivileged_userns_clone=1
```
## Too early for operation errors

After installing the snap daemon, _snapd_, it can take a short amount of time to initialise its environment.

During this initialisation period, if certain instructions are attempted either from the `snap` command or the [REST API](reference/api/redoc-static), the following error may be generated:

`error: too early for operation, device not yet seeded or device model not acknowledged`

The solution to errors like these is simply to wait a short while before attempting the same instruction again.

## Generate debug info

One of the best ways to solve an issue is to understand when and where the error is encountered, and there are several levels of output that can be generated.

The `snap changes` and `snap tasks <change-id>` commands, for example, output details about what changed during the last refresh:

```bash
$ snap changes
ID    Status  Spawn                   Ready                   Summary
2052  Done    today at 09:34 BST      today at 09:35 BST      Auto-refresh 7 snaps
2053  Done    today at 15:16 BST      today at 15:17 BST      Refresh snaps "gnome-calculator", "flock-chat", "gnome-characters", "gnome-system-monitor"
```

The snap daemon documents its operations to the system log. This can be retrieved and viewed with the following command: 

```bash
sudo journalctl --no-pager -u snapd
```

The `snap debug` command can be used to probe the state of the daemon:

```bash
$ sudo snap debug state /var/lib/snapd/state.json
ID    Status  Spawn                   Ready                   Label                         Summary
2955  Done    yesterday at 13:53 BST  yesterday at 13:53 BST  hotplug-remove-serial-port    Remove hotplug connections and slots of device /dev/ttyACM0 (Keyboardio Model…; serial: Ckbio01E) with interface "serial-port"
```

Don't forget to include the output from `sudo snap version` if you wish to share your output to get further help on the forum.

