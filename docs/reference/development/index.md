(reference-development-index)=
# Development

Extend snap functionality with API access and customised environments for your applications and devices.

* [Environment variables](/reference/development/environment-variables): Internal values accessible to snapped applications.
* [REST API error codes](/reference/development/error-responses): The types of errors returned by the API.

## YAML schemas

YAML schemas define exactly what a device, kernel and snap is capable of.
 - [snap.yaml](/reference/development/yaml-schemas/the-snap-format): The metadata for a snap.
 - [Gadget snap](/reference/development/yaml-schemas/the-gadget-snap): System and device properties. 
 - [Kernel snap](/reference/development/yaml-schemas/the-kernel-snap): The Linux kernel snap, its metadata and setup files.

```{toctree}
:hidden:
:titlesonly:
:maxdepth: 2
:glob:

Environment variables <environment-variables>
API Error codes <error-responses>
Supported hooks <supported-snap-hooks>
SnapD REST API <snapd-rest-api>
YAML schemas <yaml-schemas/index>
