(explanation-how-snaps-work-refresh-awareness)=
# Refresh awareness

Snaps update automatically, and by default, the *snapd* daemon checks for updates 4 times a day. Each update check is called a *refresh* and is described in more detail in [Managing updates](/how-to-guides/work-with-snaps/manage-updates).

If a refresh occurs while an affected desktop application is running, **refresh app awareness** helps to mitigate any potential issues, using a combination of in-place updates, deferred updates, and desktop notifications.

Refresh awareness requires snapd _2.57+_

```{note}
[Service management](/how-to-guides/manage-snaps/control-services) is not affected, as services are started and stopped manually as part of the refresh process, unless a specific _endure_ value has been embedded into the snap by the snap developer. See [snapcraft.yaml refresh-mode](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/snapcraft-yaml/#apps.%3Capp-name%3E.refresh-mode) for further details.
```

## In-place updates

If an application is running when an automatic refresh detects an update, the new snap revision is downloaded in the background to minimise the refresh time.

When the download is complete, the user is notified of the pending update and a snap refresh is triggered when the application stops.

![Snap pending update notification](https://assets.ubuntu.com/v1/6bcfcc2b-firefox-pending.png)

Once the snap has been refreshed, an additional notification informs the user that the new snap revision is ready to be used (requires snapd *2.59.2+*)

In-place updates only work with automatic refreshes, and not when a refresh is triggered manually.

## Deferred updates

An update can be postponed for up to 14 days for a running application. The update will be either applied when the application closes, during next automatic refresh occurs without the application running, or after 14 days even if the application remains active.

After closing the affected application, the refresh can be triggered manually with the `snap refresh` command, either globally for all snaps, or with the specific snap name:

```
snap refresh <snap-name>
```

If a manual refresh detects the application is still running, the error output will include the detected process ids of the running applications:

 ```
error: cannot refresh "firefox": snap "firefox" has running apps (firefox), pids:
        1639,1854,1912,1932,3514,3632,5814,5870
```

See [Managing updates](/how-to-guides/work-with-snaps/manage-updates) for more details controlling update frequencies, and holding updates for any period of time.

## Desktop notifications

While an affected application is running, each refresh attempt will trigger a desktop notification to inform the user that the app should be closed to avoid disruption.

On the default Ubuntu GNOME desktop, notifications can be modified and disabled by selecting Notifications from the Settings application and selecting the _Snapd User Session Agent_ application:

![Snapd User Session Agent Gnome Notification Settings](https://assets.ubuntu.com/v1/a417893f-snapd-notifications.png) 

Other desktop environments have equivalent functionality.

See [Refresh awareness security policy](/explanation/security/security-policies.md#refresh-awareness) for details on how refresh updates accommodate confinement and security policy requirements.
