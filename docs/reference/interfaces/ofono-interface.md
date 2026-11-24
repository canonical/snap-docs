---
myst:
  html_meta:
    description: Reference documentation for the ofono interface, which lets snaps configure, observe, and use oFono telephony devices with privileged access.
---

(interfaces-ofono-interface)=
#  ofono interface

`ofono` allows operating as the oFono service, enabling privileged access to configure, observe and use oFono devices.

**Auto-connect**: no

```{note}
The `ofono` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

