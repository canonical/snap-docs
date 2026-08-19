(interfaces-block-devices-interface)=
#  block-devices interface

`block-devices` provides the ability to perform operations on raw disk block devices (e.g. `/dev/sda`, `/dev/mmcblk0`). This interface grants privileged access to the device.

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

Requires snapd version _2.37+_.

When the plug sets `allow-partitions` boolean attribute to `true`, the interface will grant access to individual partition devices (e.g. `/dev/sda1`, `/dev/mmcblk0p1`). The plug needs to be declared in the following manner:

```
plugs:
  block-devices:
    allow-partitions: true
```
The `allow-partitions` attribute requires snapd version *2.71+*.

Consumers of this interface require a {ref}`snap declaration <interfaces-process-for-aliases-auto-connections-and-tracks>` for distribution via the Snap Store.


