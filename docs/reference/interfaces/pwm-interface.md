(interfaces-pwm-interface)=
#  pwm interface

The `pwm` interface allows access to a specific PWM channel on a device. The interface is restricted because it provides privileged access to PWM hardware.

Use `snap interface pwm` to see which PWM devices are available on the system:

```
$ snap interface pwm
name: pwm
summary: allows access to specific PWM channel
slots:
- gadget:led-1
- gadget:led-2
- gadget:fan-1
- gadget:fan-2
[...]
```

<h2 id='heading--example'>Example</h2>

With an example snap application called _app_ installed, the following command will connect its PWM interface to the specified PWM device channel:

```
$  snap connect app:activity-led gadget:led-1
```


## Developer details

**Auto-connect**: no
**Attributes**:
* `channel` (slot): PWM device channel number to export and expose to consuming snaps
* `chip-number` (slot): chip base number to export

To use a PWM device, the snap developer must add `plugs:[pwm]` to a snap’s[ snapcraft.yaml](/). The snap user can then access a specific pwm device with an[ interface connection](/t/interface-management/6154#heading--manual-connections).

Unless the snap is expected to actually use a set of PWM channels that is not predefined, it is recommended to define distinct plugs for each used pwm channel, like:

```yaml
plugs:
  activity-led:
    interface: pwm
  warning-led:
    interface: pwm
```

This has the advantage of being self-documenting and 1-1 connections like these are easier to track and setup with[ auto-connections](/), if the latter is needed.

When the interface is connected, `"echo (channel number) > /sys/class/pwm/pwmchipN/export"` is run internally to enable access to the PWM channel.

Once connected, the consuming snap can use the device via `/sys/class/pwm/pwmchipN/pwmX` where _N_ is the base of the PWM chip and _X_ is channel number specified by the connected slot.

Finally, when the interface is disconnected, `"echo (channel number) > /sys/class/pwmchipN/unexport" is run internally to disable access to the PWM channel.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/pwm_test.go

The source code for the pwm interface is in the snapd repository:[ https://github.com/canonical/snapd/blob/master/interfaces/builtin/pwm.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/pwm.go).

