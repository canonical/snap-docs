(interfaces-uinput-interface)=
#  uinput interface

`uinput` allows write access to `/dev/uinput` on the host system for emulating input devices from userspace that can send input events (such as a joystick).

By design, the `/dev/uinput` device allows for arbitrary input injection and its default permissions are the standard `root:root 0660` across Linux distributions.

Third-party software sometimes installs _udev_ rules that change the `/dev/uinput` device permissions to world-writable permissions (`0666`) as a shortcut to allow all system users access.

However, _snapd_ considers world-writable permissions for `/dev/uinput` to be unsafe for most systems because it potentially allows any user with access to the device the ability to inject input events into the kernel.

This means snapd does not install additional _udev_ rules to modify device permissions on behalf of snaps, and consequently, will not interfere with the permissions set by third-party software. As a result, snaps that use this interface will have the same `/dev/uinput` access as other processes on the system.

See [the joystick interface](https://snapcraft.io/docs/reference/interfaces/joystick-interface/) and {ref}`the raw-usb interface <interfaces-raw-usb-interface>` for potential alternatives.

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

Requires snapd version  *2.46+* .


