---
myst:
  html_meta:
    description: Release notes for Snapd 2.70, released on 8 July 2025. Read about selected updates, improvements and fixes in this release.
---

(release-notes_snapd-2-70)=
# Snapd 2.70

*Released on 8 July 2025*

## Highlights

* `snap-confine` no longer requires to be `setuid` root, now uses file capabilities and executes in the security context of the user who invokes it.
* snapd.apparmor is now enabled on Fedora, so that a Fedora container running on an apparmor-capable kernel works correctly.

## Notable updates

* Reset SHELL to /bin/bash in non-classic snaps ([LP: #2107443](https://bugs.launchpad.net/snapd/+bug/2107443))
* Only cancel notices requests on stop/shutdown ([LP: #2104066](https://bugs.launchpad.net/snapstore-server/+bug/2104066))
* Fix GLX on nvidia when xorg is confined by AppArmor ([LP: #2088456](https://bugs.launchpad.net/canonical-kernel-snaps/+bug/2102456))
* Fix snap-bootstrap busy loop ([LP: #2106121](https://bugs.launchpad.net/snapd/+bug/2106121))
* Update secboot and modify snap-bootstrap to remove usage of go templates to reduce size by 4MB ([LP: #2102456](https://bugs.launchpad.net/canonical-kernel-snaps/+bug/2102456))

## More about no-setuid snap confine

In an effort to increase the security and have better control over the execution of privileged binaries, the snap application bootstrapping helper, snap-confine, no longer requires to be setuid root. Instead it relies on file capabilities and executes in the security context of the user who invoked it. The required capabilities are effectively a subset of all the capabilities which were previously obtained immediately when executing the privileged binary. The effective capabilities are dynamically switched at runtime, such that the helper executes with the least set of effective privileges at any given time.

Please note that 2.70 includes all the changes in the superseded 2.69 and 2.69.1 releases.

## Changelog

* FDE: Fix reseal with v1 hook key format
* FDE: set role in TPM keys
* AppArmor prompting (experimental): add handling for expired requests or listener in the kernel
* AppArmor prompting: log the notification protocol version negotiated with the kernel
* AppArmor prompting: implement notification protocol v5 (manually disabled for now)
* AppArmor prompting: register listener ID with the kernel and resend notifications after snapd restart (requires protocol v5+)
* AppArmor prompting: select interface from metadata tags and set request interface accordingly (requires protocol v5+)
* AppArmor prompting: include request PID in prompt
* AppArmor prompting: move the max prompt ID file to a subdirectory of the snap run directory
* AppArmor prompting: avoid race between closing/reading socket fd
* Confdb (experimental): make save/load hooks mandatory if affecting ephemeral
* Confdb: clear tx state on failed load
* Confdb: modify 'snap sign' formats JSON in assertion bodies (e.g. confdb-schema)
* Confdb: add NestedEphemeral to confdb schemas
* Confdb: add early concurrency checks
* Simplify building Arch package
* Enable snapd.apparmor on Fedora
* Build snapd snap with libselinux
* Emit snapd.apparmor warning only when using apparmor backend
* When running snap, on system key mismatch e.g. due to network attached HOME, trigger and wait for a security profiles regeneration
* Avoid requiring state lock to get user, warnings, or pending restarts when handling API requests
* Start/stop ssh.socket for core24+ when enabling/disabling the ssh service
* Allow providing a different base when overriding snap
* Modify snap-bootstrap to mount snapd snap directly to /snap
* Modify snap-bootstrap to mount /lib/{modules,firmware} from snap as fallback
* Modify core-initrd to use systemctl reboot instead of /sbin/reboot
* Copy the initramfs 'manifest-initramfs.yaml' to initramfs file creation directory so it can be copied to the kernel snap
* Build the early initrd from installed ucode packages
* Create drivers tree when remodeling from UC20/22 to UC24
* Load gpio-aggregator module before the helper-service needs it
* Run 'systemctl start' for mount units to ensure they are run also when unchanged
* Update godbus version to 'v5 v5.1.0'
* Add support for POST to /v2/system-info with system-key-mismatch indication from the client
* Add 'snap sign --update-timestamp' flag to update timestamp before signing
* Add vfs support for snap-update-ns to use to simulate and evaluate mount sequences
* Add refresh app awareness debug logging
* Add snap-bootstrap scan-disk subcommand to be called from udev
* Add feature to inject proxy store assertions in build image
* Add OP-TEE bindings, enable by default in ARM and ARM64 builds
* Fix systemd dependency options target to go under 'unit' section
* Fix snap-bootstrap reading kernel snap instead of base resulting in bad modeenv
* Fix a regression during seeding when using early-config
* LP: #2107443 reset SHELL to /bin/bash in non-classic snaps
* Make Azure kernels reboot upon panic
* Fix snap-confine to not drop capabilities if the original user is already root
* Fix data race when stopping services
* Fix task dependency issue by temporarily disable re-refresh on prerequisite updates
* Fix compiling against op-tee on armhf
* Fix dbx update when not using FDE
* Fix potential validation set deadlock due to bases waiting on snaps
* LP: #2104066 Only cancel notices requests on stop/shutdown
* Interfaces: bool-file | fix gpio glob pattern as required for '[XXXX]*' format
* Interfaces: system-packages-doc | allow access to /usr/local/share/doc
* Interfaces: ros-snapd-support interface | added new interface
* Interfaces: udisks2 | allow chown capability
* Interfaces: system-observe | allow reading cpu.max
* Interfaces: serial-port | add ttyMAXX to allowed list
* Interfaces: modified seccomp template to disallow 'O_NOTIFICATION_PIPE'
* Interfaces: fwupd | add support for modem-manager plugin
* Interfaces: gpio-chardev | make unsupported and remove experimental flag to hide this feature until gpio-aggregator is available
* Interfaces: hardware-random | fix udev match rule
* Interfaces: timeserver-control | extend to allow timedatectl timesync commands
* Interfaces: add symlinks backend
