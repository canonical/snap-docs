(explanation-security-api-authentication-and-authorization)=
# API Authentication and Authorization

Snapd performs authentication and authorization checks before executing operations that may affect system state or modify snap security policies. These checks are applied to interactions with the snapd REST API, which is the primary interface used by the snap command-line tool and other clients. Authentication establishes the identity of the caller, while authorization determines whether that identity is permitted to perform a given operation. Many snap management operations - such as installing snaps, connecting interfaces, or refreshing packages - may alter the system’s security posture. Snapd therefore ensures that only authenticated and authorized callers can perform such operations.

## User identities in snapd

Snapd distinguishes between three related types of users.

### Snapd user

A snapd user is a local identity maintained by snapd. It represents an authenticated user within snapd and is used when authorizing API requests.

Each snapd user is uniquely identified by:

- a snapd user ID
- a snapd macaroon

Multiple snapd users may refer to the same store identity.

### Store user

A store user is an identity managed by the Snap Store and authenticated through login.ubuntu.com. Store users are uniquely identified by their email address. When a user logs in using snap login, the store identity is associated with a local snapd user. The Snap Store provides authentication tokens (macaroons and discharges) that allow snapd to interact with the store on behalf of that user.

### Linux system user

A Linux system user is a standard user account on the host operating system. System users are uniquely identified by their system username or user ID (UID). Snapd may associate a Linux system user with a snapd user so that API requests originating from that account can be authenticated and authorized. In managed environments such as Ubuntu Core systems, Linux system users may be created from system-user assertions signed by the device brand, or from user information retrieved from the Snap Store for a given store user email address.

On system user removal, the Linux system user is removed as well as the associated snapd user. The identity file ($HOME/.snap/auth.json) is removed indirectly when the system user is removed.

## Authentication

Snapd authenticates users using peer credential passing, snapd local macaroons, and Polkit authentication requests. Snaps are authenticated using PID-based cgroup lookup to determine which snap a requesting process belongs to.

### Summary of identities and layered authentication mechanisms

| Identity                    | Mechanism                   | Description                                                |
|-----------------------------|-----------------------------|------------------------------------------------------------|
| Snapd user                  | Local macaroons             | Authenticates the snapd user                               |
| System user                 | `SO_PEERCRED`, `SOL_SOCKET` | Authenticates calling system process, user and socket      |
| System admin                | Polkit                      | Authenticates system user as administrator                 |
| Calling snap                | PID → cgroup lookup         | Authenticates the snap that the calling process belongs to |

#### Snapd local macaroon

When a user logs in to the Snap Store using `snap login`, snapd creates or updates the associated snapd user and stores authentication information locally.
The authenticated identity is persisted in:

```console
$HOME/.snap/auth.json
```

This file contains the snapd user identity and local authentication tokens (local macaroons). The `snap` command-line tool reads this file and includes the relevant credentials in the request headers when making snapd API calls. These credentials allow snapd to authenticate snapd API calls on behalf of the logged-in user. When a user logs out using `snap logout`, the local authentication data and associated snapd user identity are removed.

#### Unix domain socket peer credential passing

UNIX domain socket peer credentials (`SO_PEERCRED`) allows a server to securely obtain  the Process ID (PID), User ID (UID), and socket to which the peer connection was established, directly from the kernel.

#### PID-based cgroup snap lookup

Snapd authenticates snaps by performing a cgroup lookup using the process PID obtained from peer credentials to determine which snap the requesting process belongs to. This identifies the calling snap, whose connected interfaces are then used for authorization decisions. The cgroup is assigned during process bootstrap, and the sandbox prevents the snap process from moving itself to a different cgroup, which helps protect this mechanism against spoofing.

#### Polkit authenticaton requests

Certain snapd API operations are authorized via Polkit. For these operations, snapd queries Polkit to determine whether the caller is permitted to perform the requested action. Polkit is an authorization framework that may require user or administrator authentication before authorization is granted.

Polkit actions with suitable messages for different scenarios are defined in:

```console
/usr/share/polkit-1/actions/io.snapcraft.snapd.policy
```

## Authorization

After authenticating the calling snap, system user, socket and snapd user, snapd determines whether the caller is authorized to perform the requested operation with access level specified by the API endpoint policy.
For details about API endpoint policy refer to the [snapd API documentation].

[snapd API documentation]: https://snapcraft.io/docs/reference/development/snapd-rest-api/

### Base access levels

#### Open

Allows requests without authentication, provided they have peer credentials and were not received on `snapd-snap.socket`.

#### Authenticated

Allows requests from authenticated users, provided they were not received on `snapd-snap.socket`.

#### Root

Allows requests from the root UID (0), provided they were not received on `snapd-snap.socket`

### Other variations

#### Snap

Allows requests from the `snapd-snap.socket` only.

#### Interface \<base access level\>

Additive to the corresponding base access level. Allows requests from `snapd-snap.socket` for snaps that plug one of the required interfaces, or carry a required slot.

#### Interface provider root

Additive to the root access level. Allows requests over `snapd-snap.socket` for snaps that have a connection of specific interface and are present on the slot side of that connection.

## Interaction with snap security policies

Snap confinement is enforced through security policies generated by snapd using mechanisms such as:

- AppArmor
- seccomp
- cgroups
- Linux namespaces

These policies define the level of isolation and permitted access for each snap and are typically derived from the interfaces declared and connected for that snap. Authorized operations performed through the snapd API - such as installing snaps or connecting interfaces - may cause snapd to generate or update these policies. Once generated, the policies are enforced by the Linux kernel. For more information, refer to the {ref}`security policies <explanation-security-security-policies>`.
