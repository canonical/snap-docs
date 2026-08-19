(interfaces-process-for-aliases-auto-connections-and-tracks)=
# Process for aliases, auto-connections and tracks

## Definitions

- Reviewers are in the [@reviewers](https://forum.snapcraft.io/groups/reviewers) forum group
- Architects are those responsible for the design of snapd.
- Votes are in favor (+1), against (-1), abstain (+0)
- Voting period is one week
- Voting period extension is 3 days

## Process

1. Requester creates a forum post in [the relevant store-requests subcategory](https://forum.snapcraft.io/t/about-the-store-requests-category/10871), using the subcategory template to provide all the required details . Voting period starts at time of request.
2. Requester may not vote on his/her own snap.
3. Reviewers and/or architects vote using the voting procedure (see below). Each vote should include a short rationale for the cast vote (longer rationale is required for voting contrary to an established pattern)
4. If after voting period there are not enough votes based on voting procedure, a voting period extension should be requested by a reviewer/architect. The extension starts the day of the request for extension
5. At the end of the voting period, a reviewer/architects tallies the results from the voting period (and extension), summarizes in the forum post and performs any necessary actions.

## Voting procedure

- The voting procedure is the same for granting and revoking auto-connections, auto-aliases and track requests.
- If reviewers and up to at most one architect voted: simple majority with at least 2 votes in favor at end of voting period/extension: perform requested action. In the event of a tie, request more votes.
- If two or more votes in favor/against from architects: reviewers votes are not tallied. If have only in favor votes from architects at end of voting period/extension: perform requested action, otherwise architects discuss until no against votes and at least one vote in favor from architects. If clear direction from architects, an architect may request the vote be tallied early.

## alias request considerations
Granting aliases requires trust in the snap's publisher and reasonable names for the aliases (eg, shouldn't request an alias for something that is a widely known command of other software).

An alias should not be granted for the snap's name since snapd already grants use of this name to the snap (eg, a snap named 'foo' with command 'foo.foo2' should not be granted the 'foo' alias, instead, the snap can rename the 'foo2' command to be 'foo' instead (and optionally request an alias for the 'foo2' command)).

## auto-connection request considerations

In the snap ecosystem it is important to remember that there are several voices when considering auto-connection: snapd (base declaration policy), the gadget snap (for device-specific auto-connections, which does not apply to auto-connection requests), the store (snap declaration policy; ie, requests using this process) and the user.

For each snap interface, a determination is made for whether or not the interface should be manual or automatically connected based on a variety of criteria (the rationale is often in the snapd code base or pull requests) and this is codified in the base declaration.

A snap's publisher may request that a normally manually-connected interface be auto-connected for a particular snap in the global, public store using the process outlined in this topic (brand store owners may grant auto-connections as appropriate for their brand). Granting auto-connection in the global, public store effectually means that the store is vouching for the publisher's intent (maintenance, security updates, etc) and snap implementation (it does what it advertises, works well, etc) to the degree that the user's initial choice on connection at install time is removed (the user may of course disconnect the interface after installation).

Reviewers must therefore consider various criteria to inform their vote on whether the request will be granted. Some of this criteria might include:

* The "officialness" of the publisher of the snap
* The "reasonableness" of the request. Eg, a "top-like" program will necessarily need the "system-observe" interface but not "network-control"
* The snap name makes it clear that an interface should be auto-connected. Eg, a snap named "webcam" with it declaring the "camera" interface
* The software is intended to be used by children
* The sensitivity of the access relative to the "user's voice" (see above)

For some interfaces there are patterns and rationale that can generally be applied. Please note the rationale is subject to change based on security concerns from the community (users, publishers, reviewers, snapd developers, etc), more appropriate technologies becoming available, new information and/or critical thinking, etc. Each request will be reviewed on its own merits and prior granting of auto-connection may be rescinded based on this new information.

* alsa - auto-connection is generally limited to snaps requiring low-level, direct access to audio devices. 
    * Rationale: a lot of hardware does not perform multiplexing of clients so a snap directly accessing the hardware might block audio for other applications on some systems. Sound servers like pulseaudio are designed to multiplex audio and snaps should typically instead plugs the `audio-playback` (and `audio-record` if needed), which grants access to pulseaudio
    * Reference: https://snapcraft.io/docs/reference/interfaces/alsa-interface/
* content - the base declaration defines that snaps that plugs the content interface will auto-connect with other snaps from the same publisher. Global auto-connect for content providers is allowed only under certain circumstances
    * Rationale: because there is no tight coupling or dependency graphs between the provider and the consumer, there are no guarantees that a providing snap cannot break consuming snaps. Publishers are expected to manage breaking changes with their snaps, but are not generally expected to be concerned about others' snaps
    * Reference:
        * https://forum.snapcraft.io/t/auto-connection-for-gnome-3-24-content-interface/1379/51
        * https://forum.snapcraft.io/t/allow-global-autoconnect-kde-frameworks-5-qt-5-14-core18/16335/4
* content for theme snaps - in addition to the above considerations, eventually snapd might suggest or auto-install theme snaps based on various criteria. Until review-tools checks are fully in place, if a publisher requests global auto-connection with greedy plugs, reviewers should:
    * ensure the snap only slots the agreed to content identifiers (ie, `content` attribute or interface reference if `content` attribute is omitted)
    * ensure the snap ships only (valid) content files (eg, css, images, audio files, etc)
    * ensure the theme snap does not ship any commands, daemon or hooks
    * vet the publisher (part of vetting shall include an agreement to agree to adhering to the above going forward)
    * Reference:
        * https://forum.snapcraft.io/t/auto-connect-custom-gtk-themes-to-gtk-3-themes-gtk-2-themes-and-icon-themes/17354/3
        * https://forum.snapcraft.io/t/auto-connect-and-greedy-plug-behaviour-for-for-gtk-common-themes-and-gtk-theme-traditionalhumanized-snaps/19113/6
* cups-control - auto-connection is limited to snaps whose core functionality is printing or design programs where printing is an expected part of the workflow. Granting requires a stated commitment from the developer that moving to a safer API will be performed (such as the Printing portal) when it is widely available
    * Rationale: cups-control unfortunately grants access to the CUPS socket which on a typical single user system, grants admin privileges for printer configuration, which is more than the intended permission to allow printing
    * Reference:
        * https://forum.snapcraft.io/t/inkscape-autoconnect-cups-control/8739/39 (initial)
        * https://forum.snapcraft.io/t/inkscape-autoconnect-cups-control/8739/40 (revisited)
* joystick - auto-connection generally limited to game snaps
* mpris - slot side is generally granted provided the `name` attribute makes sense for the snap. auto-connection of plugs is typically not auto-connected [unless the slot's publisher also agrees](https://forum.snapcraft.io/t/auto-connect-request-for-lyricfier/15533/18)
* password-manager-service - typically not auto-connected due to the sensitive nature of the access and because the user's voice in this access is so important
    * Rationale: the various keyring services do not provide sufficient isolation for snap access to the interface to be auto-connected by default. Not only can the snap see all stored passwords, but all other applications with access to the password services can also see the snap's passwords. 
    * Reference: https://forum.snapcraft.io/t/nordpass-auto-connect-to-password-manager-service-interface/14968/5
 * removable-media: typically not auto-connected since the optional access to widely varied data does not outweigh the user's voice regarding potentially sensitive data. Certain classes of applications may be granted an exception under certain circumstances.
    * Rationale: by definition data that is not always present (as is the case with removable-media) is optional access for typical snaps. All snaps with this interface connected have unrestricted access to all data from any plugged media. Considering that removable-media may contain sensitive documents, sensitive pictures/media, encryption keys, etc and that snapd has no insight on the nature of the data, the user's voice with regard to connection is preserved
    * Exceptions: the following classes of applications may be considered for removable-media auto-connection:
        * major browsers and email clients (rationale: the software is designed with security and user privacy in mind)
        * media (eg, sound, photo, video) editors (rationale: the software is very often used to import/edit/export large files on external devices)
        * media (eg, sound, photo, video) players/viewers (rationale: the software is very often used to import/preview/playback files on external devices)
        * media (eg, sound, photo, video) recorders/cameras (rationale: the software is very often used to export/edit files on external devices)

        If the application falls into one of the above categories, then the following criteria will also be considered:
        * the application itself is a mature, well-known application
        * the snap's (vetted) publisher is a mature, well-known entity
        * the snap's (vetted) publisher is the upstream of the software
        * if the snap is published by someone other than upstream, the publisher must be vetted and either be an established committer to the upstream or the wider snap ecosystem (eg, an established well-known contributor to the software itself, a member of the snapcrafters group, etc)
            *  if the publisher doesn't meet these criteria, other options may or may not be considered such as the publisher joining snapcrafters, snapcrafters becoming a collaborator on the snap, auto-connection granted conditional on the snap packaging being accepted upstream, upstream stating they trust the publisher with the packaging, etc.
    * Additional information:
        * The removable-media interface is considered a 'transitional' interface since, when connected, only traditional UNIX permissions are considered for file access. This allows, for example, a service in a snap to setup inotify/etc to programmatically monitor and exfiltrate/modify files on external media in the background
        * Eventually, applications will either use safer APIs for file access (eg, like portals) or future snapd-prompting mechanisms may be available to obviate the need for auto-connecting this interface
        * Security-conscious users may want to remove sensitive external media when installing snaps, then disconnect the interface from those snaps to prevent them from having access
        * In the future, snapd may grow controls to disable certain interface auto-connections for interfaces like removable-media
* uinput: typically not auto-connected because it allows injecting arbitrary input into the system. In addition, due to popular hardware/software instructions outside of the snap ecosystem, `/dev/uinput` may be world read and writable (default udev rules create it as root-owned with only root read and writable). Due to these considerations, publishers requesting use of (and especially auto-connect) should be vetted.

### Manual connection mitigations

If auto-connection is not granted, options for snap publishers are:
* have the snap check if the interface is connected via `snapctl is-connected <iface>` and instruct the user to use the `snap connect` CLI command or connect via the snap-store/gnome-software GUI. This could be done on startup or contextually at the time of access. Ideally when instructing the user, the details of the access would be explained so the user can make an informed choice. It is true that there is an extra step for the user, but done well, this need not be onerous and may even provide additional trust that your snap and the system as a whole are working to keep everything secure. Note, if using `snapctl is-connected` you should also add a corresponding `assumes: 2.43` to your snapcraft.yaml since this is only available in snap since 2.43 to ensure this [functions as expected](https://forum.snapcraft.io/t/interfaces-for-raspberry-pi-imager/15822/20).
* use a newer, safer API. Eg, instead of using cups-control, the application could use [the Printing portal](https://forum.snapcraft.io/t/inkscape-autoconnect-cups-control/8739/52). If an application needs access to a file from a disconnected interface/etc, use a file dialog that supports [portals](https://snapcraft.io/docs/explanation/snap-development/xdg-desktop-portals/)
* fallback gracefully. Eg, if password-manager-service is disconnected, fallback to storing passwords locally

In the future, the snapd team plans to provide a [prompt API for snaps to use ](https://forum.snapcraft.io/t/inkscape-autoconnect-cups-control/8739/39) that will not only provide appropriate messaging, but also allow the user to choose to connect within the prompt.

Finally, the desktop team has discussed the lack of isolation in secret-service with upstream GNOME and there are plans to [improve the service](https://wiki.gnome.org/Projects/GnomeKeyring/SecurityPhilosophy) (see 'Active Attacks') to provide the necessary isolation for auto-connecting. Hopefully, KDE/Plasma will follow with kwallet or move to the improved service.

### Tracks

There is a [simplified process for tracks for snaps with predictable cadence](https://forum.snapcraft.io/t/simplified-track-request-process-for-snaps-with-predictable-cadence/3136).

