(explanation-security-classic-confinement)=
# Classic confinement

Classic confinement is the most permissive level of [snap confinement](/explanation/security/snap-confinement), equivalent to the full system access that traditional, unsandboxed packages have.

It's often used as a stop-gap measure to enable developers to publish apps that need more access than snapd interfaces and permissions allow.

This page provides explanations and examples of what happens during installation and at runtime with snaps packaged using classic confinement.


## Rationale

One of the main drives behind the invention of snaps was to guarantee safe execution of software and mandate that packages abide by the principle of least privilege. The snap package format places the software in a sandbox, and snapd mediates all access to host system resources. By default, a snap is strictly confined, where it only has host access that's explicitly granted through the interface system.

Apps can be packaged as classic snaps for a variety of reasons. Primarily, this level of confinement is provided for apps that need access to arbitrary binaries on the host, which isn't possible when using strict confinement.

Apps packaged as classic snaps behave similar to software provided and installed through the host's package manager, like Aptitude (`apt`) or Red Hat Package Manager (`rpm`).


## Security

From a security standpoint, classic snaps are inherently riskier than standard snaps, as they lack the protections and guardrails offered by sandboxing. A malicious author could easily compromise a system by incorporating a compromising payload into a classic snap. And as Canonical finds is frequently the case, not all requests for classic confinement are necessary. Some authors misunderstand the snap build process, interfaces, or filesystem, and with some tweaking their snap is made to work without classic confinement.

Canonical must therefore audit and vet all classic snaps prior to distribution on any store. Without approval from the Store team, a classic snap can't be distributed. The review process that determines the eligibility and appropriateness as a classic snap is outlined in [Submit your snap for review](/).

Canonical only manages risk for its own infrastructure and channels. If a user obtains a classic snap through unofficial channels and they understand the risks, they can manually install it.


## Install-time process

When a classic snap is installed, _snapd_ will perform the following actions:

![Snap confinement at install time](https://assets.ubuntu.com/v1/35306066-confinement_02.png)

1. Mount the snap as a loopback device.

2. Skip the creation of the snap-specific private mount namespace.

3. Skip the configuration of the device cgroups.

4. Create a permissive AppArmor profile (which will be loaded in complain mode at runtime). The profile is stored under `/var/lib/snapd/apparmor/profiles`.

5. Create a permissive Seccomp profile (which will be parsed at runtime). The profile is stored under `/var/lib/snapd/seccomp/bpf` and will contain a `@unrestricted\n` entry.

## Runtime process

When a classic snap is executed on the host system, snapd will perform the following actions:

![Snap confinement at run time](https://assets.ubuntu.com/v1/d4018ec4-confinement_01.png)

1. snapd runs a sub-process called `snap-confine`, which is responsible for creating the necessary confinement for the snap (with the rules set during the installation process).

2. The [AppArmor](https://ubuntu.com/server/docs/security-apparmor) profile will be loaded in complain mode.

    This can be ascertained by running `apparmor_status` and find the relevant profiles listed in the complain section of the output, for examples `snap.XXX.hook.configure` and `snap.XXX.snapcraft`.

3. For classic snaps, the permissive Seccomp profile will be parsed. This can be ascertained by running `grep Seccomp /proc/PID/status`, with the value of `0` indicating the process does not currently use any Seccomp filtering.

4. Load the dynamic library dependencies in the following order – staged packages, `/snap/<base>` (with the relevant base specified in snap.yaml derived from the developer edited snapcraft.yaml), and then the libraries in the host environment.

    If not found, search through the host system using the system's `/etc/ld.so.cache`. Classic snaps should not have a `$LD_LIBRARY_PATH` configured as part of their runtime environment.

Feature | Strict | Classic
-|-|-
Mount namespace | private | none
cgroups | Yes | No
AppArmor | Enforce mode | Complain mode
Seccomp | Strict filtering | No filtering
`LD_LIBRARY_PATH` | Depends | Empty
Library loading | Staged packages</br>Base | Staged packages</br>Base</br>Host system

