(interfaces-xilinx-dma)=
#  xilinx-dma interface

The `xilinx-dma` interface allows access to [Xilinx](https://en.wikipedia.org/wiki/Xilinx) DMA IP from a connected [PCIe card](https://github.com/Xilinx/dma_ip_drivers/) on a device typically running {ref}`Ubuntu Core <ref-glossary_ubuntu-core>`.

## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/xilinx_dma_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/xilinx_dma.go

