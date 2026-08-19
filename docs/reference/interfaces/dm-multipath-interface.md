(ref-dm-multipath-interface_dm-multipath-interface)=
#  dm-multipath interface

The `dm-multipath` interface allows snaps to manage and access device-mapper multipath maps by communicating with the multipathd daemon. It is intended for storage orchestration software that needs to list, create, reload and remove multipath devices and react to path state changes. Direct unrestricted access to arbitrary raw block devices is not granted; normal snap device cgroup mediation still applies.

For further details on interfaces, see {ref}`How to connect interfaces <explanation-interfaces-all-about-interfaces>`.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/dm_multipath_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/dm_multipath.go
