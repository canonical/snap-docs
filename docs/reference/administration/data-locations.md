(interfaces-data-locations)=
# Data locations

A vast majority of snaps use strict confinement to isolate both their execution environments and their data from your system (see [Snap Confinement](/) for further details).

This confinement is an important security feature, but it can affect how and where you access a snap's files, including:

- configuration files
- user documents
- internal databases

Access to files like these is fundamental to the operation of most applications and snap confinement has been designed to always permit access to snap-specific locations for these files when required. These locations are described below.

## System data

Within the snap environment, [environment variables](/) are used to reference different accessible locations.  The following variables and default referenced locations are used to store system data:

* **SNAP_COMMON**: `/var/snap/<snap name>/common`</br>
This directory is owned and writable by root and is used to store data that is common across multiple [revisions](/t/glossary/14612#heading--revision) of the snap (e.g.: revision 6, revision 7, etc.).

* **SNAP_ DATA**: `/var/snap/<snap name>/<revision number>`</br>
This location it is also used to store data, mostly information utilised by background application and services, for logging, and other tasks that require persistence between snap launches.

A [snapshot](/) of `SNAP_DATA` and `SNAP_COMMON` is created and restored when performing a snap update (refresh) or revert operation. The contents of `SNAP_DATA` is specific to the snap revision, while the contents of `SNAP_COMMON` is applicable to all revisions and will overwrite the contents of `SNAP_COMMON` when restored. See [What a snapshot stores](/t/snapshots/9468#heading--what-is-stored) for more details.

## User data

Snaps can also contain user data. As with the system data environment variables, `SNAP_COMMON` and `SNAP_DATA`,  the following user-specific environment variables point to directories for user data:

- **SNAP_USER_COMMON**: `/home/<username>/snap/<snap name>/common`</br>
  This location maps user data across each revision of a snap. This data is only copied or backed-up through [Snapshots](/).

- **SNAP_USER_DATA**: `/home/<username>/snap/<snap name>/<revision>`</br>
  This contains any user data that the snap writes to its own home. This is *in contrast* to what the Linux user would consider *their* home. It is important to note this distinction, because it can be useful, and even important when users decide to perform maintenance operations with their snaps (like removal). By default, every snap will use a symlink *current*, pointing to the latest available revision.

Both `SNAP_USER_COMMON` and `SNAP_USER_DATA` only become available after a snap has been run once.

### Ubuntu Core

On Ubuntu Core, the **`SNAP_SAVE_DATA`** environment variable within a snap's environment points to a snap-specific location on the [ubuntu-save](https://ubuntu.com/core/docs/uc20/inside#heading--layouts) volume. This is used to store data that can be accessed during recovery or after re-installation of Ubuntu Core.

For example, in the reference Ubuntu Core 22 image, from within the _hello-world_ snap, `SNAP_SAVE_DATA` has the following value:

```
SNAP_SAVE_DATA=/var/lib/snapd/save/snap/hello-world
```

The above environment variable references a mount point at the following location:

```
$ mount | grep "snapd/save"
/dev/mapper/ubuntu-save on /var/lib/snapd/save type ext4 (rw,relatime)
```

## Other locations

There are several other directories you should be aware of:

* **`/var/lib/snapd/cache`**
 This is the working cache and is used to minimise download size and speed-up refreshes.
* **`/var/lib/snapd/snaps`**
 Contains all the versions of snaps installed on your system.
* **`/var/lib/snapd/snapshots/`**
  Contains both the manually generated and automatically generated [snapshots](/).


## Snap installation locations

When a user [installs a snap](/t/getting-started/3876#heading--install-snap) from the [Snap Store](https://snapcraft.io/store), the following happens:

1. The [snapd services](/t/glossary/14612#heading--snapd) downloads the snap as a single file – a SquashFS archive with a _.snap_ suffix.
1. The snap file is stored in `/var/lib/snaps/snaps`. It is then *loop mounted* to `/snap` from where its contents become readable by the system. See [The snap format](/) for further details on what is included in a snap.

By design, the read-only filesystem cannot provide a persistent experience between application launches, which is why snaps also have writable parts for system data and for user data.

## Snap deletion data remnants

When deleting and removing a snap from a system, the following will happen:

* The snap will be unmounted and no longer shown under `/snap`.
* The data under `/var/snap/<snap name>/` and `/home/<username>/snap/` will be deleted. However, a copy is be retained as a [snapshot](/) for 30-days (except on Ubuntu Core systems), allowing data to be restored or manually retrieved.

[Snapshot management](/) can be used to restore data, or unzip the archives, and only copy the data you consider necessary. With the right permissions, you can also create your own backup routine, which copies the important data like application databases, configurations or similar content to a backup path.

To remove a snap without generating a snapshot, use the additional ‘–purge’ argument:

```
$ sudo snap remove vlc --purge
vlc removed
```

