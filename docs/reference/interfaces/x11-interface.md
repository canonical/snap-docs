---
myst:
  html_meta:
    description: Reference documentation for the x11 interface, which lets snaps interact with, or run as, an X11 display server on the device.
---

(interfaces-x11-interface)=
#  x11 interface

`x11` allows interacting with or running as an X11 server.

**Auto-connect**: yes
**Transitional**: yes

```{note}
The `x11` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

See The desktop interfaces for further details.

**Condition to Connect**: If your snap has a graphical user interface, you *should* connect to this interface.

