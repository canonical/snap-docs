(interfaces-physical-memory-control-interface)=
# physical-memory-control-interface

`physical-memory-control` allows write access the to physical address space via the `/dev/mem` device. 

When the kernel is compiled with `STRICT_DEVMEM=y` (required for certified kernels), accessible memory is an architecture-specific subset for common use cases, such as (eg, X without KMS, DOSBox, etc).

This interface can write to all physical memory when the kernel is compiled with `STRICT_DEVMEM=n`.

**Auto-connect**: no

Requires snapd version _2.21+_.

> ⓘ  This is a snap interface. See [Interface management](/) and [Supported interfaces](/interfaces/index) for further details on how interfaces are used.

