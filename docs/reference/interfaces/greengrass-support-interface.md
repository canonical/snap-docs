---
myst:
  html_meta:
    description: Reference documentation for the greengrass-support interface, which enables Amazon Greengrass services and Lambda functions and is restricted to that project.
---

(interfaces-greengrass-support-interface)=
#  greengrass-support interface

`greengrass-support` allows operating as the Greengrass service to access resources and syscalls necessary to run Amazon Greengrass services and lambda functions. Snaps specifying this interface can currently only be established with the Amazon Greengrass project.

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes

```{note}
The `greengrass-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```

Requires snapd version _2.26+_.

