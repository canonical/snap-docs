(reference-operations-exit-codes)=
# Exit codes
The `snap` command uses the following exit codes. These are useful when scripting `snap` operations or
diagnosing failures.

| Code | Meaning | Description |
|:---|:---|:---|
| 0   | Success | The command completed without error. |
| 1   | General error | The command failed for a reason not covered by a more specific exit code. |
| 10  | Retriable error | Another snap operation is in progress resulting in a `snap-change-conflict`. Wait for it to finish and try again. |
| 20  | Build error | `mksquashfs` failed when building a snap (e.g. during `snap pack`). |
| 46  | Internal error | The snap app binary dispatch failed. Either the `/snap/bin/` symlink could not be resolved, or the snap app could not be run. |
| 64  | Usage error | Invalid flags, arguments, or an unknown command was provided. |
