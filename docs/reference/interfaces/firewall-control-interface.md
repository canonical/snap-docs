---
myst:
  html_meta:
    description: firewall-control interface
---

(interfaces-firewall-control-interface)=
#  firewall-control interface

`firewall-control` allows control over the network firewall.

**Auto-connect**: no

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```


