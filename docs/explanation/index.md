---
myst:
  html_meta:
    description: Explanatory and conceptual guides for snap packages - discussion and clarification of key topics for snap users and snap package developers, including how snaps work, interface connections, update management and security.
---

(explanation-index)=
# Explanation

Our explanatory and conceptual guides are written to provide a better understanding of how snap and the snap daemon (_snapd_) work. They enable you to expand your knowledge and become better at both building snaps and getting the most out of the snap ecosystem.

## How snaps work

Understand how snaps update automatically, and use revisions and transactional updates to manage risk and mitigate potential issues.

* {ref}`Refresh awareness <explanation-how-snaps-work-refresh-awareness>`: How updates are handled when apps are running.
* {ref}`Using channels <explanation-how-snaps-work-channels-and-tracks>`: Understanding channels, tracks, risk-levels and branches.
* {ref}`Revisions <explanation-how-snaps-work-revisions>`: The unique identity for each and every snap version.
* {ref}`Transactional updates <explanation-how-snaps-work-transactional-updates>`: Update a group of snaps together, or none at all. 
* {ref}`Snap performance <explanation-how-snaps-work-snap-performance>`: How snaps limit any performance overhead.

## Interfaces

As you begin to use snaps more, interfaces can be used to carefully permit and limit access to resources.

* {ref}`All about interfaces <explanation-interfaces-all-about-interfaces>`: The permission system used to manage access to resources.
* {ref}`Interface auto-connection <explanation-interfaces-interface-auto-connection>`: How snaps gain automatic access to resources.
* {ref}`Interface hooks <explanation-interfaces-interface-hooks>`: A feature to help developers control what happens when an interface is used.

## Security

Learn about how snaps use standard Linux security policies to isolate themselves from the system, and from each other.

* {ref}`Security policies <explanation-security-security-policies>`: How we use AppArmor, Seccomp and cgroups to secure snaps.
* {ref}`Snap confinement <explanation-security-snap-confinement>`: Learn more about Snap's various degrees of isolation.
* {ref}`Assertions <explanation-security-assertions>`: Digitally signed documents used to verify all snap artefacts.
* {ref}`Snapd release process <explanation-security-snapd-release-process>`: How and when we update the snapd package.


```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

How snaps work <how-snaps-work/index>
Interfaces <interfaces/index>
Security <security/index>
Snap development <snap-development/index>
