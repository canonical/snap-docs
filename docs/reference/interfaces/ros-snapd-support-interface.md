(interfaces-ros-snapd-support)=
#  ros-snapd-support interface

The `ros-snapd-support` interface allows the snaps [`ros-snapd`](https://snapcraft.io/ros-snapd) and [`ros2-snapd`](https://snapcraft.io/ros2-snapd) the use of snapd's apps control API.

## Developer details

[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/#auto-connections): no\
[Super-privileged](https://snapcraft.io/docs/super-privileged-interfaces): yes

<h3 id='heading--endpoint-access'>Endpoint access permissions</h3>
<ul>
<li>/v2/apps</li>
</ul>

### Code examples

The test code can be found in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_snapd_support_test.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_snapd_support_test.go)

The source code for the interface is in the snapd repository:[ https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_snapd_support.go.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/ros_snapd_support.go.go)

