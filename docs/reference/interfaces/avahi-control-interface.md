---
myst:
  html_meta:
    description: avahi-control interface
---

(interfaces-avahi-control-interface)=
#  avahi-control interface

`avahi-control` allows control over service discovery on a local network via the mDNS/DNS-SD protocol suite.

**Auto-connect**: no

```{note}
The `avahi-control` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

Requires snapd version _2.28+_.

