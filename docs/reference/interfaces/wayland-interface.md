(interfaces-wayland-interface)=
#  wayland interface

`wayland` allows access to compositors supporting Wayland protocol.

**Auto-connect**: yes, except on Ubuntu Core
**Transitional**: yes

```{note}
The `wayland` slot is unsupported for {ref}`parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

See The desktop interfaces for further details.

Requires snapd version _2.28+_.


