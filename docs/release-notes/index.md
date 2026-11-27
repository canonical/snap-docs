---
myst:
  html_meta:
    description: Snapd release notes. Review new features, bug fixes, and changes across recent stable, beta, and earlier Snapd releases.
---

(reference-release-notes)=
# Release notes

This page lists the release notes of all recent versions of Snapd, summarising new features, bug fixes and changes in each version.

## Latest stable release

**{ref}`Snapd 2.78 <release-notes_snapd-2-78>`** (3 November 2026)

## Next planned release

**Snapd 2.79**

Content targeting this release must be ready by 16 October 2026.

This release was delayed because Snapd was updated to the core26 base. That base inherited [Resolute's s390x jump to z15](https://bugs.launchpad.net/ubuntu-z-systems/+bug/2126577), which breaks Snapd support for s390x z13. As a temporary solution, we are dropping Snapd's move to the core26 base while we work on a solution. The beta and candidate dates have moved. The stable date is unchanged.

| Milestone | Status | Date |
|---|---|---|
| Beta | Pending | 17 November 2026 |
| Candidate | Pending | 26 November 2026 |
| Stable | Pending | 6 January 2027 |

## Release policy and schedule

Snapd updates automatically and, by default, checks for updates 4 times a day. To manually update or modify this process, see {ref}`Managing updates <how-to-guides-work-with-snaps-manage-updates>`.

{ref}`Channels <explanation-how-snaps-work-channels-and-tracks>` are used to distinguish between stable releases, which are always available from the stable channel, and beta and testing releases, which can be installed from the candidate, beta and edge channels.

To install the snapd snap from the beta channel, for example, use the following command:

```
sudo snap refresh snapd --beta
```

To ensure you receive latest security updates and bug fixes, ensure you upgrade to a new release of Snapd shortly after it is released.

Feel free to provide your test feedback on the [forum](https://forum.snapcraft.io/c/snapd/5), or directly in [Launchpad](https://bugs.launchpad.net/snapd/+filebug).

We greatly appreciate your contributions and support!


## Older releases

* {ref}`Snapd 2.77 <release-notes_snapd-2-77>`
* {ref}`Snapd 2.76 <release-notes_snapd-2-76>`
* {ref}`Snapd 2.75 <release-notes_snapd-2-75>`
* {ref}`Snapd 2.74 <release-notes_snapd-2-74>`
* {ref}`Snapd 2.73 <release-notes_snapd-2-73>`
* {ref}`Snapd 2.72 <release-notes_snapd-2-72>`
* {ref}`Snapd 2.71 <release-notes_snapd-2-71>`
* {ref}`Snapd 2.70 <release-notes_snapd-2-70>`
* {ref}`Snapd 2.69 <release-notes_snapd-2-69>` (not released; superseded by Snapd 2.70)
* {ref}`Snapd 2.68 <release-notes_snapd-2-68>`
* {ref}`Snapd 2.67 <release-notes_snapd-2-67>`
* {ref}`Snapd 2.66 <release-notes_snapd-2-66>`
* {ref}`Snapd 2.65 <release-notes_snapd-2-65>`
* {ref}`Snapd 2.64 <release-notes_snapd-2-64>`
* {ref}`Snapd 2.63 <release-notes_snapd-2-63>`
* {ref}`Snapd 2.62 <release-notes_snapd-2-62>`
* {ref}`Snapd 2.61 <release-notes_snapd-2-61>`
* {ref}`Snapd 2.60.3 <release-notes_snapd-2-60-3>`
* {ref}`Snapd 2.59 <release-notes_snapd-2-59>`
* {ref}`Snapd 2.58 <release-notes_snapd-2-58>`
* {ref}`Snapd 2.56 <release-notes_snapd-2-56>`
* {ref}`Snapd 2.55 <release-notes_snapd-2-55>`
* {ref}`Snapd 2.54.2 <release-notes_snapd-2-54-2>`
* {ref}`Snapd 2.51 <release-notes_snapd-2-51>`
* {ref}`Snapd 2.50 <release-notes_snapd-2-50>`
* {ref}`Snapd 2.49 <release-notes_snapd-2-49>`
* {ref}`Snapd 2.48 <release-notes_snapd-2-48>`
* {ref}`Snapd 2.47 <release-notes_snapd-2-47>`
* {ref}`Snapd 2.46 <release-notes_snapd-2-46>`
* {ref}`Snapd 2.45 <release-notes_snapd-2-45>`
* {ref}`Snapd 2.44 <release-notes_snapd-2-44>`
* {ref}`Snapd 2.43 <release-notes_snapd-2-43>`
* {ref}`Snapd 2.42 <release-notes_snapd-2-42>`
* {ref}`Snapd 2.34.3 <release-notes_snapd-2-34-3>`
* {ref}`Snapd 2.33 <release-notes_snapd-2-33>`
* {ref}`Snapd 2.32 <release-notes_snapd-2-32>`
* {ref}`Snapd 2.30 <release-notes_snapd-2-30>`
* {ref}`Snapd 2.28 <release-notes_snapd-2-28>`
* {ref}`Snapd 2.27 <release-notes_snapd-2-27>`
* {ref}`Snapd 2.24 <release-notes_snapd-2-24>`
* {ref}`Snapd 2.23.6 <release-notes_snapd-2-23-6>`


```{toctree}
:hidden:
:titlesonly:

snapd-2-78
snapd-2-77
snapd-2-76
snapd-2-75
snapd-2-74
snapd-2-73
snapd-2-72
snapd-2-71
snapd-2-70
snapd-2-69
snapd-2-68
snapd-2-67
snapd-2-66
snapd-2-65
snapd-2-64
snapd-2-63
snapd-2-62
snapd-2-61
snapd-2-60.3
snapd-2-59
snapd-2-58
snapd-2-56
snapd-2-55
snapd-2-54.2
snapd-2-51
snapd-2-50
snapd-2-49
snapd-2-48
snapd-2-47
snapd-2-46
snapd-2-45
snapd-2-44
snapd-2-43
snapd-2-42
snapd-2-34.3
snapd-2-33
snapd-2-32
snapd-2-30
snapd-2-28
snapd-2-27
snapd-2-24
snapd-2-23.6
```
