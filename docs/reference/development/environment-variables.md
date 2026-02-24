(reference-development-environment-variables)=
# Environment variables

Environment variables are widely used across Linux to provide convenient access to system and application properties.

Both [Snapcraft](/) and snapd consume, set, and pass-through specific environment variables to support building and running snaps. 

See below for the various environment variables available to snap applications. For environment variables connected to Snapcraft, see [Parts environment variables](/).

## Snap specific environment variables

### List environment variables

Each snap runs in a custom environment specifically made for it. To get an overview of the variables in it, you can open a shell as the snap and run the `env` command.

```
$ snap run --shell <snap>.<command>
$ env
XDG_VTNR=1
SSH_AGENT_PID=5543
XDG_SESSION_ID=2
SNAP_USER_COMMON=/home/<user>/snap/<snap>/common
SNAP_LIBRARY_PATH=/var/lib/snapd/lib/gl:
SNAP_COMMON=/var/snap/<snap>/common
[...]
```

Alongside the many system-specific variables, this environment will include the following: 

| | |
|--|--|
| [SNAP](#heading--snap) | [SNAP_ARCH](#heading--snap-arch) |
| [SNAP_USER_DATA](#heading--snap-user-data) | [SNAP_UID](#heading--snap-uid) |
| [SNAP_USER_COMMON](#heading--snap-user-common) | [SNAP_EUID](#heading--snap-euid) |
| [SNAP_DATA](#heading--snap-data) | [SNAP_LAUNCHER_ARCH_TRIPLET](#heading--snap-laucnher-arch-triplet) |
| [SNAP_COMMON](#heading--snap-common) | [SNAP_LIBRARY_PATH](#heading--snap-library-path) |
| [SNAP_SAVE_DATA](#heading--snap-save-data) | [SNAP_VERSION](#heading--snap-version) |
| [SNAP_INSTANCE_NAME](#heading--snap-instance-name) | [SNAP_REAL_HOME](#heading--snap-real-home) |
| [SNAP_INSTANCE_KEY](#heading--snap-instance-key) | [HOME](#heading--home) |
| [SNAP_NAME](#heading--snap-name) | [PATH](#heading--path) |
| [SNAP_REVISION](#heading--snap-revision) |

<h3 id='heading--snap'><pre>SNAP</pre></h3>

Directory where the snap is mounted. This is where all the files in your snap are visible in the filesystem.
All of the data in the snap is read-only and cannot be changed.

Typical value: `/snap/hello-world/27`

<h3 id='heading--snap-user-data'><pre>SNAP_USER_DATA</pre></h3>

Directory for user data.

This directory is backed up and restored across `snap refresh` and `snap revert` operations.

Typical value: `/home/zyga/snap/hello-world/27`

The final number there is `$SNAP_REVISION`.

<h3 id='heading--snap-user-common'><pre>SNAP_USER_COMMON</pre></h3>

Directory for user data that is common across revisions of a snap.

Unlike `SNAP_USER_DATA`, data present in this directory is not backed up or restored across `snap refresh` and `snap revert` operations. The directory is suitable for large data that the application can access even if it was made or modified by a future version of a snap.

Typical value `/home/zyga/snap/hello-world/common`

<h3 id='heading--snap-data'><pre>SNAP_DATA</pre></h3>

Directory for system data of a snap.

This directory is owned and writable by `root` and is meant to be used by background applications (daemons, services). Unlike `SNAP_COMMON` this directory is backed up and restored across `snap refresh` and `snap revert` operations.

Typical value `/var/snap/hello-world/27`

<h3 id='heading--snap-common'><pre>SNAP_COMMON</pre></h3>

Directory for system data that is common across revisions of a snap.

This directory is owned and writable by `root` and is meant to be used by background applications (daemons, services). Unlike `SNAP_DATA` this directory **is not** backed up and restored across snap refresh and revert operations.

Typical value: `/var/snap/hello-world/common`

<h3 id='heading--snap-save-data'><pre>SNAP_SAVE_DATA</pre></h3>

**This variable is only exposed on [Ubuntu Core](/t/glossary/14612#heading--ubuntu-core) systems.**

It points to a snap-specific location on the ubuntu-save partition where the snap is allowed to store persistent files (like certificates or configuration files) that will survive a [factory reset](https://ubuntu.com/core/docs/recovery-modes#heading--factory) of the Ubuntu Core device.

See [ubuntu-save](https://ubuntu.com/core/docs/storage-layout#heading--save) in the Ubuntu Core documentation for more details on storage layout with this specific partition.

Requires _snapd_ 2.57+.

<h3 id='heading--snap-instance-name'><pre>SNAP_INSTANCE_NAME</pre></h3>

The name of snap instance, including instance key if one is set. 

For example snap `hello-world` with instance key `foo` has instance name equal to `hello-world_foo`.

Typical value: `hello-world`

Requires _snapd_ 2.36+

<h3 id='heading--snap-instance-key'><pre>SNAP_INSTANCE_KEY</pre></h3>

Instance key if one was set during installation or empty. 

For example instance `hello-world_foo` has an instance key `foo`.

Typical value: none

Requires _snapd_ 2.36+

<h3 id='heading--snap-name'><pre>SNAP_NAME</pre></h3>

The name of the snap as specified in the `snapcraft.yaml` file.

Typical value: `hello-world`

<h3 id='heading--snap-revision'><pre>SNAP_REVISION</pre></h3>

Revision of the snap, as allocated by the Snap Store on upload or as allocated by snapd for locally installed snaps.

The Snap Store assigns monotonic revisions to each upload of a given snap. Snapd uses Snap Store revisions if accompanying assertions are available or uses a locally generated number. Locally generated numbers are prefixed with `x` to distinguish them from Snap Store uploads.

Typical value: `27` or `x1`

<h3 id='heading--snap-arch'><PRE>SNAP_ARCH</PRE></h3>

CPU architecture of the running system.

Typical value `amd64`

Other values are: `i386`, `armhf`, `arm64`.

<h3 id='heading--snap-uid'><pre>SNAP_UID</pre></h3>

This variable contains the user ID (uid) of the user running this snap instance. See also [SNAP_EUID](#heading--snap-euid).

For this variable to be exposed by a snap, the snap developer will need to include the following [`assumes`](/t/snapcraft-top-level-metadata/8334#heading--assumes) value:

```yaml
assumes: [snap-uid-envvars]
```

Requires _snapd_ 2.59+.

<h3 id='heading--snap-euid'><pre>SNAP_EUID</pre></h3>

This variable contains the _effective_ user ID (euid) of the user running the snap instance. See also [SNAP_UID](#heading--snap-uid).

For this variable to be exposed by a snap, the snap developer will need to include the following [`assumes`](/t/snapcraft-top-level-metadata/8334#heading--assumes) value:

```yaml
assumes: [snap-uid-envvars]
```

Requires _snapd_ 2.59+.

<h3 id='heading--snap-laucnher-arch-triplet'><pre>SNAP_LAUNCHER_ARCH_TRIPLET</pre></h3>

**Only available in snaps built with a [desktop extension](/).**

The host architecture triplet on which the snap is running. For `amd64` it's `x86_64-linux-gnu`. The runtime counterpart of [`CRAFT_ARCH_TRIPLET_BUILD_FOR`](/).

<h3 id='heading--snap-library-path'><pre>SNAP_LIBRARY_PATH</pre></h3>

Directory with additional system libraries. This variable is used internally by snapcraft.

The value is always `/var/lib/snapd/lib/gl:` Please note the colon at the end of that value, the variable is a colon-separated list.

The referenced directory is typically empty unless Nvidia proprietary drivers are in use.

<h3 id='heading--snap-version'><pre>SNAP_VERSION</pre></h3>

The version string as specified in the `snapcraft.yaml`

Typical value `6.3`

<h3 id='heading--snap-real-home'><pre>SNAP_REAL_HOME</pre></h3>

The vanilla `HOME` environment variable before snapd-induced remapping, refer to [Any way to acquire the originally set `HOME` environment variable? - snapcraft - snapcraft.io](https://forum.snapcraft.io/t/any-way-to-acquire-the-originally-set-home-environment-variable/19475) for more info.

Requires _snapd_ 2.46+.

## Generic variables

<h3 id='heading--home'><pre>HOME</pre></h3>

For non-classic snaps, this environment variable is re-written to `SNAP_USER_DATA` by snapd so that each snap appears to have a dedicated home directory that is a subdirectory of the real home directory.

For classic confinement snaps, the value remains unchanged.

Typical value: `/home/_user_name_/snap/_snap_name_/_snap_revision_` (e.g. `/home/zyga/snap/hello-world/27`)

<h3 id='heading--path'><pre>PATH</pre></h3>

This environment variable is re-written by snapd so that it is consistent with the view of the filesystem presented to snap applications.

The value is always: 

* For non-classic confinement snaps:

      $SNAP/usr/sbin:$SNAP/usr/bin:$SNAP/sbin:$SNAP/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

* For classic confinement snaps:  
      `/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games`

