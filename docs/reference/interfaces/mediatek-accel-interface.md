---
myst:
  html_meta:
    description: Reference for the mediatek-accel interface, which gives snaps access to the APU and video processing hardware accelerators on MediaTek Genio devices.
---
(interfaces-mediatek-accel-interface)=
# mediatek-accel interface

The `mediatek-accel` interface allows access to the hardware accelerators on MediaTek Genio devices, such as the AI Processing Unit (APU) and the video processing units. The slot is provided implicitly by the system, so a snap only needs to declare the plug and list the accelerators it needs in the `units` attribute:

```yaml
plugs:
  mediatek-accel:
    interface: mediatek-accel
    units:
      - apu
      - vcu
```

The interface only generates AppArmor and udev rules for the listed units, so a snap gets access to just the devices it requests. Because the interface does not auto-connect, connect it manually:

```
snap connect <snap>:mediatek-accel
```

Requires snapd version _2.79+_.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>

**Attributes**:
* `units` (plug): a required, non-empty list of strings selecting which accelerators to access. Any other value is rejected. Supported units:
  * `apu`: APU (AI Processing Unit). Grants read/write access to `/dev/apusys`.
  * `vcu`: VPU (MediaTek Video Processor Unit) and MDP (MediaTek Media Data Path). Grants read/write access to `/dev/vcu` and `/dev/vcu[0-9]*`.

### Code examples

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/mediatek_accel_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/mediatek_accel.go
