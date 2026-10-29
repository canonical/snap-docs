---
myst:
  html_meta:
    description: Reference documentation for location-control, which lets a snap operate as a location service with privileged configuration, observation, and use.
---

(interfaces-location-control-interface)=
#  location-control interface

`location-control` allows operating as the location service, providing privileged access to configure, observe and use location services.

**Auto-connect**: no

```{note}
The `location-control` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

