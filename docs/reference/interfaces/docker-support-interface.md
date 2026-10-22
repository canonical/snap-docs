---
myst:
  html_meta:
    description: docker-support interface
---

(interfaces-docker-support-interface)=
#  docker-support interface

`docker-support` allows operating as the Docker daemon. This interface is for internal use by the [Docker snap](https://snapcraft.io/docker). You should not need to use this interface in your snap.

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes

```{note}
The `docker-support` plug is {ref}`unsupported for parallel instances <interfaces-parallel-installs-unsupported>`.
```

**Attributes:**
   * `privileged-containers` (plug): true|false (defaults to ``false``)

Can access resources and system calls necessary to run Docker application containers. The `privileged-containers` attribute may be used to give the necessary access to run privileged containers. Providing snaps specifying this interface currently may only be established with the Docker project.


