---
myst:
  html_meta:
    description: Reference documentation for the plymouth-replace interface, which lets snaps transition smoothly from the Ubuntu Core boot splash to a graphical interface.
---

(interfaces-plymouth-replace-interface)=
#  plymouth-replace interface

`plymouth-replace` allows a snap to provide a flicker-free transition
from the graphical boot splash screen on an Ubuntu Core device.

**Auto-connect**: no<br/>
**Super-privileged**: yes

Requires snapd version _2.79+_.

## Developer details

Ubuntu Core devices can [enable a graphical boot splash screen][core-splash]
implemented by the [plymouth daemon][plymouth]. The default behaviour
is for the system to return to text mode once the boot up process has
completed.

If the device provides a graphical interface, this can result in
unwanted flicker as the screen switches modes. The `plymouth-replace`
interface allows a snap to provide a smooth transition from the boot
splash to their own interface.

The expectation is that the snap provides a system daemon that will
draw to virtual terminal 1. If the daemon plugs the `plymouth-replace`
interface, it's startup will be sequenced to the end of the boot
process where plymouth would normally quit. It will also prevent
plymouth from quitting at this point, and stop a text mode login
prompt from showing on VT1.

To complete the process some additional work is required from the snap:

1. The snap daemon should run `plymouth deactivate` before generating
   any output. This will instruct the plymouth daemon to stop updating
   the screen.
2. When the snap daemon has first painted the screen, it should run
   `plymouth quit --retain-splash` to instruct the plymouth daemon to
   quit without switching back to text mode.

If the snap daemon fails to start, the system will recover by telling
the plymouth daemon to quit. This will return the system to text mode.

The [Ubuntu Frame snap][ubuntu-frame] uses the interface and can be
used as an example.

[core-splash]: https://documentation.ubuntu.com/core/how-to-guides/image-creation/add-a-splash-screen/
[plymouth]: https://gitlab.freedesktop.org/plymouth/plymouth
[ubuntu-frame]: https://github.com/canonical/ubuntu-frame
