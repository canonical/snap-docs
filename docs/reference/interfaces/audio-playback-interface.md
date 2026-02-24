(interfaces-audio-playback-interface)=
#  audio-playback interface

The `audio-playback` interface allows a snap to play sounds and music, via the supporting audio service running on the system, such as PulseAudio. It's used by many applications and utilities, and as such, is enabled by default.

Audio recording is enabled with the companion [audio-record](/reference/interfaces/audio-record-interface) interface, and unlike `audio-playback`, is not enabled (auto-connected) by default.

<h2 id='heading--example'>Example</h2>

The [VLC snap](https://snapcraft.io/vlc) is a good example of an application using the  audio-playback interface:


```
$ snap connections vlc
Interface               Plug                        Slot                     Notes
audio-playback          vlc:audio-playback          :audio-playback          -
audio-record            vlc:audio-record            -                        -
```

If for some reason you want to disable audio playback for a snap, use the disconnect command:

```
snap disconnect vlc:audio-playback
```

The connect command can be used to re-enable audio playback:

```
snap connect vlc:audio-playback
```


## Developer details

**Auto-connect**: yes

<h3 id='heading-code'>Code examples</h3>

The snapcraft.yaml for [VLC](https://github.com/videolan/vlc) includes audio-playback configuration:
[https://github.com/videolan/vlc/blob/master/extras/package/snap/snapcraft.yaml](https://github.com/videolan/vlc/blob/75bca603749d8bfb7048a84ea811cbdb19447596/extras/package/snap/snapcraft.yaml#L36)

The source code for this interface is in the *snapd* repository:
<https://github.com/canonical/snapd/blob/master/interfaces/builtin/audio_playback.go>

