(reference-development-environment-variables)=
# Environment variables

Environment variables are widely used across Linux to provide convenient access to system and application properties.

Both Snapcraft and snapd consume, set, and pass-through specific environment variables to support building and running snaps. 

See below for the various environment variables available to snap applications. For environment variables connected to Snapcraft, see [Parts environment variables](https://documentation.ubuntu.com/snapcraft/stable/reference/parts/parts-and-steps/).

## List environment variables

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


## Snap specific environment variables

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

### <pre>SNAP</pre>

Directory where the snap is mounted. This is where all the files in your snap are visible in the filesystem.
All of the data in the snap is read-only and cannot be changed.

Typical value: `/snap/hello-world/27`

### <pre>SNAP_USER_DATA</pre>

Directory for user data.

This directory is backed up and restored across `snap refresh` and `snap revert` operations.

Typical value: `/home/zyga/snap/hello-world/27`

The final number there is `$SNAP_REVISION`.

### <pre>SNAP_USER_COMMON</pre>

Directory for user data that is common across revisions of a snap.

Unlike `SNAP_USER_DATA`, data present in this directory is not backed up or restored across `snap refresh` and `snap revert` operations. The directory is suitable for large data that the application can access even if it was made or modified by a future version of a snap.

Typical value `/home/zyga/snap/hello-world/common`

### <pre>SNAP_DATA</pre>

Directory for system data of a snap.

This directory is owned and writable by `root` and is meant to be used by background applications (daemons, services). Unlike `SNAP_COMMON` this directory is backed up and restored across `snap refresh` and `snap revert` operations.

Typical value `/var/snap/hello-world/27`

### <pre>SNAP_COMMON</pre>

Directory for system data that is common across revisions of a snap.

This directory is owned and writable by `root` and is meant to be used by background applications (daemons, services). Unlike `SNAP_DATA` this directory **is not** backed up and restored across snap refresh and revert operations.

Typical value: `/var/snap/hello-world/common`

### <pre>SNAP_SAVE_DATA</pre>

**This variable is only exposed on {ref}`Ubuntu Core <ref-glossary_ubuntu-core>` systems.**

It points to a snap-specific location on the ubuntu-save partition where the snap is allowed to store persistent files (like certificates or configuration files) that will survive a [factory reset](https://ubuntu.com/core/docs/recovery-modes#heading--factory) of the Ubuntu Core device.

See [ubuntu-save](https://ubuntu.com/core/docs/storage-layout#heading--save) in the Ubuntu Core documentation for more details on storage layout with this specific partition.

Requires _snapd_ 2.57+.

### <pre>SNAP_INSTANCE_NAME</pre>

The name of snap instance, including instance key if one is set. 

For example snap `hello-world` with instance key `foo` has instance name equal to `hello-world_foo`.

Typical value: `hello-world`

Requires _snapd_ 2.36+

### <pre>SNAP_INSTANCE_KEY</pre>

Instance key if one was set during installation or empty. 

For example instance `hello-world_foo` has an instance key `foo`.

Typical value: none

Requires _snapd_ 2.36+

### <pre>SNAP_NAME</pre>

The name of the snap as specified in the `snapcraft.yaml` file.

Typical value: `hello-world`

### <pre>SNAP_REVISION</pre>

Revision of the snap, as allocated by the Snap Store on upload or as allocated by snapd for locally installed snaps.

The Snap Store assigns monotonic revisions to each upload of a given snap. Snapd uses Snap Store revisions if accompanying assertions are available or uses a locally generated number. Locally generated numbers are prefixed with `x` to distinguish them from Snap Store uploads.

Typical value: `27` or `x1`

### <PRE>SNAP_ARCH</PRE>

CPU architecture of the running system.

Typical value `amd64`

Other values are: `i386`, `armhf`, `arm64`.

### <pre>SNAP_UID</pre>

This variable contains the user ID (uid) of the user running this snap instance. See also SNAP_EUID.

For this variable to be exposed by a snap, the snap developer will need to include the following `assumes` value:

```yaml
assumes: [snap-uid-envvars]
```

Requires _snapd_ 2.59+.

### <pre>SNAP_EUID</pre>

This variable contains the _effective_ user ID (euid) of the user running the snap instance. See also SNAP_UID.

For this variable to be exposed by a snap, the snap developer will need to include the following `assumes` value:

```yaml
assumes: [snap-uid-envvars]
```

Requires _snapd_ 2.59+.

### <pre>SNAP_LAUNCHER_ARCH_TRIPLET</pre>

**Only available in snaps built with a [desktop extension](https://documentation.ubuntu.com/snapcraft/stable/reference/extensions).**

The host architecture triplet on which the snap is running. For `amd64` it's `x86_64-linux-gnu`. The runtime counterpart of `CRAFT_ARCH_TRIPLET_BUILD_FOR`.

### <pre>SNAP_LIBRARY_PATH</pre>

Directory with additional system libraries. This variable is used internally by snapcraft.

The value is always `/var/lib/snapd/lib/gl:` Please note the colon at the end of that value, the variable is a colon-separated list.

The referenced directory is typically empty unless Nvidia proprietary drivers are in use.

### <pre>SNAP_VERSION</pre>

The version string as specified in the `snapcraft.yaml`

Typical value `6.3`

### <pre>SNAP_REAL_HOME</pre>

The vanilla `HOME` environment variable before snapd-induced remapping, refer to [Any way to acquire the originally set `HOME` environment variable? - snapcraft - snapcraft.io](https://forum.snapcraft.io/t/any-way-to-acquire-the-originally-set-home-environment-variable/19475) for more info.

Requires _snapd_ 2.46+.

### <pre>SNAP_APP_NAME</pre>

The name of the application being run, as specified in the `snapcraft.yaml`.

Only set when running an application command.

Typical value: `cmd`

Requires _snapd_ 2.77+.

### <pre>SNAP_APP_COMMON_ID</pre>

The common identifier of the application, as specified by the `common-id` field in `snapcraft.yaml`. This is typically a reverse-DNS identifier used to associate the application with its desktop entry.

Only set when running an application that defines a `common-id`.

Typical value: `org.example.Foo`

Requires _snapd_ 2.77+.

### <pre>SNAP_APP_DESKTOP_FILE</pre>

The absolute path to the application's installed desktop file.

Only set when running an application that has an associated desktop file on disk.

Typical value: `/var/lib/snapd/desktop/applications/org.example.Foo.desktop`

Requires _snapd_ 2.77+.

### <pre>SNAP_APP_BUS_NAME</pre>

The D-Bus bus name the application is allowed to own, as specified by the `bus-name` field in `snapcraft.yaml`.

Only set when running an application that defines a `bus-name`.

Typical value: `org.example.Foo`

Requires _snapd_ 2.77+.

## Generic variables

### <pre>HOME</pre>

For non-classic snaps, this environment variable is re-written to `SNAP_USER_DATA` by snapd so that each snap appears to have a dedicated home directory that is a subdirectory of the real home directory.

For classic confinement snaps, the value remains unchanged.

Typical value: `/home/_user_name_/snap/_snap_name_/_snap_revision_` (e.g. `/home/zyga/snap/hello-world/27`)

### <pre>PATH</pre>

This environment variable is re-written by snapd so that it is consistent with the view of the filesystem presented to snap applications.

The value is always: 

* For non-classic confinement snaps:

      $SNAP/usr/sbin:$SNAP/usr/bin:$SNAP/sbin:$SNAP/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

* For classic confinement snaps:  
      `/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games`

