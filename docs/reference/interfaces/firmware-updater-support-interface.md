(ref-firmware-updater-support-interface_firmware-updater-support-interface)=
#  firmware-updater-support interface

The `firmware-updater-support` interface allows a snap to operate as the Firmware Updater.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{note}
The `firmware-updater-support` plug is unsupported for {ref}`parallel instances <interfaces-parallel-installs-unsupported>`.
```

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/firmware_updater_support_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/firmware_updater_support.go
