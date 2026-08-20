---
myst:
  html_meta:
    description: Every snap interface in a single place. Learn about the interfaces available to snap users and snap package developers, including how they work, how to use them, and how to manage them.
---

(ref-index_interfaces)=
# Interfaces

{ref}`Interfaces <explanation-interfaces-all-about-interfaces>` enable resources from one snap to be shared with another and with the system. The table below lists currently supported interfaces, with links to further details for each interface.

The following column names are used:

- **Interface** is the syntactical interface name, as used by snaps.

- **Description** is a brief overview of what the interface permits. Select the interface name to open the interface-specific page for a more detailed description on each interface.

- **Categories** are used to split interfaces into broad types, and also to indicate what kind of access they permit. Video, graphics and audio are typical desktop requirements, for example, while VM, Container, Kernel and Developer imply more specific roles. The Ubuntu Core category is used to denote when an interface is intended for {ref}`Ubuntu Core <ref-glossary_ubuntu-core>`, and _Super privileged_ is used when an interface requires extra security scrutiny. See {ref}`Super-privileged interfaces <reference-operations-interfaces-super-privileged-interfaces>` for more information.

- **Auto-connect** indicates that the interface will be connected by default when the snap is first installed, requiring no further user action. If `Auto-connect=no`, an interface can still be automatically connected if the snap developer has requested, and been granted, explicit permission. See {ref}`Interface connection mechanism <explanation-interfaces-all-about-interfaces>` for details.

---

