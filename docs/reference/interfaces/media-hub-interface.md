---
myst:
  html_meta:
    description: Reference documentation for the media-hub interface, which lets snaps operate as the media-hub service for managing media playback on the system.
---

(interfaces-media-hub-interface)=
#  media-hub interface

`media-hub` allows operating as the media-hub service.

**Auto-connect**: no

```{note}
The `media-hub` slot is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

Requires snapd version _2.25+_.


