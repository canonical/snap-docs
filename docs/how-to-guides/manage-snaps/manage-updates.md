(how-to-guides-work-with-snaps-manage-updates)=
# Manage updates

Snaps update automatically, and by default, the *snapd* daemon checks for updates 4 times a day. Each update check is called a **refresh**.

Updates can be set to occur on Friday at midnight, or for specific days of the month, such as only the third Monday, or even the last Friday of the month, between 23:00 to 01:00 the next day. They can even be postponed indefinitely, or for a set period of time.

When, if, and how often, these updates occur can is the job of the *snap refresh* command. 

```{caution}
Snaps running in [_devmode_](/explanation/security/snap-confinement), or installed locally, are typically intended for testing and do not update automatically until they've been published and downloaded from the store.
```

## Refresh update control

There are two general approaches to postponing or otherwise managing snap updates, with  either the `snap refresh --hold` command, or with system settings:

- Pause or stop updates with refresh hold
- Control updates with system options

## Pause or stop automatic updates

**Requires: snapd 2.58+**

The `snap refresh --hold` command holds, or postpones, snap updates for individual snaps, or for all snaps on the system, either indefinitely or for a specified period of time.

```
snap refresh --hold=<duration> <snap1> <snap2>...
```

Time duration units can be seconds (s), minutes (m) or hours (h), or a combination of these.  To postpone updates indefinitely, a value of `forever` is also valid.

```
$ snap refresh --hold=24h firefox
General refreshes of "firefox" held until 2022-10-26T14:10:53+01:00
```

If no duration is specified, the time duration defaults to `forever`.


If no snaps are specified, the hold applies to all snaps installed on the system:

```
$ snap refresh --hold=24h
Auto-refresh of all snaps held until 2022-10-26T14:25:58+01:00
```

To see which snaps are being held, look for `held` in the _notes_ column when running `snap list`:

```
$ snap list
Name         Version  Rev   Tracking       Publisher          Notes                         
alacritty    0.8.0    46    latest/stable  snapcrafters       classic   
vlc          3.0.18   3078  latest/stable  videolan✓          -                              
yt-dlp       18       212   latest/edge    morrisong          held      
```

However, there are important differences in how a hold is applied, depending on whether individual snaps are specified or not. These differences are described below.

### If snaps are specified

The refresh hold is:
* **Effective on auto-refreshes and general snap refresh requests**
* **Not effective on targeted snap refreshes**

When one or more snaps are specified, the hold is effective only on their auto-refreshes and general refresh requests from `snap refresh`.

However, a refresh that targets a held snap specifically will not be blocked and will always be able to proceed.

