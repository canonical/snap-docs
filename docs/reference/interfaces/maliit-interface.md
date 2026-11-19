---
myst:
  html_meta:
    description: Reference documentation for the maliit interface, which lets snaps operate as the Maliit service, commonly used for on-screen keyboards.
---

(interfaces-maliit-interface)=
#  maliit interface

`maliit` allows operating as the Maliit service, commonly useful to enabling an on-screen keyboard.

**Auto-connect**: no

```{note}
The `maliit` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

Requires snapd version _2.24+_.


