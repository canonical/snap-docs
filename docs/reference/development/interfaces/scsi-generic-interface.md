(interfaces-scsi-generic-interface)=
# scsi-generic-interface

The `scsi-generic` interface allows read and write access to [SCSI Generic driver](https://www.kernel.org/doc/html/latest/scsi/scsi-generic.html) (sg)  devices.
 
 

```{tip}

See [Interface management](/) and [Supported interfaces](/interfaces/index) for further details on how interfaces are used.
```

---

<h2 id='heading--dev-details'>Developer details </h2>

**[Auto-connect](/t/6154#heading--auto-connections)** : no</br>
**[Super-privileged](/)** : yes
 * `shared-memory` (slot and plug):   


### Code examples

```yaml
apps:
 app:
  command: foo
  plugs: [scsi-generic]
```

The test code can be found in the snapd repository: https://github.com/snapcore/snapd/blob/master/interfaces/builtin/scsi_generic_test.go

The source code for the interface is in the snapd repository: https://github.com/snapcore/snapd/blob/master/interfaces/builtin/scsi_generic.go

