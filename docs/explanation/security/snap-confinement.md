(explanation-security-snap-confinement)=
# Snap confinement

Snap confinement determines the amount of access an application has to system resources, such as files, the network, peripherals and services. There are several levels of confinement.

Confinement ensures that individual pieces of software do not impact the robustness of the user's system or cause issues with other applications. As a result, when the user runs a snap, the software it provides is isolated from the system to some degree, with a default that limits access to a strict minimum of features.

## Confinement levels

A snap's confinement level controls the degree of isolation it has from the user's system. Application developers or packagers can adjust the confinement level to specify in broad terms how much access to system resources an application needs, either for normal use or during development.

There are two levels of snap confinement for published snaps:
- **Strict** 
   Used by the majority of snaps. Strictly confined snaps run in complete isolation, up to a minimal access level that's deemed always safe. Consequently, strictly confined snaps can not access files, network, processes or any other system resource without requesting specific access via an interface ([see below](#interfaces)).
- **Classic**
   Allows access to the system's resources in much the same way traditional packages do. To safeguard against abuse, publishing a classic snap requires [manual approval](/reference/administration/reviewing-classic-confinement-snaps), and installation requires the `--classic` command line argument.

An additional mode is useful during the development process:
- **Devmode**
   A special mode for snap creators and developers. A *devmode* snap runs as a strictly confined snap with full access to system resources, and produces debug output to identify unspecified interfaces. Installation requires the `--devmode` command line argument. Devmode snaps cannot be released to the stable channel, do not appear in search results, and do not automatically refresh.

Strict confinement uses security features of the Linux kernel, including AppArmor, seccomp and namespaces, to prevent applications and services accessing the wider system.

For details on how confinement is implemented, see [Snap system architecture](/reference/operations/system-architecture).

## Getting the confinement level

Use the `snap` command to discover the confinement level for a snap:

```
$ snap info --verbose vlc
[...]
  confinement:       strict
  devmode:           false
[...]
```

To see which installed snaps are using classic confinement, look for *classic* under the *Notes* column in the output of `snap list`:

```
$ snap list
Name      Version   Rev   Tracking  Publisher       Notes
vlc       3.0.6     770   stable    videolan✓       -
code      0dd516dd  5     stable    vscode✓         classic
wormhole  0.11.2    112   stable    snapcrafters    -
```
<a name="interfaces"></a>

## Interfaces and confinement

Snaps with strict confinement must use [interfaces](/explanation/interfaces/all-about-interfaces) to access resources on the user's system, including those provided by other snaps.

