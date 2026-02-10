(explanation-how-snaps-work-snap-components)=
# Snap components

Snap _components_ are parts of a snap that can be built and uploaded in conjunction with a host snap and later optionally installed beside it.

Components are useful for distributing optional resources for a snap, such as debug symbols alongside snap binaries, and kernel modules alongside a kernel snap.

Just like a snap, a component is implemented as a squashfs file. If installed, this file is mounted in a location accessible to the host snap.

Components can be thought of as either an internal implementation detail of the host snap that remains transparent to the user, or as a visible snap component that can be installed, refreshed and removed similarly to snaps.

See [Using components](/how-to-guides/manage-snaps/using-components) for installation, removal and listing options. To control components from within a snap, see [snapctl components](/t/15002#heading--components). Components can also be managed through the [Snapd REST API](/reference/api/redoc-static).

Component requires *snapd 2.67+* .

## Schema

Components are defined with a top-level `components` keyword in a snapcraft.yaml:

```yaml
components:
  <name>:
    type: <standard|kernel-modules|...>
    summary: ...
    description: ...
  ...
```

A corresponding `meta/component.yaml` file contains the metadata for each component with the following fields:

```yaml
component: <snap_name>+<component_name>
type: <component_type>
version: <version>
summary: ...
description: ...
```

- `component` and `type` are mandatory
- `version` will inherit the snap version if not set in component.yaml

For more details on component types, see [Snapcraft components](https://canonical-snapcraft.readthedocs-hosted.com/en/latest/reference/components/). 

It is possible to create a component by running `snap pack <dir>`, however, `<dir>/meta/component.yaml` must already exist.

All files inside this directory will be included within the created squashfs file, which will be named by default `<snap_name>+<component_name>_<comp_version>.comp.`

For further details on packaging, see [How to package and upload a snap with components](https://canonical-snapcraft.readthedocs-hosted.com/en/latest/howto/components.html). 

## Revisions

Just like snaps, components have [revisions](/explanation/how-snaps-work/revisions). If a snap defines components, each snap file uploaded to the store will be matched to components with their own specific revisions 
This forms a unique tuple between the snap and each respective component. 

> ⓘ  While it will become possible to update components in a tuple, the snapcraft functionality required to individually upload an updated component has not yet been implemented.

## Component hooks

Components can implement the following  [hooks](/reference/development/supported-snap-hooks):

* install
* pre-refresh
* post-refresh
* remove

These correspond to executables with the same name that must be stored in meta/hooks/ inside the component file. Semantics will be similar as the homonymous hooks for snaps, with the caveat that if run as part of the same change that installs/refreshes/removes a snap, the following execution order is defined:

* install hook: 1st snap’s, 2nd component’s
* pre-refresh hook: 1st component’s, 2nd snap’s
* post-refresh hook: 1st snap’s, 2nd component’s
* remove hook: 1st component’s, 2nd snap’s

The rationale for the order is that components have a dependency on the snap and might need information from the snap to be present when installed. For instance, we need the plug information that is part of the snap metadata before we can run the component hook.

The component hooks might need plugs. If that is the case, they need to be defined in the snap metadata inside the snap container (as it is where we have the capability to define plugs).

The syntax in `snapcraft.yaml` and `snap.yaml` will be the same as for snap hooks, but under the components.<name> stanza:

```yaml
components:
  <name>:
    type: ...
    hooks:
      <hook_name>:
        plugs:
          - <plug_name>
          - ...
  ...
```

## Environment variables

The execution environment for component hooks will be similar to the one defined for snap applications/hooks, with the injection of the following additional [environment variables](/reference/development/environment-variables):

- `SNAP_COMPONENT`: directory where the component is mounted
- `SNAP_COMPONENT_NAME`: name of the component as specified in component.yaml
- `SNAP_COMPONENT_REVISION`: revision of the component
- `SNAP_COMPONENT_VERSION`: version of the component as specified in component.yaml

Component hooks run as confined snap applications, which is also the case for all snap hooks.

