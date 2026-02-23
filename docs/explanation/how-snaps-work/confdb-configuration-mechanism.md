(explanation-how-snaps-work-confdb-configuration-mechanism)=
# Confdb configuration mechanism

*Confdb* is a configuration mechanism that replaces individual [snap-specific configuration](/how-to-guides/manage-snaps/set-system-options) with an external [confdb-schema](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/) assertion, separating the configuration data from the snap installation. This allows for advanced configuration functionality, including:

* device onboarding and management
* cross-snap configuration
* precise access control
* evolving configuration settings without changing the affected snaps

See [How to configure snaps with confdb](/how-to-guides/manage-snaps/configure-snaps-with-confdb) for instructions on using confdb with your own snaps, and read on for specific implementation details.

Confdb is currently considered an [Experimental feature](/reference/development/experimental-features) and implementation details may change as development progresses.

## Confdb views

Settings are exposed via _views_. Views allow for both granular access control and *granular configuration contracts* to enable the evolution of a configuration value.

The `view` field in the  [confdb-schema assertion](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/#confdb-schema-assertion-fields) is a set of mappings from “request” paths to “storage” paths.

Users and snaps can access the _request_ path, while the _storage_ path defines the layout in storage.

The separation of the *request* path from the *storage* path provides the isolation, allowing the configuration layout to evolve without having to propagate those changes to every accessing snap.

### Confdb view requests

When making a request, an administrator (or a snap accessing a configuration), must specify both a view and a request path.

An attempt is then made to match the request path against a path in the view's rules. If a rule’s path contains a matching prefix then the corresponding storage path is used to retrieve a value.

If more than one rule matches the request, then the result is aggregated from all of the values. 

Multiple views can have the same “request” field, but different “storage”, facilitating backwards compatibility when transitioning to a new layout. 

#### Example implementation

The following is almost the simplest confdb-schema assertion that could be defined to obtain some information about installed snaps, although we omit the other headers and the body for brevity. See [Configure snaps with confdb](/how-to-guides/manage-snaps/configure-snaps-with-confdb) for the full details.


##### Basic example

```yaml
type: confdb-schema
account-id: system
name: snap-status

[...]

views:
  observe:
    rules:
      -
      request: snaps.firefox.status
      storage: snaps.firefox.status
      access: read

[...]
```

This above configuration could be be accessed as follows:

```
$ snap get system/snap-status/observe snaps.firefox.status
enabled
```

We now want to expand the above example to allow status and *revision* queries for many different snaps.

##### Placeholders

Instead of enumerating every possible combination, we can use a placeholder to map a variable in the request path to the storage path:

```yaml
[...]
    rules:
      -
      request: snaps.{name}.status
      storage: snaps.{name}.status
      access: read
[...]
```

This enables the snap name to be dynamically mapped into the query: 

```
$ snap get system/snap-status/observe snaps.firefox.status
enabled

$ snap get system/snap-status/observe snaps.spotify.status
disabled
```

##### Nested paths

To add more configuration paths for snaps, either add more rules or, if possible, use a “content” shorthand to define nested paths:

```yaml
[...]

    rules:
      -
      request: snaps.{name}
      storage: snaps.{name}
      access: read
      content:
        - storage: status
        - storage: revision

[...] 
```

This example only provides a storage path. When omitted, the request path is assumed to be equal to the storage path by default.

##### Aggregate results

As requests are matched on *prefixes* of the request paths in view rules, it’s possible to provide a prefix path to \`snap get\` and to obtain an aggregate result:

```
$ snap get system/snap-status/observe snaps.firefox.status
enabled

$ snap get system/snap-status/observe snaps.spotify.revision
7

$ snap get system/snap-status/observe snaps
{
  "firefox": {
    "status": "enabled"
  },
  "spotify": {
    "status": "disabled",
    "revision": 7
  }
}
```

##### Evolving configuration

All the rule mappings defined above have the same “request” and “storage” paths. As snapd maps request paths to storage paths, let’s say a user or snap is interested in knowing the system’s (in this case, snapd’s) status. To take advantage of confdb’s features for evolving configuration schemas and re-organising namespaces, we could add the following rule:

```yaml
...
    rules:
      -
      request: snaps.{name}
      storage: snaps.{name}
      access: read
      content:
        - storage: status
        - storage: revision
      -
      request: system-status
      storage: snaps.snapd.status
      access: read
```

This maps an already exposed path (snaps.snapd.status) under a new request path, allowing us to query `system-status` directly.

In the future, if a new path was intended to provide the value for `system-status`, we would only need to modify the mapping.

```
$ snap get system/snap-status/observe
{
  "snaps": {
    "firefox": {
      "status": "enabled"
    },
    "spotify": {
      "status": "disabled",
      "revision": 7
    },
    "snapd": {
      "status": "enabled"
    },
  },
  "system-status": "enabled"
}
```

Requests are compared to rule prefixes until a match occurs which means an empty request matches every rule.

##### Namespaces

If there a change in the configuration data’s layout, only the assertion needs to be modified. The snap could experience the same namespace, isolating it from schema changes. For example, the following assertion exposes the same data under the same namespace (from a user or snap’s perspective) but the storage layout it assumes is completely different:

```yaml
...
    rules:
      -
      request: snaps.{name}.status
      storage: statuses.{name}
      access: read
      -
      request: snaps.{name}.revision
      storage: revision.{name}
      access: read
      -
      request: system-status
      storage: status.snapd
      access: read
```

## Interface Plugs

Snaps can use the [confdb interface](/) to express their interest in accessing a view through the plug stanza in their snapcraft.yaml (then snap.yaml). For example, a snap wishing to access the same `observe` view would declare it as:

```yaml
plugs:
  observe-status:
    interface: confdb
    account: system
    view: snap-status/observe
```

If the snap publisher signed the confdb assertion, the confdb interface will be auto-connected. Otherwise, the plug must be connected to the `:confdb` slot manually.

The snap can then refer to this interface plug when accessing confdb with the `snapctl` commands. It must also use the `--view` flag to signal this as a confdb request:

```
$ snapctl set --view :observe-status snaps.firefox.status=enabled
$ snapctl get --view :observe-status snaps.firefox.status
enabled
```

confdb supports the same commands and options as the [original configuration mechanism](/how-to-guides/work-with-snaps/configure-snaps). This includes unsetting data using `snapctl --view unset ...` or by using `snapctl --view set` with a `\!` prefixed to the request path.

### Custodians

The confdb interface plug can have one other attribute, `role`, which is optional and can only take a value of `custodian`.

`custodian` declares that the snap has a special role in managing the data accessed through the referenced view. Custodians are responsible for a subset of the configuration data. As such, at least one custodian must be installed and connected for the data to be accessible.  

One of the key aspects of the custodian role relates to ephemeral data which we’ll cover in the next section.

## Ephemeral data

In the context of confdb, ephemeral data is configuration data for which the authoritative version is stored outside of snapd. Snapd may retain data, but this should only be considered a cache, while the custodians are responsible for loading and storing the authoritative version during read and write accesses.

Configuration paths are marked as ephemeral in the storage schema which is specified in the body of the [confdb-schema assertion](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/#ephemeral-data).

During `snap` or `snapctl` access (whether to read or write), changes are either committed or read as a transaction. Snapd will get data from its storage and then schedule certain [hooks](https://documentation.ubuntu.com/snapcraft/stable/reference/hooks/) from snaps with plugs referring to views affected by the data.

We’ll cover hooks in more detail in the next section so for now we’ll just focus on two: `save-view-<plug>` and `load-view-<plug>`. These are invoked for custodian snaps when writing and reading, respectively, and are prefixed with the name of the interface plug for which the snap is custodian. 

When snapd detects that a `snap` or `snapctl set` might impact ephemeral data, it stores the changes in a transaction object and invokes `save-view-<plug>` hooks for connected custodians. These hooks can then query the ongoing transaction with the usual `snapctl get --view ...` commands to read changes to the ephemeral data and then store them off-snapd as they wish. Snapd will also store these changes but it does so as a cache, not as an authoritative version.

When ephemeral data is read, snapd will similarly schedule `load-view-<plug>` hooks that give custodians an opportunity to read new data outside of snapd and then load into the transaction read with the usual `snapctl set --view ...` commands.

## Hooks

Confdb supports 5 types of [hooks](https://documentation.ubuntu.com/snapcraft/stable/reference/hooks/):

* `load-view-<plug>`  
* `query-view-<plug>`  
* `change-view-<plug>`  
* `save-view-<plug>`  
* `observe-view-<plug>`

`load-view-<plug>` and `query-view-<plug>` are scheduled during read operations, while `change-view-<plug>`, `save-view-<plug>` and `observe-view-<plug>` are relevant only to writes. 

The `save-view`/`load-view` hooks are mandatory if the path being accessed either maps to ephemeral data or may contain nested data that is (i.e., that is marked as ephemeral in the storage schema). The other hooks are optional.

During a read of the confdb data:
1. snapd first reads the configuration data it stores internally and creates a transaction object to carry it.
1. Snapd then schedules `load-view-<plug>` hooks for any custodian snaps with interface plugs for the referenced view. These hooks allow the snaps to load the ephemeral data, if they wish to.
1. After those hooks load any off-loaded data, the `query-view-<plug>` hooks run for any relevant custodian that defines them. These hooks give the custodian snaps a chance to modify the read data before it’s returned to the reader. This could be used to apply a constraint that couldn’t be enforced on write (e.g., if the data is ephemeral and could be modified off-snapd).

Both series of hooks are run in the same order, sorted by their snap’s name.

Writes to confdb data operate in a similar fashion to reads:
1. Snapd creates a transaction object, storing the intended changes to the confdb data. 
1. The first hooks to be scheduled are the `change-view-<plug>` hooks. These hooks provide an opportunity for custodian snaps to modify the data before it’s committed or even to reject it entirely. This is useful if the snaps must maintain complex invariants that can’t be expressed as [schema types and constraints](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/#schema-types).
1. Data modification is done with `snapctl set --view` command in the usual manner.
   To help snaps distinguish between uncommitted and pristine data, a `--pristine` flag can be used with `snapctl get --view`:

   ```
   $ snapctl get --view :plug-name path.modified
   <new_data>

   $ snapctl get --view --pristine :plug-name path.modified
   <old_data>
   ```

   It’s also possible to reject the change altogether while providing a reason for the rejection:

   ```
   $ snapctl fail <reason>
   ```

1. Once all `change-view-<plug>` hooks have run, the `save-view-<hooks>` run in the same order (i.e., ordered by snap name). If any hook should fail, the transaction would be cancelled. Any `save-view-<plug>` hooks that had been invoked would be invoked again with pristine data, in order to help custodian snaps maintain consistency among the various versions of the configuration data. 

1. Finally, snapd schedules `observe-view-<plug>` hooks, which is the only type of confdb hook that can be defined by a non-custodian snap. This hook simply notifies snaps plugging views affected by the write that configuration data relevant to them may have changed. The failure of these hooks does not prevent the committing of the changes, as non-custodians are not allowed to reject them. Once those hooks run (successfully or not), the changes are committed by snapd.

