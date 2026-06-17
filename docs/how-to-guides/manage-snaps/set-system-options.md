(how-to-guides-manage-snaps-set-system-options)=
# Set system options

Snap supports a set of system-wide options that allow you to customise your snap environment. See {ref}`System options <how-to-guides-manage-snaps-set-system-options>` for which options are supported.

As with {ref}`Configuration in snaps <how-to-guides-work-with-snaps-configure-snaps>`, these options are changed with the `set` and `get` commands, but with a target of  *system* instead of a specific snap:

```
snap set system system.timezone="Europe/London"
snap get system system.timezone
```

Configuration options can be unset by either passing their names to the unset command or by adding an exclamation mark (!) to the end of an option name:

```
$ snap unset system system.hostname
$ # or
$ snap set system system.hostname!
```

If a setting is part of the system snap, provided by either the core snap or snapd itself, the command syntax will include two instances of _system_, such as with `system.timezone`:

```
snap set system system.timezone="Europe/London"  
```

Typing `snap get system` outputs a top-level view of system-wide option categories which can be added as arguments to view their contents:

```
$ snap get system
Key           Value
experimental  {...}
refresh       {...}
seed          {...}
system        {...}
$ snap get system experimental
Key                   Value
experimental.hotplug  true
experimental.layouts  true
```

The entire set of system configuration options can be dumped as JSON by adding the -d option:

```
$ snap get -d system
{
        "experimental": {
                "hotplug": true,
                "layouts": true,
                "quota-groups": true
        },
        "refresh": {
                "last": "2017-05-25T09:03:58.664837614+01:00",
                "retain": 2
        },
        "seed": {
                "loaded": true
        },
        "system": {
                "hostname": "neon",
                "network": {},
                "timezone": "UTC"
        }
}
```

```{caution}
Options are _not visible_ until after they are set. The `snap get` command can then be used to check their state.
```

