---
myst:
  html_meta:
    description: Reference documentation for kernel-firmware-control, which sets a custom kernel firmware search path, typically for remoteproc firmware uploads.
---

(interfaces-kernel-firmware-control-interface)=
#  kernel-firmware-control interface

The ` kernel-firmware-control` interface permits the setting of a custom  [kernel firmware search path](https://www.kernel.org/doc/html/v4.18/driver-api/firmware/fw_search_path.html), and is typically used with {ref}`the remoteproc interface <interfaces-remoteproc-interface>` to upload microcontroller firmware.


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```

Requires snapd version _2.62+_.

<h3 id='heading-code'>Code examples</h3>

The test code can be found in the snapd repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_firmware_control_test.go>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_firmware_control.go>
