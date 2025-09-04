(snap-reference-operations-interfaces-hardware-interfaces)=
# Hardware interfaces

Hardware IO (input/output) interfaces, including the [serial-port](/), [gpio](/), [gpio-chardev](/) and [i2c](/) interfaces, are designed to be used on devices running [Ubuntu Core](/t/glossary/14612#heading--ubuntu-core). These interfaces are exposed as _slots_ from a device's [gadget snap](/snap-reference/development/yaml-schemas/the-gadget-snap) which is used to define and configure a device's system properties.

This approach is more robust because it allows the gadget snap providing the slot to centralise and arbitrate the connection conditions. These conditions include which other snaps, identified by their snap ID, can connect to the slots the gadget offers and, consequently, gain privileged access to the hardware.  For the application snap, usually no change is required other than to declare and use an appropriately-configured plug.


The following are exeptions to the above, and can be used without being declared in the gadget snap:
- [gpio-control interface](/)
- [serial-port interface](/) (experimental support)

See [Supported interfaces](/snap-reference/operations/interfaces/index) for a complete list of interfaces.

## Interface considerations

The extent of access an interface has is granted through both _connection permissions_ and the specifics of the _interface connections_ being requested.

1. **Connection permissions**: [auto-connect](/snap-explanation/interfaces/interface-auto-connection) | [privileged](/snap-how-to-guides/work-with-snaps/connect-interfaces) | [super-privileged](/snap-reference/operations/interfaces/super-privileged-interfaces)
   </br>Connection requirements are dependent on which store a developer is using.
     - [Global Snap Store](https://forum.snapcraft.io/t/glossary/14612#heading--snap-store): privileged and super-privileged interfaces require store approval because of the level of trust and permissiveness these interfaces have, which is also why certain interfaces need certain oversight. See [Permission requests](/) for further details.
    * [Dedicated Snap Store](/t/glossary/14612#heading--dedicated): trust and permissiveness are now  the responsibility of the store owner, and many privileged interface connections can be self-served and defined within the dedicated snap store and the device context.
1. **Interface connections**: hardware IO interfaces | app-provided interfaces | other interfaces
    * **Hardware IO interfaces**: These require either a [slot](/t/interface-management/6154#heading--slots-plugs) to be defined by a device's _gadget snap_ or an interface with [Hotplug support](/), in which case the slot appears from the system snap.
      * An unconstrained [auto-connection](/t/the-interface-auto-connection-mechanism/20179#heading--autoconnect) cannot be used because there may be _many slots of a given interface_, resulting in ambiguity that requires  an extensive set of store rules to manage and maintain.
      * Each plug should therefore be connected to a slot, for example:
        * green led plug on app => green led slot on gadget
        * red led plug on app => red led slot on gadget
      - This kind of 1-to-1 connections can usually be established via [slot rules in the snap-declaration](/snap-explanation/interfaces/interface-auto-connection) for the gadget.
    * **App-provided interfaces**: slots are defined by apps, or occasionally from the gadget snap, 
      * May require access, such as from the [content](/) or [shared-memory](/) interfaces.
      * A slot might may be provided by the system snap to cover the case of an equivalent system service, such as [audio-playback](/)
      * the slot might be [super-privileged](/snap-reference/operations/interfaces/super-privileged-interfaces)
    * **Other interfaces**: For more system level access, slots are provided by the system snap.

<h3 id='heading--code-examples'>Code examples</h3>

The [gadget snap](https://github.com/snapcore/pi-gadget/tree/20-arm64) definition for the reference [Raspberry Pi Ubuntu Core](https://ubuntu.com/core/docs/install-raspberry-pi) image contains interface definitions for various hardware IO interfaces on the system, including slots for each specific GPIO pin, i2c connections, the Bluetooth serial port, and the generic serial ports:

```yaml
slots:
  bcm-gpio-0:
    interface: gpio
    number: 0
  bcm-gpio-1:
    interface: gpio
    number: 1
  bcm-gpio-2:
    interface: gpio
    number: 2
[...]
  i2c-0:
    interface: i2c
    path: /dev/i2c-0
[...]
  bt-serial:
    interface: serial-port
    path: /dev/ttyAMA0
[...]
  serial0:
    interface: serial-port
    path: /dev/ttyS0
  serial1:
    interface: serial-port
    path: /dev/ttyS1
```

On a Raspberry Pi, the above hardware IO interfaces are accessible to apps from the system snap without requiring any further configuration.

## Interface list

| Interface | Description | Categories | Auto-connect |
|---|----|---|---|
| [device-buttons](/) | use any device-buttons | Hardware, Developer | no |
| [dsp](/) | enables the control of digital signal processors (DSPs) | Hardware, Developer | no |
| [dvb](/) | allows access to all DVB devices and APIs | Hardware, Developer, [Media](/snap-reference/operations/interfaces/media-interfaces) | no |
| [fpga](/) | permits access to an FPGA subsystem | Hardware, Developer | no |
| [framebuffer](/) | access to universal framebuffer devices | Hardware, Developer | no |
| [gpio](/) | access specific GPIO pins | GPIO, Hardware, Developer | no |
| [gpio-chardev](/) | access specific GPIO chardev lines. | GPIO, Hardware, Developer | no |
| [gpio-memory-control](/) | allows write access to all GPIO memory | GPIO, Hardware, Developer | no |
| [hardware-observe](/) | access hardware information | [System](/snap-reference/operations/interfaces/system-interfaces), Hardware | no |
| [hardware-random-control](/) | provide entropy to hardware random number generator | [System](/snap-reference/operations/interfaces/system-interfaces), Hardware | no |
| [hardware-random-observe](/) | use hardware-generated random numbers | [System](/snap-reference/operations/interfaces/system-interfaces), Hardware | no |
| [i2c](/) | access i²c devices | [System](/snap-reference/operations/interfaces/system-interfaces), Hardware | no |
| [iio](/) | access IIO devices | [System](/snap-reference/operations/interfaces/system-interfaces), Hardware | no |
| [intel_qat](/) | provides permissions for Intel QAT devices | [Hardware](/snap-reference/operations/interfaces/hardware-interfaces) | no  |
| [joystick](/) | use any connected joystick | Hardware, Developer | no |
| [media-control](/t/the-media-control-interface/26504/) | access media control devices and Video4Linux (V4L) devices | Hardware, Developer, [Media](/snap-reference/operations/interfaces/media-interfaces), Video | no |
| [optical-drive](/) | read/write access to CD/DVD drives | Storage, Hardware, Developer | yes, unless drive can write |
| [pwm](/) | access specific PWM channels | [System](/snap-reference/operations/interfaces/system-interfaces), Developer, Hardware, WIP | no |
| [raw-input](/) | access raw input devices directly | [System](/snap-reference/operations/interfaces/system-interfaces), Developer, Hardware | no |
| [raw-usb](/) | access USB hardware directly | [System](/snap-reference/operations/interfaces/system-interfaces), Developer, Hardware | no |
| [serial-port](/) | access serial port hardware | [System](/snap-reference/operations/interfaces/system-interfaces), Developer, Hardware | no by default, yes with snaps from the same publisher |
| [spi](/) | access specific SPI devices | [System](/snap-reference/operations/interfaces/system-interfaces), Developer, Hardware | no |
| [u2f-devices](/t/the-u2f-devices-interface/9722/) | use any U2F devices | [Security](/snap-reference/operations/interfaces/security-interfaces), Hardware, Developer | no |
| [uhid](/) | create kernel UID devices from user-space | Hardware, Kernel, [System](/snap-reference/operations/interfaces/system-interfaces) | no |
| [uinput](/) | allows write access to /dev/uinput | [Super privileged](/snap-reference/operations/interfaces/super-privileged-interfaces), Hardware | no |
| [uio](/) | access uio devices | Hardware, [System](/snap-reference/operations/interfaces/system-interfaces) | no |

