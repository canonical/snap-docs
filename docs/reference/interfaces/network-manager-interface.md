---
myst:
  html_meta:
    description: Reference documentation for the network-manager interface, which lets snaps configure and observe networking via NetworkManager.
---

(interfaces-network-manager-interface)=
#  network-manager interface

`network-manager` enables access to [NetworkManager](https://docs.ubuntu.com/core/en/stacks/network/network-manager/docs/), providing privileged access to configure and observe networking.

**Auto-connect**: no

```{note}
The `network-manager` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```


