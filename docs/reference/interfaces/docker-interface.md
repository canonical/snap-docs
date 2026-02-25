(interfaces-docker-interface)=
#  docker interface

The `docker` interface allows client access to the Docker socket. Use this interface when you want to interact with the Docker daemon.

Due to the nature of containers, the permissions granted to the [Docker snap](https://snapcraft.io/docker) allow it to bypass elements of the _snapd_ security sandbox. This is acceptable because the Docker snap publisher is trusted and because applications running inside such containers are further isolated with the sandbox built by Docker itself.

While anyone can rebuild the [Docker snap from source](https://github.com/docker-snap/docker-snap), not everyone is immediately trusted with the privileged interfaces it requires to function. This interface can be used instead to permit such access by allowing snapped applications to communicate with the Docker daemon socket on the Docker snap. This enables anyone to create and publish a snap that requires Docker without requiring the same privileged interfaces required by the Docker snap itself.


```{tip}
See [Interface management](/) and [Supported interfaces](/reference/interfaces/index) for further details on how interfaces are used.
```

---

## Developer details

**[Auto-connect](/explanation/interfaces/interface-auto-connection)**: no</br>
**[Super-privileged](/)**: yes</br>

For distribution via the [Snap store ](https://snapcraft.io/store), consumers of this interface require an approved [snap declaration](https://forum.snapcraft.io/t/process-for-aliases-auto-connections-and-tracks/455/).

### Example implementation

The source code for a complete example snap that communicates with the Docker snap can be found here: [github.com/zyga/hello-docker](https://github.com/zyga/hello-docker)

The following is an excerpt from the above snap's snapcraft.yaml:

```yaml
base: core22
confinement: strict
apps:
  hello-docker:
    command: usr/bin/hello-docker
    environment:
      PATH: $SNAP/docker-snap/bin:$PATH
    plugs:
      - docker
      - docker-executables
plugs:
  docker:
    label: Access to the docker communication socket
  docker-executables:
    label: Access to the docker command-line utilities
    interface: content
    content: docker-executables
    target: $SNAP/docker-snap
    default-provider: docker
```

This snapcraft.yaml will build a [strictly confined](/) snap package which is portable across environments and works equally on IoT-centric Ubuntu Core as well as on most commonly used desktop and server distributions.

The snap has one [apps definition](/) which contains the `hello-docker` application. This application uses two snap interface plugs, one called _docker_ and the other called _docker-executables_.

The plugs for both are defined in more detail in the `plugs:` section. In this section, _docker_ refers to this specific interface while _docker-executables_ is an example of a [content interface](/reference/interfaces/content-interface). The content interface is further specified to refer to content of type docker-executables. This is important as it has to match what is [provided by the Docker snap](https://github.com/docker-snap/docker-snap/blob/058337577d4172c8919a53a41c38ebe7ee9beab0/snap/snapcraft.yaml#L90C1-L90C22) available in the store.

Plugs of the content interface have the target attribute which defines where the corresponding content is made available. In this case, it is the directory `docker-snap` inside the read-only image of the application snap. It is important that our application snap contains an empty directory with the same name, so that when the Docker snap is installed and the interfaces are connected, we can access the Docker snap's command line tools.

The app definition contains an environment variable that directs the application to look for Docker executables in the `$SNAP/docker-snap/bin` sub-directory. This sub-directory will only exist when the content interface is connected.

Lastly, the default-provider field tells snapd that if the user does not have any snap with a compatible interface installed, then upon installation of our snap, the docker snap is automatically installed and connected.

When the above example snap is built and installed, you can open a shell within the snap's environment with the following command:


```
snap run --shell hello-docker
```

The Docker command line tool, among other Docker-related executables, can be found within `$SNAP/docker-snap/bin`. Since this is within the `$PATH`, Docker can now be used within your own scripts, or for whatever purpose you may require.

