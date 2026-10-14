---
myst:
  html_meta:
    description: Official documentation for snap packages and snapd, covering installation, configuration, security, updates, and snap development.
    google-site-verification: "ptZ-UgCb6UjBHQ60paTDvhjC36oELGPKMvOxpEJJv4g"
    google-site-verification: "BMa0gPz8blugX1MVoyh9Xn4OFqDZzrmFrcU0dyKGJjE"
---

(ref-index_snap-documentation)=
# Snap documentation

**Snaps** are self-contained application packages that work across different Linux distributions on many different platforms, from embedded devices and desktops, to servers and the cloud.

The snap daemon, *snapd*, handles installation, confinement, and updates, allowing developers to focus on their applications while users get a consistent experience across platforms.

Snap packages and snapd solve the problem of inconsistent application packaging and deployment by providing a unified system that works the same way regardless of the underlying Linux distribution or hardware.

Snaps are useful for application developers seeking a universal packaging solution, system administrators managing diverse Linux environments, IoT and embedded device makers, and organizations where security and consistent deployments are priorities.

For guidance on building snaps, see the [Snapcraft build-tool documentation](https://documentation.ubuntu.com/snapcraft/stable/).

## In this documentation

### First steps

Get snap running and take a tour of its core features before diving deeper.

* **Install snapd**: {ref}`Install the snap daemon <tutorials-install-the-daemon-index>` • {ref}`Distribution support <reference-administration-distribution-support>`
* **Explore snap**: {ref}`Get started <tutorials-get-started>` with snap's main features on a single page

### Managing snaps

Install, configure, and maintain snaps day-to-day. Control updates, interfaces, services, and data.

* **Configuration**: {ref}`Configure snaps <how-to-guides-work-with-snaps-configure-snaps>` • {ref}`Apps and aliases <how-to-guides-work-with-snaps-apps-and-aliases>` • {ref}`Set system options <how-to-guides-manage-snaps-set-system-options>` • {ref}`Configure snaps with confdb <how-to-guides-manage-snaps-configure-snaps-with-confdb>`
* **Updates**: {ref}`Manage updates <how-to-guides-work-with-snaps-manage-updates>` • {ref}`Manage validation sets <how-to-guides-manage-snaps-manage-validation-sets>`
* **Services and resources**: {ref}`Control services <how-to-guides-manage-snaps-control-services>` • {ref}`Use quota resources <how-to-guides-manage-snaps-use-resource-quotas>` • {ref}`Create data snapshots <how-to-guides-manage-snaps-create-data-snapshots>` • {ref}`Disk space awareness <how-to-guides-manage-snaps-disk-space-awareness>` • {ref}`Data locations <interfaces-data-locations>`  • {ref}`Work with components <how-to-guides-manage-snaps-using-components>`
* **Troubleshooting**: {ref}`Fix common issues <how-to-guides-fix-common-issues-index>`

### Security and confinement

Understand how snaps use Linux security technologies to isolate applications and protect your system.

* **Confinement**: {ref}`Snap confinement <explanation-security-snap-confinement>` • {ref}`Classic confinement <explanation-security-classic-confinement>` • {ref}`Security policies <explanation-security-security-policies>`
* **Interfaces**: {ref}`All about interfaces <explanation-interfaces-all-about-interfaces>` • {ref}`Interface auto-connection <explanation-interfaces-interface-auto-connection>` • {ref}`Interface hooks <explanation-interfaces-interface-hooks>` • {ref}`Super-privileged interfaces <reference-operations-interfaces-super-privileged-interfaces>` • {ref}`Connect interfaces <how-to-guides-work-with-snaps-connect-interfaces>` • {ref}`Interface reference <ref-index_interfaces>`
* **Verification**: {ref}`Assertions <explanation-security-assertions>` • {ref}`Snapd release process <explanation-security-snapd-release-process>`

### Snap development

For guidance on building snaps, see the [Snapcraft build-tool documentation](https://documentation.ubuntu.com/snapcraft/stable/).

Extend snap functionality using the REST API, internal tooling, and in-development features.

* **APIs and tools**: {ref}`REST API <how-to-guides-manage-snaps-use-the-rest-api>` • {ref}`Use snapctl <how-to-guides-manage-snaps-use-snapctl>` • {ref}`Environment variables <reference-development-environment-variables>` • {ref}`Supported snap hooks <reference-development-supported-snap-hooks>` • {ref}`API authentication and authorization <explanation-security-api-authentication-and-authorization>`
* **Publishing**: {ref}`Public, private and unlisted snaps <interfaces-public-private-unlisted-snaps>`
* **Desktop integration**: {ref}`XDG desktop portals <interfaces-xdg-desktop-portals>`
* **Testing**: {ref}`Using snap try <interfaces-snap-try>` • {ref}`Install modes <interfaces-install-modes>` • {ref}`Debug snaps <how-to-guides-fix-common-issues-debug-snaps>` • {ref}`Test snapd fixes <how-to-guides-fix-common-issues-test-snapd-fixes>` • {ref}`In-development features <ref-experimental-features_experimental-features>`
* **YAML schemas**: {ref}`The snap.yaml <reference-development-yaml-schemas-the-snap-format>` • {ref}`Gadget snap <reference-development-yaml-schemas-the-gadget-snap>` • {ref}`Kernel snap <reference-development-yaml-schemas-the-kernel-snap>`

### System internals

Understand how the snap system works: updates, channels, confinement, storage, and performance.

* **Updates and versions**: {ref}`Refresh awareness <explanation-how-snaps-work-refresh-awareness>` • {ref}`Channels and tracks <explanation-how-snaps-work-channels-and-tracks>` • {ref}`Revisions <explanation-how-snaps-work-revisions>` • {ref}`Transactional updates <explanation-how-snaps-work-transactional-updates>` • {ref}`Snap deltas <how-to-guides-manage-snaps-snap-deltas>`
* **Components and configuration**: {ref}`Snap components <explanation-how-snaps-work-snap-components>` • {ref}`Confdb configuration mechanism <explanation-how-snaps-work-confdb-configuration-mechanism>` • {ref}`Parallel installs <interfaces-parallel-installs>` • {ref}`Network requirements <reference-administration-network-requirements>` • {ref}`Timer string format <interfaces-timer-string-format>`
* **Performance**: {ref}`Snap performance <explanation-how-snaps-work-snap-performance>` • {ref}`System architecture <reference-operations-system-architecture>`

## How this documentation is organised

This documentation uses the [Diátaxis documentation structure](https://diataxis.fr/).

* {ref}`Tutorials <tutorials-index>` take you step-by-step through building and deploying your first Ubuntu Core image.
* {ref}`How-to guides <how-to-guides-index>` provide instructions for specific tasks like customizing snaps, deploying to platforms, and managing devices.
* {ref}`Reference <reference-index>` provides technical specifications, formats, and details you need while working.
* {ref}`Explanation <explanation-index>` provides conceptual context about architecture, security, storage, and update mechanisms.

## Project and community

Snap and Snapcraft are members of the Ubuntu family. They're both open source projects that welcome community involvement, contributions, suggestions, fixes and constructive feedback.

* [Our Code of Conduct](https://ubuntu.com/community/code-of-conduct)
* [Get support](https://forum.snapcraft.io/c/snap/14)
* [Join the Discourse forum](https://forum.snapcraft.io/)
* [Interactive chat on Matrix.org](https://matrix.to/#/#snapd:ubuntu.com)
* {ref}`Contribute to our documentation <contribute-to-our-docs>`
* [Project roadmap](https://forum.snapcraft.io/t/the-snapd-roadmap/1973)

Thinking about using snap for your next project? [Get in touch!](https://forum.snapcraft.io/)

```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

Tutorials <tutorials/index>
How-to guides <how-to-guides/index>
Reference <reference/index>
Explanation <explanation/index>
```

```{toctree}
:hidden:
:maxdepth: 2

Contributing <contributing/index.md>
```