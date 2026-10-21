(interfaces-upower-observe-interface)=
#  upower-observe interface

`upower-observe` allows operating as, or reading, from the UPower service. This provides the history and statistics of power devices, such as their battery levels and power usage.

**Auto-connect**: yes

```{note}
The `upower-observe` slot is unsupported for {ref}`parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

