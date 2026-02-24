(how-to-guides-manage-snaps-configure-snaps-with-confdb)=
# Configure snaps with confdb

_Confdb_ is a configuration system that allows snaps to be configured in fine-grained ways using a [confdb-schema](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/) assertion.

This guide will detail the steps required to use confdb, as well as explore some of its features. For implementation details, see the [Confdb configuration mechanism](/explanation/how-snaps-work/confdb-configuration-mechanism). 

We'll use an example where one snap creates a Wi-Fi configuration that another snap can view.

```{caution}
Confdb is currently considered an [Experimental feature](/reference/development/experimental-features) and implementation details may change as development progresses.
```

## Prerequisites

We first need to ensure the latest version of snapd is installed. This is important as confdb is still being actively developed:

```
snap refresh
```
We can then enable confdb with its experimental feature flag:

```
sudo snap set system experimental.confdb=true
```

## Creating a confdb-schema assertion

To use confdb, we must first create a [confdb-schema assertion](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/).

There are two main parts to a confdb-schema assertion:
- View rules
- Storage schema
 
The *view rules* determine the “schema” of the configuration namespace exposed to the snap, i.e., what paths can be accessed and how they’re mapped onto the storage schema.

The *storage schema* determines what the actual stored data looks like and what constraints apply.

We’ll start by defining a storage schema.

### Storage schema

When creating the storage schema, we can constrain the format and values that the stored data can take, such as the characters you can include in a password.

For example:

```json
  {
    "storage": {
      "aliases": {
        "password": {
          "type": "string",
          "pattern": "^[\w~!@#\$%\^&-\+=\;:,\.\/\?]{8,63}$"
      },    
    },
      "schema": {
        "wifi": {
          "schema": {
            "psk": "$password",
            "ssid": "string",
            "state": {
              "type": "string",
              "choices": [
                "up",
                "down"
              ]
            }
          }
        }
      }
    }
  }
```

The above schema describes three configuration paths: an SSID, a password and a connection state.

Snapd expects the storage schema to conform to a very precise format, using 2 spaces for indentation and sorting map entries. Both Python 3’s `json.dump` and Golang’s `json.MarshalIndent` can be used to produce this format. `jq -S` can also be used to sort the schema. It’s useful to keep the storage schema in its own file so we can modify it over time.

