(interfaces-desktop-interface)=
# desktop interface

`desktop` allows access to basic graphical desktop resources, such as Wayland.

**Auto-connect**: yes</br>
**Attributes**:</br>
   * `desktop-file-ids` (plug): optional, list of desktop file ids with valid D-Bus well-known names (e.g. `[org.example, org.example.Foo]`). This would indicate that the snap would like to install desktop file(s) named `org.example.desktop` and `org.example.Foo.desktop` (found under `meta/gui`) without name mangling (ie, without the snap name prefix) (requires *snapd 2.66*).
