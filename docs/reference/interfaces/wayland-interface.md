---
myst:
  html_meta:
    description: Reference documentation for the wayland interface, which lets snaps access display compositors that support the Wayland protocol.
---

(interfaces-wayland-interface)=
#  wayland interface

`wayland` allows access to compositors supporting Wayland protocol.

**Auto-connect**: yes, except on Ubuntu Core
**Transitional**: yes

```{note}
The `wayland` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

See The desktop interfaces for further details.

Requires snapd version _2.28+_.


