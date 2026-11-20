(interfaces-intel-qat)=
#  intel-qat interface

The ` intel-qat` interface provides permissions for [Intel QAT](https://www.intel.com/content/www/us/en/products/details/processors/xeon/features/quick-assist-technology.html) devices to access `VFIO`, `IOMMU` and `QAT_ADF_CTL` nodes.


## Developer details

**Auto-connect**: no

For Intel QAT implementation details, see the [kernel support](https://elixir.bootlin.com/linux/v6.10.3/source/drivers/crypto/intel/qat) and [userspace manager](https://github.com/intel/qatlib) repositories.

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/intel_qat_test.go

The source code for the interface is in the snapd repository:</br>https://github.com/canonical/snapd/blob/master/interfaces/builtin/intel_qat.go

