---
myst:
  html_meta:
    description: Reference documentation for the time-control interface, which lets snaps change and query the system date and time via systemd-timedated.
---

(interfaces-time-control-interface)=
#  time-control interface

`time-control` allows the system date and time to be changed, and queried, via *systemd-timedated*.

**Auto-connect**: no

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```


