(interfaces-acrn-support-interface)=
#  acrn-support interface

The `acrn` interface  allows access to, and control of, user virtual machines using the [ACRN hypervisor](https://projectacrn.org/).

**This interface is primarily intended to be used with {ref}`Ubuntu Core <ref-glossary_ubuntu-core>` devices.**


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: no</br>

```{note}
Snaps that declare an `acrn-support` plug are not supported as {ref}`parallel instances <interfaces-parallel-installs-unsupported>`.
```

### Code examples

The following (third-party) repository contains recipes to create snap packages for ACRN: https://github.com/gvancuts/acrn-snap

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/acrn_support_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/acrn_support.go

