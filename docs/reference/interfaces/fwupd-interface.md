---
myst:
  html_meta:
    description: Reference documentation for the fwupd interface, which lets snaps operate as the fwupd service with privileged access to update UEFI firmware.
---

(interfaces-fwupd-interface)=
#  fwupd interface

`fwupd` allows operating as the fwupd service, enabling privileged access to update UEFI firmware.


**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>

```{note}
The `fwupd` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

