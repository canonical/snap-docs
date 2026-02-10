# Interfaces

[Interfaces](/explanation/all-about-interfaces) enable resources from one snap to be shared with another and with the system. The table below lists currently supported interfaces, with links to further details for each interface.

The following column names are used:

- **Interface** is the syntactical interface name, as used by snaps.

- **Description** is a brief overview of what the interface permits. Select the interface name to open the interface-specific page for a more detailed description on each interface.

- **Categories** are used to split interfaces into broad types, and also to indicate what kind of access they permit. Video, graphics and audio are typical desktop requirements, for example, while VM, Container, Kernel and Developer imply more specific roles. The Ubuntu Core category is used to denote when an interface is intended for [Ubuntu Core](https://forum.snapcraft.io/t/glossary/14612#heading--ubuntu-core), and _Super privileged_ is used when an interface requires extra security scrutiny. See [Super-privileged interfaces](/explanation/interfaces/super-privileged-interfaces) for more information.

- **Auto-connect** indicates that the interface will be connected by default when the snap is first installed, requiring no further user action. If `Auto-connect=no`, an interface can still be automatically connected if the snap developer has requested, and been granted, explicit permission. See [Interface connection mechanism](/explanation/interface-auto-connection) for details.

---

| Interface | Description | Categories | Auto-connect |
|---|----|---|---|
| [accel-interface](accel-interface) | permits access to the Linux compute accelerators subsystem | System | yes |
| [account-control](account-control-interface) | add/remove user accounts or change passwords | System, Account | no |
| [accounts-service](accounts-service-interface) | allows communication with the accounts service | System, Account | no |
| [acrn](acrn-interface) | allows access to user VMs using the ACRN hypervisor | VM, Hypervisor, Developer | no |
| [adb-support](adb-support-interface) | allows operating as Android Debug Bridge service | ADB, Developer | no |
| [allegro-vcu](allegro-vcu-interface) | access the Allegro Video Core Unit | Video, Graphics | no |
| [alsa](alsa-interface) | play or record sound | Audio, Media | no |
| [appstream-metadata](appstream-metadata-interface) | allows access to AppStream metadata | System, Developer, Manage software | no |
| [audio-playback](audio-playback-interface) | allows audio playback via supporting services | Audio, Media, Playback | yes |
| [audio-record](audio-record-interface) | allows audio recording via supported services | Audio, Media, Record | no |
| [auditd-support](auditd-support-interface) | permits snaps to operate as the auditd service on the system | Super privileged | no |
| [autopilot-introspection](autopilot-introspection-interface) | be controlled by Autopilot software | System, Developer | no |
| [avahi-control](avahi-control-interface) | advertise services over the local network | Network, Local network, Nearby devices | no |
| [avahi-observe](avahi-observe-interface) | detect services and devices over the local network | Network, Local network, Nearby devices | no |
| [block-devices](block-devices-interface) | access to disk block devices | Super privileged, Storage, Low level | no |
| [bluetooth-control](bluetooth-control-interface) | access Bluetooth hardware directly | Network, Bluetooth, Nearby devices | no |
| [bluez](bluez-interface) | use Bluetooth devices | Network, Bluetooth, Nearby devices | no |
| [bool-file](bool-file-interface) | allows access to specific file with bool semantics | System, Low level, Privileged | no |
| [broadcom-asic-control](broadcom-asic-control-interface) | control Broadcom network switches | Network, System | no |
| [browser-support](browser-support-interface) | use functions essential for Web browsers | Browser, Network | no when allow-sandbox: true, yes otherwise |
| [calendar-services](calendar-services-interface) | allows communication with Evolution Data Server calendar | Personal data, Contacts and calendar | no |
| [camera](camera-interface) | use your camera or webcam | Camera, Media, Personal data | no |
| [can-bus](can-bus-interface) | allows access to the CAN bus | System, Developer | no |
| [checkbox-support](checkbox-support-interface) | access for the Canonical checkbox test and certification system | Super privileged | no |
| [cifs-mount](cifs-mount-interface) | allows the mounting and unmounting of CIFS filesystems | Network,Storage | no |
| [classic-support](classic-support-interface) | enable resource access to classic snap | Super privileged, Ubuntu Core | no |
| [confdb](confdb-interface) | permit access confdb configuration system | System | no |
| [contacts-service](contacts-service-interface) | allows communication with the Evolution Data Server address book | Personal data, Contacts and calendar| no |
| [content](content-interface) | access resources across snaps | Storage, Files, Attributes | yes for snaps from same publisher, no otherwise |
| [core-support](core-support-interface) | deprecated since snap 2.34 | System, Other | no |
| [cpu-control](cpu-control-interface) | set certain CPU values | System, Developer | no |
| [cuda-driver-libs](cuda-driver-libs-interface) | permits access to CUDA acceleration on Nvidia GPUs | System | no |
| [cups-control](cups-control-interface) | access to the CUPS control socket to configure printing | Printing | no |
| [cups](cups-interface) | access to the CUPS socket for printing | Printing | not applicable |
| [custom-device](custom-device-interface) | permits access to a specific class of device | Super privileged, Ubuntu Core | no |
| [daemon-notify](daemon-notify-interface) | allows sending daemon status changes to service manager | System, Developer | no |
| [dbus](dbus-interface) | allow snaps to communicate over D-Bus | System, Developer | no |
| [dcdbas-control](dcdbas-control-interface) | shut down or restart Dell devices | Developer | no |
| [desktop](desktop-interface) | provides access to common desktop elements | Desktop | yes |
| [desktop-launch](desktop-launch-interface) | identify and launch desktop apps from other snaps | Super privileged, Desktop | no |
| [desktop-legacy](desktop-legacy-interface) | enables the use of legacy desktop methods (including input method and accessibility services) | Desktop | yes |
| [device-buttons](device-buttons-interface) | use any device-buttons | Hardware, Developer | no |
| [display-control](display-control-interface) | allows configuring display parameters | Display, Graphics | no |
| [dm-crypt](dm-crypt-interface) | access encrypted storage devices | Super privileged, Ubuntu Core, Storage | no |
| [dm-multipath](dm-multipath-interface) | access device-mapper multipath maps though the multipathd daemon | Super privileged, Ubuntu Core, Storage | no |
| [docker](docker-interface) | start, stop, or manage Docker containers | Super privileged, Containers | no |
| [docker-support](docker-support-interface) | allows operating as the Docker daemon | Super privileged, Containers | no |
| [dsp](dsp-interface) | enables the control of digital signal processors (DSPs) | Hardware, Developer | no |
| [dvb](dvb-interface) | allows access to all DVB devices and APIs | Hardware, Developer, Media | no |
| [egl-driver](egl-driver-interface) | access to EGL the graphics sub-system | Under development | no |
| [empty](empty-interface) | allows testing without additional permissions | System, Other | no |
| [firewall-control](firewall-control-interface) | configure a network firewall | Network | no |
| [firmware-update-support](firmware-updater-support-interface) | allows a snap to operate as the Firmware Updater | Super privileged | no |
| [fpga](fpga-interface) | permits access to an FPGA subsystem | Hardware, Developer | no |
| [framebuffer](framebuffer-interface) | access to universal framebuffer devices | Hardware, Developer | no |
| [fuse-support](fuse-support-interface) | enables access to the FUSE filesystems | Storage | no |
| [fwupd](fwupd-interface) | allows operating as the fwupd service | System, Security, Firmware | no |
| [gbm-driver-libs](gbm-driver-libs-interface) | exposes GBM driver libraries to the system | Super privileged | no |
| [gconf](gconf-interface) | access the legacy GConf config system | System, Developer, Settings | no |
| [gpg-keys](gpg-keys-interface) | read GPG user configuration and keys | GPG, Personal data, Security | no |
| [gpg-public-keys](gpg-public-keys-interface) | read GPG non-sensitive configuration and public keys | GPG, Personal data, Security | no |
| [gpio](gpio-interface) | access specific GPIO pins | GPIO, Hardware, Developer | no |
| [gpio-chardev](gpio-chardev-interface) | permits access to specific GPIO chardev lines | Hardware | no |
| [gpio-control](gpio-control-interface) | allows to export/unexport and control all GPIOs | Super privileged, GPIO | no |
| [gpio-memory-control](gpio-memory-control-interface) | allows write access to all GPIO memory | GPIO, Hardware, Developer | no |
| [greengrass-support](greengrass-support-interface) | allows operating as the Greengrass service | Super privileged, Edge, AWS, Discrete | no |
| [gsettings](gsettings-interface) | provides access to any GSettings item for current user | System, Developer, Settings | yes |
| [hardware-observe](hardware-observe-interface) | access hardware information | System, Hardware | no |
| [hardware-random-control](hardware-random-control-interface) | provide entropy to hardware random number generator | System, Hardware | no |
| [hardware-random-observe](hardware-random-observe-interface) | use hardware-generated random numbers | System, Hardware | no |
| [hidraw](hidraw-interface) | access hidraw devices | System | no |
| [home](home-interface) | access non-hidden files in the home directory | Storage, Personal data | yes on classic (traditional distributions), no otherwise |
| [hostname-control](hostname-control-interface) | allows configuring the system hostname | Network | no |
| [hugepages-control](hugepages-control-interface) | control HugePages memory blocks | System, Memory, Kernel | no |
| [i2c](i2c-interface) | access i²c devices | System, Hardware | no |
| [iio](iio-interface) | access IIO devices | System, Hardware | no |
| [intel-mei](intel-mei-interface) | access to the Intel MEI management interface | System, Firmware | no |
| [intel-qat](intel-qat-interface) | provides permissions for Intel QAT devices | Hardware | no  |
| [io-ports-control](io-ports-control-interface) | allows access to all I/O ports | System, | no |
| [ion-memory-control](ion-memory-control-interface) | access Android's ION memory allocator | Super privileged, System  | no |
| [iscsi-initiator](iscsi-initiator-interface) |  discover, connect to, and manage iSCSI targets for block storage access | Super privileged | no |
| [jack1](jack1-interface) | allows interaction with the JACK audio connection server | Audio, Media | no |
| [joystick](joystick-interface) | use any connected joystick | Hardware, Developer | no |
| [juju-client-observe](juju-client-observe-interface) | read the Juju client configuration | Developer, Discrete | no |
| [kerberos-tickets](kerberos-tickets-interface) | access Kerberos tickets in /tmp | Under development | no |
| [kernel-crypto-api](kernel-crypto-api-interface) | read and manage kernel supported crypto ciphers | System, Kernel, Security | no |
| [kernel-firmware-control](kernel-firmware-control-interface) | permits a custom kernel firmware search path | Super privileged | no |
| [kernel-module-control](kernel-module-control-interface) | insert, remove and query kernel modules | Super privileged, System, Kernel | no |
| [kernel-module-load](kernel-module-load-interface) | load, or deny loading, specific kernel modules | Super privileged, System, Kernel | no |
| [kernel-module-observe](kernel-module-observe-interface) | query kernel modules | System, Kernel | no |
| [kubernetes-support](kubernetes-support-interface) | use functions essential for Kubernetes | Super privileged, Hypervisor, Discrete | no |
| [kvm](kvm-interface) | allows access to the kvm device | VM, Hypervisor, Developer | no |
| [libvirt](libvirt-interface) | provides access to the libvirt service | VM, Hypervisor, Developer | no |
| [locale-control](locale-control-interface) | change system language and region settings | Language and region, Personalisation | no |
| [location-control](location-control-interface) | allows operating as the location service | Location | no |
| [location-observe](location-observe-interface) | access your location | Location | no |
| [log-observe](log-observe-interface) | read system logs | System, Developer | no |
| [login-session-control](login-session-control-interface) | allows setup of login sessions and grants privileged access to user sessions | System, Security | no |
| [login-session-observe](login-session-observe-interface) | allows reading login and session information | System, Security | no |
| [lxd](lxd-interface) | provides access to the LXD socket | Super privileged, Container, Discrete | no |
| [lxd-support](lxd-support-interface) | allows operating as the LXD service | Super privileged, Container, Discrete | no |
| [maliit](maliit-interface) | use an on-screen keyboard | Developer | no |
| [media-control](media-control-interface) | access media control devices and Video4Linux (V4L) devices | Hardware, Developer, Media, Video | no |
| [media-hub](media-hub-interface) | access snaps providing the media-hub interface | Developer, Media | yes |
|  [microceph](microceph-interface) |  permits access to the MicroCeph socket, which is used internally by the microceph snap | Super privileged, Container | no |
| [microceph-support](microceph-support-interface) | permits the microceph snap to operate as the MicroCeph service | Super privileged, Container | no |
| [microovn](microovn-interface) | used only by the MicroOVN snap for socket access | Network, Super privileged | no |
| [microstack-support](microstack-support-interfacet/the-microstack-support-interface/26505/) | multiple service access to the Microstack infrastructure | Super privileged, Container, Discrete | no |
| [mir](mir-interface) | enables access to the Mir display service | Display | yes |
| [modem-manager](modem-manager-interface) | use and configure modems | Network | no |
| [mount-control](mount-control-interface) | mount and unmount transient and persistent filesystem mount points | Super privileged, Storage | no |
| [mount-observe](mount-observe-interface) | read mount table and quota information | Storage | no |
| [mpris](mpris-interface) | media key control of music and video players | Sound | no |
| [multipass-support](multipass-support-interface) | multipass-support allows operating as the Multipass service | Super privileged, VM, Discrete | no |
| [netlink-audit](netlink-audit-interface) | allows access to kernel audit system through Netlink | Inter-process communication (IPC), Netlink, Developer | no |
| [netlink-connector](netlink-connector-interface) | communicate through the kernel Netlink connector | Inter-process communication (IPC), Netlink, Developer | no |
| [netlink-driver](netlink-driver-interface) | operate a kernel driver module exposed via Netlink | Inter-process communication (IPC), Netlink, Developer | no |
| [network](network-interface) | enables network access | Network | yes |
| [network-bind](network-bind-interface) | operate as a network service | Network | yes |
| [network-control](network-control-interface) | change low-level network settings | Network | no |
| [network-manager](network-manager-interface) | configure and observe networking via NetworkManager | Network | no |
| [network-manager-observe](network-manager-observe-interface) | allows observing NetworkManager settings | Network | no |
| [network-observe](network-observe-interface) | query network status information | Network | no |
| [network-setup-control](network-setup-control-interface) | change network settings via Netplan | Network | no |
| [network-setup-observe](network-setup-observe-interface) | read network settings | Network | no |
| [network-status](network-status-interface) | access the NetworkStatus service | Network | yes |
| [nfs-mount](nfs-mount-interface) | allows the mounting and unmounting of Network File System mount points | Network, Service | no |
| [nomad-support](nomad-support-interface) |  enable's HashiCorp's Nomad to access CPU and memory management | System, Containers, Service | no |
| [nvidia-drivers-support](nvidia-drivers-support-interface) | internally used NVIDIA access | Super privileged, Ubuntu Core | no |
| [nvme-control](nvme-control-interface) | manage and access NVMe controllers | Super privileged | no |
| [ofono](ofono-interface) | allows operating as the oFono service | Network, Discrete, Developer | no |
| [online-accounts-service](online-accounts-service-interface) | access to the Online Accounts service | Service, Developer | yes |
| [opengl](opengl-interface) | access OpenGL/GPU hardware | Display, Graphics | yes |
| [opengl-driver-libs](opengl-driver-libs-interface) | exposes OpenGL driver libraries to the system | Super privileged | no |
| [opengles-driver-libs](opengles-driver-libs-interface) | exposes OpenGLES driver libraries to the system | Super privileged | no |
| [openvswitch](openvswitch-interface) | control Open vSwitch hardware | Network, Service, Developer | no |
| [openvswitch-support](openvswitch-support-interface) | enables kernel support for Open vSwitch | Network, Service, Developer | no |
| [optical-drive](optical-drive-interface) | read/write access to CD/DVD drives | Storage, Hardware, Developer | yes, unless drive can write |
| [packagekit-control](packagekit-control-interface) | control the PackageKit service | Super privileged, Packaging | no |
| [password-manager-service](password-manager-service-interface) | read, add, change, or remove saved passwords | System, Security | no |
| [pcscd](pcscd-interface) | permits communication with PCSD smart card daemon | Security | no |
| [personal-files](personal-files-interface) | read or write files in the user's home directory | Super privileged, Personal data, Attributes | no |
| [physical-memory-control](physical-memory-control-interface) | read and write memory used by any process | System, Memory, Kernel | no |
| [physical-memory-observe](physical-memory-observe-interface) | read memory used by any process | System, Memory, Kernel | no |
| [pipewire](pipewire-interface) | access the PipeWire server | Audio, Media, Video | no |
| [pkcs11](pkcs11-interface) |  enables the cryptographic token interface standard to be used | Security, Super privileged | no |
| [polkit](polkit-interface) | access to the polkit authorisation manager | Security, System, Super privileged | no |
| [polkit-agent](polkit-agent-interface) | permits applications to register as _polkit_ agents | Security, System, Super privileged | no |
| [posix-mq](posix-mq-interface) | enables inter-process communication (IPC) messages | Super privileged, IPC | no by default, yes with snaps from the same publisher |
| [power-control](power-control-interface) | read and write system power settings | System, Power | no |
| [ppp](ppp-interface) | access to configure and observe PPP networking | Network | no |
| [process-control](process-control-interface) | pause or end any process on the system | System | no |
| [ptp](ptp-interface) | access to the Precision Time Protocol subsystem | System, Developer | no |
| [pulseaudio](pulseaudio-interface) | play and record sound | Audio, Media | no |
| [pwm](pwm-interface) | access specific PWM channels | System, Developer, Hardware, WIP | no |
| [pwm-control](pwm-control-interface) | permits control over any aspect of all PWM channels | Super privileged | no |
| [qualcomm-ipc-router](qualcomm-ipc-router-interface) | access Qualcomm IPC router sockets | IPC, Kernel, System | no |
| [raw-input](raw-input-interface) | access raw input devices directly | System, Developer, Hardware | no |
| [raw-usb](raw-usb-interface) | access USB hardware directly | System, Developer, Hardware | no |
| [raw-volume](raw-volume-interface) | access specific disk partitions | Storage | no |
| [remoteproc](remoteproc-interface) | interact with the kernel's Remote Processor Framework  |Super privileged | no |
| [removable-media](removable-media-interface) | read/write files on removable storage devices | Storage | no |
| [ros-opt-data](ros-opt-data-interface) | read-only access to ROS directories | Storage | no |
| [ros-snapd-support](ros-snapd-support-interface) | allows the snaps ros-snapd and ros2-snapd the use of snapd’s apps control API | Super privileged | no |
| [screen-inhibit-control](screen-inhibit-control-interface) | prevent screen sleep, lock and screensaver | Display | yes |
| [screencast-legacy](screencast-legacy-interface) | allows screen recording and audio recording alongside writing to arbitrary filesystem paths | Legacy | no |
| [scsi-generic](scsi-generic-interface) | read and write access to SCSI Generic driver devices | Storage, Super privileged | no |
| [sd-control](sd-control-interface) | control SD cards on specific devices | Super privileged, Storage | no |
| [serial-port](serial-port-interface) | access serial port hardware | System, Developer, Hardware | no |
| [shared-memory](shared-memory-interface) | enables two snaps to access the same shared memory | Super privileged, IPC | no by default, yes with snaps from the same publisher |
| [shutdown](shutdown-interface) | restart or power off the device | Super privileged, System, Power | no |
| [snap-fde-control](snap-fde-control-interface) | allows access to the FDE subset of snapd’s system-volumes API | Super privileged | no |
| [snap-interfaces-requests-control](snap-interfaces-requests-control-interface) | enables the prompting API and its access to prompting-related notice types | System | no |
| [snap-refresh-control](snap-refresh-control-interface) | permits bespoke snap refresh control | Super privileged, Packaging | no |
| [snap-refresh-observe](snap-refresh-observe-interface) | enables the tracking of snap refreshes | Super privileged, Packaging | no |
| [snap-themes-control](snap-themes-control-interface) | permits the use of snapd’s theme installation API | Super privileged | no |
| [snapd-control](snapd-control-interface) | install or remove software | Super privileged, Packaging | no |
| [spi](spi-interface) | access specific SPI devices | System, Developer, Hardware | no |
| [ssh-keys](ssh-keys-interface) | access SSH private and public keys | Security | no |
| [ssh-public-keys](ssh-public-keys-interface) | access SSH public keys | Security | no |
| [steam-support](steam-support-interface) | allows the Steam snap to access pressure-vessel containers | Super privileged, Discrete | no |
| [storage-framework-service](storage-framework-service-interface) | operate as, or interact with, the Storage Framework | Storage | no |
| [system-backup](system-backup-interface) | read-only access to the system for backups | Storage | no |
| [system-files](system-files-interface) | read or write files in the system | Super privileged, Storage, Attributes | no |
| [system-observe](system-observe-interface) | read process and system information | Monitoring, System | no |
| [system-packages-doc](system-packages-doc-interface) | access system documentation in /usr/share/doc | Developer | no |
| [system-source-code](system-source-code-interface) | access kernel source and headers in /usr/src | Developer | no |
| [system-trace](system-trace-interface) | monitor or control any running program | Monitoring, System | no |
| [tee](tee-interface) | permits access to the Trusted Execution Environment | Super privileged, Security, Ubuntu Core | no |
| [thumbnailer-service](thumbnailer-service-interface) | create thumbnail images from local media files | Storage, Media | no |
| [time-control](time-control-interface) | change the date and time | Time | no |
| [timeserver-control](timeserver-control-interface) | change time server settings | Time | no |
| [timezone-control](timezone-control-interface) | change the time zone | Time | no |
| [tpm](tpm-interface) | allows access to the Trusted Platform Module device | Kernel, Security | no |
| [u2f-devices](u2f-devices-interfacet/the-u2f-devices-interface/9722/) | use any U2F devices | Security, Hardware, Developer | no |
| [ubuntu-pro-control](ubuntu-pro-control-interface) | control the Ubuntu Pro desktop daemon | Super privileged, System | no |
| [ubuntu-download-manager](ubuntu-download-manager-interface) | use the Ubuntu Download Manager | System, Developer, Manage software | yes |
| [udisks2](udisks2-interface) | access the UDisks2 service | Storage | no |
| [uhid](uhid-interface) | create kernel UID devices from user-space | Hardware, Kernel, System | no |
| [uinput](uinput-interface) | allows write access to /dev/uinput | Super privileged, Hardware | no |
| [uio](uio-interface) | access uio devices | Hardware, System | no |
| [unity7](unity7-interface) | access legacy desktop resources from Unity7 | Display | yes |
| [unity8](unity8-interface) | share data with other Unity 8 apps | Display, Super privileged | yes |
| [unity8-calendar](unity8-calendar-interface) | read/change shared calendar events in Ubuntu Unity 8 | Personal data | no |
| [unity8-contacts](unity8-contacts-interface) | read/change shared contacts in Ubuntu Unity 8 | Personal data | no |
| [upower-observe](upower-observe-interface) | access battery level and power usage | System, Power | yes |
| [usb-gadget](usb-gadget-interface) | allows snaps to access the USB Gadget API using configfs | Ubuntu Core | no |
| [userns](userns-interface) | permits a snap to create a new namespace | Super privileged | no |
| [vcio](vcio-interface) | access a Raspberry Pi's VideoCore multimedia processor | Video, Graphics, Ubuntu Core | no |
| [wayland](wayland-interface) | access compositors providing the Wayland protocol | Display | yes |
| [x11](x11-interface) | monitor mouse/keyboard input and graphics output of other apps | Display | yes |
| [xilinx-dma](xilinx-dma-interface) | allows access to Xilinx DMA IP from a connected PCIe card | Ubuntu Core, Super privileged | no |


```{toctree}
:titlesonly:
:maxdepth: 2
:glob:

*
