(interfaces-timeserver-control-interface)=
#  timeserver-control interface

`timeserver-control` allows the setting of system time synchronisation servers via *systemd-timedated* and directly (and independently of `config core`).

**Auto-connect**: no

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`interfaces-parallel-installs-shared-resources`.
```


