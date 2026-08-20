(interfaces-hardware-observe-interface)=
#  hardware-observe interface

The `hardware-observe` interface allows for getting hardware information from the system.

`hardware-observe` grants read-only access to many files and directories, primarily in `/sys` and `/proc`. Additionally, it provides access to many utility files and binaries such as `lspci`, `lsusb`, and `hwinfo`.

`hardware-observe` is a more general and broad interface. If more specific hardware access is required, such as for GPIO or I2C devices, See the {ref}`gpio <interfaces-gpio-interface>` and {ref}`i2c <interfaces-i2c-interface>` interfaces.


---

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>

### Path access

`hardware-observe` grants **read** access to the following paths:

* **For tools like `hwinfo --short` to get hardware information**:</br>
`/proc/ioports`</br>
`/proc/dma`</br>
`/proc/tty/driver/{,*}`</br>
`/proc/sys/dev/cdrom/info`</br>

* **For tools like `lshw -quiet` to get hardware information**:</br>
`/proc/devices`</br>
`/proc/ide/{,**}`</br>
`/proc/scsi/{,**}`</br>
`/proc/device-tree/{,**}`</br>
`/sys/kernel/debug/usb/devices`</br>
`/proc/sys/abi/{,*}`</br>

* **For tools like `lspci -A linux-sysfs` to get information on files in `/sys`**:</br>
`/sys/{block,bus,class,devices,firmware}/{,**}`

* **For tools like `lspci -A linux-proc` to get information on `/proc`**:</br>
`/bus/pci/{,**}`
`/{,usr/}lib/modprobe.d/{,*}`

* **For tools like `lspci -k` to get information on loaded modules**:</br>
Examples: `/etc/modprobe.d/{,*}`,</br>

* **For tools like `lsusb` to get USB information**:</br>
`/var/lib/usbutils/usb.ids`</br>
`/dev/`</br>
`/dev/bus/usb/{,**/}`</br>
`/etc/udev/udev.conf`</br>
*Note:* lsusb and its database have to be shipped in the snap if not on classic</br>

* **For tools like `sensors` to get sensor information**:</br>
`/etc/sensors3.conf`</br>
`/etc/sensors.d/{,*}`

* **For tools like `udevadm` to get device information**:</br>
`/run/udev/data/**`

* **For  hugepage and transparent_hugepage statuses (but not the pages themselves)**:</br>
`/sys/kernel/mm/{hugepages,transparent_hugepage}/{,**}`</br>

* **For information on available input devices**:</br>
`/proc/bus/input/devices`

* **For power information**:</br>
`/sys/power/{,**}`</br>
`/run/udev/data/+power_supply:*`

* **For interrupts**:</br>
`/proc/interrupts`

* **For  loaded kernel module information**:</br>
`/proc/modules`

* **For VM information**:</br>
`/proc/cpuinfo`</br>
`/proc/sysinfo`</br>
`/proc/xen/capabilities`</br>
`/proc/1/sched`</br>
`/sys/hypervisor/properties/features`</br>
`/sys/hypervisor/type`</br>

* **For container information**:</br>
`/run/systemd/container`</br>

### Binary access

`hardware-observe` grants executable access to the following binaries:
* **For tools provided by `util-linux`**:</br>
`/{,usr/}bin/lsblk`</br>
`/{,usr/}bin/lscpu`</br>
`/{,usr/}bin/lsmem`</br>

* **For tools like `lsusb`**:</br>
`/{,usr/}bin/lsusb`</br>

* **For tools like `systemd-detect-virt`**:</br>
`/{,usr/}bin/systemd-detect-virt`</br>

### Capability access

`hardware-observe` grants the following *capabilities*:

* **For tools like `lscpu` and `lspci -A` to inspect specific PCI access methods**:</br>
`capability sys_rawio`</br>
`capability sys_admin`</br>

### Socket access

`hardware-observe` grants the following *socket access:*

* **For udevadm to read netlink**:</br>
`network netlink raw`</br>

The test code for the interface is in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe_test.go)

The source code for the interface is in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/hardware_observe.go)

