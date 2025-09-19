(interfaces-acrn-support-interface)=
# acrn-support-interface

The `acrn` interface  allows access to, and control of, user virtual machines using the [ACRN hypervisor](https://projectacrn.org/).

**This interface is primarily intended to be used with [Ubuntu Core](/t/glossary/14612#heading--ubuntu-core) devices.**

```{tip}

See [Interface management](/) and [Supported interfaces](/interfaces/index) for further details on how interfaces are used.
```

---

<h2 id='heading--dev-details'>Developer details </h2>

**[Auto-connect](/t/interface-management/6154#heading--auto-connections)**: no</br>
**[Super-privileged](/t/the-interface-connection-mechanism/20179#heading--super)**: no</br>

### Code examples

The following (third-party) repository contains recipes to create snap packages for ACRN: https://github.com/gvancuts/acrn-snap

The test code can be found in the snapd repository: https://github.com/snapcore/snapd/blob/master/interfaces/builtin/acrn_support_test.go

The source code for the interface is in the snapd repository: https://github.com/snapcore/snapd/blob/master/interfaces/builtin/acrn_support.go

