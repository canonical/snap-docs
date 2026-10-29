---
myst:
  html_meta:
    description: Reference documentation for the nvme-control interface, which lets snaps manage NVMe controllers and namespaces via in-kernel NVMe interfaces.
---

(ref-nvme-control-interface_nvme-control-interface)=
#  nvme-control interface

The `nvme-control` interface allows snaps to manage and access NVMe controllers,alongside namespaces via in-kernel NVMe interfaces (PCI & NVMe-oF).

This interface provides access to enumerate devices, create/delete/attach/detach namespaces, and read device health/ telemetry data.

Access is limited to NVMe management operations through sysfs, nvme-fabrics char device, and controller/namespace device nodes. Raw block I/O remains constrained by device cgroups. The nvme and nvme-tcp kernel modules may auto-load as needed.

For further details on interfaces, see {ref}`How to connect interfaces <explanation-interfaces-all-about-interfaces>`.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/nvme_control_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/nvme_control.go
