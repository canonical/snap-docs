---
myst:
  html_meta:
    description: Reference documentation for the mir interface, which lets snaps operate as the Mir display service for compositing graphical applications.
---

(interfaces-mir-interface)=
#  mir interface

`mir` allows operating as the Mir display service.

**Auto-connect**: no

```{note}
The `mir` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```


