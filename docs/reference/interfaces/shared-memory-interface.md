(interfaces-shared-memory-interface)=
#  shared-memory interface

The `shared-memory` interface allows two snaps to communicate with each other using a specific predefined shared-memory path or directory in `/dev/shm`, an area of a POSIX-compliant filesystem reserved for shared memory. The location is defined by one snap and connected to from another.

Requires snapd version *2.54+* .


## Developer details

| Permissions |  |  |
|--|--|--|
| **[Auto-connect](/t/interface-management/6154#heading--auto-connections)** | **no** by default | **yes** when `private` is enabled, or with snaps from the same publisher |
| **[Super-privileged](/)** | **no** for plugs | **yes** for slots |

**Attributes**:

 * `shared-memory` (slot and plug):
optional, arbitrary identifier for the shared memory area(s) defined in the slot. A consumer snap must use the same identifier as the provider snap in order to work on the same shared memory object(s). Defaults to either local slot name or local plug name for slot/plug definitions respectively.
* `private` (plug): when `true`, creates a directory that is only accessible to the snap. This directory has read/write permissions, is mounted over `/dev/shm`, and permits an auto-connection to the `system:shared-memory` slot.
* `read` (slot): list of *read-only* paths (after the implicit `/dev/shm/`) to be exposed to a consuming snap.
* `write` (slot): list of *read and write* paths (after the implicit `/dev/shm/`) to be exposed to a consuming snap.

The `read` and `write` attributes are used on the slot side to specify the names of the shared memory objects being shared (in read-only mode for `read`, and with full read-write mode for `write`); the prefix `/dev/shm/` is implicit and must not be specified. Both attributes can be specified simultaneously for different paths, but the two values should not duplicate each other.

### Code examples

An example plug definition:

```yaml
plugs:
 my-ipc:
  interface: shared-memory
  # this could be omitted since we already adjusted ​the plug name
  # to match the slot's shared-memory name:
  shared-memory: my-ipc
```

A matching slot definition which would auto-connect if in a snap from the same publisher:

```yaml
slots:
 shmem:
  interface: shared-memory
  shared-memory: my-ipc
  write: [ students ]  # gives read/write access to /dev/shm/students
  read: [ teachers ]   # gives readonly access to /dev/shm/teachers
```

Creating `private` shared memory for the snap:

```yaml
plugs:
  shared-memory:
    private: true
```

When `private: true` is used,  the shared-memory interface is automatically connected:

```
$ snap connections <example-private-shared-memory-snap>
Interface      Plug                      Slot            Notes
shared-memory  os-release:shared-memory  :shared-memory  -
```


The test code can be found in the snapd repository:
[shared_memory_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/shared_memory_test.go).
The source code for the interface is in the snapd repository:
[shared_memory.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/shared_memory.go)</br>

