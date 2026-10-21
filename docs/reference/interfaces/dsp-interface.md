(interfaces-dsp-interface)=
#  dsp interface

The `dsp` interface allows for the control of digital signal processors (DSPs) on specific devices and systems (such as specific _Ambarella_ devices)



## Developer details

**Auto-connect**: no

```{note}
The `dsp` plug is unsupported for {ref}`parallel instances <interfaces-parallel-installs-unsupported>`. Instances would perform conflicting operations on the same system resources.
```

This interface allows privileged access to hardware and kernel drivers related to the digital signal processor and thus is only allowed on specific devices providing the slot via a gadget and is also not auto-connected.

Requires snapd version _2.51+_.

<h3 id='heading-code'>Code examples</h3>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/dsp.go>

