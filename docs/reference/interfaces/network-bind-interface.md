(interfaces-network-bind-interface)=
#  network-bind interface

`network-bind` allows operating as a network service, typically enabling a snap to run a server.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: yes</br>

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. For an example of configuring services to avoid port conflicts, see {ref}`Ports <interfaces-parallel-installs-ports>`.
```
