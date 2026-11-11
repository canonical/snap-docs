---
myst:
  html_meta:
    description: Reference documentation for the upower-observe interface, which lets snaps read power device history and statistics from the UPower service.
---

(interfaces-upower-observe-interface)=
#  upower-observe interface

`upower-observe` allows operating as, or reading, from the UPower service. This provides the history and statistics of power devices, such as their battery levels and power usage.

**Auto-connect**: yes

```{note}
The `upower-observe` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

