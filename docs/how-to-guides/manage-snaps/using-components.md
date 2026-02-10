(how-to-guides-manage-snaps-using-components)=
# Work with components

A snap *component* is part of a snap that has been declared as optional. A snap component may then be either installed or not installed alongside its host snap.
See [How components work](/explanation/how-snaps-work/snap-components) for further details.

Component support requires _snapd 2.67+_.

## Installing components

Components can be installed with the snap install command:

```sh
snap install my-snap+comp1+comp2
```

The syntax `<snap_name>+<comp_1>+...+<comp_N>` will be used to refer to components from the command line.

The above command will install _my-snap_ alongside components _comp1_ and _comp2_. If the snap is already installed, the command will instead install only the missing components.

Once installed, the (asserted) components will refresh when new revisions are available in the store, in the same way as for snaps.

It is also possible to install components from local files. If [unasserted](/explanation/security/assertions), they can be installed only if the host snap is unasserted too and you will need to use the --dangerous flag:

```sh
snap install --dangerous ./my-snap+comp1+comp2_1.0.comp
```

When refreshing a snap, all components will refresh to the new revisions tuple. If the new snap revision does not define some components defined in the previously installed snap and that are currently installed, those components will be removed.

Refreshing an unnasserted snap requires  new component builds to be installed manually.

## Updating components

It is also possible to refresh a snap and install a component at the same time:

```sh
snap refresh my-snap+comp1
```

## Listing components

The `snap components` command is used to list the components installed and available on the system:

```sh
$ snap components
Component                    Status     Type
snap-with-comps+one          installed  standard
snap-with-comps+two          installed  standard
snap-with-comps+three        available  standard
other-snap-with-comps+one    installed  standard
other-snap-with-comps+two    installed  standard
other-snap-with-comps+three  available  standard
```

A snap name can be optionally provided to filters the list of reported components to those only associated with the provided snap:

```bash
$ snap components snap-with-comps
Component                	Status 	Type
snap-with-comps+one      	installed  standard
snap-with-comps+two      	installed  standard
snap-with-comps+three    	available  standard
Note that there are some plans for a "snap component" subcommand, but that is not yet implemented and there are talks of changing its design.
```

Using the `snap info` command displays a summary of the ratio of installed components to components available from the store. If both installed and available components are zero, the summary will be omitted

```bash
$ snap info qwen-vl 
name:      qwen-vl
summary:   Qwen VL inference snap
...
installed:          2.5            (248) 332MB -
components: 4/14
```

## Introspecting components

In order to view information regarding an installed/available component(s), the `snap component` command may be used.

```bash
$ snap component qwen-vl+llamacpp
component: qwen-vl+llamacpp
type: standard
summary: llama.cpp Engine using default CPU instruction sets
description: |
  LLM inference in C/C++
installed: b5794 (240) 30MB
```

The last line, `installed:` is only printed if a component is installed.

```bash
$ snap component qwen-vl+llamacpp+model-qwen2-5-vl-3b-instruct-q4-k-m
component: qwen-vl+llamacpp
type: standard
summary: llama.cpp Engine using default CPU instruction sets
description: |
  LLM inference in C/C++
installed: b5794 (247) 31MB
---
component: qwen-vl+model-qwen2-5-vl-3b-instruct-q4-k-m
type: standard
summary: Qwen 2.5 VL 3B Q4
description: |
  Quantized model with 3B parameters in gguf format with Q4_K_M weight encoding
```

## Removing components

To remove only the components, use the "remove" command, followed by the snap and component names:

```sh
snap remove my-snap+comp1+comp2
```

To remove the snap plus any installed components, just remove the snap:

```sh
snap remove my-snap
```

