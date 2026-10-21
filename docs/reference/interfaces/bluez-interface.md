(interfaces-bluez-interface)=
#  bluez interface

`bluez` enables access to the bluez Bluetooth service.

The plug is the client and the slot provides access to the bluez (Bluetooth) service. Connecting the two allows a client to access devices registered by the bluez service through the slot.

For example, a game with a _bluez_ plug could connect to the system's _bluez_ slot to access a Bluetooth game controller.


**Auto-connect**: no

```{note}
The `bluez` slot is unsupported for {ref}`parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```


