---
myst:
  html_meta:
    description: Explanatory and conceptual guides for snap packages - discussion and clarification of key topics for snap users and snap package developers, including how snaps work, interface connections, update management and security.
---

(explanation-how-snaps-work-index)=
# How snaps work

Understand how snaps update automatically, and use revisions and transactional updates to manage risk and mitigate potential issues.

* {ref}`Refresh awareness <explanation-how-snaps-work-refresh-awareness>`: How updates are handled when apps are running.
* {ref}`Using channels <explanation-how-snaps-work-channels-and-tracks>`: Understanding channels, tracks, risk-levels and branches.
* {ref}`Revisions <explanation-how-snaps-work-revisions>`: The unique identity for each and every snap version.
* {ref}`Transactional updates <explanation-how-snaps-work-transactional-updates>`: Update a group of snaps together, or none at all. 
* {ref}`Snap performance <explanation-how-snaps-work-snap-performance>`: How snaps limit any performance overhead.

```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

Channels and tracks <channels-and-tracks>
Home locations <home-outside-home>
Snap deltas <snap-deltas>
Snap revisions <revisions>
Snap components <snap-components>
Parallel installs <parallel-installs>
Refresh awareness <refresh-awareness>
Confdb <confdb-configuration-mechanism>
Validation sets <validation-sets>
Transactional updates <transactional-updates>
Hotplug support <hotplug-support>
Hotplug development <developing-hotplug-interfaces>
Snap performance <snap-performance>
Startup performance <debuging-startup-performance>
System snap <system-snap-directory>
