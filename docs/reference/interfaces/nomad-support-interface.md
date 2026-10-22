---
myst:
  html_meta:
    description: nomad-support interface
---

(interfaces-nomad-support)=
#  nomad-support interface

The `nomad-support` interface provides permissions to enable [HashiCorp Nomad](https://www.nomadproject.io/) to access [cpuset](https://man7.org/linux/man-pages/man7/cpuset.7.html) CPU and memory management, alongside Nomad-specific capabilities such as the NVIDIA plugin support, slice functions, and Nomad running as a service.

See {ref}`Interface management <how-to-guides-work-with-snaps-connect-interfaces>` and {ref}`Supported interfaces <ref-index_interfaces>` for further details on how interfaces are used.

## Developer details

**Auto-connect**: no

```{note}
The `nomad-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/nomad_support_test.go

The source code for the interface is in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/nomad_support.go

