---
myst:
  html_meta:
    description: power-control interface
---

(interfaces-power-control-interface)=
#  power-control interface

The `power-control` interface allows the reading and setting of system power settings.

This interface is primarily intended to be used with {ref}`Ubuntu Core <ref-glossary_ubuntu-core>`.


## Developer details

**Auto-connect**: no

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```

This interface enables:
- reading of all power settings:
`/sys/devices/**/power/`
- setting wake-up events for supported devices:
`/sys/devices/**/power/wakeup`
- configuring power management for supported devices at runtime:
 `/sys/devices/**/power/control`


### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/power_control_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/power_control.go

