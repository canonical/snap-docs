---
myst:
  html_meta:
    description: Reference documentation for the pipewire interface, which lets snaps access the user's PipeWire socket for audio and video handling.
---

(interfaces-pipewire-interface)=
#  pipewire interface

The `pipewire` interface allows full access to the user's pipewire socket, for those cases where the available portals are not enough, like when running a snapped desktop environment.

## **Developer details**

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>

```{note}
The `pipewire` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

## **Path Access**

The `pipewire` interface grants read-write access to the following paths:

1. pipewire socket
* `/run/user/[0-9]*/pipewire-[0-9]` (all systems)
* `/run/user/[0-9]*/snap.SLOT-PROVIDER-SNAP-NAME/pipewire-[0-9]` (Core systems)

It also offers `shmctl' access.

* The source code for the Pipewire interface is in the snapd repository: [pipewire.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/pipewire.go)
* For further testing details, see: [pipewire\_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/pipewire_test.go)

