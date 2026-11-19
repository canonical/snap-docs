---
myst:
  html_meta:
    description: Reference documentation for the pulseaudio interface, which lets snaps access the PulseAudio sound server for playback and recording (deprecated).
---

(interfaces-pulseaudio-interface)=
#  pulseaudio interface

As of snapd 2.41, this interface is deprecated and the {ref}`audio-playback <interfaces-audio-playback-interface>` and {ref}`audio-record <interfaces-audio-record-interface>` interfaces should be used instead. They provide access to PulseAudio and will provide access to other sound servers in the future.

`pulseaudio` enables access to the PulseAudio sound server for sound playback and recording. 

**Auto-connect**: no

```{note}
The `pulseaudio` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

*Note: The {ref}`audio-playback <interfaces-audio-playback-interface>` interface is auto-connected.*


