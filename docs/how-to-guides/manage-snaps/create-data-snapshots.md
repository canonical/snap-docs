(how-to-guides-manage-snaps-create-data-snapshots)=
# Create data snapshots

A *snapshot* is a copy of the user, system and configuration data stored by *snapd* for one or more snaps on your system. This data can be found in `$HOME/snap/<snap-name>` and `/var/snap/<snap-name>`.

Snapshots are generated **manually** with the `snap save` command and **automatically when a snap is removed** (unless `--purge` is used with remove, in which case no snapshot is created). A snapshot can be used to backup the state of your snaps, revert snaps to a previous state and to restore a fresh snapd installation to a previously saved state.

## Generating a snapshot

The `snap save` command creates a snapshot for all installed snaps, or if declared individually, specific snaps:

```
$ sudo snap save
Set  Snap         Age    Version               Rev   Size   Notes
30   core         1.00s  16-2.37~pre1          6229   250B  -
30   core18       886ms  18                    543    123B  -
30   go           483ms  1.10.7                3092   387B  -
30   vlc          529ms  3.0.6                 770   882kB  -
```

Each snapshot has a unique ID, or revision, shown in the *Set* column above. This value is unique to each *save* operation, regardless of the number of snaps it includes. *Age* is the period of time since the snapshot was created, while *Version* and *Rev* refer to the specific snap at the time of the snapshot. *Size* is the amount of storage used by a snapshot. 

If you'd rather not wait for the *save* operation to complete before regaining access to your terminal, add the `--no-wait` argument.

You can see the state of your system's snapshots with the `snap saved` command. Adding `--id=<set/unique ID>` allows you to query a specific snapshot:

```
$ snap saved --id=29
Set  Snap             Age    Version               Rev   Size   Notes
29   vlc              2h41m  3.0.6                 770   882kB  -
```

Both the _saved_ and _check-snapshot_ commands accept a `–users=` option with a comma-separated list of users to filter on.

## What a snapshot stores

A snapshot is a copy of the user, system and configuration data stored by *snapd* for one or more snaps on your system. For each snap, this data can be found in `$HOME/snap/<snap-name>` and `/var/snap/<snap-name>`.

More specifically, these are locations that snapped application access through the following environment variables from within the snap:

System-wide locations:
- **SNAP_COMMON** ( `/var/snap/<snap-name>/common `)
- **SNAP_DATA** (`/var/snap/<snap-name>/<revision>`)

User-specific locations:
- **SNAP_USER_COMMON** (`/home/<username>/snap/<snap-name>/common`)
- **SNAP_USER_DATA** (`/home/<username>/snap/<snap-name>/<revision>`)

It's important to note that **SNAP_DATA** and **SNAP_USER_DATA** place their data within a directory specific to each snap [revision](/explanation/how-snaps-work/revisions), whereas  **SNAP_COMMON** and  **SNAP_USER_COMMON** do not.

You need to be aware of what data is copied forward when you move from one revision to the next and which data will be restored if you switch to a previous snapshot.

When you move from one revision to the next, the revision-specific contents of  **SNAP_DATA** and  **SNAP_USER_DATA** are copied into new directories for the new revision. The contents of  **SNAP_COMMON** and  **SNAP_USER_COMMON** remain the same. A snapshot **only** includes the data for the installed revision, plus the contents of the two **COMMON** directories.

When a snapshot is restored:
1. The contents of   **SNAP_COMMON** and  **SNAP_USER_COMMON** will be _overwritten_ and restored to their state when the restored snapshot was created.

1. The revision-specific contents of **SNAP_DATA** and  **SNAP_USER_DATA** will be copied into and _overwrite_ the contents of the revision-specific directory of the currently installed revision.

