(interfaces-netlink-audit-interface)=
# netlink-audit-interface

The `netlink-audit` interface allows access to the kernel part of the Linux Audit Subsystem through Netlink.

See also [netlink-driver](/interfaces/netlink-driver-interface) and [netlink-connector]().

```{tip}

See [Interface management](/) and [Supported interfaces](/interfaces/index) for further details on how interfaces are used.
```

---

<h2 id='heading--dev-details'>Developer details </h2>

**Auto-connect**: no

Requires snapd version _2.26+_.

<h3 id='heading-code'>Code examples</h3>

The snap of the [usbtop]() kernel module, used to monitor the bandwidth of USB buses and devices, uses the _netlink-audit_ interface:
[https://github.com/ogra1/usbtop/blob/master/snap/snapcraft.yaml](https://github.com/ogra1/usbtop/blob/3743b5a55e6df70e6dd95292121279f1013ba570/snap/snapcraft.yaml#L50)


The source code for this interface is in the *snapd* repository:
<https://github.com/snapcore/snapd/blob/master/interfaces/builtin/netlink_audit.go>

