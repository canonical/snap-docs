---
myst:
  html_meta:
    description: modem-manager interface
---

(interfaces-modem-manager-interface)=
#  modem-manager interface

`modem-manager` allows operating as the ModemManager service, giving privileged access to configure, observe and use modems.

**Auto-connect**: no

```{note}
The `modem-manager` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```


