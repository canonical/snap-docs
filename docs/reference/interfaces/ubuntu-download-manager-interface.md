---
myst:
  html_meta:
    description: Reference documentation for the ubuntu-download-manager interface, which lets snaps operate as, or interact with, the Ubuntu download manager.
---

(interfaces-ubuntu-download-manager-interface)=
#  ubuntu-download-manager interface

`ubuntu-download-manager` allows operating as, or interacting with, the Ubuntu download manager.

**Auto-connect**: yes

```{note}
The `ubuntu-download-manager` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```


