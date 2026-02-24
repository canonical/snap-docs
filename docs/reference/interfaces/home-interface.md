(interfaces-home-interface)=
#  home interface

The `home` [interface](/) allows access to non-hidden files owned by the user in the user's home ($HOME) directory where a user normally stores their personal files and documents.

The majority of snaps use [strict confinement](/) and do not have arbitrary access a system's resources, including file and directories in the _\/home_ directory. Without this access, _home_ will not be visible in file requesters, or as a destination from within the snap application.

To check whether a snap can connect to $HOME, use the _snap connections_ command:

```
$ snap connections <snap-name>
Interface  Plug                Slot         Notes
home       <snap-name>:home    -        -
```

The above output shows that `<snap-name>` does provide a home interface (in the _Plug_ column), but that it's not connected to any slot (denoted by the `-` in the slot column).

Use the _snap connect_ command to connect an interface:

```
$ snap connect <snap-name>:home :home
```
The `:home` slot, with no \<snap-name\>  before the colon (`:`) is equivalent to directing the plug to connect to the system, which in this case is the $HOME directory.

A snap developer can [request permission](https://forum.snapcraft.io/t/permission-requests/12822) to have the `home` interface connected automatically. In this case, non-hidden files and directories will be accessible from that snap without any further configuration being necessary.

Requires snapd version _2.33+_.

## Developer details

**[Auto-Connect](/t/the-interface-connection-mechanism/20179#heading--autoconnect)**:
-  **yes** on traditional distributions
-  **no** on all other systems, including [Ubuntu Core](/t/glossary/14612#heading--ubuntu-core)

**Transitional**: yes</br>
**Attributes**:
 * `read` (plug):
  optional, when set to 'all', also allows reading non-hidden files in the home directories of all users as traditional file permissions allow.
  _When set to 'all' this plug becomes non-autoconnect._

### Example snaps

* [OBS Studio](https://github.com/snapcrafters/obs-studio): [snapcraft.yaml](https://github.com/snapcrafters/obs-studio/blob/master/snap/snapcraft.yaml)
* [Signal Desktop](https://github.com/snapcrafters/signal-desktop): [snapcraft.yaml](https://github.com/snapcrafters/signal-desktop/blob/master/snap/snapcraft.yaml)

### Interface source code

[snapd/home.go at master · canonical/snapd](https://github.com/canonical/snapd/blob/master/interfaces/builtin/home.go)