See [confdb-schema types](https://documentation.ubuntu.com/core/reference/assertions/confdb-schema/#schema-types) for a detailed description of types and contrains. 

### View rules

Now let’s create some view rules to access confdb.

In our example, we’ll use one snap to configure the network and another to access, which means we need two views: `configure-wifi` and `access-wifi`.

* `configure-wifi` exposes parameters and allows them to be set.
* `access-wifi` allows the snap to list Wi-Fi connections and read SSID and state information (e.g., up, down).

Both of these can be defined as follows:

```yaml
type:         confdb-schema
authority-id: <account-id>
account-id:   <account-id>
name:         network
summary:      Configure network parameters
timestamp:    2025-04-02T19:31:32Z
views:
  configure-wifi:
    summary: Configure Wi-Fi networks
    rules:
      -
      request: "{name}.ssid"
      storage: "wifi.{name}.ssid"
      -
      request: "{name}.password"
      storage: "wifi.{name}.psk"
      -
      request: "{name}.state"
      storage: "wifi.{name}.state"

  access-wifi:
    summary: List and read Wi-Fi SSIDs
    rules:
      -
      request: "{name}"
      storage: "wifi.{name}"
      access: read
      content:
        -
        storage: ssid
        access: read
        -
        storage: state
        access: read

body-length: 552
sign-key-sha3-384: 74KHeq1foV…
```

See [Access Ubuntu One](https://documentation.ubuntu.com/core/tutorials/build-your-first-image/access-ubuntu-one/#retrieve-your-developer-account-id) for details on retrieving your `account-id`.

## Putting it together

Now we’re ready to create the assertion. Run the following command, filling in the account ID and key name:

```shell
snapcraft edit-confdb-schema <account-id> network --key-name=<key-name>
```

Next, edit the template assertion, replacing the views and storage schema with the ones we defined above.

The end result should look something like the following:

```yaml
account-id: <account-id>
name: network
views:
  configure-wifi:
    rules:
      -
        request: "{name}.ssid"
        storage: "wifi.{name}.ssid"
      -
        request: "{name}.password"
        storage: "wifi.{name}.psk"
      -
        request: "{name}.state"
        storage: "wifi.{name}.state"

  access-wifi:
    rules:
      -
        request: "{name}"
        storage: "wifi.{name}"
        access: read
        content:
          -
            storage: ssid
            access: read
          -
            storage: state
            access: read

body: |-
  {
    "storage": {
      "aliases": {
        "password": {
          "pattern": "^[a-zA-Z0-9~!@#\\$%&-=:,\\.]{8,63}$",
          "type": "string"
        }
      },
      "schema": {
        "wifi": {
          "values": {
            "schema": {
              "psk": "$password",
              "ssid": "string",
              "state": {
                "choices": ["up", "down"],
                "type":"string"
              }
            }
          }
        }
      }
    }
  }
```

Then exit the editor and sign the assertion when prompted.

## Creating the snaps

See [Create a new snap](https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/) for a general overview of the snap creation process.

There are two things a snap needs to be able to use confdb:
* a plug to declare its intent to use a confdb namespace and 
* an optional set of [hooks](/reference/development/supported-snap-hooks) that snapd invokes when the namespace is accessed

### Custodian snap

The interface plug specifies an `account` and a `view` which together identify the view through which the configuration is being accessed. It can also optionally declare a `role`, with a value of `custodian`.

Custodian snaps have a special role when accessing ephemeral data. They're responsible for saving or loading this data to an external source outside of snapd.

The data that snapd stores for ephemeral configuration is only a cached, non-authoritative version of the external data. At least one custodian snap must be installed in the system for a particular confdb-schema.

The first snap will configure the Wi-Fi network to be used, so let’s configure it accordingly:

```yaml
plugs:
  configure-wifi:
    interface: confdb
    account: <account-id>
    view: network/configure-wifi
    role: custodian
```

The other component that must be defined in the snap are the [hooks](/reference/development/supported-snap-hooks). 

Snaps interact with confdb through [snapctl](/how-to-guides/manage-snaps/use-snapct) and, in turn, snapd invokes various hooks when confdb is read from or written to.

In this case, the custodian snap will only define the `change-view-<plug>`, which provides an opportunity for the snap to modify values being set.

As an example, we’ll say that the SSID must be prefixed with our company’s name: “Acme”. The configuration can be set by the administrator using [snap set](/how-to-guides/manage-snaps/configure-snaps) or by any other snap with access to that view, so it’s the custodian snap’s responsibility to enforce that the prefix is enforced.

Our `change-view-configure-wifi` hook looks like this:

```shell
#!/bin/bash -xe

# prefix the SSID with "acme", if not already present
value=$(snapctl get --view :configure-wifi acme.ssid)
if [[ "$?" -eq 0 && "$value" != acme-* ]]; then
  snapctl set --view :configure-wifi ssid="acme-$value"
fi
```

That’s it for the custodian snap.

### Reader snap

Now we’ll create a snap that will read the configuration. Its plug will reference the read-only view and it will omit the `role`:

```yaml
plugs:
  access-wifi:
    interface: confdb
    account: <account-id>
    view: network/access-wifi
```

Non-custodian snaps can only define an `observe-view-<plug>` hook, which allows them to be notified when the confdb-schema referenced by that plug has been used to modify data.

```shell
#!/bin/sh -xe

# read the new SSID and store it somewhere
new_ssid=$(snapctl get --view :access-wifi acme.ssid)
echo "$new_ssid" >> "$SNAP_COMMON"/ssid
```

## Install and connect the snaps

We can mediate snap access to confdb-schema views by connecting their confdb plugs.

Note that when a snap is published by the same account ID as the assertion, the interface plug will be auto-connected.

```shell
snap install custodian-snap reader-snap 
snap connect custodian-snap:configure-wifi 
snap connect reader-snap:access-wifi 
```

## Setting data

Now we’re ready to start setting data, we’ll use `snap run --shell` to mimic the snaps interacting with confdb:

```shell
$ sudo snap run --shell custodian-snap.sh
# snapctl set --view :configure-wifi acme.ssid=some-ssid acme.password=super-secret
# exit

$ sudo snap run --shell reader-snap.sh
# snapctl get --view :access-wifi acme.ssid
acme-some-ssid
# exit

$ snap get <account-id>/network/access-wifi acme.ssid
acme-some-ssid
```

As expected, the `change-view-configure-wifi` hook was invoked when `custodian-snap` modified the SSID and prefixed the value with “acme”.

We were also able to read the same value from both another connected snap and through the snapd API using `snap get`.

We can also check that the `reader-snap`’s `observe-view-access-wifi` hook was invoked when the SSID was changed and that it saved the new value in SNAP\_COMMON:

```shell
$ snap changes
ID   Status  Spawn               Ready               Summary
123  Done    today at ...        today at ...        Set confdb through "<account-id>/network/configure-wifi"
...

$ snap change 123
Status  Spawn  Ready  Summary
Done    ...    ...    Clears the ongoing confdb transaction from state (on error)
Done    ...    ...    Run hook change-view-manage-wifi of snap "custodian-snap"
Done    ...    ...    Run hook observe-view-manage-wifi of snap "test-snap"
Done    ...    ...    Commit changes to confdb (NI7Jstuu8gffcoXr02i1kYt898p6Co0A/network/wifi-setup)
Done   ...    ...   Clears the ongoing confdb transaction from state


$ cat /snap/reader-snap/common/ssid
acme-some-ssid
```