| Interface | Description | Categories | Auto-connect |
|---|----|---|---|
| {ref}`accel-interface <interfaces-accel>` | permits access to the Linux compute accelerators subsystem | System | yes |
| {ref}`account-control <interfaces-account-control-interface>` | add/remove user accounts or change passwords | System, Account | no |
| {ref}`accounts-service <interfaces-accounts-service-interface>` | allows communication with the accounts service | System, Account | no |
| {ref}`acrn <interfaces-adb-support-interface>` | allows access to user VMs using the ACRN hypervisor | VM, Hypervisor, Developer | no |
| {ref}`adb-support <interfaces-adb-support-interface>` | allows operating as Android Debug Bridge service | ADB, Developer | no |
| {ref}`allegro-vcu <interfaces-allegro-vcu-interface>` | access the Allegro Video Core Unit | Video, Graphics | no |
| {ref}`alsa <interfaces-alsa-interface>` | play or record sound | Audio, Media | no |
| {ref}`appstream-metadata <interfaces-appstream-metadata-interface>` | allows access to AppStream metadata | System, Developer, Manage software | no |
| {ref}`audio-playback <interfaces-audio-playback-interface>` | allows audio playback via supporting services | Audio, Media, Playback | yes |
| {ref}`audio-record <interfaces-audio-record-interface>` | allows audio recording via supported services | Audio, Media, Record | no |
| {ref}`auditd-support <interfaces-auditd-support>` | permits snaps to operate as the auditd service on the system | Super privileged | no |
| {ref}`autopilot-introspection <interfaces-autopilot-introspection-interface>` | be controlled by Autopilot software | System, Developer | no |
| {ref}`avahi-control <interfaces-avahi-control-interface>` | advertise services over the local network | Network, Local network, Nearby devices | no |
| {ref}`avahi-observe <interfaces-avahi-observe-interface>` | detect services and devices over the local network | Network, Local network, Nearby devices | no |
| {ref}`block-devices <interfaces-block-devices-interface>` | access to disk block devices | Super privileged, Storage, Low level | no |
| {ref}`bluetooth-control <interfaces-bluetooth-control-interface>` | access Bluetooth hardware directly | Network, Bluetooth, Nearby devices | no |
| {ref}`bluez <interfaces-bluez-interface>` | use Bluetooth devices | Network, Bluetooth, Nearby devices | no |
| {ref}`bool-file <interfaces-bool-file-interface>` | allows access to specific file with bool semantics | System, Low level, Privileged | no |
| {ref}`broadcom-asic-control <interfaces-broadcom-asic-control-interface>` | control Broadcom network switches | Network, System | no |
| {ref}`browser-support <interfaces-browser-support-interface>` | use functions essential for Web browsers | Browser, Network | no when allow-sandbox: true, yes otherwise |
| {ref}`calendar-services <interfaces-calendar-service-interface>` | allows communication with Evolution Data Server calendar | Personal data, Contacts and calendar | no |
| {ref}`camera <interfaces-camera-interface>` | use your camera or webcam | Camera, Media, Personal data | no |
| {ref}`can-bus <interfaces-can-bus-interface>` | allows access to the CAN bus | System, Developer | no |
| {ref}`checkbox-support <ref-checkbox-support-interface_checkbox-support-interface>` | access for the Canonical checkbox test and certification system | Super privileged | no |
| {ref}`cifs-mount <interfaces-cifs-mount-interface>` | allows the mounting and unmounting of CIFS filesystems | Network,Storage | no |
| {ref}`classic-support <interfaces-classic-support-interface>` | enable resource access to classic snap | Super privileged, Ubuntu Core | no |
| {ref}`confdb <interfaces-confdb>` | permit access confdb configuration system | System | no |
| {ref}`contacts-service <interfaces-contacts-service-interface>` | allows communication with the Evolution Data Server address book | Personal data, Contacts and calendar| no |
| {ref}`content <interfaces-content-interface>` | access resources across snaps | Storage, Files, Attributes | yes for snaps from same publisher, no otherwise |
| {ref}`core-support <interfaces-core-support-interface>` | deprecated since snap 2.34 | System, Other | no |
| {ref}`cpu-control <interfaces-cpu-control-interface>` | set certain CPU values | System, Developer | no |
| {ref}`cuda-driver-libs <interfaces-cuda-driver-libs>` | permits access to CUDA acceleration on Nvidia GPUs | System | no |
| {ref}`cups-control <interfaces-cups-control-interface>` | access to the CUPS control socket to configure printing | Printing | no |
| {ref}`cups <interfaces-cups-interface>` | access to the CUPS socket for printing | Printing | not applicable |
| {ref}`custom-device <interfaces-custom-device-interface>` | permits access to a specific class of device | Super privileged, Ubuntu Core | no |
| {ref}`daemon-notify <interfaces-daemon-notify-interface>` | allows sending daemon status changes to service manager | System, Developer | no |
| {ref}`dbus <interfaces-dbus-interface>` | allow snaps to communicate over D-Bus | System, Developer | no |
| {ref}`dcdbas-control <interfaces-dcdbas-control-interface>` | shut down or restart Dell devices | Developer | no |
| {ref}`desktop <interfaces-desktop-interface>` | provides access to common desktop elements | Desktop | yes |
| {ref}`desktop-launch <interfaces-desktop-launch-interface>` | identify and launch desktop apps from other snaps | Super privileged, Desktop | no |
| {ref}`desktop-legacy <interfaces-desktop-legacy-interface>` | enables the use of legacy desktop methods (including input method and accessibility services) | Desktop | yes |
| {ref}`device-buttons <interfaces-device-buttons-interface>` | use any device-buttons | Hardware, Developer | no |
| {ref}`display-control <interfaces-display-control-interface>` | allows configuring display parameters | Display, Graphics | no |
| {ref}`dm-crypt <interfaces-dm-crypt-interface>` | access encrypted storage devices | Super privileged, Ubuntu Core, Storage | no |
| {ref}`dm-multipath <ref-dm-multipath-interface_dm-multipath-interface>` | access device-mapper multipath maps though the multipathd daemon | Super privileged, Ubuntu Core, Storage | no |
| {ref}`docker <interfaces-docker-interface>` | start, stop, or manage Docker containers | Super privileged, Containers | no |
| {ref}`docker-support <interfaces-docker-support-interface>` | allows operating as the Docker daemon | Super privileged, Containers | no |
| {ref}`dsp <interfaces-dsp-interface>` | enables the control of digital signal processors (DSPs) | Hardware, Developer | no |
| {ref}`dvb <interfaces-dvb-interface>` | allows access to all DVB devices and APIs | Hardware, Developer, Media | no |
| {ref}`egl-driver-libs] <interfaces-egl-driver-libs>` | access to EGL the graphics sub-system | Under development | no |
| {ref}`empty <interfaces-empty-interface>` | allows testing without additional permissions | System, Other | no |
| {ref}`firewall-control <interfaces-firewall-control-interface>` | configure a network firewall | Network | no |
| {ref}`firmware-update-support <ref-firmware-updater-support-interface_firmware-updater-support-interface>` | allows a snap to operate as the Firmware Updater | Super privileged | no |
| {ref}`fpga <interfaces-fpga-interface>` | permits access to an FPGA subsystem | Hardware, Developer | no |
| {ref}`framebuffer <interfaces-framebuffer-interface>` | access to universal framebuffer devices | Hardware, Developer | no |
| {ref}`fuse-support <interfaces-fuse-support-interface>` | enables access to the FUSE filesystems | Storage | no |
| {ref}`fwupd <interfaces-fwupd-interface>` | allows operating as the fwupd service | System, Security, Firmware | no |
| {ref}`gbm-driver-libs <ref-gbm-driver-libs-interface_gbm-driver-libs-interface>` | exposes GBM driver libraries to the system | Super privileged | no |
| {ref}`gconf <interfaces-gconf-interface>` | access the legacy GConf config system | System, Developer, Settings | no |
| {ref}`gpg-keys <interfaces-gpg-keys-interface>` | read GPG user configuration and keys | GPG, Personal data, Security | no |
| {ref}`gpg-public-keys <interfaces-gpg-public-keys-interface>` | read GPG non-sensitive configuration and public keys | GPG, Personal data, Security | no |
| {ref}`gpio <interfaces-gpio-interface>` | access specific GPIO pins | GPIO, Hardware, Developer | no |
| {ref}`gpio-chardev <interfaces-gpio-chardev>` | permits access to specific GPIO chardev lines | Hardware | no |
| {ref}`gpio-control <interfaces-gpio-control-interface>` | allows to export/unexport and control all GPIOs | Super privileged, GPIO | no |
| {ref}`gpio-memory-control <interfaces-gpio-memory-control-interface>` | allows write access to all GPIO memory | GPIO, Hardware, Developer | no |
| {ref}`greengrass-support <interfaces-greengrass-support-interface>` | allows operating as the Greengrass service | Super privileged, Edge, AWS, Discrete | no |
| {ref}`gsettings <interfaces-gsettings-interface>` | provides access to any GSettings item for current user | System, Developer, Settings | yes |
| {ref}`hardware-observe <interfaces-hardware-observe-interface>` | access hardware information | System, Hardware | no |
| {ref}`hardware-random-control <interfaces-hardware-random-control-interface>` | provide entropy to hardware random number generator | System, Hardware | no |
| {ref}`hardware-random-observe <interfaces-hardware-random-observe-interface>` | use hardware-generated random numbers | System, Hardware | no |
| {ref}`hidraw <interfaces-hidraw-interface>` | access hidraw devices | System | no |
| {ref}`home <interfaces-home-interface>` | access non-hidden files in the home directory | Storage, Personal data | yes on classic (traditional distributions), no otherwise |
| {ref}`hostname-control <interfaces-hostname-control-interface>` | allows configuring the system hostname | Network | no |
| {ref}`hugepages-control <interfaces-hugepages-control-interface>` | control HugePages memory blocks | System, Memory, Kernel | no |
| {ref}`i2c <interfaces-i2c-interface>` | access i²c devices | System, Hardware | no |
| {ref}`iio <interfaces-iio-interface>` | access IIO devices | System, Hardware | no |
| {ref}`intel-mei <interfaces-intel-mei-interface>` | access to the Intel MEI management interface | System, Firmware | no |
| {ref}`intel-qat <interfaces-intel-qat>` | provides permissions for Intel QAT devices | Hardware | no  |
| {ref}`io-ports-control <interfaces-io-ports-control-interface>` | allows access to all I/O ports | System, | no |
| {ref}`ion-memory-control <interfaces-ion-memory-control-interface>` | access Android's ION memory allocator | Super privileged, System  | no |
| {ref}`iscsi-initiator <ref-iscsi-initiator-interface_iscsi-initiator-interface>` |  discover, connect to, and manage iSCSI targets for block storage access | Super privileged | no |
| {ref}`jack1 <interfaces-jack1-interface>` | allows interaction with the JACK audio connection server | Audio, Media | no |
| {ref}`joystick <interfaces-joystick-interface>` | use any connected joystick | Hardware, Developer | no |
| {ref}`juju-client-observe <interfaces-juju-client-observe-interface>` | read the Juju client configuration | Developer, Discrete | no |
| {ref}`kerberos-tickets <ref-kerberos-tickets-interface_kerberos-tickets-interface>` | access Kerberos tickets in /tmp | Under development | no |
| {ref}`kernel-crypto-api <interfaces-kernel-crypto-api-interface>` | read and manage kernel supported crypto ciphers | System, Kernel, Security | no |
| {ref}`kernel-firmware-control <interfaces-kernel-firmware-control-interface>` | permits a custom kernel firmware search path | Super privileged | no |
| {ref}`kernel-module-control <interfaces-kernel-module-control-interface>` | insert, remove and query kernel modules | Super privileged, System, Kernel | no |
| {ref}`kernel-module-load <interfaces-kernel-module-load-interface>` | load, or deny loading, specific kernel modules | Super privileged, System, Kernel | no |
| {ref}`kernel-module-observe <interfaces-kernel-module-observe-interface>` | query kernel modules | System, Kernel | no |
| {ref}`kubernetes-support <interfaces-kubernetes-support-interface>` | use functions essential for Kubernetes | Super privileged, Hypervisor, Discrete | no |
| {ref}`kvm <interfaces-kvm-interface>` | allows access to the kvm device | VM, Hypervisor, Developer | no |
| {ref}`libvirt <interfaces-libvirt-interface>` | provides access to the libvirt service | VM, Hypervisor, Developer | no |
| {ref}`locale-control <interfaces-locale-control-interface>` | change system language and region settings | Language and region, Personalisation | no |
| {ref}`location-control <interfaces-location-control-interface>` | allows operating as the location service | Location | no |
| {ref}`location-observe <interfaces-location-observe-interface>` | access your location | Location | no |
| {ref}`log-observe <interfaces-log-observe-interface>` | read system logs | System, Developer | no |
| {ref}`login-session-control <interfaces-login-session-control-interface>` | allows setup of login sessions and grants privileged access to user sessions | System, Security | no |
| {ref}`login-session-observe <interfaces-login-session-observe-interface>` | allows reading login and session information | System, Security | no |
| {ref}`lxd <interfaces-lxd-interface>` | provides access to the LXD socket | Super privileged, Container, Discrete | no |
| {ref}`lxd-support <interfaces-lxd-support-interface>` | allows operating as the LXD service | Super privileged, Container, Discrete | no |
| {ref}`maliit <interfaces-maliit-interface>` | use an on-screen keyboard | Developer | no |
| {ref}`media-control <interfaces-media-control-interface>` | access media control devices and Video4Linux (V4L) devices | Hardware, Developer, Media, Video | no |
| {ref}`media-hub <interfaces-media-hub-interface>` | access snaps providing the media-hub interface | Developer, Media | yes |
|  {ref}`microceph <interfaces-microceph>` |  permits access to the MicroCeph socket, which is used internally by the microceph snap | Super privileged, Container | no |
| {ref}`microceph-support <interfaces-microceph-support>` | permits the microceph snap to operate as the MicroCeph service | Super privileged, Container | no |
| {ref}`microovn <interfaces-microovn-interface>` | used only by the MicroOVN snap for socket access | Network, Super privileged | no |
| {ref}`microstack-support <interfaces-microceph-support>` | multiple service access to the Microstack infrastructure | Super privileged, Container, Discrete | no |
| {ref}`mir <interfaces-mir-interface>` | enables access to the Mir display service | Display | yes |
| {ref}`modem-manager <interfaces-modem-manager-interface>` | use and configure modems | Network | no |
| {ref}`mount-control <interfaces-mount-control-interface>` | mount and unmount transient and persistent filesystem mount points | Super privileged, Storage | no |
| {ref}`mount-observe <interfaces-mount-observe-interface>` | read mount table and quota information | Storage | no |
| {ref}`mpris <interfaces-mpris-interface>` | media key control of music and video players | Sound | no |
| {ref}`multipass-support <interfaces-multipass-support-interface>` | multipass-support allows operating as the Multipass service | Super privileged, VM, Discrete | no |
| {ref}`netlink-audit <interfaces-netlink-audit-interface>` | allows access to kernel audit system through Netlink | Inter-process communication (IPC), Netlink, Developer | no |
| {ref}`netlink-connector <interfaces-netlink-connector-interface>` | communicate through the kernel Netlink connector | Inter-process communication (IPC), Netlink, Developer | no |
| {ref}`netlink-driver <interfaces-netlink-driver-interface>` | operate a kernel driver module exposed via Netlink | Inter-process communication (IPC), Netlink, Developer | no |
| {ref}`network <interfaces-network-interface>` | enables network access | Network | yes |
| {ref}`network-bind <interfaces-network-bind-interface>` | operate as a network service | Network | yes |
| {ref}`network-control <interfaces-network-control-interface>` | change low-level network settings | Network | no |
| {ref}`network-manager <interfaces-network-manager-interface>` | configure and observe networking via NetworkManager | Network | no |
| {ref}`network-manager-observe <interfaces-network-manager-observe-interface>` | allows observing NetworkManager settings | Network | no |
| {ref}`network-observe <interfaces-network-observe-interface>` | query network status information | Network | no |
| {ref}`network-setup-control <interfaces-network-setup-control-interface>` | change network settings via Netplan | Network | no |
| {ref}`network-setup-observe <interfaces-network-setup-observe-interface>` | read network settings | Network | no |
| {ref}`network-status <interfaces-network-status-interface>` | access the NetworkStatus service | Network | yes |
| {ref}`nfs-mount <interfaces-nfs-mount>` | allows the mounting and unmounting of Network File System mount points | Network, Service | no |
| {ref}`nomad-support <interfaces-nomad-support>` |  enables HashiCorp's Nomad to access CPU and memory management | System, Containers, Service | no |
| {ref}`nvidia-drivers-support <interfaces-nvidia-drivers-support-interface>` | internally used NVIDIA access | Super privileged, Ubuntu Core | no |
| {ref}`nvme-control <ref-nvme-control-interface_nvme-control-interface>` | manage and access NVMe controllers | Super privileged | no |
| {ref}`ofono <interfaces-ofono-interface>` | allows operating as the oFono service | Network, Discrete, Developer | no |
| {ref}`online-accounts-service <interfaces-online-accounts-service-interface>` | access to the Online Accounts service | Service, Developer | yes |
| {ref}`opengl <interfaces-opengl-interface>` | access OpenGL/GPU hardware | Display, Graphics | yes |
| {ref}`opengl-driver-libs <ref-opengl-driver-libs-interface_opengl-driver-libs-interface>` | exposes OpenGL driver libraries to the system | Super privileged | no |
| {ref}`opengles-driver-libs <ref-opengles-driver-libs-interface_opengles-driver-libs-interface>` | exposes OpenGLES driver libraries to the system | Super privileged | no |
| {ref}`openvswitch <interfaces-openvswitch-interface>` | control Open vSwitch hardware | Network, Service, Developer | no |
| {ref}`openvswitch-support <interfaces-openvswitch-support-interface>` | enables kernel support for Open vSwitch | Network, Service, Developer | no |
| {ref}`optical-drive <interfaces-optical-drive-interface>` | read/write access to CD/DVD drives | Storage, Hardware, Developer | yes, unless drive can write |
| {ref}`packagekit-control <interfaces-packagekit-control-interface>` | control the PackageKit service | Super privileged, Packaging | no |
| {ref}`password-manager-service <interfaces-password-manager-service-interface>` | read, add, change, or remove saved passwords | System, Security | no |
| {ref}`pcscd <interfaces-pcscd-interface>` | permits communication with PCSD smart card daemon | Security | no |
| {ref}`personal-files <interfaces-personal-files-interface>` | read or write files in the user's home directory | Super privileged, Personal data, Attributes | no |
| {ref}`physical-memory-control <interfaces-physical-memory-control-interface>` | read and write memory used by any process | System, Memory, Kernel | no |
| {ref}`physical-memory-observe <interfaces-physical-memory-observe-interface>` | read memory used by any process | System, Memory, Kernel | no |
| {ref}`pipewire <interfaces-pipewire-interface>` | access the PipeWire server | Audio, Media, Video | no |
| {ref}`pkcs11 <interfaces-pkcs11>` |  enables the cryptographic token interface standard to be used | Security, Super privileged | no |
| {ref}`polkit <interfaces-polkit-interface>` | access to the polkit authorisation manager | Security, System, Super privileged | no |
| {ref}`polkit-agent <interfaces-polkit-agent-interface>` | permits applications to register as _polkit_ agents | Security, System, Super privileged | no |
| {ref}`posix-mq <interfaces-posix-mq-interface>` | enables inter-process communication (IPC) messages | Super privileged, IPC | no by default, yes with snaps from the same publisher |
| {ref}`power-control <interfaces-power-control-interface>` | read and write system power settings | System, Power | no |
| {ref}`ppp <interfaces-ppp-interface>` | access to configure and observe PPP networking | Network | no |
| {ref}`process-control <interfaces-process-control-interface>` | pause or end any process on the system | System | no |
| {ref}`ptp <interfaces-ptp-interface>` | access to the Precision Time Protocol subsystem | System, Developer | no |
| {ref}`pulseaudio <interfaces-pulseaudio-interface>` | play and record sound | Audio, Media | no |
| {ref}`pwm <interfaces-pwm-interface>` | access specific PWM channels | System, Developer, Hardware, WIP | no |
| {ref}`pwm-control <interfaces-pwm-control-interface>` | permits control over any aspect of all PWM channels | Super privileged | no |
| {ref}`qualcomm-ipc-router <interfaces-qualcomm-ipc-router-interface>` | access Qualcomm IPC router sockets | IPC, Kernel, System | no |
| {ref}`raw-input <interfaces-raw-input-interface>` | access raw input devices directly | System, Developer, Hardware | no |
| {ref}`raw-usb <interfaces-raw-usb-interface>` | access USB hardware directly | System, Developer, Hardware | no |
| {ref}`raw-volume <interfaces-raw-volume-interface>` | access specific disk partitions | Storage | no |
| {ref}`remoteproc <interfaces-remoteproc-interface>` | interact with the kernel's Remote Processor Framework  |Super privileged | no |
| {ref}`removable-media <interfaces-removable-media-interface>` | read/write files on removable storage devices | Storage | no |
| {ref}`ros-opt-data <interfaces-ros-opt-data>` | read-only access to ROS directories | Storage | no |
| {ref}`ros-snapd-support <interfaces-ros-snapd-support>` | allows the snaps ros-snapd and ros2-snapd the use of snapd’s apps control API | Super privileged | no |
| {ref}`screen-inhibit-control <interfaces-screen-inhibit-control-interface>` | prevent screen sleep, lock and screensaver | Display | yes |
| {ref}`screencast-legacy <interfaces-screencast-legacy-interface>` | allows screen recording and audio recording alongside writing to arbitrary filesystem paths | Legacy | no |
| {ref}`scsi-generic <interfaces-scsi-generic-interface>` | read and write access to SCSI Generic driver devices | Storage, Super privileged | no |
| {ref}`sd-control <interfaces-sd-control-interface>` | control SD cards on specific devices | Super privileged, Storage | no |
| {ref}`serial-port <interfaces-serial-port-interface>` | access serial port hardware | System, Developer, Hardware | no |
| {ref}`shared-memory <interfaces-shared-memory-interface>` | enables two snaps to access the same shared memory | Super privileged, IPC | no by default, yes with snaps from the same publisher |
| {ref}`shutdown <interfaces-shutdown-interface>` | restart or power off the device | Super privileged, System, Power | no |
| {ref}`snap-fde-control <ref-snap-fde-control-interface_snap-fde-control-interface>` | allows access to the FDE subset of snapd’s system-volumes API | Super privileged | no |
| {ref}`snap-interfaces-requests-control <interfaces-snap-interfaces-requests-control>` | enables the prompting API and its access to prompting-related notice types | System | no |
| {ref}`snap-refresh-control <interfaces-snap-refresh-control-interface>` | permits bespoke snap refresh control | Super privileged, Packaging | no |
| {ref}`snap-refresh-observe <interfaces-snap-refresh-observe-interface>` | enables the tracking of snap refreshes | Super privileged, Packaging | no |
| {ref}`snap-themes-control <interfaces-snap-themes-control-interface>` | permits the use of snapd’s theme installation API | Super privileged | no |
| {ref}`snapd-control <interfaces-snapd-control-interface>` | install or remove software | Super privileged, Packaging | no |
| {ref}`spi <interfaces-spi-interface>` | access specific SPI devices | System, Developer, Hardware | no |
| {ref}`ssh-keys <interfaces-ssh-keys-interface>` | access SSH private and public keys | Security | no |
| {ref}`ssh-public-keys <interfaces-ssh-public-keys-interface>` | access SSH public keys | Security | no |
| {ref}`steam-support <interfaces-steam-support-interface>` | allows the Steam snap to access pressure-vessel containers | Super privileged, Discrete | no |
| {ref}`storage-framework-service <interfaces-storage-framework-service-interface>` | operate as, or interact with, the Storage Framework | Storage | no |
| {ref}`system-backup <interfaces-system-backup-interface>` | read-only access to the system for backups | Storage | no |
| {ref}`system-files <interfaces-system-files-interface>` | read or write files in the system | Super privileged, Storage, Attributes | no |
| {ref}`system-observe <interfaces-system-observe-interface>` | read process and system information | Monitoring, System | no |
| {ref}`system-packages-doc <interfaces-system-packages-doc>` | access system documentation in /usr/share/doc | Developer | no |
| {ref}`system-source-code <interfaces-system-source-code-interface>` | access kernel source and headers in /usr/src | Developer | no |
| {ref}`system-trace <interfaces-system-trace-interface>` | monitor or control any running program | Monitoring, System | no |
| {ref}`tee <interfaces-tee-interface>` | permits access to the Trusted Execution Environment | Super privileged, Security, Ubuntu Core | no |
| {ref}`thumbnailer-service <interfaces-thumbnailer-service-interface>` | create thumbnail images from local media files | Storage, Media | no |
| {ref}`time-control <interfaces-time-control-interface>` | change the date and time | Time | no |
| {ref}`timeserver-control <interfaces-timeserver-control-interface>` | change time server settings | Time | no |
| {ref}`timezone-control <interfaces-timezone-control-interface>` | change the time zone | Time | no |
| {ref}`tpm <interfaces-tpm-interface>` | allows access to the Trusted Platform Module device | Kernel, Security | no |
| {ref}`u2f-devices <interfaces-u2f-devices-interface>` | use any U2F devices | Security, Hardware, Developer | no |
| {ref}`ubuntu-pro-control <interfaces-ubuntu-pro-control-interface>` | control the Ubuntu Pro desktop daemon | Super privileged, System | no |
| {ref}`ubuntu-download-manager <interfaces-ubuntu-download-manager-interface>` | use the Ubuntu Download Manager | System, Developer, Manage software | yes |
| {ref}`udisks2 <interfaces-udisks2-interface>` | access the UDisks2 service | Storage | no |
| {ref}`uhid <interfaces-uhid-interface>` | create kernel UID devices from user-space | Hardware, Kernel, System | no |
| {ref}`uinput <interfaces-uinput-interface>` | allows write access to /dev/uinput | Super privileged, Hardware | no |
| {ref}`uio <interfaces-uio-interface>` | access uio devices | Hardware, System | no |
| {ref}`unity7 <interfaces-unity7-interface>` | access legacy desktop resources from Unity7 | Display | yes |
| {ref}`unity8 <interfaces-unity8-interface>` | share data with other Unity 8 apps | Display, Super privileged | yes |
| {ref}`unity8-calendar <interfaces-unity8-calendar-interface>` | read/change shared calendar events in Ubuntu Unity 8 | Personal data | no |
| {ref}`unity8-contacts <interfaces-unity8-contacts-interface>` | read/change shared contacts in Ubuntu Unity 8 | Personal data | no |
| {ref}`upower-observe <interfaces-upower-observe-interface>` | access battery level and power usage | System, Power | yes |
| {ref}`usb-gadget <ref-usb-gadget-interface_usb-gadget-interface>` | allows snaps to access the USB Gadget API using configfs | Ubuntu Core | no |
| {ref}`userns <interfaces-userns-interface>` | permits a snap to create a new namespace | Super privileged | no |
| {ref}`vcio <interfaces-vcio-interface>` | access a Raspberry Pi's VideoCore multimedia processor | Video, Graphics, Ubuntu Core | no |
| {ref}`wayland <interfaces-wayland-interface>` | access compositors providing the Wayland protocol | Display | yes |
| {ref}`x11 <interfaces-x11-interface>` | monitor mouse/keyboard input and graphics output of other apps | Display | yes |
| {ref}`xilinx-dma <interfaces-xilinx-dma>` | allows access to Xilinx DMA IP from a connected PCIe card | Ubuntu Core, Super privileged | no |


```{toctree}
:titlesonly:
:maxdepth: 2
:hidden:
:glob:

*
