---
myst:
  html_meta:
    description: udisks2 interface
---

(interfaces-udisks2-interface)=
#  udisks2 interface

`udisks2` enables access to the UDisks2 service, giving privileged access to storage on the device.

When used on [Ubuntu Core](https://ubuntu.com/core/docs), the _udisks2_ interface requires access enabled from a corresponding [gadget snap](https://ubuntu.com/core/docs/gadget-snaps).

**Auto-connect**: no

```{note}
The `udisks2` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```


