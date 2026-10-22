---
myst:
  html_meta:
    description: fpga interface
---

(interfaces-fpga-interface)=
#  fpga interface

The `fpga` interface allows access to the [FPGA subsystem](https://www.kernel.org/doc/html/latest/driver-api/fpga/index.html).


## Developer details

**Auto-connect**: no
**Allow-installation**: yes

```{note}
The `fpga` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. Instances would perform conflicting operations on the same system resources.
```

Devices:
`/dev/fpga[0-9]* rw,`


### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/fpga_test.go

The source code for the interface is in the snapd repository:[https://github.com/canonical/snapd/blob/master/interfaces/builtin/fpga.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/fpga.go)
