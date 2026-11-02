---
myst:
  html_meta:
    description: The network-observe interface lets a snap query network status. Covers what read-only means here and which sockets it still allows.
---

(interfaces-network-observe-interface)=
#  network-observe interface

`network-observe` enables the querying of the network's status, giving privileged read-only access to networking information.

"Read-only" means the snap can't change network settings. It can still open TCP and UDP connections, through the name-resolution rules the interface includes, and raw sockets for `ping`. A snap with `network-observe` connected can therefore reach the network even without the {ref}`network <interfaces-network-interface>` interface.

**Auto-connect**: no
