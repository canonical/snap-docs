(interfaces-nfs-mount)=
#  nfs-mount interface

The `nfs-mount` interface allows the mounting and unmounting of Network File System mount points within a snap's writable areas.

**Note:** This interface only supports NFSv4. This should not cause problems as earlier versions are now considerably old and are unlikely to be being used.


## Developer details

**[Auto-connect](/t/6154#heading--auto-connections)** : no</br>
**[Super-privileged](/)** : no

Requires snapd version _2.62+_.

This interface requires only the addition of `nfs-mount` to a snap's list of `plugs` , unlike other mounting interfaces which require additional rules.

Additionally, the userspace binaries required to mount shares are not included in base snaps. They will need to be installed manually from the `nfs-common` package.

<h3 id='heading-code'>Code examples</h3>

The following is a simple example `snapcraft.yaml` with accompanying _mount_ and _unmount_ scripts for a snap that will mount and unmount an NFS share within `$SNAP_COMMON`:

```yaml
name: nfs4-example
base: core22
version: '0.1'
summary: Example Snap showing off the new nfs-mount interface.
description: |
  This snap provides two commands: nfs-mount and nfs-unmount.
  Mount takes a single argument in the form of <hostname>:<nfs-share-name>.

grade: stable
confinement: strict

apps:
  nfs-mount:
    command: bin/nfs-mount.sh
    plugs: [nfs-mount]
  nfs-unmount:
    command: bin/nfs-unmount.sh
    plugs: [nfs-mount]

parts:
  scripts:
    plugin: dump
    source: ./src
    organize:
      '*': bin/
  packages:
    plugin: nil
    stage-packages: [nfs-common]
```

The mount script `nfs-mount.sh`:
```sh
#!/bin/sh -eux

# If not argument is provided, print help and exit
[ -n "$1" ] || {
  printf '%s <hostname>:<nfs-share-path>\n' "$0"
  exit 1
}

# Ensure that the mount point has been created
[ -d "${SNAP_COMMON}/mnt" ] \
  || mkdir -p "${SNAP_COMMON}/mnt"

# Attempt to mount the share
mount.nfs4 "$1" "${SNAP_COMMON}/mnt"
```

And the unmount script, `nfs-unmount.sh`:

```sh
#!/bin/sh -eux

umount "${SNAP_COMMON}/mnt"
```

The test code for this interface can be found in the snapd repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/nfs_mount_test.go>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/nfs_mount.go>

