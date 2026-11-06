---
myst:
  html_meta:
    description: Reference documentation for the gbm-driver-libs interface, which lets snaps expose Generic Buffer Management (GBM) driver libraries to the system.
---

(ref-gbm-driver-libs-interface_gbm-driver-libs-interface)=
#  gbm-driver-libs interface

The `gbm-driver-libs` interface allows exposing GBM driver libraries to the system.

For further details on interfaces, see {ref}`How to connect interfaces <explanation-interfaces-all-about-interfaces>`.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{note}
The `gbm-driver-libs` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The client driver symlink exported by the slot cannot distinguish between instances.
```

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/gbm_driver_libs_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/gbm_driver_libs.go
