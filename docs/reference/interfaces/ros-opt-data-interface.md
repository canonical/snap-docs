(interfaces-ros-opt-data)=
#  ros-opt-data interface

The `ros-opt-data` interface creates a read-only mount from within a snap to the standard Robot Operating System (ROS) directory (`/opt/ros/*`) on the host system, enabling robotics-based snaps to share ROS robot data, such as the URDF.

This interface cannot currently be used on Ubuntu Core. Requires snapd version *2.62+*.

To add this interface to a snap, define a plug in the [app](/) section of its [snapcraft.yaml](/) for the application that requires ROS data access:

```yaml
apps:
  hello-world:
    command: ./hello.sh
    plugs: [ros-opt-data]   #this is the new interface plug name
```

## Mount location

This interface uses the standard snap location for mounted directories:
`/var/lib/snapd/hostfs/`.

For example, if this interface is used to access `/opt/ros/noetic/robot-urdf/models` on the host machine, it will be found within the snap at `/var/lib/snapd/hostfs/opt/ros/noetic/robot-urdf/models`.

## Developer details

**[Auto-connect](/explanation/interfaces/interface-auto-connection)**: yes</br>

### Code examples

The following is a simple _hello-world_ example that includes an additional plug/slot mechanism for enabling the `ros-opt-data` interface. We're going to modify this example to show how the interface can access ROS-related data on the host system.

 The initial snapcraft.yaml is as follows:

```yaml
name: hello-world
version: '0.1'
summary: A simple hello world application
description: |
  A simple hello world application.
base: core22

grade: devel
confinement: strict

apps:
  hello-world:
    command: ./hello.sh

parts:
  hello-world:
    plugin: dump
    source: files
```

When the snap is built, installed and executed, it runs the following `hello.sh` script (which for now only outputs  “hello world”).

```sh
#!/bin/bash
echo "hello world"
```

We now want to change the above script to output the contents of a `setup.bash` file located in the host's `/opt/ros` directory.

The following modification assumes we're using ROS Noetic Ninjemys, but the file location can be adapted for any other ROS distro:

```sh
#!/bin/bash
cat /var/lib/snapd/hostfs/opt/ros/noetic/setup.bash
```

We now modify the snapcraft.yaml to insert the new plug:

```yaml
name: hello-world
version: '0.1'
summary: A simple hello world application
description: |
  A simple hello world application.
base: core22

grade: devel # must be 'stable' to release into candidate/stable channels
confinement: strict

apps:
  hello-world:
    command: ./hello.sh
    plugs: [ros-opt-data]

parts:
  hello-world:
    plugin: dump
    source: files
```

When the new snap is built, installed and executed, the output will now be the contents of `/opt/ros/noetic/setup.bash`.

---

The test code can be found in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_opt_data_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_opt_datae_test.go)

The source code for the interface is in the snapd repository:
[https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_opt_data.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_opt_data.go)

