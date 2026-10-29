---
myst:
  html_meta:
    description: Reference documentation for the unity8-contacts interface, which lets snaps read and change contacts in the Unity 8 global contacts list.
---

(interfaces-unity8-contacts-interface)=
#  unity8-contacts interface

`unity8-contacts` enables snaps to access the Unity 8 contacts interface, and consequently, read and change contacts in the Unity 8 global contacts list.

**Auto-connect**: no

```{note}
The `unity8-contacts` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```


