---
myst:
  html_meta:
    description: Complete reference for requesting and reviewing snap aliases, interface auto-connections, and tracks through the Snap Store process.
---

(interfaces-process-for-aliases-auto-connections-and-tracks)=
# Store-reviews: process and criteria

Store-reviews is how [@reviewers](https://forum.snapcraft.io/groups/reviewers) have traditionally referred to store request reviews, more specifically, reviews of privileged interface and classic confinement requests. This document defines the process and the criteria used to review these requests.

## Process

The snap publisher will first evaluate the requirements for their snap to be functional according to the principle of [least privilege](https://community.owasp.org/controls/Least_Privilege_Principle). Then, the snap publisher will evaluate whether the snap is eligible to be granted the  necessary permissions according to the criteria below. If so, the publisher will create the request for privileged interfaces or classic confinement in the corresponding store-requests subcategory using the appropriate template to provide all the required information for the request to be evaluated.

* Privileged interfaces: [subcategory](https://forum.snapcraft.io/c/store-requests/privileged-interfaces/27) | [template](https://forum.snapcraft.io/t/about-the-privileged-interfaces-category/43831)
* Classic confinement: [subcategory](https://forum.snapcraft.io/c/store-requests/classic-confinement/26) | [template](https://forum.snapcraft.io/t/about-the-classic-confinement-category/43830)

Failing to create the request under the corresponding subcategory or using the appropriate template will result in the request not being reviewed.

A reviewer evaluates the request according to the criteria below. If the request is approved, the reviewer will take appropriate action and inform the snap publisher once the requested permissions are granted.


## Criteria

Snaps are meant to be the most secure way to distribute Linux applications. To protect our users from malicious and/or vulnerable snaps, **strict confinement is always the default option**. However, additional permissions granted by the interfaces are sometimes required for applications to function properly. Therefore, to enable all publishers to distribute their applications though the snap store, we are willing to grant manual connection and let users decide whether they are willing to accept the associated risks, as long as:

* There are valid **technical reasons** why a given functionality cannot be achieved without the requested interface.
* The interface name makes it clear the permissions it grants

The snap can make use of `snapctl is-connected <iface>` to check whether a given interface is connected during the application startup or at runtime and show the user appropriate instructions to decide if they want to connect the interface and how to do it.

Granting **interfaces auto-connection and/or classic confinement** in the global, public store effectively means that the store is vouching for the publisher’s intent (maintenance, security updates, etc.) and snap implementation (it does what it advertises, works well, etc.). In order to consider any request for interface auto-connection or classic confinement, all the criteria below must be met in addition to technical reasons.

### Technical reasons (least privilege)

Granting additional privileges increases the attack surface that an attacker, via a malicious or a vulnerable snap, can abuse to accomplish their purposes. Thus, in order to grant any privilege additional to what is allowed by the default sandbox, technical reasons must exist and they must be properly justified in the request for every interface or for classic confinement.


If the provided justification does not make it clear to the reviewer why some of the requested permissions are needed, the reviewer will ask the snap publisher for evidence, such as application logs, AppArmor denials, and similar information.

#### Classic confinement

Classic confinement is a mechanism designed to circumvent some temporary limitations related to strict confinement rather than a shortcut to make the snap implementation faster or easier. That’s why classic confinement is not supported on Ubuntu Core and Ubuntu Core Desktop and strict confinement should always be the way to go.

To help reviewers make informed decisions and ensure that publishers understand and adhere to this rule, requests for classic confinement must always include evidence demonstrating why the application cannot work under strict confinement using the existing interfaces. Failing to provide application logs, AppArmor denials, and similar information that backs the need for classic confinement may result in the request not being reviewed.

### Publisher vetting

#### Organizations

In general, organizations are expected to be mindful of the snaps they publish in the Snap Store to protect their own business interests and reputation. Organizations are vetted using the [Verified accounts](https://forum.snapcraft.io/t/verified-accounts/34002) process. 

#### Well-known projects

The project’s reputation supports its upstream members publishing it to the Snap Store. In this case, the snap publisher’s connection with the upstream project will be verified using the existing [Process for performing Snap Publisher Vetting](https://forum.snapcraft.io/t/process-for-performing-snap-publisher-vetting/43531).

This is **reserved for truly long-standing Linux projects** with big communities around and a large number of maintainers and contributors. However, exceptions may, or may not, be considered case by case, when the application maturity is appropriate for the requested level of privilege. Project history, user base and community will be considered alongside the concrete permissions being requested. The very **minimum requirements for requesting an exception** are:

* Track record of active development and maintenance for at least one year.
* There is evidence that the application and/or the snap has a regular user base
* For higher levels of privilege (explicit list of interfaces to be determined), the upstream project and the snap have at least two active maintainers.

Requests for classic confinement are not subject to these exceptions.

#### Trusted groups

There are some groups that have been considered trusted in the ecosystem for a long time. These groups include:

* Snapcrafters, publishing to the snapcrafters account
* [Ubuntu core-dev](https://launchpad.net/~ubuntu-core-dev)

We want to add other groups that already have a high level of trustworthiness in the ecosystem to this list. These groups will likely include other Ubuntu developers and Debian maintainers. However, we still need to define a consistent and reliable way to prove this group membership and establish all the possible rules around it.

### Snap implementation

Snaps in the global store are expected to meet the highest quality standards, be updated at the same cadence as the upstream project and stay free of vulnerabilities over time. Failing to meet these standards may result in requests being denied. In the same way, missing this maintenance commitment will result in auto-connections being removed initially and potentially snaps being removed from all stable channels if the situation is not addressed in a reasonable period of time.

In order to guarantee that snaps in the global store stay healthy over time, we encourage publishers to automate the snap maintenance as much as possible. Whilst this won’t be enforced in the short term, we believe that the right direction going forward will likely be asking snap publishers to add automated processes to:

* Fix security issues in the application code or in their dependencies.
* Keep the snap up to date with the latest upstream releases
* Proactively identify if a given revision will break any snap functionality before the revision is promoted to a stable channel.

#### Classic confinement

Snap applications running under classic confinement run in the global mount namespace (i.e., the host’s filesystem) as opposed to what is specified by `base` in the snap’s YAML. For this reason, great care must be taken for the snap to work reliably across all distributions since, for example, as part of the build process snapcraft will adjust the snap’s binaries through binary patching and/or setting environment variables to look into the $SNAP directory for paths, either of which could affect the snap’s reliability when running on arbitrary cross-distribution host filesystems.

### User voice

This is especially important for requests for auto-connection, as they override the user's initial choice on connection at install time. The following factors are expected to be considered:

* Is the interface required for a core functionality or for an optional one?
* How sensitive are the permissions granted by the interface?
* Would the average user expect the auto-connection according to the snap name, description and functionality?

Depending on the answers to these questions, reviewers may decide not to grant a given auto-connection even if all the other criteria are fulfilled.

If needed, the reviewer may ask other reviewers, architects and long-standing members of the community for their input. The reviewer will evaluate and balance all the different arguments to make a decision. This is more likely to be required when the publisher vetting is done via the well-known projects exception route.

### Exceptions

There are some known exceptions to these general guidelines that require special consideration.

#### Never granted

The following permissions pose a risk for the users and/or for the ecosystem and won’t ever be granted even if all the requirements are met.

* Auto-connection to password-manager-service (use secret portal instead)
* Manual connection to personal-files that allow confinement escape
  * ~/.local/share/applications
  * ~/.local/share/mime
  * *-support interfaces

#### May be granted

The following permissions may be granted even if all the criteria above is not fulfilled.
* Personal-files where the application is the clear owner of the requested files and the snap is published by the upstream
  * ~/.<snap-name>
  * ~/.config/<snap-name>

