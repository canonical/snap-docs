(interfaces-i2c-interface)=
#  i2c interface

The `i2c` interface permits access to a specific I2C controller. It's intended to be used with Ubuntu Core and its scope and specification are defined as part of the {ref}`gadget snap <reference-development-yaml-schemas-the-gadget-snap>` for the deployed Ubuntu Core image.

Hardware IO interfaces covers some general considerations common to these kinds of devices.

To permit access, the application snaps define an i2c *plug* which is associated with a corresponding and identically-named i2c *slot* in the gadget snap.

Using the `i2c` interface does not require Store approval and permission, but usage **is** restricted because it provides privileged access to hardware devices. Enabling the `i2c` interface to auto-connect can be managed in the [dashboard](https://dashboard.snapcraft.io). The snap user can also access a specific i2c device with a {ref}`manual interface connection <explanation-interfaces-all-about-interfaces>`.


---

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>

**Attributes**:
 * **`path` (plug, slot)**: path to i2c device node.</br>
Example: `path: /dev/i2c-0`
 * **`sysfs-name` (plug, slot)**: a proper name found in `/sys/bus/i2c/devices`</br>
Example: `sysfs-name: 1-0050`

Only one of `path` or `sysfs-name` should be used in either the plug or slot definition, but both must match. That is to say, if the gadget declares the slot-side using `sysfs-name`, the snap declaring the plug-side must also use `sysfs-name`.

The slot-side of the interface is used to derive which i2c node in `/dev/` is provided to the plug-side of the connection:

```yaml
slots:
  i2c-1:
    interface: i2c
    path: /dev/i2c-1
```

To prevent connection to arbitrary i2c slots, the plug and slot must share the same i2c attribute, including the name of the plug and slot:

```yaml
plugs:
  i2c-1:
    interface: i2c
    path: /dev/i2c-1
```

When the slot and plug are connected, a udev rule is automatically generated and tagged for the plug side for the device path, such as:

```
KERNEL=="i2c-1", TAG+="snap_client-snap_app-accessing-1-port"
```

The test code for the interface is in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/i2c_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/i2c_test.go)
The source code for the interface is in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/i2c.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/i2c.go)

