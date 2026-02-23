(interfaces-hotplug-support)=
# Hotplug support

Hotplug support gives snaps the ability to integrate with Linux's [USB hotplugging](https://www.kernel.org/doc/html/v4.13/driver-api/usb/hotplug.html) and Udev device management subsystem. This enables snaps to recognise specific classes of device and create corresponding [system slots](/) when a device is connected.

Developers wishing to add hotplug functionality to their own interfaces should see [Developing hotplug interfaces](/reference/interfaces/developing-hotplug-interfaces).

Initially, only USB serial port adapters using the [serial-port interface](/reference/interfaces/serial-port-interface) are supported. Other types of device, such as USB cameras, will be added in the future.

In addition to creating a slot, snapd's hotplug support also remembers connections. If the device is unplugged, its slot disappears from the system. When the device is reconnected, its slot and connections are restored. 

*snapd* tracks devices by matching specific udev attributes. This means that even when a device is reconnected with a different udev path, such when it uses a different USB port or gets a non-deterministic enumeration by the kernel, it is still recognised as the old device by snapd and its old connections are restored with updated attributes.

## Enabling hotplug

Hotplug is currently an experimental feature that needs to be enabled. First ensure you have a recent snapd installed, either via the core snap or the snapd snap, at least 2.39. 

Then enable hotplug support with the following command:

```bash
sudo snap set system experimental.hotplug=true
```

You will need to either restart snapd (with `sudo systemctl restart snapd`, for example), or reconnect USB devices to initiate hotplug processing for connected devices.

## Hotplug slots

The name of a hotplug slot is typically derived from a device’s udev attributes, such as `NAME`, `ID_MODEL_FROM_DATABASE` and `ID_MODEL`. If multiple devices of the same type are connected, a numeric suffix could be added to make their names unique.

For example, a USB serial adapter from Future Technology Devices International (FTDI) with a model name of *FT232R_USB_UART*, will create the following slot for the system snap when connected:

```bash
$ snap interface serial-port
name:    serial-port
summary: allows accessing a specific serial port
slots:
  - core:ft232rusbuart

$ snap connections system
Interface           Plug            Slot                Notes
[...]
serial-port         -               :ft232rusbuart      -
```

## Current limitations

Along with only supporting USB serial port adapters, hotplug is restricted to devices that provide a specific set of udev attributes; name, vendor identifier and/or serial number.

These attributes are needed to identify and track devices. This isn’t normally a problem for branded devices, but it may cause issues with unbranded devices. Without the required attributes, a device cannot be supported and will be ignored when connected. 

There is also no easy way to list connected devices and their corresponding slots. This limitation will be addressed in an upcoming snapd release.