See [Data locations](/reference/operations/data-locations) for more details on how these locations are intended to be used by a snap, and see [Inside a snapshot](#inside-a-snapshot) to see how they're stored within a snapshot.

## Verifying a snapshot

To verify the integrity of a snapshot, use the `check-snapshot` command:

```
$ sudo snap check-snapshot 30
Snapshot #30 verified successfully.
```

## Exporting and importing a snapshot

By default, snapshots are maintained and stored on the system that created them. However, to help with backup and recovery, individual snapshots can also be exported and restored.

To export a snapshot, use the `snap export-snapshot <set-id> <new-filename>` command:

```
$ sudo snap export-snapshot 30 my-snapshot.zip
Exported snapshot #30 into "my-snapshot.zip"
```

The resultant snapshot file is a _zip_ archive that contains two _json_ files to validate the snapshot and a _zip_ archive containing the user, system and configuration data for the specific revision of the snap installed when the snapshot was created.

To import a previously exported snap shot, use the `snap import-snapshot` command:

```
$ sudo snap import-snapshot mysnapshot
Imported snapshot as #30
Set  Snap  Age    Version  Rev   Size    Notes
30   vlc   3d02h  1.11.13  4286  255B  -
```

If the snapshot with the same snapshot identifier exists, the import will overwrite it. If the snapshot doesn't exist, it will be imported and assigned a new snapshot identifier.

## Restoring a snapshot

The `restore` command replaces the current user, system and configuration data with the corresponding data from the specified snapshot:

```
$ sudo snap restore 30
Restored snapshot #30.
```

Before using this command, make sure you have the snap application installed, and that its services, if any, are stopped (`snap stop <snap-name>`). 
Start them again once the snapshot has been successfully restored.

By default, this command restores all the data for all the snaps in a snapshot. You can restore data for specific snaps by simply listing them after the command and for specific users with the `--users=<usernames>` argument.

Excluding a snap's system and configuration data from *snap restore* is not currently possible. 

## Deleting a snapshot

The `forget` command deletes a snapshot. This operation removes a snapshot from local storage and can not be undone:

```
$ sudo snap forget 30
Snapshot #30 forgotten.
$ snap saved --id=30
No snapshots found.
```

By default, this command deletes all the data for all the snaps in a snapshot. You can delete the data for specific snaps by listing them after the command.

## Automatic snapshots

Apart from on [Ubuntu Core](https://www.ubuntu.com/core) devices, where the feature is disabled by default, a snapshot is generated automatically when a snap is removed. These snapshots are retained for 31 days before being deleted automatically.

To see which snapshots are generated automatically,  look for `auto` in the *Notes* column output from *snap saved*:

```
$ snap saved
Set  Snap              Age    Version               Rev   Size   Notes
30   go                25d5h  1.10.7                3092   387B  -
30   vlc               25d0h  3.0.6                 770   882kB  -
31   vlc               529ms  3.0.6                 770   882kB  auto
```

As with manual snapshots, automatically generated snapshots can be manually deleted with `snap forget <set-id>`.

Automatic snapshot retention time is configured with the `snapshots.automatic.retention` [system option](/how-to-guides/manage-snaps/set-system-options). The value needs to be greater than 24 hours:

```
snap set system snapshots.automatic.retention=30h
```

To disable automatic snapshots, set the retention time to `no`:

```
snap set system snapshots.automatic.retention=no
```

> Disabling automatic snapshots will *not* affect pre-existing automatically generated snapshots, only those generated by the removal of subsequent snaps.

Automatic snapshots require snap version _2.39+_. 

## Inside a snapshot

On Ubuntu-based systems, snapshots are stored in the `/var/lib/snapd/snapshots` directory and are both stored and exported as a *zip* file. This zip file contains the following:

```yaml
<snap-snapshot-zip>
├── <snapshot-number>_<snap-name>_<revision>.zip
└────── archive.tgz
    │   ├── <revision-number>
    │   └── $SNAP_DATA (/var/snap/<snap-name>-<revision>)
    │   └── common
    │       └── $SNAP_COMMON (/var/snap/<snap-name>/common)
    ├── meta.json
    ├── meta.sha3_384
    └── user
        └── <username>.tgz
            ├── <revision-number>
            │   └── $SNAP_USER_DATA (/home/<username>/snap/<snap-name>/<revision>)
            └── common
                └── $SNAP_USER_COMMON(/home/<username>/<snap-name>)

```

- **meta.json**: describes the contents of the snapshot, alongside its configuration and checksums for the archives.
