(how-to-guides-work-with-snaps-apps-and-aliases)=
# Apps and aliases

When installing a snap, you're often installing an application. If an application uses a GUI, it will be integrated into your desktop environment and it can be launched just like any other GUI application. 

But applications installed from a snap can also be run from the command line, regardless of whether they're GUI-based or terminal-based.

The following sections describe how to work with such snap applications.

## Running applications

As covered in [Get started](/tutorials/get-started), a snap's installed application(s) can be found under `/snap/bin`, and subsequently, often added to _$PATH_. This makes commands directly accessible from the command line. 

If executing a command directly doesn't work, try prefixing it with the */snap/bin* path:

```
$ /snap/bin/vlc
```
Adding `/snap/bin` to your default _$PATH_ makes running snaps that don't automatically add themselves more convenient.


```{caution}
A few Linux distributions use a path of `/var/lib/snapd/snap/bin` instead of the standard `/snap/bin`. You may need to experiment and update your path accordingly.
```

## Application commands

The output of `snap info` lists the applications a snap makes available beneath the *commands:* section:

```
$ snap info vlc
name:      vlc
summary:   The ultimate media player
(...)
commands:
  - vlc
(...)
```

To avoid the potential conflict of snaps exposing applications with the same name, every snap has a namespace reserved for itself.  The namespace uses the following syntax:

- `<snap name>`
- `<snap name>.<application name>`

The first option is used automatically when the exposed application name matches the name of the  snap, such as with *vlc*. The second option is used for every other case.

<h2 id='heading--aliases'>Application aliases</h2>

The namespace syntax (see above) is effective at preventing conflicts, but it's not ideal when applications have well known names that third-party scripts depend upon. This is where *aliases* are useful.

For example, [LXD](https://canonical.com/lxd) snap exposes the application as *lxd*. However, many third-party scripts depend on this being  *lxc*. To solve this issue, the LXD snap creates an alias for *lxc*.

Aliases can be viewed with the `snap aliases` command: 

```
$ snap aliases lxd
Command  Alias  Notes
lxd.lxc  lxc    -
```
Unlike applications that use a snap's namespace, there is no guarantee that an alias is going to be unique. For this reason, aliases can be easily disabled and re-enabled with the `unalias` and `prefer` commands:

```
$ sudo snap unalias lxd
Removed:
  - lxd.lxc as lxc

$ sudo snap prefer lxd 
Added:
  - lxd.lxc as lxc
```

The *prefer* command enables all aliases for a given snap in preference to conflicting aliases from other snaps. This allows you to switch application preference between alternative options provided by other snaps.

A snap can also be installed with an additional `--unaliased` argument to prevent aliases being created automatically:

```
$ snap install lxd --unaliased
lxd 4.22 from canonical✓ installed
$ snap aliases lxd
Command  Alias  Notes
lxd.lxc  lxc    disabled
```

## Requesting aliases

As there is no guarantee that an alias is going to be unique, and potential conflicts create a minor inconvenience, a snap's *default aliases* are only enabled after a simple public review process.

The same review process also ensures that any default commands exposed by a snap are either named after the snap or, when different, reviewed to ensure the alias is relevant within the context of the application. This helps maintain a sane shared namespace for everyone.

If you want an alias enabled for your snap, please open a forum topic [in the store requests forum category](https://forum.snapcraft.io/c/store-requests) with the details.

## Manual aliases

Snap's aliasing system supports the creation of arbitrary custom aliases defined for the local system. This allows applications to be exposed under any name that is convenient locally.

For example, the following exposes a new command under `/snap/bin` to support calling the `vlc` application as `my-vlc`:

```
$ sudo snap alias vlc my-vlc
Added:
  - vlc as my-vlc

$ snap aliases vlc
Command  Alias   Notes
vlc      my-vlc  manual
```

When a manual alias is set, the original application name will continue to function.

Removing a manually created alias is also straightforward:

```
$ sudo snap unalias my-vlc    
Removed:
  - vlc as my-vlc
```

