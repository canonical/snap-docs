---
myst:
  html_meta:
    description: Step-by-step guides on how to manage snap packages - control when snaps update, connect interfaces, set system options, control services and more for snap users and snap package developers.
---

(how-to-guides-manage-snaps-index)=
# Manage snaps

Outside of whatever facilities a snapped application may provide, additional snap functionality includes  data snapshots, usage quotas and control over if and when a service runs.

## System configuration

The snap system has been designed to look after itself with automatic security and update policies. However, these elements, and many others, can also be configured and managed manually.

- {ref}`Connect interfaces <how-to-guides-work-with-snaps-connect-interfaces>`: Control exactly what a snap can access, and what it can’t.
- {ref}`Manage updates <how-to-guides-work-with-snaps-manage-updates>`: Control when snaps update, or hold an update indefinitely .
- {ref}`Configure snaps <how-to-guides-work-with-snaps-configure-snaps>`: Learn how to set options for your servers and daemons.
- {ref}`Configure the system <how-to-guides-manage-snaps-set-system-options>`: The main way to configure your snapped applications.
- {ref}`Apps and aliases <how-to-guides-work-with-snaps-apps-and-aliases>`: Use your preferred names for your snapped applications.
- {ref}`Control services <how-to-guides-manage-snaps-control-services>`: Start, stop and restart snapped background service.
- {ref}`Validation sets <how-to-guides-manage-snaps-manage-validation-sets>`: Ensure a defined set of snaps are installed and updated together.

- {ref}`Fix common issues <how-to-guides-fix-common-issues-index>`: If you do run into problems, find common solutions here.

## Storage
- {ref}`Create data snapshots <how-to-guides-manage-snaps-create-data-snapshots>`: Make a copy of a snap’s user, system and configuration data.
- {ref}`Use quota resources <how-to-guides-manage-snaps-use-resource-quotas>`: Set processor and memory resource limits on your snaps.
- {ref}`Disk space awareness <how-to-guides-manage-snaps-disk-space-awareness>`: Check whether there’s enough disk space before certain operations.


```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

Connect interfaces <connect-interfaces>
Manage updates <manage-updates>
Configure snaps <configure-snaps>
Configure the system <set-system-options>
Apps and aliases <apps-and-aliases>
Control services <control-services>
Manage validation sets <manage-validation-sets>

Create data snapshots <create-data-snapshots>
Use resource quotas <use-resource-quotas>
Disk space awareness <disk-space-awareness>
Work with components <using-components>
Configure with confdb <configure-snaps-with-confdb>
Fix common issues <fix-common-issues>
