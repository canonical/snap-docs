---
myst:
  html_meta:
    description: Reference documentation for the adb-support interface, which lets snaps operate the Android Debug Bridge service with privileged access to Android devices.
---

(interfaces-adb-support-interface)=
#  adb-support interface

`adb-support` allows a snap to operating the Android Debug Bridge service, providing privileged access to an Android device.

<h2 id='heading--example'>Example</h2>

[guiscrcpy](https://snapcraft.io/guiscrcpy) uses _adb-support_ to help share an Android screen on a Linux desktop.


## Developer details

**Auto-connect**: no

```{note}
The `adb-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```


Requires snapd version _2.36+_.

<h3 id='heading-code'>Code examples</h3>

The adb-support interface is used in the _guiscrcpy_ snap: <https://github.com/srevinsaju/guiscrcpy/blob/master/snap/snapcraft.yaml>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/adb_support.go>
