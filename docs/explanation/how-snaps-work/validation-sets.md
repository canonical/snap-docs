(explanation-how-snaps-work-validation-sets)=
# Validation sets

A validation set is an [assertion](/explanation/security/assertions) that lists specific snaps and components that are either required to be installed together or are permitted to be installed together on a device or system.

They can be created using the `snapcraft` command, and monitored with the `snap` command.  See [How to manage validation sets](/how-to-guides/manage-snaps/manage-validation-sets) for further details. For devices running [Ubuntu Core](/reference/glossary.md#ubuntu-core), they can be declared as part of the [model](https://ubuntu.com/core/docs/reference/assertions/model) definition.

## Why use a validation set

A validation set can help a group of interdependent snaps maintain their testing and certification integrity, as well as help orchestrate their updates. But they can equally be used to simplify dependency deployment and to help manage devices.

In particular, if the [model assertion](https://ubuntu.com/core/docs/reference/assertions/model) for a device includes optional snaps, a validation set can be used to ensure specific collections of snaps are installed together on derivatives of the same devices.

Enforced validation sets prevent listed snaps and components from being removed from the system

"""bash
error: cannot remove component "mysnap+mycomp" as it is required by an enforcing validation set
"""
