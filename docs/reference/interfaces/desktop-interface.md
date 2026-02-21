(interfaces-desktop-interface)=
# desktop interface

`desktop` allows access to basic graphical desktop resources, such as Wayland.

**Auto-connect**: yes</br>
**Attributes**:</br>

* `desktop-file-ids` (plug): optional, list of valid [destkop file IDs](https://specifications.freedesktop.org/desktop-entry/latest/file-naming.html#desktop-file-id) (based on DBus well-known names - e.g. `[org.example.desktop, org.example.Foo.desktop]`).
<br />This would indicate that the snap would like to install desktop file(s) named `org.example.desktop` and `org.example.Foo.desktop` (found under `meta/gui`) without name mangling (ie, without the snap name prefix).
<br />(requires *snapd 2.66*).

Important note:

* `desktop-file-ids` attribute is not compatible with [parallel installs](/explanation/how-snaps-work/parallel-installs) and existing parallel instances will not be refreshed if the new revision introduced the `desktop-file-ids` attribute.

See [The desktop interfaces](/reference/interfaces/desktop-interfaces) for further details.
