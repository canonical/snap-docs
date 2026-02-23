(tutorials-get-started)=
# Get started

A snap is a bundle of one or more applications that works without dependencies or modification across many different Linux distributions. Snaps are discoverable and installable from the [Snap Store](https://snapcraft.io/store), a public app store with an audience of millions.

This tour introduces all of snap's main features. We suggest going through the first few steps and then playing with what you've learnt. Come back when you feel comfortable and wish to further your knowledge.

By the end of the tour, you'll have a good understanding of how to use snaps, from how they're installed and updated, to how they're backed-up and removed.

## Requirements

Snaps can be installed and removed with a graphical package manager, such as Ubuntu Software Centre, but most advanced functionality is only available from the Linux command shell.

The command shell is accessible from [Terminal](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) and many similar applications. It helps if you have some familiarity with this, but if you don't, this tour is itself an ideal introduction to get you started.

Many Linux distributions, including Ubuntu, support _snap_ by default. You can check by running the `snap` command. If the snap command is not found, take a look at our [Installation guides](install-the-daemon/index) for further help.

## List installed snaps

Snap is installed with a few other snaps, and a good place to start is to display these with the `snap list` command:

```console
$ snap list
Name             Version        Rev    Tracking         Publisher   Notes
core22           20231123       1033   latest/stable    canonical✓  base
firefox          120.0.1-1      3504   latest/stable    mozilla✓    -
snapd            2.60.4         20290  latest/stable    canonical✓  snapd
```

Versions and revisions, under the _Version_ and _Rev_ columns respectively, convey different details about one specific release of a snap:

- _Version_ : the version of the software being packaged, as assigned by the developers
- _Revision_: the sequence number assigned by the store when the snap file was uploaded

The *version* is a name or number that was arbitrarily assigned to a release by its developers, according to their development practices. It tells the user what content to expect from a snap. The *revision* is an automatic number assigned by the store to give every snap release a unique identity within the channel across every architecture supported by the snap.

## Finding snaps

There are snaps for many popular applications, including [Spotify](https://snapcraft.io/spotify), [Slack](https://snapcraft.io/slack) and the [Chromium web browser](https://snapcraft.io/chromium).

The best way to find new snaps is to use the online [Snap Store](https://snapcraft.io/store), either by searching for apps and words you’re interested in, such as "Spotify", “music” or “maths”, or by browsing through categories.

To search for snaps with ‘media player’ in either their names or descriptions, type `snap find "media player"` into your terminal:

```console
$ snap find "media player"
Name  Version  Developer    Notes  Summary
vlc   3.0.4     videolan✓   -      The ultimate media player.
```

The `✓` alongside *videolan* in the above output indicates that the snap publisher has been _verified_. Verified publishers are trusted to produce and maintain high-quality packages and include institutions, foundations, and companies.

### Section categories

Typing `snap find` without any arguments will return a list of suggested snaps and those suggestions can also be limited to a category with an additional `--section=` argument. The following section names are valid:

| | | | |
|-|-|-|-|
| art-and-design |  books-and-reference | development | devices-and-iot |
| education| entertainment| featured| finance|
| games | health-and-fitness| music-and-audio| news-and-weather|
| personalisation | photo-and-video| productivity| science|
| security | server-and-cloud|  social| utilities||

### Learn about a snap

The `snap info` command makes it easy to find more details about a specific snap. These details include what a snap does, who publishes it, which commands it provides.

The final part of the output lists the _channels_ for the snap:

``` yaml
channels:
  latest/stable:    3.0.19                      2023-10-13 (3721) 336MB -
  latest/candidate: 3.0.19                      2023-10-02 (3721) 336MB -
  latest/beta:      3.0.20-27-g795b1bc62b       2023-12-13 (3862) 336MB -
  latest/edge:      4.0.0-dev-26928-g9bc7ded0f0 2023-12-13 (3863) 692MB -
installed:          3.0.19                                 (3721) 336MB -
```

[Channels](/explanation/how-snaps-work/channels-and-tracks) declare which release of a snap is installed and tracked for updates. The *latest/stable* channel is used by default, but opting to install from a different channel can be useful for testing new features, or for installing old legacy versions of an application. Which snaps are released to which channels is entirely up to the snap publisher.

## Install the snap

Type `snap install` followed by the name of the snap to install the snap:

```
sudo snap install vlc
```

When _install_ is run for the first time, one or more dependencies may be automatically installed alongside the snap you requested. Your network speed will determine how long this process takes. Snap operations can always be safely cancelled with ctrl+c, and one of snap's best features is that an operation is either wholly successful, or it's cleanly rolled back to the previous state.

A channel can also be optionally specified with the `channel` option:

```
sudo snap install --channel=edge vlc
```

After installation, the channel being monitored for updates can be changed with:

```
sudo snap switch --channel=stable vlc
```

## Run apps and commands from the snap

The vast majority of snap-installed applications will run as you expect, from either the command line or from the desktop launcher.

If executing a command directly doesn't work, use the `snap run` command:

```
snap run vlc
```

Links to snapped applications are located in `/snap/bin` which is added to the system \$PATH.

## Update an installed snap

Snaps are updated automatically. However, to manually check for updates, use the following command:

```
sudo snap refresh vlc
```

The above will check the channel being tracked by the snap. If a newer version of the snap is available, it will be downloaded and installed.

Changing the channel being tracked and refreshing the snap can be accomplished with a single command:

```
sudo snap refresh --channel=beta vlc
```

Updates are automatically installed within 6 hours of a revision being made to a tracked channel, keeping most systems up-to-date. This schedule can be tuned via configuration options and disabled with the `--hold` option.

To check which channel a snap is tracking use the following command:

```
snap refresh --tracking vlc
```

## Pause or stop automatic updates

The `snap refresh --hold` command holds, or postpones, snap updates for individual snaps, or for all snaps on the system, either indefinitely or for a specified period of time.

```
snap refresh --hold=<duration> <snap1> <snap2>...
```

Time duration units can be seconds (s), minutes (m) or hours (h), or a combination of these.  To postpone updates indefinitely, a value of `forever` is also valid.

```
$ snap refresh --hold=24h firefox
General refreshes of "firefox" held until 2023-10-26T14:10:53+01:00
```

If no duration is specified, the hold period defaults to `forever`.

Refer to [Managing updates](/how-to-guides/work-with-snaps/manage-updates) for more details.

## Revert to an earlier revision

A snap may be reverted to an earlier revision with the `snap revert` command. By default, it will attempt to revert to the previous revision:

```
$ sudo snap revert vlc
vlc reverted to 3.0.5-1
```

The optional `--revision` argument can be specified to request a specific revision:

```
snap revert vlc --revision 500
```

This operation will revert both the snap revision and the configuration data associated with the software. If the previously used revision of the snap is from a different channel, that snap will be installed but the channel being tracked won't change.

User data, such as data generated by the snap and stored in a database, is often stored in a _common_ directory and will not be reverted. See [Data locations](/reference/operations/data-locations) for more details on what information is stored and where.

A snap won't automatically update to a version previously reverted from, and the output from `snap refresh` will continue to state *All snaps up to date*. A reverted snap will be automatically updated when a new and different revision is made available by the publisher.

However, explicitly adding the snap name to `snap refresh` *will* update the snap, regardless of whether the latest revision was previously reverted from or not:

```
$ snap list --all vlc
Name  Version  Rev  Tracking  Publisher  Notes
vlc   3.0.5-1  768  stable    videolan✓  -
vlc   3.0.6    770  stable    videolan✓  disabled
$ sudo snap refresh
All snaps up to date.
$ sudo snap refresh vlc
vlc 3.0.6 from VideoLAN✓ refreshed
```

A previously used snap that was reverted from will display *disabled* in the Notes column of the output.

## Connect an interface

Interfaces put you in control of what applications can and cannot do with your system by either permitting or denying access to resources outside a snap's confinement. They're most commonly used to enable access to a webcam, to permit sound recording, for network access, or to read and write to your $HOME directory or remote storage.

Which interfaces a snap requires, and *provides*, depends on the type of snap and its own requirements.

To see which interfaces a snap is using, and which interfaces it could use but isn't, type `snap connections <snapname>`:

```
$ snap connections vlc
Interface       Plug                   Slot                 Notes
audio-playback  vlc:audio-playback     :audio-playback      -
audio-record    vlc:audio-record       -                    -
camera          vlc:camera             -                    -
desktop         vlc:desktop            :desktop             -
home            vlc:home               :home                -
(...)
```

The slot is the provider of the resource while the plug is the consumer, and a slot can support multiple plug connections. In the above output, the [`camera`](/reference/interfaces/camera-interface) interface is not connected because its slot is empty. This means VLC cannot access any connected cameras. The `<snap-name>:<interface-name>` syntax describes which snap is responsible for which component. If there's no snap, such as with `:audio-playback`, the component is directly connected to the system.

To allow a camera to be accessible to VLC, the interface can be connected with the `snap connect` command:

```
snap connect vlc:camera
```
<!--

The Ubuntu Software/[Snap Store](https://snapcraft.io/snap-store) desktop application can also be used to enable and disable interface connections.

To access its interface management functions, either search for an installed snap, or select it from the *Manage* view. The interfaces for the selected application can then be viewed by selecting **Permissions** :

![Snap Store VLC interface connections](https://assets.ubuntu.com/v1/a2609611-store-05.png)

-->

As you can see the output from `snap connections vlc`, and in the above image, VLC  already has access a  user's _/home_ directory because the [`home`](/reference/interfaces/home-interface) interface is connected to the system `$HOME` directory. This is an [automatic connection](/explanation/interfaces/interface-auto-connection), and is granted to certain interfaces and snaps when an interface provides fundamental functionality, such as VLC accessing your personal video and audio files.

Refer to [Interfaces](/explanation/interfaces/all-about-interfaces) for more information.

## Where snaps store data

Most snaps use strict confinement. This isolates both their execution environments and their data from your system (see [Snap Confinement](/explanation/security/snap-confinement) for further details). A confined snap that needs user-access to files will most likely use the [`home`](/reference/interfaces/home-interface) interface to bridge this confinement gap, allowing you to save and load files from your home directory automatically.

You can see whether the _home_ interface is being used in the output to `snap connections <snap name>`:

```
$ snap connections nethack
Interface  Plug          Slot   Notes
home       nethack:home  :home  -
```

Regardless of whether the home interface is used or not, a snap can also store user data, such as a database or configuration files, within its own directory under _$HOME/snap_. Data within this snap-specific directory is stored in one of two further directories, depending on whether the data needs to be tied to a specific release, or whether it can be used across multiple releases.

Data for a specific release is stored within a directory named after the [revision](/reference/glossary) of a release. This is a numeric value, such as `55` or `56`. The data for each specific revision is often copied from one release to the next, so that reverting from one revision to a previous revision will restore a working configuration, for instance. The snap directory also contains a symbolic link called `current` that points to the snap revision currently active.

Data that can be shared across releases is stored in a directory called `common`, and might include image or audio caches, or a database. This data is not copied between releases.

For more details on where snaps store their data, see [Data locations](/reference/operations/data-locations).

## Create and restore a snapshot

A *snapshot* is a copy of the user, system and configuration data stored by *snapd* for one or more snaps on your system, and a snapshot of the data found in both `$HOME/snap/<snap-name>` and `/var/snap/<snap-name>` is stored in `/var/lib/snapd/snapshots/` (see [Data locations](/reference/operations/data-locations) for more details).

Snapshots are generated **manually** with the `snap save` command and **automatically when a snap is removed**. A snapshot can be used to backup the state of your snaps, revert snaps to a previous state and to restore a fresh snapd installation to a previously saved state.

The `snap save` command creates a snapshot for all installed snaps, or if declared individually, specific snaps:

```
$ sudo snap save
Set  Snap         Age    Version               Rev   Size   Notes
30   core         1.00s  16-2.37~pre1          6229   250B  -
30   core18       886ms  18                    543    123B  -
30   go           483ms  1.10.7                3092   387B  -
30   vlc          529ms  3.0.6                 770   882kB  -
```

The `restore` command replaces the current user, system and configuration data with the corresponding data from the specified snapshot:

```
$ sudo snap restore 30
Restored snapshot #30.
```

By default, this command restores all the data for all the snaps in a snapshot. You can restore data for specific snaps by simply listing them after the command, and for specific users with the `--users=<usernames>` argument.

Excluding a snap’s system and configuration data from *snap restore* is not currently possible.

See [Snapshots](/how-to-guides/manage-snaps/create-data-snapshots) for further details on creating, exporting, importing and validating snapshots.

## Remove a snap

To remove a snap from your system, along with its internal user, system and configuration data, use the *remove* command:

```
$ sudo snap remove vlc
vlc removed
```

Add the `--no-wait` option to return immediately to the command prompt and run the removal in the background.

By default, all of a snap's revisions are also removed. To remove a specific revision, add the `--revision=<revision-number>` argument to the *remove* command.

Prior to removal (except on [Ubuntu Core](https://www.ubuntu.com/core) systems), a snap's internal user, system, and configuration data is saved as a *snapshot* (_snapd 2.39+_), and retained for 31 days.

To  remove a snap without generating a snapshot, use the additional `--purge` argument:

```
$ sudo snap remove vlc --purge
vlc removed
```

For more details information on using snaps, see our [Snap How-to guides](/how-to-guides/index).

