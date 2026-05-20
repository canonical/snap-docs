---
myst:
  html_meta:
    description: Complete reference documentation for snap packages - technical details on all snap packaging features for snap users and snap package developers, including the snapd REST API, YAML schemas, system architecture and more. 
---

(reference-index)=
# Reference

This *Reference* section is for when you need to know which options can be used, what functions the API supports, which environment variables can be accessed and the contents of *gadget.yaml*. 

## Operations

Details that help with the day-to-day operations of working with snaps.

* {ref}`Glossary <reference-operations-glossary>`: Terms and definitions specific to the world of snaps.
* {ref}`Interfaces <ref-index_interfaces>`: Every interface alongside their most important attributes.
* {ref}`Snap system architecture <reference-operations-system-architecture>`: What snapd uses to manage confinement and security. 
* {ref}`System options <reference-operations-system-options>`: Configurations options for the system and native snap devices.
* {ref}`Exit codes <reference-operations-exit-codes>`: Exit codes returned by the `snap` command.

## Administration

Deepen your understanding of how snaps can run on all kinds of devices, in all kinds of environments.

* {ref}`Network requirements <reference-administration-network-requirements>`: What network access snaps require to operate correctly.
* {ref}`Distribution support <reference-administration-distribution-support>`: The status of current builds for Linux distributions with snap support.

## Snap development

Extend snap functionality with API access and customised environments for your applications and devices.

* {ref}`Environment variables <reference-development-environment-variables>`: Internal values accessible to snapped applications.
* <a id="openapi-link" href="api/redoc-static.html">Snapd REST API</a>: Interactive OpenAPI documentation for the Snapd REST API.
* {ref}`REST API error codes <reference-development-rest-api-error-responses>`: The types of errors returned by the API.

YAML schemas define exactly what a device, kernel and snap is capable of.
 - {ref}`snap.yaml <reference-development-yaml-schemas-the-snap-format>`: The metadata for a snap.
 - {ref}`Gadget snap <reference-development-yaml-schemas-the-gadget-snap>`: System and device properties. 
 - {ref}`Kernel snap <reference-development-yaml-schemas-the-kernel-snap>`: The Linux kernel snap, its metadata and setup files.


```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

Glossary <glossary>
Release notes <release-notes>
System architecture <system-architecture>
Interfaces <interfaces/index>
Administration <administration/index>
Snap development <development/index>
Exit codes <exit-codes>
