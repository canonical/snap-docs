(interfaces-kernel-module-load-interface)=
#  kernel-module-load interface

`kernel-module-load` provides the ability to load, or deny loading, specific kernel modules. This interface gives privileged access to the device.

See also the {ref}`kernel-module-control interface <interfaces-kernel-module-control-interface>` for inserting, removing and querying kernel modules.


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no<br />
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

```{caution}
This interface controls a resource shared by the whole system. Snaps that use it can be installed as parallel instances, but every instance acts on the same system resource and snapd does not coordinate between them. Make sure each instance manages different resources, or run only one instance at a time. See {ref}`interfaces-parallel-installs-shared-resources`.
```

**Attributes**:
  * `name` (plug, required): provides the name of the kernel module to be loaded (eg, '`name: pcspkr`')
  * `load` (plug): string to declare when, or whether, to load this module. Values can be one of the following:
     - `on-boot` (default): loads the kernel module at boot time (eg. `load: on-boot`)
     - `denied`: prevents the module from being loaded at all (eg. `load: denied`). Also known as _denylisting_ in the Linux kernel.
     - `dynamic`: enables runtime loading and unloading of the kernel module. The snap can load and unload the module using snapctl kmod.
  * `options` (plug): string of options to use when loading the module (eg, `options: p1=3 p2=true p3`)

**In addition to the `name` attribute being required, either `options` or `load` must also be specified.**

Consumers of this interface require a {ref}`snap declaration <interfaces-process-for-aliases-auto-connections-and-tracks>` for distribution via the Snap Store.

Requires snapd version _2.54+_.

<h3 id='heading-code'>Code examples</h3>

The following is an example snippet for an application snap to load the module `foo` with options `param=2`, and to deny loading the module `bar`:

```yaml
plugs:
  load-foo:
    interface: kernel-module-load
    modules:
    - name: foo
      options: param=2
  deny-bar:
    interface: kernel-module-load
    modules:
    - name: bar
      load: denied
```

The `load-foo` _foo_ kernel module can be more verbosely by declared with the `load` attribute, resulting in the same behaviour:

```yaml
plugs:
  load-foo:
    interface: kernel-module-load
    modules:
    - name: foo
      load: on-boot
      options: param=2
```

The test code can be found in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_module_load.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_module_load.go)

The source code for the interface is in the snapd repository:[https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_module_load_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/kernel_module_load_test.go)

