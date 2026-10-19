---
myst:
  html_meta:
    description: Reference documentation for the mpris interface, which lets snaps control media players through the Media Player Remote Interfacing Specification.
---

(interfaces-mpris-interface)=
#  mpris interface

`mpris` enables access to the Media Player Remote Interfacing Specification (mpris) via DBus, allowing a snap to control music and video players.

This interface is most commonly used to pass media key control through to a media player, such as _play_ and _pause_ and music playback.

Consuming snaps can access media players implementing mpris via the providing snap's well-known DBus name.

**Auto-Connect**: no</br>
**Attributes**:</br>
   * `name` (slot): optional, media player name to use for DBus well-known name 
      (ie, `org.mpris.MediaPlayer2.$name`). If omitted, use the snap's name.


