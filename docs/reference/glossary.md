(reference-operations-glossary)=
# Glossary

<!--

:construction: This topic is under construction. Feel free to add new terms.

To help with linking to these terms, we're using the following syntax as the heading for each title definition:

```html
<h3 id='heading--term'>term</h3>
```

TODO:
plugin
snapcraft.yaml
metrics
dangerous
[/quote]

-->

There are a significant number of terms and definitions that are unique to the snap, snapd, and snapcraft ecosystem. This page defines the terminology and other terms touched by these tools and links to further information when required.

If you're new to using snaps, take a look at [Getting started](/tutorials/get-started), and if you're looking to build your own snaps, take a look at the [Snapcraft overview](/).

## Terms and definitions

### appliance

An appliance is a pre-configured [Ubuntu Core](#heading--ubuntu-core) bootable image that includes one or more snaps to provide a specific set of features. The [OpenHAB](https://ubuntu.com/appliance/openhab) smart home system, the [Plex](https://ubuntu.com/appliance/plex) media server, and the [Nextcloud Server](https://ubuntu.com/appliance/nextcloud) platform, are all available as appliances, for example.

See [What is an Ubuntu Appliance](https://ubuntu.com/appliance/about) for more details.

### assertion

An assertion is a digitally signed document that either verifies the validity of a process, as attested by the signer, or carries policy information, as formulated by the signer.

Snapcraft, snapd, Ubuntu Core and the Snap Store all use assertions to handle a variety of functions and processes, including authentication, policy setting, identification and validation.

See [Assertions](/explanation/security/assertions) for more details.

### base

A  base is a special kind of snap that provides a run-time environment with a minimal set of libraries that are common to most applications. They’re transparent to users, but they need to be considered, and specified, when building a snap.

See [Base snaps](/) for more details.

### branch

A branch is an optional finer subdivision of a channel for a published snap that allows for the creation of a short-lived sequences of snaps that can be pushed on demand by snap developers to help with fixes or temporary experimentation.

See [Branches](/t/channels/551#heading--branches) for more details.

### brand store

See [dedicated Snap Store](#heading--dedicated)

### channel

Channels define which release of a snap is installed and tracked for updates. They consist of, and are subdivided by, tracks (`latest`, or developer defined, e.g `1.0`), risk-levels (stable, candidate, beta and edge), and optional branches. The _tracking_ value for an installed snap shows which channel is being installed and followed.

See [Channels](/explanation/how-snaps-work/channels-and-tracks) for more details.

### classic

_Classic_ is a snap confinement level that allows access to your system’s resources in much the same way traditional packages do. It's used sparingly and only after a manual review.

See [Snap confinement](/explanation/security/snap-confinement) for more details.

### confinement

A snap’s confinement level is the degree of isolation it has from your system. There are three levels of snap confinement: strict, classic and devmode. The majority of snaps use _strict_ confinement, and run in complete isolation up to a level of minimal access that's always deemed safe, or through access given via explicit interface connections.

See [Snap confinement](/explanation/security/snap-confinement) for more details.

### core

_core_ is a base snap built from [Ubuntu 16.04 LTS](http://releases.ubuntu.com/16.04/). It's different from _core16_ (see below) because it bundles _snapd_ and its associated tools whereas core16 does not.

See [Base snaps](/) for more details.

### core16

_core16_ is a base snap built from [Ubuntu 16.04 LTS](http://releases.ubuntu.com/16.04/). It's different from _core_ (see above) because it does not include _snapd_ and its associated tools.

See [Base snaps](/) for more details.

### core18

_core18_ is a base snap built from [Ubuntu 18.04 LTS](http://releases.ubuntu.com/18.04/). It's the current standard base for snap building and is the recommended base for the majority of snaps. It’s what the [snapcraft init](/t/snapcraft-overview/8940#heading--creating-snapcraft) command includes when generating a new project’s template  *snapcraft.yaml* .

See [Base snaps](/) for more details.

### core20

_core20_ is under active development. It's a base snap built from [ Ubuntu 20.04 LTS (Focal Fossa)](https://releases.ubuntu.com/20.04/), released April 23, 2020.

See [Base snaps](/) for more details on base snaps.

### Dedicated Snap Store

A *Dedicated Snap Store* (formerly known as a *Brand Store* ) allows vendors running Ubuntu Core and snap-based devices to control exactly what snaps are available and when.

It can inherit selected packages from other snap stores, and host a set of snaps specific to a brand and device models, and be either open to all developers or a specific list.

See [Store overview](https://core.docs.ubuntu.com/en/build-store/#brand-stores) in our Ubuntu Core documentation for more details.


### devmode

_devmode_ is a snap confinement level used by snap developers when creating their snaps. With *devmode*, a snap runs as a strictly confined snap with full access to system resources, and produces debug output to identify unspecified interfaces.

See [Snap confinement](/explanation/security/snap-confinement) for more details.

### epoch

Epochs enable snap developers to control how users receive a new application release when an application’s data format becomes incompatible with older versions of the application.

When a new release breaks data compatibility with an older version, incrementing the epoch in the new release stops old users automatically refreshing to the new version.

See [Epochs](/) for more details.

### extension

Snapcraft extensions enable snap developers to easily incorporate a set of common requirements into a snap. There are extensions to help with the packaging of both Gnome and KDE Plasma applications.

See [Snapcraft extensions](/) for more details.

### gadget

A gadget is a device or other deployment running Ubuntu Core alongside a vendor-specified, managed and maintained set of snaps. A gadget could be a router, for example, a home automation device or even a VM cloud instance. Its properties are defined within an embedded _gadget snap_.

See [The gadget snap](/reference/development/yaml-schemas/the-gadget-snap) for more details.

### hook

A hook is an executable that runs within a snap’s confined environment when a certain action occurs. Actions include snap installation and removal, changes to its configuration or connection state, and before or after a refresh.

For more details, see [Supported snap hooks](/reference/development/supported-snap-hooks).

### interface

An interface enables resources from one snap to be shared with another and with the system. Interfaces require a connection, which is commonly made automatically, or manually with the `snap connect` command.

For a snap to use an interface, its developer needs to have first defined its corresponding plugs and slots within a snap’s [snapcraft.yaml](/) file.

See [Interfaces](/explanation/interfaces/all-about-interfaces) and [Interface management](/how-to-guides/work-with-snaps/connect-interfaces) for more details.

### Launchpad

Launchpad is a code collaboration and secure build system for open source projects. It is used by Ubuntu and other projects to coordinate work on bugs and fixes.

Launchpad provides the ability to build your snap for multiple architectures - x86, ARM, RISC-V, POWER, s390. If you use Launchpad for snap building then you need to provide it with your source code and snapcraft. It will build and publish new revisions of your snap, which you can test and release. If you do not already have a good multi-arch CI/CD system up and running then we recommend you use Launchpad to support all devices with your snap.

See [Remote build](/) for more details.

### layout

Layouts help snap developers make snap-confined elements accessible from locations such as  `/usr` ,  `/var`  and  `/etc` inside the snap. This helps when using pre-compiled binaries and libraries that expect to find files and directories outside of locations referenced by  `$SNAP`  or  `$SNAP_DATA`.

They cannot be used to expose elements to non-permitted locations on the host environment (such as exposing a file to `/etc/` on the host filesystem).

See [Snap layouts](/) for more details.

### LXD

[LXD](https://linuxcontainers.org/lxd/introduction/) is a next generation system container manager. It offers a user experience similar to virtual machines but using Linux containers instead. It can be used by the _snapcraft_ command to isolate the build process from the host system.

See [Building with LXD](/) for details.

### Model

Snaps are a containerised application format which is designed for desktops and devices. Unlike Docker images, which are designed for scale-out environments where the mapping of hosts to containers can vary dynamically, snaps are designed to be installed on a specific machine, alongside other snaps. The snap container format allows for detailed integration between snaps, using low-level host-specific capabilities like shared directories and shared memory. These host-specific mechanisms are generally not used with Docker, because one cannot predict if other containers will be on the same machine or not.

Each machine where snaps are installed has its own sense of type - a model. This comes from the IoT world, where a box which is acting as a security camera recorder would be expected to have a very different software load than a box which is acting as an elevator control system. The manufacturer of the box specifies the model. Based on that model, snaps will follow specific rules about software installation. For example, on an elevator control system, the model might dictate that certain snaps must be installed, and other snaps may not be installed.

### Multipass

[Multipass](https://multipass.run/) is a lightweight VM manager for Linux, Windows and macOS. It's designed for developers who want a fresh Ubuntu environment with a single command. It uses KVM on Linux, Hyper-V on Windows and HyperKit on macOS to run the VM with minimal overhead.

By default, the  _snapcraft_ command uses Multipass to isolate the build process from the host system.

See [Building your snap](/t/snapcraft-overview/8940#heading--building-your-snap) for further details.

### parallel installs

Parallel installs enable you to run multiple instances of the same snap on the same system. Each instance is completely isolated from all other instances, including its name, configuration, interface connections, data locations, services, applications and aliases.

See [Parallel installs](/) for more information.

### part

A snap may seem like a single application but it can often include code from many different open source upstream projects. The snapcraft build description needs to specify, for each component, where to fetch it and how to build it. We call each of those elements a *part*.

Part definitions can be shared and reused, to enable many different snaps to get the component without re-specifying in detail how to build it.

### platform snap

A platform snap contains the parts, packages, interface connections and environment variables, among other elements, to enable other snaps to use a platform without additional dependencies or configuration.

Examples include kde-frameworks to provide KDE Plasma compatibility, and WINE to help snaps more easily run Microsoft Windows executables.

A platform snap cannot be installed directly by users. They are instead invoked by snap developers as the [default-provider](/t/the-content-interface/1074#heading--default) in a [content interface](/t/the-content-interface).

### preseeding

When Ubuntu Core boots for the first time, a seeding process installs an initial set of snaps and runs their respective hooks.

_Preseeding_ speeds up this process by performing as many of these seed administrative tasks as possible in advance when an image is created. During deployment, snapd still performs the seeding process but it automatically skips the parts that have already been performed.

See [Preseeding](https://ubuntu.com/core/docs/preseeding) for more details.

### refresh

Snaps update automatically, and by default, the snapd daemon checks for updates 4 times a day. Each update check is called a _refresh_.

When, and how often, these updates occur can be modified with the snap command. Updates can be set to occur on Friday at midnight, for example, or for specific days of the month, such as only the third Monday, or even the last Friday of the month, between 23:00 to 01:00 the next day.

See [Managing updates](/how-to-guides/work-with-snaps/manage-updates) for further details.

### remote build

Remote build is a feature in [Snapcraft](https://snapcraft.io/docs/snapcraft-overview) (from  *[Snapcraft 3.9+](/t/snapcraft-release-notes)* onwards) that enables anyone to run a multi-architecture snap build process on remote servers using [Launchpad](https://launchpad.net/). With remote build, you can build snaps for hardware you don’t have access to and free up your local machine for other tasks.

See [Remote build](/) for further details.

### revision

A snap's *revision* is a number assigned by the [Snap Store](#heading--snap-store) automatically to give each snap a unique identity within and across its channels.

It's important to note that there is no real concept of higher or lower snap revisions and the current revision of the snap is simply the one that is released onto a channel.

The revision number is applied to the snap binary on upload to the Snap Store, and while it does increment with each new upload, it is only used to differentiate uploads.

The output to `snap info <snapname>` includes the revision for each snap in each track and channel as a number in brackets after the publishing date:

```
channels:
  latest/stable:    20.0.7snap1               2021-02-05 (26119) 286MB -
  latest/candidate: ↑
  latest/beta:      20.0.7snap1+git11.5aeea85 2021-03-06 (26711) 284MB -
  latest/edge:      master-2021-03-09         2021-03-09 (26758) 292MB -
  20/stable:        20.0.7snap1               2021-02-05 (26119) 286MB -
```

In the above example output, the latest/edge snap has a revision of `26758` and is the most recent published revision of the snap.

However, neither the revision number (nor its version) enforce an order of release. The local system will simply attempt to install whatever snap is recommended by the publisher in the channel being tracked.

See [Revisions](/explanation/how-snaps-work/revisions) for further details.

### seeding

When Ubuntu Core boots for the first time, the _seeding_ process installs an initial set of snaps and runs their respective hooks.

Each installed snap needs to be verified and have their respective AppArmor and seccomp security profiles, systemd units and mount points created. The time this takes is proportional to the number of asserted snaps being seeded but installing many snaps can impact first boot speed.

The seeding process runs quicker with [preseeding](https://ubuntu.com/core/docs/preseeding).

### series

In the domain of snaps, assertions and Ubuntu Core, the term _series_ is used to indicate a version of backwards compatible snap namespaces and assertion formats.

This can most obviously be seen in the output to _snap version_:

```
$ snap version
snap    2.52
snapd   2.52
series  16
ubuntu  20.04
kernel  5.13.0-31-generic
```

The above output shows that the installed package is compatible with other `series: 16` snap assertions and namespaces.

A snap series **is not correlated** to an Ubuntu series, such as _18_ for Ubuntu 18.04, or _20_ for Ubuntu 20.04, despite the numbers being the same or similar. This similarity is due to initial design considerations that have not yet been developed further, and the vast majority of snap series definitions simply take the value of _16_.

### snap

Snaps are app packages for desktop, cloud and IoT that are easy to install, secure, cross-platform and dependency-free, and _snap_ is both the command line interface and the application package format. The command is used to install and remove snaps and interact with the wider snap ecosystem.

See [Getting started](/tutorials/get-started) for more details.

### snapcraft

Snapcraft is both the command and the framework used to build your own snaps. The command and framework are cross-platform and can help you to easily build and publish your snaps to the [Snap Store](https://snapcraft.io/store)

See [Snapcraft overview](/) for more details.

### snapd

_snapd_ is the background service that manages and maintains your snaps.

Alongside its various service and management functions, snapd provides the _snap_ command, implements the confinement policies that isolate snaps from the base system and from each other, and governs the interfaces that allow snaps to access specific system resources outside of their confinement.

See [Snap documentation](https://snapcraft.io/docs) for more details.

### snappy

Snappy was the predecessor to [Ubuntu Core](#heading--ubuntu-core). The term is still occasionally used informally to refer to various aspects of the snap ecosystem, such as the command, the package format, the Snap Store and Ubuntu Core. It's best to avoid using this term; use *Snap* or *the Snap ecosystem* instead.

See [Snap documentation](https://snapcraft.io/docs) for general details about the snap ecosystem.

### snapshot

A  *snapshot*  is a copy of the user, system and configuration data stored by  *snapd*  for one or more snaps on your system.

Snapshots are generated manually with the  `snap save`  command and automatically when a snap is removed. A snapshot can be used to backup the state of your snaps, revert snaps to a previous state and to restore a fresh snapd installation to a previously saved state.

See [Snapshots](/how-to-guides/manage-snaps/create-data-snapshots) for further details.

### Snap Store

[Snap Store](https://snapcraft.io/store)  provides a place to upload your snaps, and for users to browse and install. It hosts thousands of snaps for millions of users on multiple architectures across 41 different Linux distributions.

See [snapcraft.io/store](https://snapcraft.io/store) for more details.

### spread

Spread is our open source testing utility that enables multiple shell scripts to run in parallel on many different systems in an entirely reproducible way. It currently runs a process that tests the snap ecosystem on real-world platforms 150,000 times a day.

See [https://github.com/canonical/spread](https://github.com/canonical/spread) for the project's code repository.

### strict

_Strict_ is the default snap confinement level. It runs snaps in complete isolation, and consequently, with no access your files, network, processes or any other system resource without requesting specific access via an interface.

See [Snap confinement](/explanation/security/snap-confinement) for more details.

### tracks

Tracks enable snap developers to publish multiple supported releases of their application under the same snap name. They are one of the levels of channel subdivision.

See [Tracks](/t/channels/551#heading--tracks) for more details.

### Transitional interface

A _transitional interface_ is an [interface](/how-to-guides/work-with-snaps/connect-interfaces) that can be used by a trusted snap to access traditional Linux desktop environments that were not designed to integrate with [snap confinement](/explanation/security/snap-confinement). These interfaces will become deprecated as replacement or modified technologies that enforce strong application isolation become available.

### Ubuntu Core

Ubuntu Core is Ubuntu for embedded devices and built using snaps. The operating system is read-only, and updates are transactional, with an absolute emphasis on maintaining a system’s integrity.

See our [Ubuntu Core](https://ubuntu.com/core/docs) documentation for more details.

### Version

The *version* of a snap is a string assigned to a project by its developers. You can see the version string assigned to a snap in the output from `snap info <snapname>` or `snap find`:

```
$ snap find nextcloud
Name          Version       Publisher   Notes  Summary
nextcloud     20.0.7snap1   nextcloud✓  -      A safe home for all your data
```

The version string typically reflects the general release version of a snap's primary application, but it can equally be any arbitrary value assigned by the snap creator.

The version string for the [Nextcloud snap](https://snapcraft.io/nextcloud) in its latest/stable channel, for example, tracks the version of the latest stable release, such as `20.0.7`. The version string for Nextcloud in its latest/edge channel represents its source code branch and build date, such as `master-2021-03-09`.

See [Getting started](https://forum.snapcraft.io/t/getting-started/3876) for more details.

