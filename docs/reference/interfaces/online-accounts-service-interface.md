---
myst:
  html_meta:
    description: online-accounts-service interface
---

(interfaces-online-accounts-service-interface)=
#  online-accounts-service interface

`online-accounts-service` allows access to the Online Accounts service.

**Auto-connect**: yes

```{note}
The `online-accounts-service` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

Requires snapd version _2.25+_.

