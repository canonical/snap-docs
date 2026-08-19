---
myst:
  html_meta:
    description: Deepen your understanding of how snaps can run on all kinds of devices, in all kinds of environments. Learn about system options, data locations, distribution support, network requirements and more for snap users and snap package developers.
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

* {ref}`Process for aliases, auto-connections and tracks <interfaces-process-for-aliases-auto-connections-and-tracks>`: How to ask for permission reviews on your snaps.
* {ref}`Public, private and unlisted-snaps <interfaces-public-private-unlisted-snaps>`: The difference between the snaps everyone can see, and those limited to specific users.
* {ref}`Reviewing classic confinement snaps <interfaces-reviewing-classic-confinement-snaps>`: How classic confinement permissions are granted.

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
Request aliases, tracks and connections <process-for-aliases-auto-connections-and-tracks>
Public, Private and unlisted snaps <public-private-unlisted-snaps>
Reviewing classic confinement <reviewing-classic-confinement-snaps>
