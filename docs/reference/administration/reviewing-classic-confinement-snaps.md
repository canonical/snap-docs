---
myst:
  html_meta:
    description: Guidelines around classic confinement, considering supported and unsupported use cases.
---

(interfaces-reviewing-classic-confinement-snaps)=
# Classic confinement guidelines

There are situations where a given application cannot work properly under strict confinement. Technical reasons may include:

* access to files on the host outside the snap's runtime (eg, /usr)
* running arbitrary command (esp if user-configurable such as a developer tool to organize dev environments)
* access to resources not yet supported by snapd and where the requirement is clearly understood to be supportable by snapd. This may result in temporarily granting classic until snapd supports the use case in strict mode

However, being known to require classic confinement alone does not justify granting classic confinement. The full criteria defined in {ref}`Store-reviews: process and criteria <interfaces-process-for-aliases-auto-connections-and-tracks>` must be met.

Additionally, sometimes it might make sense for a snap to be allowed the use of classic (eg, for classic distro) but be usable in strict mode (eg, for Ubuntu Core). In these cases, rather than having two separate snaps, it is considered best to have [two separate tracks](https://forum.snapcraft.io/t/new-track-classic-request-for-the-nano-snap/10762/11), the default track and another called `classicmode`.

## Supported categories

Classic requests generally fall under a number of categories. Below lists categories that developers may consult for things that are understood to require classic confinement. 

* compilers
* debug tools
* IDEs
* juju helpers
* kubernetes tools requiring [arbitrary authentication agents](https://forum.snapcraft.io/t/classic-confinement-for-kontena-lens/13729/18)
* [nautilus scripts](https://forum.snapcraft.io/t/synchrorep-need-classic-confinement/13347/8)
* programming languages
* public cloud agents
* tools for local, non-root user driven configuration of/switching to development workspaces/environments
* terminal emulators, multiplexers and shells
* HPC or orchestration agents/software for running workloads on systems without traditional users where the systems are otherwise managed outside of the agent (ie, the software simply orchestrates running workloads on systems and doesn't manage the systems themselves). Note: many HPC/orchestration applications can run with strict confinement and classic should only be granted if snapd does not support the specific use case (eg, the [need for user accounting](https://forum.snapcraft.io/t/request-for-classic-confinement-slurm/18309/11)).
* Installer snaps for Ubuntu Flavors based on the official [ubuntu-flavor-installer](https://github.com/canonical/ubuntu-flavor-installer) 
* AI agent/assistant that runs arbitrary user-directed code and needs to reach files and programs that aren’t known at build time

## Unsupported categories

There are also some reasons that are well understood to not be supported and some of them have well-known workarounds:

* management snaps
* 3rd party installer snaps (eg, for native packages, AppImages, Flatpaks, Snaps, etc)
* difficulty making strict confinement work
* dependent software only available on host (ship in instead snap (eg, stage-packages, build from source))
* access to dot files in $HOME (use $HOME instead of getent*, personal-files)
* access to /etc (use layouts, system-files)
* hard-coded paths (use snapcraft-preload, layouts)
* ability to run other snaps directly (as opposed to defined interfaces)
* access to arbitrary files on the system because the application isn't designed with confinement in mind (if a desktop application, use portals or [xdg-open](https://forum.snapcraft.io/t/allowing-xdg-open-to-open-files/3789/11))
* access to arbitrary files on the system due to developer/user inertia ({ref}`home <interfaces-home-interface>` and {ref}`removable-media <interfaces-removable-media-interface>` is almost always sufficient, though {ref}`personal-files <interfaces-personal-files-interface>` and {ref}`system-files <interfaces-system-files-interface>` may be used under certain circumstances)
* access to arbitrary files on the system to avoid increasing a snap's size
* [GNOME shell extensions](https://forum.snapcraft.io/t/yaru-dark-theme-toggle-review-request/13169/7)
* [nautilus extensions](https://forum.snapcraft.io/t/synchrorep-need-classic-confinement/13347/8)
* access to [org.kde.PlasmaShell.evaluateScript](https://forum.snapcraft.io/t/issue-establishing-dbus-interface-with-org-kde-plasmashell/14908/4)
* access to [org.kde.klauncher5 (klauncher)](https://forum.snapcraft.io/t/18377) ([modify application](https://forum.snapcraft.io/t/18377/3) to launch programs directly)
* direct access to sudo (modify program (eg, check if root and if not, alert user to run under sudo))
* direct access to pkexec (modify program (eg, check if root and if not, alert user to run under sudo; note a polkit backend is planned but not roadmapped, so a snap may one day be able to use pkexec, but this is TBD)).
