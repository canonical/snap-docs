(interfaces-developing-hotplug-interfaces)=
# Developing hotplug interfaces

This page describes how developers can implement an [interface](/) that supports [USB hotplugging](https://www.kernel.org/doc/html/v4.13/driver-api/usb/hotplug.html),via snapd's built-in hotplug support.

For a general user overview, including enabling this functionality and hotplug interface management, see [Hotplug support](/reference/interfaces/hotplug-support).

Hotplug support is currently [under active development](/reference/development/experimental-features).

## Adding hotplug interfaces

The code for a snapd interface has be modified to support hotplug, and subsequently create slots on the system snap, by implementing the following new function:

```go
HotplugDeviceDetected(deviceInfo *hotplug.HotplugDeviceInfo) (*hotplug.ProposedSlot, error)
```

When defined, `HotplugDeviceDetected` is executed whenever a *any* hotplug device is connected to the system. The purpose of the function is to decide whether a freshly connected device is relevant for any given interface by returning one of the following:

- if the connected device is not relevant, the function should return `nil, nil`
- if the connected device is relevant, a definition of the _proposed_ hotplug slot that needs to be created should be returned (see below)
- if the connected device is relevant, but it’s impossible to create a slot definition for it, an error should be returned

It is important to note that this function may be called multiple times as the device connected because, in many cases, the kernel creates various pseudo- and virtual- devices for given physical device. The function should filter out irrelevant calls and only create a single slot definition for the actual device.

The returned slot is a _proposed slot_ because snapd’s hotplug subsystem mediates the creation of the final slot. It may simply update the slot if:

- the device is being reconnected
- the slot previously existed and had connections

## Attribute access methods

The above function receives the `hotplug.HotplugDeviceInfo` structure which contains all the attributes provided by the udev event for the device, and offers the following methods to access them:

* **`Subsystem() string`**
 
    Returns the name of the kernel subsystem of the device, for example `tty` or `sound`.

* **`DeviceName() string`**

    Corresponds to udev’s `DEVNAME` attribute and provides the actual device path, e.g. */dev/ttyUSB0*. This is the path that the interface is generally interested in, as far as confinement rules are concerned.

* **`DevicePath() string`**

    Corresponds to udev’s `DEVPATH` attribute and provides device path under the sysfs filesystem, e.g. */sys/devices/pci0000:00/0000:00:14.0/usb1/1-2*.

* **`DeviceType() string`**

    Corresponds to udev’s `DEVTYPE` attribute, e.g. *disk*.

* **`Major() string`** and **`Minor() string`**

    Correspond to udev’s `MAJOR` and `MINOR` attributes which provide major/minor device numbers (if applicable).

* **`Attribute(name string) (string, bool)`**

    A generic method to query any udev attribute. It returns false if the attribute is not present in udev event data.

     
The `hotplug.ProposedSlot` structure is created by `HotplugDeviceDetected` in response to a udev event, and may define a name and label for the slot.

However, they are both optional and, in most cases, should be empty. Snapd’s hotplug subsystem will automatically generate them by probing and sanitising some of the well-defined udev attributes, such as model and vendor names. This ensures the resulting name, whether provided by interface code or left empty for snapd to figure out, is unique.

However, the `hotplug.ProposedSlot` must have some attributes set, and in typical cases, should at least include an attribute that carries the path of the device.

The path attribute can then be read by the following methods of the interface (and others, as applicable), to create respective security profiles for the snap and the given device:

- **`AppArmorConnectedSlot`**
- **`SecCompConnectedPlug`**
- **`SecCompConnectedSlot`**

## Example implementation

The following is one potentially complete implementation of `HotplugDeviceDetected`:

```go
func (iface *myInterface) HotplugDeviceDetected(di *hotplug.HotplugDeviceInfo) (*hotplug.ProposedSlot, error) {
	bus, _ := di.Attribute("ID_BUS”)
        // some arbitrary criteria to filter irrelevant devices out
	if di.Subsystem() != "tty" || bus != "usb” || di.Major() != „123” )  {
		return nil, nil
	}

	slot := hotplug.ProposedSlot{
		Attrs: map[string]interface{}{
			"path": di.DeviceName(),
		},
	}
        return slot, nil
}
```

When creating filtering logic for the above function, it is useful to inspect udev attributes of the respective device. One way of doing this with the is with the [udevadm](https://www.freedesktop.org/software/systemd/man/udevadm.html) command. This can be used to report all currently existing devices (eg. `udevadm info -e`) or run in monitor mode (`udevadm monitor -p`) to continuously report all udev event, along with their attributed, as devices connected and unplugged.

As an example, the following is an example of output from *udevadm* for a USB serial port adapter:

```
P: /devices/pci0000:00/0000:00:11.0/0000:02:00.0/usb2/2-2/2-2.1/2-2.1:1.0/ttyUSB0/tty/ttyUSB0
N: ttyUSB0
S: serial/by-id/usb-FTDI_FT232R_USB_UART_AH06W0EQ-if00-port0
S: serial/by-path/pci-0000:02:00.0-usb-0:2.1:1.0-port0
E: DEVLINKS=/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AH06W0EQ-if00-port0 /dev/serial/by-path/pci-0000:02:00.0-usb-0:2.1:1.0-port0
E: DEVNAME=/dev/ttyUSB0
E: DEVPATH=/devices/pci0000:00/0000:00:11.0/0000:02:00.0/usb2/2-2/2-2.1/2-2.1:1.0/ttyUSB0/tty/ttyUSB0
E: ID_BUS=usb
E: ID_MM_CANDIDATE=1
E: ID_MODEL=FT232R_USB_UART
E: ID_MODEL_ENC=FT232R\x20USB\x20UART
E: ID_MODEL_FROM_DATABASE=FT232 Serial (UART) IC
E: ID_MODEL_ID=6001
E: ID_PATH=pci-0000:02:00.0-usb-0:2.1:1.0
E: ID_PATH_TAG=pci-0000_02_00_0-usb-0_2_1_1_0
E: ID_PCI_CLASS_FROM_DATABASE=Serial bus controller
E: ID_PCI_INTERFACE_FROM_DATABASE=UHCI
E: ID_PCI_SUBCLASS_FROM_DATABASE=USB controller
E: ID_REVISION=0600
E: ID_SERIAL=FTDI_FT232R_USB_UART_AH06W0EQ
E: ID_SERIAL_SHORT=AH06W0EQ
E: ID_TYPE=generic
E: ID_USB_DRIVER=ftdi_sio
E: ID_USB_INTERFACES=:ffffff:
E: ID_USB_INTERFACE_NUM=00
E: ID_VENDOR=FTDI
E: ID_VENDOR_ENC=FTDI
E: ID_VENDOR_FROM_DATABASE=Future Technology Devices International, Ltd
E: ID_VENDOR_ID=0403
E: MAJOR=188
E: MINOR=0
E: SUBSYSTEM=tty
E: TAGS=:systemd:
E: USEC_INITIALIZED=415122796440
```

Snapd hardware interfaces, whose slots may appear as part of their [gadget.yaml](/) definition, for example, allowing `gadget` in their `allow-installation` section of the base declaration, must additionally implement the following function:

```go
HandledByGadget(deviceInfo *HotplugDeviceInfo, slot *snap.SlotInfo) bool
```
The above function acts as a predicate that should return true if the device described by `deviceInfo` is the same as the one represented by the given slot. It’s called by the hotplug subsystem whenever a device is connected, and it receives slot(s) of the given interface defined statically in *gadget.yaml*.

In the typical cases where gadget slots are defined by means of device paths, the implementation of this method becomes a simple comparison of device path and the path attribute of the slot, for example:


```go
func (iface *myInterface) HandledByGadget(di *hotplug.HotplugDeviceInfo, slot *snap.SlotInfo) bool {
  var path string
  if err := slot.Attr("path", &path); err != nil {
    return false
  }
  return di.DeviceName() == path
}
```

## Hotplug and interface hooks

When a supported device is connected to the system, snapd creates a hotplug slot for its respective interface. If the slot is then connected to a plug, either manually by the user, or via the auto-connect mechanism, the following interface hooks are executed if they exist:

- **`prepare-plug-<plugname>`**
- **`connect-plug-<plugnname>`** (for the snap on the plug side)
 
Similarly, when the device is disconnected and its slot had been connected to a plug, its `disconnect` interface hooks get executed, eg:

- **`disconnect-plug-<plugname>`**

This mechanism can be used by snaps to react to devices appearing/disappearing from their connected plugs. Please refer to the documentation on [Interface Hooks](/) for more details on this functionality.

