---
myst:
  html_meta:
    description: egl-driver-libs interface
---

(interfaces-egl-driver-libs)=
#  egl-driver-libs interface

The `egl-driver-libs` interface permits access to EGL the graphics sub-system.

**This interface is under development and is not currently available for general use**.

## Developer details 

**Auto-connect**: no

```{note}
The `egl-driver-libs` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The library source files exported by the slot cannot distinguish between instances.
```

### Code examples

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/egl_driver_libs.go>
