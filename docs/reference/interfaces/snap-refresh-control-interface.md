(interfaces-snap-refresh-control-interface)=
#  snap-refresh-control interface

The `snap-refresh-control` interface allows extended control, via {ref}`snapctl <how-to-guides-manage-snaps-use-snapctl>`, of refreshes targeting the snap.

**This interface and the full set of features it requires to function are currently under development.**


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

`snap-refresh-control` is a marker interface  (with no associated AppArmor or Seccomp rules).

Currently it allows connected snaps to execute `snapctl refresh --proceed` to unblock pending refreshes outside of the context of the `gate-auto-refresh` hook. This interface should be used with caution.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_refresh_control_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/snap_refresh_control.go

