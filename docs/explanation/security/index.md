---
myst:
  html_meta:
    description: Learn about how snaps use standard Linux security policies to isolate themselves from the system, and from each other. Understand snap confinement, security policies and the snapd release process.
---

(explanation-security-index)=
# Security

Learn about how snaps use standard Linux security policies to isolate themselves from the system, and from each other.

* {ref}`Security policies <explanation-security-security-policies>`: How we use AppArmor, Seccomp and cgroups to secure snaps.
* {ref}`Assertions <explanation-security-assertions>`: Digitally signed documents used to verify all snap artefacts.
* {ref}`Snap confinement <explanation-security-snap-confinement>`: Learn more about snap's various degrees of isolation.
* {ref}`Classic confinement <explanation-security-classic-confinement>`: Learn more about classic confinement.
* {ref}`API authentication and authorization <explanation-security-api-authentication-and-authorization>`: How snapd authenticates API callers and authorizes operations.
* {ref}`Decommissioning <explanation-security-decommissioning>`: How to completely remove snapd and associated data.
* {ref}`Snapd release process <explanation-security-snapd-release-process>`: How and when we update the snapd package.


```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

Security policies <security-policies>
Assertions <assertions>
Snap confinement <snap-confinement>
Classic confinement <classic-confinement>
API authentication and authorization <api-authentication-and-authorization>
Decommissioning <decommissioning>
Release process <snapd-release-process>
