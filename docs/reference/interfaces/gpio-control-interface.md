(interfaces-gpio-control-interface)=
# The gpio-control interface

The `gpio-control` interface provides privileged access to all aspects of GPIO pins. For accessing specific GPIO pins with limited scope, see [The gpio interface](/interfaces/gpio-interface) instead.

Due to its wide-ranging access, it is a [super-privileged interface](/), and as such, is restricted by default. This interface requires modification of its snap declaration for distribution via the Snap Store.

This interface is used for:

* Fine-grained control of GPIO pins (input and output).  
* Building custom hardware interfaces, such as LEDs, relays, or sensors.  
* Low-level interaction with GPIO hardware using character devices or sysfs.

## **Developer Details**

**[Auto-connect](/t/interface-management/6154#heading--auto-connections)**: no</br>
**[Super-privileged](/)**: yes</br>

## **Path Access**

The `gpio-control` interface grants read-write access to the following paths:

1. Sysfs Interface:  
* `/sys/class/gpio/` paths for exporting, setting direction, toggling values, and more:  
  * `/sys/class/gpio/{,un}export`  
  * `/sys/class/gpio/gpio\[0-9\]\*/{active\_low,direction,value,edge}`  
* Additional symlink paths (platform-specific):  
  * `/sys/devices/platform/\*\*/gpio/gpio\[0-9\]\*/{active\_low,direction,value,edge} `
2. Gpiochip Interface:  
* `/dev/gpiochip\[0-9\]\` paths for direct hardware interaction through the _gpiod_ API.

The following UDev rules are applied to enable device access:

* `SUBSYSTEM=="gpio", KERNEL=="gpiochip[0-9]*"`

Requires snapd version 2.41+. `gpoichip\*` access requires snapd version 2.65+.

The following is an example of a snapcraft.yaml configuration for the GPIO control interface, following the descriptive interface reference practice for clarity:

```yaml
name: gpio-control-app
version: '1.0'
summary: An example snap for controlling GPIO pins
description: |
  This snap demonstrates how to use the GPIO Control interface to manage GPIO hardware for custom applications.

grade: stable
confinement: strict

plugs:
  gpio-pins-control:
    interface: gpio-control

apps:
  gpio-app:
    command: bin/gpio-app
    plugs:
      - gpio-pins-control
```

After building and installing the snap, use the following command to connect the interface manually:

```
sudo snap connect gpio-control-app:gpio-pins-control
```

This ensures clarity and aligns with the best practices for naming interface references when using `snap connections`, `snap interfaces`, `snap connect`, or `snap disconnect`.

* The source code for the GPIO Control interface is in the snapd repository: [gpio\_control.go](https://github.com/snapcore/snapd/blob/master/interfaces/builtin/gpio_control.go)  
* For further testing details, see: [gpio\_control\_test.go](https://github.com/snapcore/snapd/blob/master/interfaces/builtin/gpio_control_test.go)

