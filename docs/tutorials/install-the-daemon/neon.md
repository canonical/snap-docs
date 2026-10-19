---
myst:
  html_meta:
    description: Learn how to re-install snap on KDE Neon through Discover or the command line, and enable Discover support for finding snaps.
---

(interfaces-installing-snap-on-kde-neon)=
# Install snap on KDE Neon

Snap should be installed by default on KDE Neon. In case it has been removed, it can be re-installed from *Discover*, the KDE software centre application. This can be found in the Application Launcher. From Discover,  search for *snapd* and select **Install**.

It's also possible to use the *Discover* desktop application to search for available snaps. To enable this feature, select on *Settings* within Discover and scroll down to the *Missing Backends* section. Select **Install** alongside *Discover - Snap backend*.

## Install from the command line

Snap can also be installed from the command line. Open the *Konsole* terminal and enter the following:

```
sudo apt update
sudo apt install snapd
```

