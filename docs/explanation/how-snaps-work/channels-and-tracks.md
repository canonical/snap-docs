(explanation-how-snaps-work-channels-and-tracks)=
# Channels and tracks

Channels are an important snap concept. They define which release of a snap is installed and tracked for updates.

A channel consists of, and is subdivided by, tracks, risk-levels and branches:

- [Tracks](#heading--tracks) enable snap developers to publish multiple supported releases of their application under the same snap name.
- [Risk-levels](#heading--risk-levels) represent a progressive potential trade-off between stability and new features.
- [Branches](#heading--branches) are optional and hold temporary releases intended to help with bug-fixing.

The complete channel name can be structured as three distinct parts separated by slashes:

```
<track>/<risk>/<branch>
```

The _tracking_ value for an installed snap, as shown in the output from the `snap list` command, shows which channel is installed and is being followed for that snap.

To view the channel a snap is tracking, the following command may also be used:

```
snap refresh --tracking vlc
```

## Tracks

All snaps have a default track. Without the snap developer specifying otherwise, the default track is called *latest*. Similarly, when no track is specified, a snap will implicitly install from the *latest* track. The track can also be specified explicitly:

```
snap install vlc --channel=latest/edge
```

Developers can optionally choose whether to supplement the default _latest_ track with additional tracks. The developer is also free to designate one of these as the default track to be installed when no further preference is given.

Microsoft's [Skype snap](https://snapcraft.io/skype) is a good example of how tracks can be used. It contains two tracks: the default _latest_ track for the majority of users, and an  _insider_ track for Microsoft's QA team and users interested in testing the latest Skype developments ahead of a stable release.

Equally, a track could also be used to track minor updates (2.0.1, 2.0.2), major updates (2.1, 2.2), or releases held for long-term support (3.2, 4.1).

Tracks are listed in the *channels* section of the output from the `snap info` command:

```
$ snap info skype
[...]
channels:                                  
  stable:            8.28.0.41  (51) 148MB classic
  candidate:         ↑                     
  beta:              ↑                     
  edge:              ↑                     
  insider/stable:    8.30.76.41 (53) 151MB classic
  insider/candidate: ↑                     
  insider/beta:      ↑                     
  insider/edge:      ↑  
[...]
```

In the above output, the [Skype](https://snapcraft.io/skype) snap includes the custom *insider* track. You can also see which tracks a snap supports by clicking *Other versions* from its online Store entry.

To install Skype from its *insider* track, for example, use the following
command:

```
snap install skype --channel=insider/stable
```

A user who already has Skype installed can switch channel with the ``snap refresh`` command:

```
snap refresh skype --channel=insider/stable
```

Alternatively if using GNOME Software, select the ‘stable’ channel in the store page for Skype, and select a channel to switch to.

Developers must currently make a request for tracks to be added to their snap via the [#store-requests](https://forum.snapcraft.io/c/store-requests) forum category. Releases are verified and checked to ensure that reasonable user expectations are being  met. For example, only _3.2.*_ versions are accepted into a _3.2_ track.

## Risk-levels

There are four risk-levels: stable, candidate, beta and edge. These represent decreasing levels of stability for a snap, although that decision is ultimately up to the snap's publisher. 

Installing from a less stable risk-level will typically mean that updates for a snap will be more frequent than for a more stable risk-level.

The risk-levels have the following meaning:

- **stable**:  for the vast majority of users running on production environments.

    Releases at this risk level are as stable as they will ever get, according to the project's standards. Important software will only reach this stage once it’s ready for production use and may be used in products. There is an implied promise to avoid any changes that would disrupt those usages.

- **candidate**: for users who need to test updates prior to stable deployment, or those verifying whether a specific issue has been resolved.

   Candidate releases are considered almost ready for going into stable, but     need some additional real world experimentation before they move forward. Software reaching this stage will typically have passed all available QA and review processes, since users following it expect a high stability level. Should almost never break.

- **beta**: for users wanting to test the latest features, typically outside of a production environment.

   Beta is the first level towards the stabilisation of what was before a fast moving stream of changes. Specific projects may have slightly different terminology for such releases (alpha, beta, etc) but all of these are welcome on this risk level. These releases will almost certainly have passed some sort of review and QA, but may still have unfinished parts. Breaking changes are still relatively common here.

- **edge**:  for users wanting to closely track development.

    Edge releases often include a moving stream of changes without QA or review promises and are typically built automatically by a CI process from an arbitrary source code snapshot. Often the CI will only publish after some sort of automatic QA passed, and code reviews remain a good practice, but these are project specific. Assume edge releases may break often.

Snaps are installed from the stable risk-level by default. For example, the following command installs VLC from its stable channel:

```
sudo snap install vlc
```

Use the `--channel` option to select a different risk-level. The following command will install the latest beta snap of VLC:

```
sudo snap install --channel=beta vlc
```

If the beta snap is not available, a snap will be installed from the closest
channel with a more stable risk-level.

> ⓘ For brevity,  `--stable`, `--candidate`, `--beta` and `--edge` can be used instead of `--channel=<risk-level>`

After installation, the risk-level being tracked can be changed with the use of the ``switch`` command option:

```
sudo snap switch --channel=stable vlc
```

This option will not automatically refresh the snap to force the installation
of a new snap. To switch channels and update the snap with a single command, add the `--channel` option to the *refresh* command:

```
sudo snap refresh --channel=stable vlc
```

To check which channel a snap is tracking, look for the *tracking* field in the output from the `snap info` command:

```
$ snap info vlc
[...]
snap-id:      RT9mcUhVsRYrDLG8qnvGiy26NKvv6Qkd
tracking:     edge
refresh-date: yesterday at 19:54 BST
[...]
```

Risk-levels may not match a project's internal conventions. Some projects may use *alpha* instead of *edge*, for instance. However, a project's own release nomenclature should be close enough to a snap's risk-levels to allow you to judge the relative stability of the version you're installing.

## Branches

A branch is an optional, fine-grained subdivision of a channel for a published snap that allows for the creation of short-lived sequences of snaps that can be pushed on demand by snap developers to help with fixes or temporary experimentation.

Branch names convey their purpose, such as `fix-for-bug123`, but the name isn't exposed in the normal way, such as with the `snap info` command. Instead, they can only be installed by someone who knows the branch name, and this is usually only shared by the snap developer to test a specific fix or release.

After 30 days with no further updates, a branch will be closed automatically. The replacement snap will then be chosen as it would be with closed channels (see below). For example, *beta/fix-for-bug123* will fall back to *beta* after the *fix-for-bug123* branch is closed.

See Snapcraft's [Manage revisions and releases](https://documentation.ubuntu.com/snapcraft/stable/how-to/publishing/manage-revisions-and-releases/) for more details on how snap developers can use branches to publish temporary snap releases.

## Closing channels

A channel can be closed by a snap publisher when there is no longer a snap that fits a channel's original purpose or specification. 

For example, when a specific risk-level channel is closed, the snap store will select a snap from a more stable risk-level of the same track. If the original channel is re-opened, snaps will once again be selected from the original channel.

This approach is commonly used for beta testing. If a snap is following a *beta* channel that is then closed, the store will offer the snap from the *candidate* channel. If the *candidate* channel is not available, the snap from the *stable* channel will be selected. If the *beta* channel re-opens, the snap will once again be selected from that channel.

In some cases, when a specific revision is given, it may appear that a snap is being installed from a less stable channel when a revision is not available on the  more stable channel being tracked:

```
$ snap install hello-world --revision=28
hello-world (edge) 6.3 from Canonical✓ installed
Channel latest/stable for hello-world is closed; temporarily forwarding to edge.
```
This does not mean that the snap is now being tracked from a potentially riskier channel (_edge_, in the above example), but that the requested revision could only fetched from a riskier channel:

```
$ snapcraft list-revisions hello-world
Rev.    Uploaded              Arches    Version    Channels
29      2019-04-17T16:43:58Z  all       6.4        latest/beta*,latest/candidate*,latest/edge*,latest/stable*
28      2017-11-20T07:59:46Z  all       6.3        latest/edge
27      2016-07-12T16:37:23Z  all       6.3        latest/beta,latest/candidate,latest/edge,latest/stable
26      2016-05-31T07:02:32Z  all       6.1        latest/edge,latest/stable
24      2016-04-19T15:37:06Z  all       6          latest/beta,latest/candidate,latest/edge,latest/stable
```

