---
myst:
  html_meta:
    description: checkbox-support interface
---

(ref-checkbox-support-interface_checkbox-support-interface)=
#  checkbox-support interface

The `checkbox-support` interface is a privileged interface designed for the Canonical checkbox test and certification system. The system is able to run a wide collection of system tests and is thus allowed to execute any command mostly bypassing the sandbox.

The interface is allowed to run on both core and classic systems, so that certification can use the same snap across the entire range of devices.

**This interface is under development and is not currently available for general use**.

## Developer details 

**Auto-connect**: no

```{note}
The `checkbox-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```

### Code examples

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/checkbox_support.go>
