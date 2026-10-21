(interfaces-kernel-module-control-interface)=
#  kernel-module-control interface

`kernel-module-control` provides the ability to insert, remove and query kernel modules. This interface gives privileged access to the device.

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`interfaces-parallel-installs-shared-resources`.
```

Consumers of this interface require a {ref}`snap declaration <interfaces-process-for-aliases-auto-connections-and-tracks>` for distribution via the Snap Store.


