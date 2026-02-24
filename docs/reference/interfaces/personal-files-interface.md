(interfaces-personal-files-interface)=
#  personal-files interface

The `personal-files` interface provides access to specified files in the user's home directory, and consequently, gives privileged access to the user's data.

This interface is typically used to provide read-only access to top-level hidden data directories (directories starting with a dot) within a user's real home directory in order to support importing data from existing applications where the snap is the clear owner of the target directory. 

By default, snaps have access to everything under `~/snap/<snap name>/<revision>` and it's this path stored in the `$SNAP_USER_DATA` [environment variable](/). For non-daemon commands within the snap, this location is also where the `$HOME` environment variable points to, and where they can read and write to hidden files freely.

Requires snapd version _2.37+_.


## Developer details

**[Auto-connect](/explanation/interfaces/interface-auto-connection)**: no</br>
**[Super-privileged](/)**: yes</br>
**Transitional**: no</br>
**Attributes**:</br>
  * `read` (plug): list of files and/or directories for read-only access (eg, '`read: [ $HOME/.file-read, $HOME/.dir-read ]`'
  * `write` (plug): list of files and/or directories for read/write access (eg, '`write: [ $HOME/.file-write, $HOME/.dir-write ]`'

Specifying a directory in `read` and `write` allows access to the directory and all files under it. If there are missing directories between `$HOME` and the target file or directory, these are created automatically when the associated application is first run by a non-root user. 

## Approval process

For distribution via the [Snap store](https://snapcraft.io/store), snaps that use the personal-files interface need an approved [snap declaration](/t/process-for-aliases-auto-connections-and-tracks/455/). For acceptance, the publisher needs to make a descriptive interface reference, as used by `snap connections|interfaces|connect|disconnect` commands.

## Code examples

If a *foo* application is being packaged as a snap and its publisher wants the snap to:
1. Import an existing configuration from `~/.config/foo` into `$SNAP_USER_DATA/.config/foo` (ie, `$HOME/.config/foo` within the snap's runtime environment or `~/snap/foo/<revision>/.config/foo`) on the host)
1. Save user-specific data in `$HOME/.local/share/foo`, where `$HOME/.local` and `$HOME/.local/share/` will be automatically created for the calling user if it does not exist

The *snapcraft.yaml* could include the following:

```yaml
name: foo
...
plugs:
  dot-config-foo:
    interface: personal-files
    read:
    - $HOME/.config/foo
  dot-local-share-foo:
    write:
    - $HOME/.local/share/foo

apps:
  foo:
    plugs:
    - dot-config-foo
    slots:
    - dot-local-share-foo
    ...
```

When declaring an instance of the `personal-files` plug or slot, it should be named with a descriptive name that indicates to a user what access it grants. In the above example, `dot-config-foo` is used to reflect the access to `~/.config/foo`, and `dot-local-share-foo` is used to reflect the access to `~/.local/share/foo`.

You would then be able to use the following to enable access to personal files:

```
snap connect foo:dot-config-foo
```

