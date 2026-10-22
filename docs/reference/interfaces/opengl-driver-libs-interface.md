---
myst:
  html_meta:
    description: opengl-driver-libs interface
---

(ref-opengl-driver-libs-interface_opengl-driver-libs-interface)=
#  opengl-driver-libs interface

The `opengl-driver-libs` interface allows exposing OpenGL driver libraries to the system

For further details on interfaces, see {ref}`How to connect interfaces <explanation-interfaces-all-about-interfaces>`.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{note}
The `opengl-driver-libs` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The library source files exported by the slot cannot distinguish between instances.
```

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/opengl_driver_libs_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/opengl_driver_libs.go
