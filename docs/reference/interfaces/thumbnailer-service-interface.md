(interfaces-thumbnailer-service-interface)=
#  thumbnailer-service interface

`thumbnailer-service` allows operating as, or interacting with, the system Thumbnailer service, a DBus service for creating thumbnail images from local media files.

**Auto-connect**: no

```{note}
The `thumbnailer-service` slot is unsupported for {ref}`parallel instances <interfaces-parallel-installs-unsupported>`. The slot owns a unique system-wide resource that instances would conflict over.
```

Requires snapd version _2.22+_.


