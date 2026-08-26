---
myst:
  html_meta:
    description: Step-by-step guides covering key operations and common tasks for snap users and snap package developers, including how to manage updates, connect interfaces, control services and more.
---

(how-to-guides-index)=
# How-to guides

Our _How-to_ guides help you achieve a specific goal while working with snaps. They may require you to understand and adapt the steps to fit your specific requirements.

## Work with snaps

The snap system has been designed to look after itself with automatic security and update policies. However, these elements, and many others, can also be configured and managed manually.

* {ref}`Manage updates <how-to-guides-work-with-snaps-manage-updates>`: Control when snaps update, or hold an update indefinitely .
* {ref}`Connect interfaces <how-to-guides-work-with-snaps-connect-interfaces>`: Control exactly what a snap can access, and what it can't.
* {ref}`Configure snaps <how-to-guides-work-with-snaps-configure-snaps>`: Learn how to set options for your servers and daemons.
* {ref}`Apps and aliases <how-to-guides-work-with-snaps-apps-and-aliases>`: Use your preferred names for your snapped applications.

## Manage snaps

Outside of whatever facilities a snapped application may provide, snaps also provides data snapshots, usage quotas and control over if and when a service runs.

* {ref}`Create data snapshots <how-to-guides-manage-snaps-create-data-snapshots>`: Make a copy of a snap's user, system and configuration data.
* {ref}`Use quota resources <how-to-guides-manage-snaps-use-resource-quotas>`: Set processor and memory resource limits on your snaps.
* {ref}`Disk space awareness <how-to-guides-manage-snaps-disk-space-awareness>`: Check whether there's enough disk space before certain operations.
* {ref}`Set system options <how-to-guides-manage-snaps-set-system-options>`: The main way to configure your snapped applications.
* {ref}`Control services <how-to-guides-manage-snaps-control-services>`: Start, stop and restart snapped background service.
* {ref}`Validation sets <explanation-how-snaps-work-validation-sets>`: Ensure a defined set of snaps are installed and updated together.
* {ref}`Use the REST API <how-to-guides-manage-snaps-use-the-rest-api>`: Learn how to access and use our REST API.

## Problem solving

The vast majority of snap users and developers experience very few issues, but any technology this complex and diverse will likely encounter some issues and incompatibilities. 

* {ref}`Fix common issues <how-to-guides-fix-common-issues-index>`: If you do run into problems, find common solutions here.
* {ref}`Test snapd fixes <how-to-guides-fix-common-issues-test-snapd-fixes>`: Run a bugfix build of the snap daemon.
* {ref}`Debug running snaps <how-to-guides-fix-common-issues-debug-snaps>`: Test bugfix releases of snapd.

## Snap development

Extend snap functionality with API access, internal tools, and customised environments for your applications and devices.

* {ref}`Use the REST API <how-to-guides-manage-snaps-use-the-rest-api>`: how to access the SnapD REST API.
* {ref}`Use snapctl <how-to-guides-manage-snaps-use-snapctl>`: use the snapctl tool within a snap application.
* {ref}`Test snapd fixes <how-to-guides-fix-common-issues-test-snapd-fixes>`: test out the latest release of the snap daemon.
* {ref}`Debug snaps <how-to-guides-fix-common-issues-debug-snaps>`: solve issues with snapped application.
* {ref}`snap try <interfaces-snap-try>`: test a snap package on your system.
* {ref}`Using in-development features <interfaces-using-in-development-features>`: learn how to use cutting edge snap features.


```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

Manage snaps <manage-snaps/index>
Snap development <snap-development/index>
