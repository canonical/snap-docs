(interfaces-adb-support-interface)=
# The adb-support interface

`adb-support` allows a snap to operating the Android Debug Bridge service, providing privileged access to an Android device.

<h2 id='heading--example'>Example</h2>

[guiscrcpy](https://snapcraft.io/guiscrcpy) uses _adb-support_ to help share an Android screen on a Linux desktop.

```{tip}

See [Interface management](/) and [Supported interfaces](/interfaces/index) for further details on how interfaces are used.
```

---

<h2 id='heading--dev-details'>Developer details </h2>

**Auto-connect**: no


Requires snapd version _2.36+_.

<h3 id='heading-code'>Code examples</h3>

The adb-support interface is used in the _guiscrcpy_ snap: <https://github.com/srevinsaju/guiscrcpy/blob/master/snap/snapcraft.yaml>

The source code for this interface is in the *snapd* repository:
<https://github.com/snapcore/snapd/blob/master/interfaces/builtin/adb_support.go>

