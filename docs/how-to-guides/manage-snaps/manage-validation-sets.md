(how-to-guides-manage-snaps-manage-validation-sets)=
# Manage validation sets

A [validation sets](/explanation/how-snaps-work/validation-sets) ensures only specific snaps are installed, and optionally, only specific snaps at fixed [revisions](/reference/glossary.md#revision).

For [Landscape](https://ubuntu.com/landscape)-managed devices, see [How to manage snaps in Landscape with validation sets](https://documentation.ubuntu.com/landscape/how-to-guides/iot-for-devices/manage-snaps-with-validation-sets/) after a validation set has been created.

## Create a validation set

```{tip}
For devices running [Ubuntu Core](/reference/glossary.md#ubuntu-core), a validation set can be declared as part of the [model](https://ubuntu.com/core/docs/reference/assertions/model) definition.
```

Ensure you have an [Ubuntu One](https://documentation.ubuntu.com/core/tutorials/build-your-first-image/access-ubuntu-one/) and know your *Developer account id*.

The `snapcraft edit-validation-sets` command is used to create a validation set from the command line:

```
snapcraft edit-validation-sets <account-id> <set-name> <sequence>
```

This command requires your developer account id (`<account-id`), an arbitrary name for the validation set (`<set-name>`), and a sequence number (`<sequence>`). The sequence number starts at 1:

```
snapcraft edit-validation-sets xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f myset1 1
```

An additional `--key-name` argument can be used to specify a key other than the default.

### Validation set template

After running the `edit-validation-sets` command, a text editor will open containing the following template for a validation set assertion that needs to be filled in by the developer issuing the assertion:

```yaml
account-id: <account-id>
name: <set-name>
sequence: <sequence>
# The revision for this validation set
# revision: 0
snaps:
#  - name: <name>  # The name of the snap.
#    id:   <id>    # The ID of the snap. Optional, defaults to the current ID for
                   # the provided name.
#    presence: [required|optional|invalid]  # Optional, defaults to required.
#    revision: <n> # The revision of the snap. Optional.
```
#### Template fields

The template validation set assertion needs to be populated with the details of the snaps you wish to include in the set. These are listed beneath the `snaps:` section, and each snap can use the following fields:

- **account-id** (*required*) the brand account associated with this validation set, as retrieved with `snapcraft whoami`.
- **name** your descriptive name for this validation set.
- **sequence** an integer that should be manually incremented with each updated validation set snap or snap revision. If an update fails to apply, snapd can revert only to a previous sequence.
- **revision** defaults to 0 if not included. An arbitrary number used to differentiate between different uploaded versions of the validation set.


**snaps:**
- **`name`** (*required*):
   The name of the snap, as you find on the store or in _snap search_. 
- **`id`** (*optional*): 
   The unique snap-id of the snap (see _snap info \<snap name\>_ ).
   Defaults to the snap-id of the named snap.
- **`presence`** (*optional*):
   Can be either `required`, `optional` or `invalid`. 
   `required` snaps need to be installed, `optional` snaps are permitted to be installed and `invalid` snaps explicitly must not be installed.
   Defaults to _required_.
- **`revision`** (*optional*):
   Specifies which revision of the snap needs to be installed.

We strongly recommend incrementing the sequence number whenever a validation set used on production devices is modified—especially when updating snap revisions.

This enables snapd to revert to the previous validation set if applying the updated assertion fails. The sequence mechanism was introduced to enable safe rollbacks, because reverting to an earlier validation set revision of the same sequence is not supported.

#### Template example

A basic validation set template example:
```yaml
account-id: xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f
name: myset1
# revision: 0
sequence: 1
snaps:
  - name: hello-world
    id: buPKUD3TKqCOgLEjjHx5kSiCpIs5cMuQ
    presence: required
  - name: test-snapd-base-bare
    id: oXC9AkhtCxhlY80KZA3peZzWbnO4xPOT
    presence: optional
  - name: bare
    id: EISPgh06mRh1vordZY9OZ34QHdd7OrdR
    presence: optional
```

We also recommend making a copy of the saved validation set assertion before closing the editor.  Closing the editor will first check the integrity of the assertion before automatically uploading it to the store.

To modify the assertion at a later point, run the same `snapcraft edit-validation-sets` command with the same name but an incremented sequence number and/or revision. 


```{caution}
Modifying a validation set without updating the sequence can violate the constraints of an enforced validation set, leading to an invalid state that cannot be automatically recovered. For example, accidentally specifying an approved revision of a snap meant for a different architecture will cause the refresh to fail, leaving the validation set in an invalid state.
```

<h2 id='heading--listing'>Listing validation sets</h2>

Use the `snapcraft validation-sets` command to check which validation sets area available in the store:

```
$ snapcraft validation-sets
Account-ID                       Name      Sequence  Revision  When
xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f myset1    1         0         2021-04-08
xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f testset1  2         0         2021-03-31
```

To list only validation-sets with a specific set name, use the additional `--name` argument:

```
$ snapcraft validation-sets --name myset1
Account-ID                       Name      Sequence  Revision  When
xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f myset1    1         0         2021-04-08
```

An additional `--sequence` argument can be used to list validation sets with a specific sequence number:

```
$ snapcraft validation-sets --name myset1 --sequence 1
Account-ID                       Name      Sequence  Revision  When
xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f myset1    1         0         2021-04-08
```

By default, only the _latest_ validation sets are listed. To list every validation set available, add the `--all` argument.

<h2 id='heading--using'>Monitoring assertion validity</h2>

The `snap validate --monitor` command is used to enable monitoring of a validation assertion on the system; in this mode the constraints of the assertion are not enforced (e.g. snaps may get automatically refreshed to newer revisions that make the assertion invalid as shown in the next example):

```
snap validate --monitor xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/testset1
```

The `snap validate` command, with no further arguments, checks whether the `snaps:` rules for all validation set assertions in the store are valid for the system:

```
$ snap validate
Validation                                 Mode     Seq  Current    Notes
xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/myset1    monitor  1    valid  
xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/testset1  monitor  2    invalid
```

An assertion is invalid if snaps in the system do not satisfy the constraints of the assertion, such as if required snaps are missing or whether unwanted snaps are present. Multiple validation sets can be used, as shown above, as long as they don't have conflicting constraints and that they can cover different sets of snaps.

A specific validation set can be checked with `snap validate <account id>/<validation set name>`, with an optional sequence point set by adding `=<sequence>` to the validation set name:

```
$ snap validate xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/myset1=1
valid
```

A validation set assertion can be _pinned_ by the system administrator at the given sequence number:

```
snap validate --monitor xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/testset1=3
```

A pinned validation set is kept at the given sequence number, even if there's a higher sequence number in the store. However, the validation will be updated to a newer version if one becomes available with the same sequence number.

Monitor mode validation requires a manual action (`snap validate`, as shown above), but nothing is enforced in the system. Only when _enforce mode_ has been implemented will validation sets have an impact on the system and will prevent installing/removing snaps that violate an assertion's constraints.

Finally, to remove a validation set from the system, use the `--forget` argument:

```
snap validate --forget xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/myset1
```

<h2 id='heading--enforcing'>Enforcing assertion validity</h2>

When validation set validity is enforced, snapd will block any operations that would result in snap revisions violating the validation set’s constraints and rendering it invalid.

A validation set can only be enforced if all required snaps are installed, and at the correct revision if specified. This is done by adding the `--enforce` argument to the ‘snap validate’ command:

```
snap validate --enforce xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/myset1
```

This command will fetch the validation set assertion from the store if not available on the system, but will not refresh assertions, install missing snaps or remove invalid snaps. However, the `--refresh --enforce` arguments can be used to refresh the validation set assertion, install or refresh any snaps and revisions required for the assertion to become valid. Note that, if the assertion requires snaps to be removed, the `--refresh --enforce` request will not remove them and will instead quit without making any changes.

```
snap validate --refresh --enforce xSfWKGdLoQBoQx88vIM1MpbFNMq53t1f/myset1
```

After enforcement is enabled, snapd ensures the consistency of the enforced validation sets, and the snaps they reference, during install, refresh and remove operations.

During auto-refreshes or manual refreshes, enforced validation set assertions on the system may be updated to a newer revision. 

If a validation set assertion is not pinned to a specific sequence, the system will move to the latest sequence available in the store, provided that the installed snaps, including any newer revisions available in store, satisfy its constraints. 

However, if the assertion is pinned to a specific sequence, or if a newer revision of the same sequence is available, the system will move to that revision without re-evaluating whether its constraints are still satisfied. This can cause the validation set to become invalid without warning. 

To ensure safe rollbacks and consistent behavior, always increment the sequence number when creating a new revision of a validation set used in production.

In this way, the `snapcraft edit-validation-sets` command can be used to control the updates of multiple snaps at the same time.

For brief periods during multi-snap updates, different snap revisions, from previous and incoming validation set sequence points, can co-exist. Validation set enforcement is not intended to deal with any breaking hard version dependencies during transitions.

As with monitor mode, enforcing can be disabled for select validation sets with the ‘snap validate --forget’ command.

When using `snap install` and `snap refresh`, the `--ignore-validation` flag can be added to bypass validation set enforcement for the snaps affected. Doing so will ignore the validation of the given snap, and for subsequent refresh operations. This may result in the validation set becoming _invalid_ in `snap validate` output.

