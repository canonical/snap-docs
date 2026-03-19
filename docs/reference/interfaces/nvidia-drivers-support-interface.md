(interfaces-nvidia-drivers-support-interface)=
#  nvidia-drivers-support interface

The `nvidia-drivers-support` interface is for internal Ubuntu Core use only.

This interface permits the [nvidia-assemble](https://snapcraft.io/nvidia-assemble) snap to access to NVIDIA char devices, `/dev/nvidiactl` and `/dev/nvidia-uvmfrom`, which it needs to assemble and load the NVIDIA kernel drives.


---

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/nvidia_drivers_support_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/nvidia_drivers_support.go

