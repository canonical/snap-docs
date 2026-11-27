---
myst:
  html_meta:
    description: Release notes for Snapd 2.28, announced as 2.28.1 on 10 October 2017. Read about selected updates and improvements in this release.
---

(release-notes_snapd-2-28)=
# Snapd 2.28

* **New "post-refresh" hook** ([topic](https://forum.snapcraft.io/t/478/10/)): A new hook, `post-refresh`, runs after the snap is refreshed but before services are started, useful for refresh-related housekeeping.
* **Initial base snap support** ([topic](https://forum.snapcraft.io/t/381/)): The new "base" snap allows snaps to select which base filesystem they require, rather than always using the `core` snap. This release adds support for bases and provides an example base snap called `bare`, which is empty and useful for minimal, statically linked snaps. New bases are not automatically downloaded in this release; that capability came in 2.29.
* **Polkit integration** ([topic](https://forum.snapcraft.io/t/1206)): Provides integration with the "polkit" mechanism of the GUI environment, making it possible to download and install snaps from graphical package management interfaces without logging into the store, as was previously required when operating as root or via sudo in the terminal.
* **Full xdg-open support via `snap userd`** ([topic](https://forum.snapcraft.io/t/1420)): Allows opening `http`, `https`, and `mailto` links directly from confined snaps without installing extra software.
* **Full bash-completion** ([topic](https://forum.snapcraft.io/t/2261)): Bash-completion support was added in 2.27, requiring an extra step to enable it in the shell. That step is now eliminated and is fully automatic. Completion of aliases is not yet supported.
* **New `snap switch` command** ([topic](https://forum.snapcraft.io/t/1418)): A convenient way to switch the channel of a snap without refreshing it right away, useful when offline or on a high-cost connection.
* **Proxy configuration on Core devices** ([topic](https://forum.snapcraft.io/t/467)): Core devices can now have their system-wide proxies configured via `snap set core proxy.{http,https,ftp}=<url>`.
* **Snap service management** ([topic](https://forum.snapcraft.io/t/262)): The new `snap services <snap>` command shows a snap's services and their status, also summarized in `snap info <snap>`. Services can be started/stopped via the new `snap start/stop/restart <snap.app>` commands, with logs available via `snap logs <snap.app>`. All of these are also exposed via the API.
* **Classic confinement on distributions that do not use the `/snap` directory** ([topic](https://forum.snapcraft.io/t/1732)): Classic-confinement snaps, which may refer to paths under `/snap`, now also work on distributions that use a different directory layout, once a symlink from `/snap` to the non-standard snap directory (usually `/var/lib/snapd/snap`) is created. The related error message was also improved.

Complete details are available in the project's commit history.
