---
myst:
  html_meta:
    description: Reference documentation for the avahi-observe interface, which lets snaps discover services on a local network via the mDNS/DNS-SD protocol suite.
---

(interfaces-avahi-observe-interface)=
#  avahi-observe interface

`avahi-observe` allows discovery on a local network via the mDNS/DNS-SD protocol suite.

**Auto-connect**: no

```{note}
The `avahi-observe` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

