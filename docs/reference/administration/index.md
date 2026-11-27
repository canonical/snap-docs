---
myst:
  html_meta:
    description: Reference documentation for administering snaps across devices and environments, including system options, data locations, distribution support, and networks.
---

(reference-administration-index)=
# Administration

Deepen your understanding of how snaps can run on all kinds of devices, in all kinds of environments.

* {ref}`System options <reference-operations-system-options>`: Configurations options for the system and native snap devices.
* [Data locations]():
* {ref}`Distribution support <reference-administration-distribution-support>`: The status of current builds for Linux distributions with snap support.
* {ref}`Network requirements <reference-administration-network-requirements>`: What network access snaps require to operate correctly.
* {ref}`Timer string format <interfaces-timer-string-format>`: The string format to use whenever times, dates and durations are defined.

## Requesting permission

Snaps that require privileged access to resources need to go through a review step.

* {ref}`Store-reviews: process and criteria <interfaces-process-for-aliases-auto-connections-and-tracks>`: How to ask for permission reviews on your snaps.
* {ref}`Public, private and unlisted-snaps <interfaces-public-private-unlisted-snaps>`: The difference between the snaps everyone can see, and those limited to specific users.
* {ref}`Classic confinement guidelines <interfaces-reviewing-classic-confinement-snaps>`: When is classic confinement typically required and when it is not.

```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

System options <system-options>
Data locations <data-locations>
Distribution support <distribution-support>
Network requiremnts <network-requirements>
Timer string format <timer-string-format>
Store-reviews: process and criteria <process-for-aliases-auto-connections-and-tracks>
Public, Private and unlisted snaps <public-private-unlisted-snaps>
Classic confinement guidelines <reviewing-classic-confinement-snaps>
