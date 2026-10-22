---
myst:
  html_meta:
    description: dm-crypt interface
---

(interfaces-dm-crypt-interface)=
#  dm-crypt interface

The `dm-crypt`  interface enables the following access functions to  [dm-crypt](https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/dm-crypt.html) encrypted external block storage devices:

- setting up a LUKS partition
- locking and unlocking _dm-crypt_ partitions
- adding key(s) to kernel keyring
- formatting encrypted partition(s) ( creation of fs)
- mounting of encrypted partition(s)


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{note}
The `dm-crypt` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. Instances would perform conflicting operations on the same system resources.
```

Often, _dm-crypt_ is statically linked into the kernel (`CONFIG_DM_CRYPT=y`). This is expected when working with custom kernels on projects where disk encryption is required.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/dm_crypt_test.go

The source code for the interface is in the snapd repository:[ https://github.com/canonical/snapd/blob/master/interfaces/builtin/dm_crypt.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/dm_crypt.go)

