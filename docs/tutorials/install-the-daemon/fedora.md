(tutorials-install-the-daemon-fedora)=
# Install snap on Fedora

Snap can be installed on Fedora from the command line:

```
sudo dnf install snapd
```
Either log out and back in again, or restart your system, to ensure snap's paths are updated correctly.

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
Snap is now installed and ready to go.

## Troubleshooting

### system does not fully support snapd: cannot mount squashfs image using "squashfs"

Installing your first snap on a cloud image of Fedora may produce an error similar to the following:

```
error: system does not fully support snapd: cannot mount squashfs image using "squashfs": mount:
       /tmp/sanity-mountpoint-156693269: unknown filesystem type 'squashfs'.
```

If using a container, install the _fuse_ and _squashfuse_ packages (`sudo dnf install fuse squashfuse`).

Otherwise install _kernel-modules_ package (`sudo dnf install kernel-modules`).

### Fedora Silverblue prevents symbolic links

[Fedora Silverblue](https://silverblue.fedoraproject.org/) implements a read-only root filesystem and, consequently, cannot allow symbolic links to be created. See the following associated GitHub issue for further details: [Make it easier to link in or bind folders to the root directory?](https://github.com/projectatomic/rpm-ostree/issues/1711)

