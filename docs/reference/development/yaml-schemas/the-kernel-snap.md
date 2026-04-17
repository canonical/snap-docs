(reference-development-yaml-schemas-the-kernel-snap)=
# The kernel snap

As the name implies, the _kernel_ snap is responsible for defining the Linux
kernel that will run in a snap-based system. The correct kernel snap for a given
system is selected via the model assertion, produced and signed by the device's
brand account before the image is built. Once the image is built, the kernel
snap may be updated, but it cannot be replaced by a completely different kernel
snap.

Canonical publishes some reference kernel snaps as well as kernel snaps for main
Canonical models such as official Ubuntu Core VMs on various certified public
clouds, as well as general purpose computing images for popular physical devices
such as the 64-bit x86 PC and Raspberry Pi 2 and 3.

For details on building a kernel snap, see [Build a kernel snap](https://documentation.ubuntu.com/core/how-to-guides/image-creation/build-a-kernel-snap/)
in the Ubuntu Core documentation.

## Setup files

In addition to traditional snap metadata, the kernel snap also holds some setup
files fundamental to the initialization and lifecycle of the device.

The layout for a kernel snap has some variation, but usually follows:

- `meta/snap.yaml` - Traditional snap details, with `type: kernel` explicitly defined
- `meta/kernel.yaml` - Optional kernel-specific metadata defining kernel-provided assets
- `snapd-info` - Information about the snapd packaged in the initrd
- `modules/<version>/` - Kernel modules; version must match the one in `snap.yaml`
- `firmware/` - Optional firmware files
- `dtbs/` - Optional binary device-tree files, if gadget.yaml states `device-tree-origin: kernel`
- kernel - The actual kernel image
- initrd - The initrd image

The kernel and initrd may be discrete objects, usually named `kernel.img` and
`initrd.img`, respectively. However, they could also be distributed as a single [Unified Kernel Image](https://uapi-group.org/specifications/specs/unified_kernel_image/)
(UKI) or as a [Flatted Image Tree](https://docs.u-boot.org/en/v2024.07/usage/fit/source_file_format.html)
(FIT) image. These are usually named `kernel.efi` or `kernel.img`, respectively.

### kernel.yaml

The `kernel.yaml` provides information used by snapd to determine
kernel-specific asset information. Primarily, this is about device trees and
kernel modules. The standard format is:

```yaml
dynamic-modules: $SNAP_DATA
assets:
  dtbs:
    update: true
    content:
      - dtbs/
```

* `dynamic-modules` points to a folder which contains `modules/` and `firmware/`
directories, usually created by a kernel component.

* `assets` details a list of content the kernel snap provides, usually device
tree files, to the gadget snap. These are then referenceable in the gadget
snap's `gadget.yaml` like so:

```yaml
volumes:
  platform:
    schema: gpt
    bootloader: grub
    structure:
      - name: ubuntu-seed
        role: system-seed
        filesystem: vfat
        type: C12A7328-F81F-11D2-BA4B-00A0C93EC93B
        size: 800M
        offset: 8M
        content:
          - source: $kernel:dtbs/dtbs/
            target: /dtbs/
```

### initrd

The initrd component of the kernel snap plays a fundamental role in the booting
of an Ubuntu Core system.

The initrd is usually built using the ubuntu-core-initramfs tool.

