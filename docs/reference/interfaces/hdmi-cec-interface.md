(interfaces-hdmi-cec-interface)=
# hdmi-cec interface

The `hdmi-cec` interface allows a snap to communicate with HDMI Consumer Electronics Control (CEC) devices through a system CEC adapter.
It is intended for snaps that need to send commands to, or receive events from, HDMI-connected equipment such as televisions and audio systems.

The interface provides an implicit system slot on Ubuntu Core and classic systems.
The interface is not auto-connected; the user must connect the application plug to the system slot manually.

An application snap declares the plug:

```yaml
apps:
  controller:
    plugs: [hdmi-cec]
```

Connect the plug to the implicit system slot with:

```bash
snap connect controller-snap:hdmi-cec :hdmi-cec
```

The interface grants access to Linux CEC device nodes such as `/dev/cec0`, as well as legacy platform-specific nodes including `/dev/hdmicec`, `/dev/CEC`, `/dev/aocec`, `/dev/mxc_hdmi_cec`, `/dev/tegra_cec`, and Raspberry Pi's `/dev/vchiq`.
It also permits the CEC sysfs discovery and metadata access needed by CEC libraries and selected legacy backends.
The available node depends on the hardware, kernel, and enabled driver; not every system provides all of these paths.

USB-attached serial CEC adapters are not covered by `hdmi-cec`. Use the {ref}`raw-usb interface <interfaces-raw-usb-interface>` for USB device access.

**Auto-connect**: no

This interface has no plug or slot attributes. Hardware access still requires a supported CEC adapter and driver on the system.

The test code can be found in the snapd repository: [hdmi_cec_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/hdmi_cec_test.go).

The source code for the interface is in the snapd repository: [hdmi_cec.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/hdmi_cec.go).