This can be useful if a snap upgrade is known to be problematic. That specific snap can be held while the remainder of the system is safely refreshed. After the snap upgrade problem has been solved, and a new revision of the snap published, that snap can then be manually refreshed as a specific target. If the upgrade works as expected, the hold can be safely removed (see [Remove a hold](#remove-a-hold)).

### If no snaps are specified

The refresh hold is:
* **Effective only on auto-refreshes**
* **Not effective on general snap refresh requests and targeted snap refreshes**

If no snaps are specified, a hold applies to all snaps installed on the system, however the hold is only effective on auto-refreshes and will not block either general refresh requests from 'snap refresh', or specific snap requests from 'snap refresh target-snap'.

### Remove a hold

The `snap refresh --unhold` command removes a refresh hold, either for the specified snaps or for all snaps when no snaps are targeted specifically.

For a single snap:

```
$ snap refresh --unhold firefox
Removed general refresh hold of "firefox"
```

For for all snaps:

```
$ snap refresh --unhold
Removed auto-refresh hold on all snaps
```

## Control updates with system options

The refresh rate is freely configurable, and can be set to any duration above a lower bound of once every 20 minutes. There are four [system-wide options](/how-to-guides/manage-snaps/set-system-options) that manage how updates are handled:

- **refresh.timer**: defines the refresh frequency and schedule
- **refresh.hold**: delays the next refresh until the defined time and date
- **refresh.metered**: pauses refresh updates when network connection is metered
- **refresh.retain**: sets how many revisions of a snap are stored on the system

### refresh.timer

Use *refresh.timer* to modify when, and how frequently, your snaps are refreshed.

The following example asks the system to only refresh snaps between  4.00am and 7.00am, and 7.00pm and 10:10pm:

```
sudo snap set system refresh.timer=4:00-7:00,19:00-22:10 
```

Other examples for the time and frequency option include:

| Options | Result |
|---|---|
| `mon,10:00,,fri,15:00` | Mondays at 10:00, Fridays at 15:00 |
| `mon,fri,10:00,15:00` | Mondays at 10:00 and 15:00, Fridays at 10:00 and 15:00 |
| `mon-wed,fri,9:00-11:00/2` | Monday to Wednesday and on Friday, twice between 9:00 and 11:10 |
| `mon,9:00~11:00,,wed,22:00~23:00` | Mondays, some time between 9:00 and 11:00, and on Wednesdays, some time between 22:00 and 23:00 |
| `mon,wed` | Monday and on Wednesday, at 0:00 |
| `mon2-wed,23:00-24:00` | 2nd Monday of the month, through the following Wednesday, between 23:00 and 24:00 |
| `fri5,23:00-01:00` | Last Friday of the month, from 23:00 to 1:00 the next day |

See [Timer string format](/reference/operations/timer-string-format) for a comprehensive breakdown of the syntax used to define times and frequencies. 

You can check the update frequency for your environment with the `refresh` command:

```
$ snap refresh --time
timer: 00:00~24:00/4
last: today at 07:47 BST
next: today at 12:13 BST
```

By default, the snap system is scheduled to refresh four times per day, as shown in the above output.

### refresh.hold

Use *refresh.hold* to delay snap refreshes until a defined time and date (up to 90 days). The time and date format needs to conform to [RFC 3339](https://tools.ietf.org/html/rfc3339). 

For example, *5:22pm (BST), Tuesday 23rd April 2019*, would look like the following: 

```
2019-04-23T17:22:54+01:00
```
The correct format can be generated with the *date* command:

```
$ date --date="BST 2023-09-23 17:22:54" +%Y-%m-%dT%H:%M:%S%:z
2023-09-23T17:22:54+01:00

$ sudo snap set system refresh.hold="$(date --date=tomorrow +%Y-%m-%dT%H:%M:%S%:z)"
$ sudo snap get system refresh.hold
2019-04-24T17:22:54+01:00
```

After a refresh, the next refresh can be delayed by up to 90 days, after which a refresh will be performed regardless of the *refresh.hold* value.

### refresh.metered

Use *refresh.metered* to pause and re-enable the refresh process when  *NetworkManager* detects a metered connection, such as an LTE link with a limited data plan. 

To hold refreshing snaps when on a metered connection:

```
sudo snap set system refresh.metered=hold
```

To allow refreshing:

```
sudo snap set system refresh.metered=null
```

By default, *refresh.metered* is enabled when a metered connection is detected.

[quote]
ⓘ  refresh.metered is available in snap 2.33 and later.
[/quote]

<a name="retain"></a>

### refresh.retain

Use *refresh.retain* to set the maximum number of a snap's revisions stored by the system *after* the next refresh:

```
sudo snap set system refresh.retain=3
```
The *refresh.retain* value can be a number between 2 and 20. The default is `refresh.retain=3` on Ubuntu Core systems and `refresh.retain=2` on *classic* Ubuntu systems, such as those running an Ubuntu LTS release.

[quote]
ⓘ  refresh.retain is available in snap 2.34 and later.
[/quote]

## Manual updates

Regardless of when a refresh is scheduled, a refresh can be initiated with the `snap refresh` command:

```
$ snap refresh
gnome-system-monitor 3.28.2 from 'canonical' refreshed
gnome-calculator 3.28.2 from 'canonical' refreshed
```
The *refresh* command can also be used to see when the last refresh occurred and when the next is scheduled:

```
$ snap refresh --time
timer: 00:00~24:00/4
last: today at 09:16 GMT
next: today at 17:39 GMT
```

The first line in the above output shows the value of the *timer* system option. This defines how and when a refresh should be scheduled.

To see which snaps are going to be updated with the next _refresh_, use the additional `--list` argument:

```
$ snap refresh --list
Name           Version                    Rev   Publisher     Notes
core           16-2.45.1+git2022.b6b3c25  9584  canonical✓    core
get-iplayer    3.26                       250   snapcrafters  -
qt551          5.5                        30    keshavnrj     -
```

## Locally installed snaps

The `snap refresh --ammend` command can be used to replace a locally installed snap with an identically named snap on the store.

## Monitor changes

Use the `snap changes` and `snap tasks <change-id>` commands to see details about what changed during the last refresh:

```
$ snap changes
ID    Status  Spawn                   Ready                   Summary
2052  Done    today at 09:34 BST      today at 09:35 BST      Auto-refresh 7 snaps
2053  Done    today at 15:16 BST      today at 15:17 BST      Refresh snaps "gnome-calculator", "flock-chat", "gnome-characters", "gnome-system-monitor"
```

Add the _change-id_ to see what actions a specific change performed:

```
$ snap tasks 2053
Status  Spawn               Ready               Summary
Done    today at 15:16 BST  today at 15:16 BST  Ensure prerequisites for "gnome-calculator" are available
Done    today at 15:16 BST  today at 15:16 BST  Download snap "gnome-calculator" (199) from channel "stable"
Done    today at 15:16 BST  today at 15:16 BST  Fetch and check assertions for snap "gnome-calculator" (199)
⋮
Done    today at 15:16 BST  today at 15:16 BST  Start snap "gnome-system-monitor" (54) services
Done    today at 15:16 BST  today at 15:16 BST  Clean up "gnome-system-monitor" (54) install
Done    today at 15:16 BST  today at 15:16 BST  Run configure hook of "gnome-system-monitor" snap if present
```

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

This operation will revert both the snap revision and the configuration data associated with the software. If the previously used revision of the snap is from a different channel, that snap will be installed but the channel being tracked won’t change.

User data, such as data generated by the snap and stored in a database, is often stored in a *common* directory and will not be reverted. See [Data locations](/reference/operations/data-locations) for more details on what information is stored and where.

A snap won’t automatically update to a version previously reverted from, and the output from `snap refresh` will continue to state *All snaps up to date*. A reverted snap will be automatically updated when a new and different revision is made available by the publisher.

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

> **Reverting to a previous version of *snapd*** </br>
The snapd snap manages the snap packaging system, and is therefore a special case if you wish to revert it, or downgrade the currently running version. It must be reverted on its own, and there cannot be any pending changes for other snaps in the pipeline.

