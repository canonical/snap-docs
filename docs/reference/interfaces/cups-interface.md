(interfaces-cups-interface)=
#  cups interface

The `cups` interface allows access to the CUPS socket for printing via the [`cups` snap](https://snapcraft.io/cups).

This interface is intended to be used by snap developers who wish to add safe printing functionality to their snapped applications without requiring their users to make make a manual interface connection. This is possible because the cups interface does not permit administration or configuration of printers via the CUPS socket, only the submission of print jobs and auxiliary tasks, such as listing available printers.

Formerly, to print from a snapped application, the [cups control interface](/reference/interfaces/cups-control-interface) was required. This needs either a manual connection or Snap Store permissions to auto-connect. Alongside printer access, the _cups control interface_ also allows any user to create and modify queues, and their permissions, and to read and delete anyone’s print jobs. This isn't ideal in a multi-user environment.

The `cups-control` interface will continue to be available to allow printer setup tools (and general system admin tools, like [this one](https://github.com/ubuntu-flutter-community/settings)) to be snapped.

Available since _snapd 2.55.3_.

## On systems with a classically installed CUPS
(Via a deb, RPM, or from source, for example).

The CUPS snap will run in proxy mode, working as a proxy or firewall between the application snaps and the system’s CUPS. The CUPS snap will replicate the system print queues and pass jobs through to the system’s CUPS. The user will be able to access the same queues and printer drivers when printing from classically installed applications *and* application snaps.

## On systems with no CUPS installed
(or using the CUPS snap).

The CUPS snap will run in standalone mode, listening not only on `$SNAP_COMMON/run/cups.sock` but also on `/run/cups/cups.sock`. This way all applications, both classically installed or snapped, print via the CUPS Snap. Queues have to be created on the snapped CUPS, drivers have to be [Printer Applications](https://snapcraft.io/search?q=OpenPrinting). Also here the user sees the same print queues for both classic and snapped applications.

## Developer details

**[Auto-connect](/)**: not applicable

* If you are snapping a **new application** that has print functionality, add the `cups` interface.
* If you are **maintaining an application snap** currently using `cups-control` for printing, switch to the `cups` interface.
* If you are creating or maintaining a **snap of a printer setup tool**, you have to plug [cups-control interface](/reference/interfaces/cups-control-interface) and ask your users to manually connect the interface, or request an auto-connection from the Snap Store team.

The slot side of the interface is intended to be provided by a reference snap, such as the [`cups` snap](https://snapcraft.io/cups). The reference snap will permit any connecting snap to connect automatically, which snaps with the `cups` plug can _auto-connect_ to the reference snap's `cups` slot, and print, without any further action from the user.

On systems where this slot is provided by a snap application, the _cups_ interface is the companion interface to the [cups control interface](/reference/interfaces/cups-control-interface).

However, the _cups_ interface and the _cups-control_ interface should not be used as plugs in the same snap.

The design of both of these interfaces is based on the idea that the slot implementation (eg. _cupsd_) is expected to query snapd to determine if the cups-control interface is connected or not for the peer-client process. The print service will then mediate admin functionality (ie, the rules in these interfaces allow connecting to the print service, but do not implement enforcement rules; it is up to the print service to provide enforcement).

### Current requirements

As the CUPS interface is new, we currently recommend the following additions be made to the top level of your  [snapcraft.yaml](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/snapcraft-yaml/).

1) Adding _assumes_ will ensure snapd is updated to a CUPS interface compatible version:

    ```yaml
    # snapd 2.55 or later is needed for cups interface support
    assumes: [snapd2.55]
    ```

2) The following will trigger the automatic installation of the cups snap:

    ```yaml
    plugs:
      foo-install-cups:
        interface: content
        content: foo
        default-provider: cups
        target: $SNAP_DATA/foo
    ```

The above additions should only be temporary and can be removed after the CUPS interface becomes better established.

For background information and design discussions about this interface, see [About the cups interface](https://forum.snapcraft.io/t/the-cups-interface/29873).

### Code examples

See the test CUPS consumer snap:
https://github.com/canonical/test-snapd-cups-consumer

The source code for the interface is in the snapd repository: [https://github.com/canonical/snapd/blob/master/interfaces/builtin/cups.go](https://github.com/canonical/snapd/blob/master/interfaces/builtin/cups.go)

