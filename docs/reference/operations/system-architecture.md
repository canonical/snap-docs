(reference-operations-system-architecture)=
# System architecture

The snap packaging system consists of many components, from system-level Linux kernel security modules, managed by the snap daemon, _snapd_, to the network connected Snap Store for package retrieval and updates.

These components inter-communicate and operate together to create a secure and confined execution environment for application and service deployment. The overall process with these components and their communication is outlined below.

## System process overview

![Snap system process overview, showing how the snap daemon, snapd, manages snaps within a sandbox and configures the system security modules for access|666x500](/images/system-architecture.png)
[wrap="center"]
**Snap system process overview, showing how the snap daemon, snapd, manages snaps within a sandbox and configures the system security modules for access**
[/wrap]

The snap daemon, **snapd**,  handles **snap management** to configure and maintain each snap. 

The snap damon also maintains the **security configuration** that creates the **sandbox** for both snap executables and data. This is implemented using various **security modules** of the **Linux kernel**, including Seccomp, AppArmor and Cgroups.

Snaps have the least possible privileges by default. Additional system resources are permitted through the **[interfaces](t/35928)** mechanism which changes the security profile for each snap.

A **snap package** is a self-contained and immutable _SquashFS_ file carrying application-specific content alongside metadata to tell the system how it should be manipulated. 

Package **downloads and updates** are managed through a connection to the remote **Snap Store**, which includes package integrity and validation.

## Security modules

The snap daemon uses privilege isolation mechanisms rooted in the Linux kernel through Cgroups and Namespaces, AppArmor and Seccomp.

|  |  |
|--|--|
| **Cgroups** Limit the amount of resources and which devices the process confined to a snap can consume (CPU, memory, network bandwidth, and so on). | **Namespaces** Make sure processes in a snap see their own personal view of the system (files, processes, network interfaces, hostname, and so on). 
|**AppArmor** Allows system administrators to restrict snap capabilities with default security profiles that can be extended. |**Seccomp** Isolates processes running in a snap by limiting the system calls they are allowed to make. |

The state of snapd, and many of its key functions, can be accessed through its [REST API](/reference/development/rest-api/snapd-rest-api), enabling remote device configuration, updates and orchestration. 

## System process

* **snapd -> Snap Store** : retrieves snap and assertion data from the package repository.
* **snapd -> AppArmor**: sets up security profiles using permissions and capabilities by creating AppArmor profiles for each and modifying them whenever new interfaces are connected.
* **snapd -> Seccomp**: as with AppArmor, uses per-snap profiles to limit the system calls a snap can make.

For services:
* **snapd -> systemd** : handles mounting, sockets, Cgroup limits and tracks service lifecycles for each snap.

## Process components

The package ecosystem can be separated at the binary level, including the socket files, and these components include the following:

* **snap packages**:  each snap is a _SquashFS_ file carrying content alongside metadata to tell the system how it should be manipulated.  
* **snapd**: the background service that manages, maintains, installs and removes snap packages.
* **snap**: the command-line interface for interacting with snap functionality.
* **snap-confine**: used internally to set up the confinement and namespaces for individual snaps before executing into the snap
* **snapctl**: used from within the running snap environment to access snap management functions.
 -  `/run/snapd.socket`: Unix socket used by snap
  - `/run/snapd-snap.socket`: Unix socket used by snapctl

### Process component relationships

* **snapd -> `/run/snapd.socket`**:  exposes REST API through
* **snapd -> `/run/snapd-snap.socket`**: exposes REST API through
* **snap -> `/run/snapd.socket`**: makes user requests
* **snapctl -> `/run/snapd-snap.socket`**: makes snap requests
* **snaps -> `snapctl`**: uses snap management features exposed by *snapd*
* **snapd -> `snap run`**: prepares confinement/execs into snap

