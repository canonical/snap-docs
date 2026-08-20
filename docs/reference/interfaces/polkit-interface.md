(interfaces-polkit-interface)=
#  polkit interface

The `polkit` interface provides daemons with:
1. The permission to use the [polkit authorisation manager](https://www.freedesktop.org/software/polkit/docs/latest/polkit.8.html) (_polkitd_)  to make access control decisions for requests from unprivileged clients.
2. The ability to install custom polkit rules.


## Developer details

**{ref}`Auto-connect <explanation-interfaces-interface-auto-connection>`**: no</br>
**{ref}`Super-privileged <reference-operations-interfaces-super-privileged-interfaces>`**: yes</br>

**Attributes**:

 * **action-prefix** (plug):  indicate that all actions published by the snap are equal to the action prefix or match `${action-prefix}.*` .
  * **install-rules** (plug, requires *snapd 2.69*):  a list of polkit rule files (and their hash for integrity validation) to be installed on the system. Each entry must contain:
    * **name**: name of the polkit rule file to be installed.
    * **sha3-384**: RFC 4648 base 64 encoded sha3-384 hash of the specified rule file.

**Note: At least one of `action-prefix` or `install-rules` attributes must be set*.

## Polkit actions

To perform polkit authorisation checks, a daemon needs to do two things:

1. Install a .policy file to `$SNAP/meta/polkit/${plug_name}.*.policy` describing the actions it will use (codifying the type of administrative access a user might be granted). Snapd will install the policy file when the plug is connected.
3. Before performing administrative work on behalf of a client app, make a `CheckAuthorization` D-Bus call to polkitd to ask if they have access. The D-Bus call passes a string action ID describing the access, and a “subject” struct describing the client application.

There are two primary ways a daemon can describe the subject of the check:

1. For D-Bus daemons they can use a `system-bus-name` subject, sending the unique bus name of the client app.
2. For non-D-Bus daemons, they can use a `unix-process` subject, sending the process ID (as retrieved through `SO_PEERCRED` or `SCM_CREDENTIALS`).

See https://forum.snapcraft.io/t/proposal-add-polkit-and-polkit-agent-interfaces-to-snapd/23876 for the original interface proposal and reasoning.

## Polkit rules

To install polkit rules to the host system, a snap has to include a .rules file to `$SNAP/meta/polkit/${plug_name}.*.rules`. Snapd will install the rule file when the plug is connected given that there is a corresponding entry under `install-rules` with the same rule file name and the specified integrity `sha3-384` hash matches.

### Approval process for `install-rules`
For distribution via the [Snap store](https://snapcraft.io/store), snaps that use the polkit interface with the `install-rules` attribute need an approved {ref}`snap declaration <interfaces-process-for-aliases-auto-connections-and-tracks>`.

For acceptance, the publisher needs to:
* Explain the rationale for installing the polkit rule.
* Attach the polkit rule file content.
* Include the matching RFC 4648 base 64 encoded sha3-384 hash of the attached rule file content.

## Code examples

```yaml
plugs:
 polkit:
  action-prefix: org.example.foo
  install-rules:
      - name: polkit.bar.rules
        sha3-384: 2YM8oyXyE7xuXR07EXqUpixvr8duiJwgPQqhnxZgrBCU8ZSDowV0Gyujvs1j0-KR

apps:
 app:
  command: foo
  plugs: [polkit]
```

The test code can be found in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/polkit_test.go

The source code for the interface is in the snapd repository: https://github.com/canonical/snapd/blob/master/interfaces/builtin/polkit.go

