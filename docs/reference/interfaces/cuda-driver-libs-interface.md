---
myst:
  html_meta:
    description: cuda-driver-libs interface
---

(interfaces-cuda-driver-libs)=
#  cuda-driver-libs interface

**This interface is under development and is not currently available for general use**.

The `cuda-driver-libs` interface permits access to CUDA acceleration on Nvidia GPUs.


## Developer details

**Auto-connect**: no

```{note}
The `cuda-driver-libs` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The library source files exported by the slot cannot distinguish between instances.
```

<h3 id='heading-code'>Code examples</h3>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/cuda_driver_libs.go>

