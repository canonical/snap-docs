(explanation-security-decommissioning)=
# Decommissioning

Snapd runs on three system types:

 - [Ubuntu Core]
 - Hybrid Classic
 - Classic

The approach to decommissioning snapd differs depending on the system type, as snapd provides core system functionality on Ubuntu Core and Hybrid Classic systems, but is an optional package on Classic Ubuntu systems.

[Ubuntu Core]: https://documentation.ubuntu.com/core/

## Ubuntu Core systems

On Ubuntu Core systems, snapd is a fundamental component of the operating system and part of the overall device image and product lifecycle. Ubuntu Core devices are typically deployed as integrated IoT or appliance-style systems with a fixed software lifetime.

Decommissioning of Ubuntu Core systems should be performed at the system level rather than by removing snapd, and is therefore outside the scope of this section.

## Hybrid Classic systems

Hybrid Classic system is a classic system with kernel snap e.g. Ubuntu 26.04 using the TPM backed FDE installation option. It provides a Classic Ubuntu user experience but rely on snapd for essential system functionality such as system snaps, recovery, and full disk encryption. On these systems, snapd is not an optional component and should not be removed.

Decommissioning of Hybrid Classic systems should be performed at the system level rather than by removing snapd, and is therefore outside the scope of this section.

## Classic systems

On Classic Ubuntu systems, snapd is an optional component and may be decommissioned if it is no longer required. Snapd is bootstrapped by the snapd deb package, but installation of any non-essential snap (core, gadget, kernel, snapd) would also trigger installation of snapd snap. On Classic Ubuntu systems, re-execution is enabled by default, which means the deb package will re-execute to snapd provided by the snap package whenever that version is more recent than the deb package version.

Decommissioning snapd on Classic systems involves:

 - Removing installed snaps
 - Removing the snapd package
 - Removing remaining snap data, state directories, and stored snapshots (including user, system, and configuration data)

Typical locations where snap data may remain include:

- `/var/snap/`:         Snap system data and persistent application data
- `/var/lib/snapd/`:    Snapd state, installed snap revisions, assertions, snapshots
- `/var/cache/snapd/`:  Downloaded snap packages and cache
- `/snap/`:             Mounted snap squashfs files (read-only runtime files)
- `/home/$USER/snap/`:  Per-user snap data, configuration, and user files
- `/home/$USER/.snap/`: Authentication data and signing keys
- `/var/log/journal/`:  Persistent logging (configurable)
- `/run/log/journal/`:  Non-persistent logging (default)

### Removing installed snaps

Removal of the snapd snap requires first removing all other snaps. Removing installed snaps with `snap remove --purge <snap>` prevents taking an automatic snapshot, however existing [snapshots] still remain.

[snapshots]: https://snapcraft.io/docs/how-to-guides/manage-snaps/create-data-snapshots/

### Removing the snapd snap

When all other snaps have been removed the snapd snap can also be removed. Removal of the snapd snap does not remove /var/lib/ in order to allow the snapd deb package
to function.

### Removing the snapd deb package

Removal of the snapd deb package with `sudo apt remove --purge snapd` removes:
- `/var/snap`
- `/var/lib/snapd/`
- `/var/cache/snapd/`
- `/snap/`

### User data

If required, root and other user data should be manually removed by wiping `/root/snap/` and `/root/.snap/` as well as `/home/$USER/snap/` and `/home/$USER/.snap/`.

### Removing journal logs

If deemed necessary, journal containing snapd logs can be removed, but this cannot be done cleanly without impacting non-snapd logging. Identify if the journal contains any snapd files using `journalctl --directory=/var/log/journal -u snapd` and remove the log if required.
