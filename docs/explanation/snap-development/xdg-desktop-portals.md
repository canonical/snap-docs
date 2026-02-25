(interfaces-xdg-desktop-portals)=
# xdg-desktop-portals

Portals are a standardised framework allowing desktop applications to use resources outside of their sandbox. The file chooser portal, for example, opens a native file chooser on the host system. When the user selects a file, the application is granted access to that file.

Portals provide a range of common features to applications, including:

* Opening a file with a file chooser
* Opening URIs in other applications
* Preventing the device from suspend/sleep/powering off
* Sending email
* Showing notifications
* Taking screenshots and screencasts

See the [Portal API reference](https://docs.flatpak.org/en/latest/portal-api-reference.html) for all supported portals.

> ⓘ Portals originated from the [Flatpak](https://flatpak.org/) project, but are now a common Linux desktop standard with support from GNOME, KDE and Snapcraft. They are even used outside of sandboxes to provide a standardised API to common desktop features such as [screenshots and screen casts on wayland](https://github.com/emersion/xdg-desktop-portal-wlr/wiki/FAQ).

## How to use portals in your snap

1. **Use the Portal APIs in your application**
  Unlike regular [Snapcraft interfaces](/reference/interfaces/index), *portals require applications to use a new API* in order to access resources. Toolkits like GTK 3 and Qt5, however, provide transparent support for portals. See [Portal support in GTK 3](https://docs.flatpak.org/en/latest/portals.html#portal-support-in-gtk) or [Portal support in Qt5 and KDE](https://docs.flatpak.org/en/latest/portals.html#portal-support-in-qt-and-kde) for detailed information.
If your application is not using one of those toolkits, you will need to use the Portals API directly. See [the Portals API documentation](https://flatpak.github.io/xdg-desktop-portal/docs/portal-interfaces.html) for more information.

2. **Add the `desktop` interface to your snap**
  This interface gives your snap access to the portals.

3. **Enable Portal support in your application.** 
  - **GTK 3**:  turn on portal support in GTK 3 by setting the following environment variable:
   `GTK_USE_PORTAL=1`

-  **Qt**:  often defaults to using portals, but you can enable it manually by changing the platform theme:
      Set `QT_QPA_PLATFORMTHEME=gtk3` on GTK based desktops and
      Set `QT_QPA_PLATFORMTHEME=flatpak` and `QT_QPA_FLATPAK_PLATFORMTHEME=kde` for Qt based desktops.

- **Electron**:  portal support is present in the Electron file chooser.

> ⓘ Both the [`gnome` extension](https://snapcraft.io/docs/gnome-extension) and the  [`kde-neon` extension](https://snapcraft.io/docs/kde-neon-extension) automatically enable portal support for GTK 3 and Qt applications on GTK-based desktops. If your snap uses either extension, you only need to do step 1.


<h2 id="heading--portal-vs-home">File chooser portal vs home interface<sup><a href=#heading--portal-vs-home>⚓</a></sup></h2>

It is recommended to use the file chooser portal instead of the [`home`](/reference/interfaces/home-interface) and [`removable-media`](/reference/interfaces/removable-media-interface) interfaces for the following reasons:

* The portal gives the user complete control over what exact files your application should access while the interfaces are all-or-nothing toggles.
* The portal works with hidden files and folders in the home directory. If a user chooses a hidden file, the portal will give your application access to it. The `home` interface does not give your app access to hidden files and folders in the home directory for security reasons. Note that the `home` interface does give access to hidden files and folders elsewhere, just not in the home directory itself.
* The portal works with removable-media out of the box. If a user chooses a file from a USB stick, your app will get access to it. The `removable-media` interface, however, does not auto-connect by default.

However, the file chooser portal works a bit differently than the home interface:

* Files are fuse-mounted to `/run/user/<uid>/doc/<hash>/` in order to give your application access to it. So the path your application sees is different from the path a user chose, even though both are the same file.

The FileChooser portal also contains a few bugs:


* ["Executable" permissions are currently not retained](https://github.com/flatpak/xdg-desktop-portal/issues/517). All files will appear as non-executable to your application.
* Support for selecting folders instead of files will only work on distributions using `xdg-desktop-portal` > 1.8.0.
* Currently, the files are mounted even if your application has access to the file using another interface. See [Improving XDG Desktop Support](https://forum.snapcraft.io/t/improving-xdg-desktop-portal-support/13035) for the current status on fixing this issue.

## Known Limitations

* `org.freedesktop.portal.Flatpak.Spawn` only works in a Flatpak. If your application needs to run arbitrary binaries on the host system, you can use [classic confinement](/).
* Portal support depends on the version of `xdg-desktop-portal` in the host system. Older versions do not support all portals. [Repology](https://repology.org/project/xdg-desktop-portal/versions) shows what version of `xdg-desktop-portal` each distribution has and the [portals NEWS](https://github.com/flatpak/xdg-desktop-portal/blob/master/NEWS) file explains what portals each version supports.

> ⓘ See [Desktop applications](/reference/interfaces/desktop-applications) for more information on how to snap a desktop application.

