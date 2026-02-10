(how-to-guides-manage-snaps-disk-space-awareness)=
# Disk space awareness

The snap daemon, _snapd_, can check whether there is enough free disk space before performing the following space-requiring operations:

- **snap installation**: checks storage required to download a snap
- **snap refresh and update**: checks storage required to download updates and to store previous snap revisions
- **snap removal**: checks storage required to create the [automatic snapshot](/how-to-guides/manage-snaps/create-data-snapshots.md#automatic-snapshots) generated when the last revision of a snap is removed (unless disabled)

```{caution}
Disk space awareness is currently an experimental feature.
```

When enabled, snapd checks whether there is enough space in `/var/lib/snapd` to complete an operation, such as enough space to store a requested snap to download. If there isn't enough space, an error is returned and the operation is not performed:

```bash
$ snap install foo
error: cannot install "foo" due to low disk space
```

The error output can also include a hint on how a space requirement could be mitigated, such as suggesting the `--purge` flag with `snap remove` to disable the automatic snapshot generation:

```bash
$ snap remove foo
error: cannot remove "foo" due to low disk space, use --purge to avoid creating a snapshot
```

The [REST API](/how-to-guides/snap-development/use-the-rest-api) will also return an `insufficient-disk-space` [error response](/reference/development/error-responses) object when disk space awareness is enabled and an error is encountered.

## Enable disk space awareness

To enable disk space awareness, set one or more of the following _experimental_ feature flags to _true_:

- `experimental.check-disk-space-install`
- `experimental.check-disk-space-refresh`
- `experimental.check-disk-space-remove`

To enable the pre-install check, for example, use the following command:
```bash
snap set system experimental.check-disk-space-install=true
```

See [System options](/how-to-guides/manage-snaps/set-system-options) for more details on setting and disabling options.

