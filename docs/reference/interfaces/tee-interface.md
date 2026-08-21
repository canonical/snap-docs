(interfaces-tee-interface)=
#  tee interface

The `tee` interface  permits access to Trusted Execution Environment (TEE) devices via the [TEE subsystem](https://www.kernel.org/doc/html/latest/tee/index.html) in the Linux kernel.


This interface is primarily intended to be used with {ref}`Ubuntu Core <ref-glossary_ubuntu-core>`.


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

Intended for snaps needing to access the TEE subsystem over `/dev/tee[0-9]*`, `/dev/teepriv[0-0]*` or  the Qualcomm equivalent _qseecom_  (Qualcomm Secure Execution Environment Communicator) at `/dev/qseecom`.

### Code examples

The official [Ubuntu Core gadget snap](https://github.com/kubiko/imx-gadget) for the [i.MX8M Mini Evaluation Kit](https://www.nxp.com/design/design-center/development-boards-and-designs/8MMINILPD4-EVK) uses this interface: https://github.com/kubiko/imx-gadget/blob/24/imx8mm-evk/snap/snapcraft.yaml

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/tee_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/tee.go

