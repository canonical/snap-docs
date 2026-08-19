(interfaces-system-files-interface)=
#  system-files interface

The `system-files` interface enables a snap to access specific system files and directories (such as files in `/etc`). Consequently,  the interface can provide access to privileged system data and is not connected by default.

This interface is typically used to provide read-only access to system configuration directories created by a non-snap version of an application now running from an equivalent snap.

<h2 id='heading--example'>Example</h2>

The [Firefox](https://snapcraft.io/firefox), [Chromium](https://snapcraft.io/chromium) and [Thunderbird](https://snapcraft.io/thunderbird) snaps use this interface to enable access to system-installed policies to customise each respective application.

> See {ref}`Interface management <how-to-guides-work-with-snaps-connect-interfaces>` and {ref}`Supported interfaces <ref-index_interfaces>` for further details on how interfaces are used.


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

**Attributes**:
  * `read` (plug): list of files and/or directories for read-only access (eg, '`read: [ /etc/file-read, /etc/dir-read ]`'
  * `write` (plug): list of files and/or directories for read/write access (eg, '`write: [ /etc/file-write, /etc/dir-write ]`'

Requires snapd version _2.37+_.

Consumers of this interface require a {ref}`snap declaration <interfaces-process-for-aliases-auto-connections-and-tracks>` for distribution via the [Snap Store](https://snapcraft.io/store) and acceptance in the store requires that the interface is not be used to access:
- system files where the snap is not the clear owner (eg, /dev, /proc, /sys, /usr, etc).
- paths in `/dev`, such as `/dev/sda1`
  Access to `/dev` device nodes requires both AppArmor policy and device control group inclusion, but the _system-files_ interface does not have enough information to generate the necessary policy to enable these use cases. As such, purpose-specific interfaces should be used instead, such as  {ref}`block-devices <interfaces-block-devices-interface>` or {ref}`raw-volume <interfaces-raw-volume-interface>`.


> ⓘ  Do not share data between snaps
</br>While `system-files` can be used to share data with another snap, such as within a configuration file, this behaviour is not recommended. The {ref}`content interface <interfaces-content-interface>` should be used instead.



An additional requirement for acceptance in the Global store is using a descriptive interface reference for use with `snap connections|interfaces|connect|disconnect`.

For example, the 'foo' application is packaged as a snap and the snap publisher wants to import existing configuration from `/etc/foo` into the snap. The snapcraft.yaml might be:

```
name: foo
...
plugs:
  etc-foo:
    interface: system-files
    read:
    - /etc/foo

apps:
  foo:
    plugs:
    - etc-foo
    ...
```

Note, when declaring an instance of the `system-files` plug as above, it should be named with a descriptive name that indicates to a user what access it grants. In this case, the name `etc-foo` is used to reflect the access to `/etc/foo`.

With the above, a `snap connect` command would look like: `snap connect foo:etc-foo`.

<h3 id='heading-code'>Code examples</h3>

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/system_files.go>

