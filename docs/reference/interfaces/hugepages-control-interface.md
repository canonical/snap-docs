---
myst:
  html_meta:
    description: Reference documentation for the hugepages-control interface, which lets snaps control Linux HugePages memory block management.
---

(interfaces-hugepages-control-interface)=
#  hugepages-control interface

The `hugepages-control` interface allows controlling [HugePages](https://www.kernel.org/doc/Documentation/vm/hugetlbpage.txt), a Linux kernel feature that enables memory blocks to be managed in larger page sizes.


## Developer details

**Auto-connect**: no

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`Snaps that are unsupported as parallel instances <interfaces-parallel-installs-shared-resources>` for details..
```

This interface assumes that _huge pages_ are mounted at either:
- `/dev/hugepages` (Debian, Ubuntu)
- `/run/hugepages` (various other distributions)

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/hugepages_control_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/hugepages_control.go

