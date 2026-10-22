---
myst:
  html_meta:
    description: classic-support interface
---

(interfaces-classic-support-interface)=
#  classic-support interface

The `classic-support` interface sets special permissions for the [classic snap](https://snapcraft.io/classic), effectively giving device ownership to its connected snaps.

This interface is intended to be used only with {ref}`Ubuntu Core <ref-glossary_ubuntu-core>`.

Requires snapd version _2.23+_.


## Developer details


**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{note}
The `classic-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/classic_support_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/classic_support.go

