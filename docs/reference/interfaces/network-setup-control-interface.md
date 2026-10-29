---
myst:
  html_meta:
    description: Reference documentation for the network-setup-control interface, which lets snaps read and write Netplan network configuration files.
---

(interfaces-network-setup-control-interface)=
#  network-setup-control interface

`network-setup-control` allows read/write access to Netplan configuration files. This is restricted because it gives access to system network configuration which can contain network security details.

**Auto-connect**: no

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```

Requires snapd version _2.22+_.


