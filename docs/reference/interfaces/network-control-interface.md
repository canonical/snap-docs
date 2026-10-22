---
myst:
  html_meta:
    description: network-control interface
---

(interfaces-network-control-interface)=
#  network-control interface

`network-control` enables the configuration of networking and network namespaces via `ip netns`, providing a wide, privileged access to networking.

**Auto-connect**: no

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```

Requires snapd version _2.20+_.


