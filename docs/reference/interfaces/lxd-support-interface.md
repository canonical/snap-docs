---
myst:
  html_meta:
    description: Reference documentation for the lxd-support interface, which lets snaps operate as the LXD service for the upstream LXD project.
---

(interfaces-lxd-support-interface)=
#  lxd-support interface

`lxd-support` enables operating as the LXD service. This interface can currently only be established with the upstream LXD project.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>
**Transitional**: yes

```{note}
The `lxd-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```

**Attributes**:

 * **enable-unconfined-mode** (plug, optional):  indicates that snapd should make use of the AppArmor `unconfined` profile mode (if this is supported by the system) when generating the associated AppArmor profiles for the snap which plugs this interface.


