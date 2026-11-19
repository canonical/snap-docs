---
myst:
  html_meta:
    description: Reference documentation for the microstack-support interface, which lets snaps access multiple services required by the Microstack OpenStack deployment.
---

(interfaces-microstack-support-interface)=
#  microstack-support interface

The `microstack-support` interface enables multiple service access for the _Microstack infrastructure_. It's used by the [Microstack](https://microstack.run/) snap, a full OpenStack deployment within a single snap package.

Virtual machines are spawned as QEMU processes with libvirt acting as a management daemon (including for activities such as applying AppArmor profiles).

Networking is provided largely via OpenVSwitch and Neutron, with dnsmasq acting as an auxiliary daemon. A tun/tap kernel module is used for creating virtual interfaces.

Virtual machines rely on KVM for virtualisation acceleration and the vhost framework in the kernel (vhost_net, vhost_scsi, vhost_vsock).


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{note}
The `microstack-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```

This interface allows MicroStack to operate by allowing the necessary system calls to be used by the following services:
- libvirt
- qemu
- qemu-img
- Nova
- Neutron
- Keystone
- Glance
- Cinder

### Code examples

The snapcraft.yaml for MicroStack can be found here: https://github.com/coreycb/microstack/blob/1-tls/snapcraft.yaml

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/microstack_support.go

