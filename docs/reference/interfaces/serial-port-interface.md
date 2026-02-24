(interfaces-serial-port-interface)=
#  serial-port interface

The `serial-port` interface enables input and output access to a specific serial port on a device typically running [Ubuntu Core](/t/glossary/14612#heading--ubuntu-core). As a result, and because it provides such privileged access to configure serial port hardware,  `serial-port` is considered a restricted interface.

Use  `snap interface serial-port` to see which serial-port devices are available on the system:

```
$ snap interface serial-port
name:    serial-port
summary: allows accessing a specific serial port
slots:
  - core:model01 (allows accessing a specific serial port)
  - core:monome (allows accessing a specific serial port)
```

Once connected, the consuming snap can use the device via the path specified by the connected slot.


## Developer details

**Auto-Connect**: no</br>
**Attributes**:
  - Should specify a single path attribute:
    * `path` (slot): path to serial device node e.g. `/dev/ttyS1`

* Or three attributes:
    * `usb-vendor` (slot): integer representing the USB Vendor ID, must be in range 0 < vid <= 65535
    * `usb-product` (slot): integer representing the USB Product ID, must be in range 0 <= vid <= 65535
    * `path` (slot): path of the form `/dev/serial-port-...` where a symlink will be created to the device e.g. `/dev/serial-port-mydevice`

[Hardware IO interfaces](/reference/interfaces/hardware-io-interfaces) covers some general considerations common to these kinds of devices.


To use a serial-port device, the snap developer must add `plugs: [ serial-port ]` to a snap's [snapcraft.yaml](/). The snap user can then access a specific serial-port device with an [interface connection](/t/interface-management/6154#heading--manual-connections).

<h3 id='heading--code-examples'>Code examples</h3>

The following example shows the slot configuration, such as from the gadget snap, and includes  which snaps are permitted to connect automatically:

```yaml
serial-port:
    allow-auto-connection:
      -
        on-store:
          - (whatever)
        plug-names:
          - serial-foo
        plug-snap-id:
          - foooVbn5YriRw2sRVw7Cuj5PbjJjwnFb
        slot-attributes:
          path: /dev/whatever
        slot-names:
          - serial-foo
```

All attributes must match for an auto-connection attempt to be successful. The above example requires a connecting snap to have a matching snap-id and plug name. For example, the following snapcraft.yaml stanza for the connecting snap would _not_ connect:

```yaml
apps:
  whatever:
     plugs:
        serial-port
```

While the following snapcraft.yaml stanza for the connecting snap would automatically connect:

```yaml
apps:
  whatever:
     plugs:
        serial-foo
plugs:
   serial-foo:
      interface: serial-port
```

The test code can be found in the snapd repository:
[serial_port_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/serial_port_test.go).

The source code for the interface is in the snapd repository:
[serial_port.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/serial_port.go)</br>

