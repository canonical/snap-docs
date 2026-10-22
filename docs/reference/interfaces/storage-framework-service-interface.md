---
myst:
  html_meta:
    description: storage-framework-service interface
---

(interfaces-storage-framework-service-interface)=
#  storage-framework-service interface

`storage-framework-service` allows operating as, or interacting with, the Storage Framework.

**Auto-connect**: no

```{note}
The `storage-framework-service` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

Requires snapd version _2.25+_.


