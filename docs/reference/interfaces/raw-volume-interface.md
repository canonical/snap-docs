(interfaces-raw-volume-interface)=
#  raw-volume interface

`raw-volume` provides access to a specific disk partition. This interface is restricted because it provides privileged access to device partitions.

The slot is intended to be implemented by a gadget snap and is not provided by the core system snap.

**Auto-Connect**: no
**Attributes**:
 * `path` (slot): path to device partition e.g. `/dev/mmcblk0p1`

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`interfaces-parallel-installs-shared-resources`.
```

Requires snapd version *2.43+*.

To use a disk partition, the snap developer must add `plugs: [ raw-volume ]` to a snap's [snapcraft.yaml](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/snapcraft-yaml). The snap user can then access a specific disk partition with an {ref}`interface connection <explanation-interfaces-all-about-interfaces>`.

Use  `snap interface raw-volume` to see which disk partitions are available on the system for snaps to use:

```
$ snap interface raw-volume
name:    raw-volume
summary: allows access to specific disk partition
slots:
  - foo:mmcblk0p1
  - foo:mmcblk0p2
```

Once connected, the consuming snap can use the device via the path specified by the connected slot.


