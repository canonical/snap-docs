---
myst:
  html_meta:
    description: Use the snapd REST API to integrate TPM-FDE into a custom Ubuntu installer, including pre-install checks and fixes, PIN or passphrase setup, and preseeding.
---

(how-to-guides-installer-with-tpm-fde)=
# Integrate TPM-FDE into a custom Ubuntu installer using the snapd REST API

This guide shows you how to integrate [hardware-backed Full Disk Encryption](https://ubuntu.com/desktop/docs/en/latest/explanation/hardware-backed-disk-encryption/#hardware-backed-disk-encryption) (TPM-FDE) into a custom Ubuntu installer using the snapd REST API.

Refer to the {ref}`snapd REST API reference<reference-development-snapd-rest-api>` for a list of all API actions and endpoints. For general instructions, refer to the {ref}`guide on how to use the REST API<how-to-guides-manage-snaps-use-the-rest-api>`.

Follow the steps in order. Some steps are optional.

## Prerequisites

To follow this guide, your installer must have access to a recovery system seed available to snapd. A recovery system seed is the set of files that describes the Ubuntu system to be installed. It includes:
- a [model assertion](https://documentation.ubuntu.com/core/reference/assertions/model/) describing the Ubuntu system to install; and
- the essential snaps making up that system, including the [base](https://documentation.ubuntu.com/snapcraft/stable/reference/base), {ref}`kernel<reference-development-yaml-schemas-the-kernel-snap>`, {ref}`gadget<reference-development-yaml-schemas-the-gadget-snap>`, and {ref}`snapd<ref-glossary_snapd>` snaps.

To get Canonical's reference model for the Ubuntu release used in this guide, run:
```sh
snap known model --remote series=16 brand-id=canonical model=ubuntu-classic-2604-amd64
```

For more information, see:
- [Create a model](https://documentation.ubuntu.com/core/tutorials/build-your-first-image/create-a-model/)
- [Create a recovery system from the API](https://documentation.ubuntu.com/core/how-to-guides/manage-ubuntu-core/create-a-recovery-system-from-the-api/)

To learn about the layout of a recovery system seed, see also [Ubuntu Core storage layout](https://documentation.ubuntu.com/core/explanation/core-elements/storage-layout/).

## Get system label

Each recovery system is identified by a unique label, corresponding to its directory in the installer seed. Normally, this directory is `/var/lib/snapd/seed/systems/<label>/`. 

To get the system label, make a `GET` request to `/v2/systems`. Snapd will return a synchronous response (`200 OK`) with a list of all the available systems, including their labels. For example:


```{code-block} json
:caption: Response body, `result`

{
  ...
  "systems": [
    {
      "current": true,
      "default-recovery-system": true,
      "label": "20261001",
      "model": {
        "model": "my-device",
        "brand-id": "example-brand",
        "display-name": "My Device"
      },
      ...
    }
  ],
  ...
}
```

Select the appropriate label to [perform the pre-install checks](#perform-pre-install-checks).

## Perform pre-install checks

To perform the pre-install checks, use the system label to make a `GET` request to `/v2/systems/{label}`. Snapd will return a synchronous response (`200 OK`) with the system details. The `storage-encryption` object describes the target system's storage encryption capabilities. It will state whether encryption is available. If it is not available, it will list the errors and the actions that can fix them.

### Encryption is available

If encryption is available, `storage-encryption` will include the target system's features and requirements, and no errors. For example:

```{code-block} json
:caption: Response body, `result`
{
  ...
  "storage-encryption": {
    "support": "available",
    "features": ["passphrase-auth", "pin-auth"],
    "storage-safety": "prefer-encrypted",
    "encryption-type": "cryptsetup",
    "requirements": ["volumes-auth"]
  },
  ...
}
```

Since there are no errors, the installation can proceed. The features and requirements of the target system will be relevant when you set up the its storage encryption. Skip ahead to the [Set up storage encryption section](#set-up-storage-encryption).

### Encryption is unavailable due to recoverable errors

If encryption is unavailable due to recoverable errors, `storage-encryption` will include `unavailable-reason` and `availability-check-errors`. For example:

```{code-block} json
:caption: Response body, `result`
{
  ...
  "storage-encryption": {
    "support": "unavailable",
    "features": ["passphrase-auth", "pin-auth"],
    "storage-safety": "prefer-encrypted",
    "unavailable-reason": "not encrypting device storage as checking TPM gave: error with TPM2 device: TPM2 device is present but is currently disabled by the platform firmware",
    "availability-check-errors": [
      {
        "kind": "tpm-device-disabled",
        "message": "error with TPM2 device: TPM2 device is present but is currently disabled by the platform firmware",
        "actions": [
          "enable-tpm-via-firmware",
          "enable-and-clear-tpm-via-firmware",
          "reboot-to-fw-settings"
        ]
      }
    ],
    "requirements": ["volumes-auth"]
  },
  ...
}
```

In this example, the target system has a TPM 2.0 device that is disabled in the firmware. This error can be resolved by executing the fix actions listed in the `actions` array, in the order in which they are presented. See the [Perform pre-install fix actions section](#perform-pre-install-fix-actions) for guidelines and further details.

The initial `GET` request to `/v2/systems/{label}` runs pre-install checks and creates an in-memory context that will be used while fixing the errors. Another `GET` request to the same endpoint replaces that context, resetting the sequence of fix actions. The context is also lost if snapd restarts or the system reboots.

The table below lists error kinds that snapd might return, with a suggested message to show the user, and example fix actions. The list is not exhaustive: snapd can return error kinds and fix actions that the table does not include. Treat it as a starting point, rather than a specification.

```{dropdown} Recoverable error kinds
| Error kind                                    | Suggested message to present to the user                                                                                                       | Example fix action(s)                                                                   |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `efi-variable-access`                         | Error occurred when accessing an EFI variable.                                                                                                 | `contact-oem`                                                                           |
| `tpm-device-failure`                          | The TPM device has failed an internal self check.                                                                                              | `reboot`, `contact-oem`                                                                 |
| `tpm-device-disabled`                         | There is a TPM device that is currently disabled.                                                                                              | `reboot-to-fw-settings`, `enable-tpm-via-firmware`, `enable-and-clear-tpm-via-firmware` |
| `tpm-hierarchies-owned`                       | One or more TPM hierarchy is currently owned, either because it has an authorization value or policy set.                                      | `reboot-to-fw-settings`, `clear-tpm-via-firmware`, `enable-and-clear-tpm-via-firmware`  |
| `tpm-device-lockout-locked-out`               | The TPM's lockout hierarchy is currently unavailable because it is locked out.                                                                 | `reboot-to-fw-settings`, `clear-tpm-via-firmware`, `enable-and-clear-tpm-via-firmware`  |
| `insufficient-tpm-storage`                    | Insufficient storage space available to support FDE along with reprovisioning in the future.                                                   | `reboot-to-fw-settings`, `clear-tpm-via-firmware`, `enable-and-clear-tpm-via-firmware`  |
| `no-suitable-pcr-bank`                        | It is not possible to select a suitable PCR bank. This could be because some mandatory PCR values are inconsistent with the TCG log.           | `reboot-to-fw-settings`, `contact-oem`                                                  |
| `running-in-vm`                               | The current environment is a virtual machine.                                                                                                  | `proceed`                                                                               |
| `insufficient-dma-protection`                 | I/O DMA remapping was disabled during the current boot cycle.                                                                                  | `reboot-to-fw-settings`, `contact-oem`, `proceed`                                       |
| `no-kernel-iommu`                             | The OS kernel was not built with DMA remapping support, or some configuration has resulted in it being disabled.                               | `reboot-to-fw-settings`, `contact-os-vendor`, `proceed`                                 |
| `host-security`                               | Problem with the system security that is not represented by a more specific error kind.                                                        | `contact-oem`                                                                           |
| `tpm-pcr-unusable`                            | An error in the way that the platform firmware performs measurements such that the PCR becomes unusable.                                       | `contact-oem`                                                                           |
| `addon-drivers-present`                       | Drivers running from value-added-retailer components were detected.                                                                            | `proceed`                                                                               |
| `sys-prep-applications-present`               | System preparation applications were detected to be running before the operating system.                                                       | `proceed`                                                                               |
| `absolute-present`                            | Absolute was detected to be executing before the initial OS loader.                                                                            | `reboot-to-fw-settings`, `contact-oem`, `proceed`                                       |
| `invalid-secure-boot-mode`                    | The secure boot mode is invalid.                                                                                                               | `reboot-to-fw-settings`                                                                 |
| `weak-secure-boot-algorithms-detected`        | Either pre-OS components were authenticated with weak Authenticode digests, or CAs with weak public keys were used to authenticate components. | `proceed`                                                                               |
| `pre-os-secure-boot-auth-by-enrolled-digests` | Pre-OS components were authenticated by matching their Authenticode digest to an entry in `db`.                                                | `proceed`                                                                               |
| `no-hardware-root-of-trust`                   | The platform's UEFI firmware is not verified nor measured by a hardware root of trust.                                                         | `proceed`                                                                               |
```

### Encryption is unavailable due to non-recoverable errors

If `storage-encryption` includes `unavailable-reason` but not `availability-check-errors` or if `availability-check-errors` is empty,
the target system does not support encryption as defined in the recovery system seed. For example:

```{code-block} json
:caption: Response body, `result`
{
  ...
  "storage-encryption": {
    "support": "unavailable",
    "storage-safety": "prefer-encrypted",
    "unavailable-reason": "cannot use encryption with the gadget, disabling encryption: gadget does not support encrypted data: required partition with system-save role is missing",
  },
  ...
}
```

In this example, encryption is not possible because the gadget lacks a system-save partition. This is a fatal error that cannot be resolved by snapd. No further steps are applicable until the gadget is replaced.

If `storage-encryption` includes `availability-check-errors`, but none of the errors includes fix actions, the target system also does not support encryption as defined in the recovery system seed. For example:

```{code-block} json
:caption: Response body, `result`
{
  ...
  "storage-encryption": {
    "support": "unavailable",
    "storage-safety": "prefer-encrypted",
    "unavailable-reason": "no suitable TPM2 device is available",
    "availability-check-errors": [
      {
        "kind": "no-suitable-tpm2-device",
        "message": "no suitable TPM2 device is available"
      }
    ]
  }
  ...
}
```

In this example, the target system's machine does not have a TPM 2.0 device suitable for TPM-FDE. This is a fatal error that cannot be resolved by snapd. No further steps are applicable until the hardware is replaced.

The table below lists error kinds that snapd might return, with a suggested message to show the user. The list is not exhaustive: snapd can return error kinds that the table does not include. Treat it as a starting point, rather than a specification.

```{dropdown} Non-recoverable error kinds
| Error kind                | Suggested message to present to the user                                                                                    |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `internal-error`          | Unexpected internal error occurred.                                                                                         |
| `system-not-efi`          | The current host system is not an EFI system.                                                                               |
| `no-suitable-tpm2-device` | The device has no suitable TPM2 device.                                                                                     |
| `measured-boot`           | Error with the TCG log or some other error detected from the TCG log that is not represented by a more specific error kind. |
| `tpm-command-failed`      | An error occurred whilst executing a TPM command.                                                                           |
| `invalid-tpm-response`    | The response from the TPM is invalid, which makes it impossible to obtain a response code.                                  |
| `tpm-communication`       | An error occurred at the transport layer when executing a TPM command.                                                      |
| `unsupported-platform`    | The current host platform is not compatible with FDE.                                                                       |
```

## Perform pre-install fix actions

```{note}
Pre-install fix actions can only be performed after an initial pre-install check. See the [Perform pre-install checks section](#perform-pre-install-checks) for details.
```

If [encryption is unavailable due to recoverable errors](#encryption-is-unavailable-due-to-recoverable-errors), you can fix them by performing the fix actions listed in the `actions` array of each error in `availability-check-errors`. The order of the errors and their corresponding fix actions should be respected. 

To perform a fix action with snapd, make a `POST` request to `/v2/systems/{label}` with `action` set to `fix-encryption-support` and `fix-action` set to the first entry in the error's `actions` array. For example, to enable the TPM via the firmware, send this request body:

```json
{
  "action": "fix-encryption-support",
  "fix-action": "enable-tpm-via-firmware"
}
```

If successful, snapd will return a synchronous response (`200 OK`) with the updated system details, which might include a different list of errors. For example:

```{code-block} json
:caption: Response body, `result`
{
  ...
  "storage-encryption": {
    "support": "unavailable",
    "features": ["passphrase-auth", "pin-auth"],
    "storage-safety": "prefer-encrypted",
    "unavailable-reason": "not encrypting device storage as checking TPM gave: a reboot is required to complete the action",
    "availability-check-errors": [
      {
        "kind": "reboot-required",
        "message": "a reboot is required to complete the action",
        "actions": ["reboot"]
      }
    ],
    "requirements": ["volumes-auth"]
  },
  ...
}
```

In this example, the recommended fix action is to reboot the system. Since this requires manual intervention from the user, this fix action cannot be executed by snapd. 

Any fix action that requires a system reboot discards the pre-install check context created by the initial `GET` request to `/v2/systems/{label}`. After the target system reboots, make a new `GET` request to the same endpoint to create a new pre-install check context. Follow these steps again to fix any lingering errors. Keep in mind that fix actions should be performed in the same order in which they appear in the `actions` array.

If snapd cannot perform an action, it will return a synchronous response (`200 OK`) with the system details and updated `availability-check-errors`. The table below lists error kinds that snapd might return in that situation, with a suggested message to show the user, and example fix actions. The list is not exhaustive: snapd can return error kinds and fix actions that the table does not include. Treat it as a starting point, rather than a specification.

```{dropdown} Error kinds returned if a fix action cannot be performed
| Error kind          | Suggested message to present to the user                                                                                    | Example fix action(s) |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------|
| `shutdown-required` | System shutdown is required to complete a previous action.                                                                  | `shutdown`            |
| `reboot-required`   | System reboot is required to complete a previous action.                                                                    | `reboot`              |
| `unexpected-action` | The provided action is unexpected because it is either not supported or not associated with the previously returned errors. | none                  |
| `invalid-argument`  | One or more of the supplied arguments are of an invalid type or value.                                                      | none                  |
| `action-failed`     | The provided action did not succeed.                                                                                        | none                  |
| `missing-argument`  | Not enough action arguments provided.                                                                                       | none                  |
```

Some of these errors, such as `unexpected-action`, `invalid-argument`, and `action-failed`, offer no further fix actions. If you encounter one, make a new `POST` request to `/v2/systems/{label}` with the following request body:

```json
{
  "action": "fix-encryption-support",
  "fix-action": ""
}
```

Setting `fix-action` to an empty string tells snapd not to perform another fix action. Snapd will return a synchronous response (`200 OK`) with the system details from before the previous action was attempted.

Continue checking and resolving errors until the system details show that [encryption is available](#encryption-is-available). The installation can then proceed.

### Arguments accepted by fix actions

Most fix actions neither require nor accept arguments. There are two exceptions: `proceed` and `clear-tpm`.

The following example shows errors for which `proceed` is a possible fix action:

```{code-block} json
:caption: Response body, `result.storage-encryption.availability-check-errors`
[
  {
    "kind": "addon-drivers-present",
    "message": "detected drivers running from value-added-retailer components",
    "actions": ["proceed"]
  },
  {
    "kind": "weak-secure-boot-algorithms-detected",
    "message": "components were authenticated using weak Authenticode digests or weak public keys",
    "actions": ["proceed"]
  }
]
```

If the fix action `proceed` is executed without arguments, snapd will ignore all errors at once. This is not recommended, as it gives the user no visibility into which errors are being ignored. To ignore one error at a time, make a `POST` request to `/v2/systems/{label}`, passing `error-kinds` in `args`:

```json
{
  "action": "fix-encryption-support",
  "fix-action": "proceed",
  "args": {
    "error-kinds": ["<error-kind>"]
  }
}
```
Replace `<error-kind>` with the kind of the error to ignore, as reported in `availability-check-errors` (for example, `addon-drivers-present`). It is recommended to list one error at a time.

The fix action `clear-tpm` normally does not accept arguments. However, if you attempt it against a TPM that has an auth value set in the TPM lockout hierarchy, you must supply that auth value. This can happen, for example, if the following error is returned:

```{code-block} json
:caption: Response body, one entry of `result.storage-encryption.availability-check-errors`
{
  "kind": "tpm-hierarchies-owned",
  "message": "error with TPM2 device: one or more of the TPM hierarchies is already owned",
  "args": {
    "with-auth-value": [1073741834]
  },
  "actions": [
    "clear-tpm-via-firmware",
    "enable-and-clear-tpm-via-firmware",
    "clear-tpm",
    "reboot-to-fw-settings"
  ]
}
```

If `clear-tpm-via-firmware` and `enable-and-clear-tpm-via-firmware` cannot be performed or do not fix the issue, attempt `clear-tpm`. Make a `POST` request to `/v2/systems/{label}` and pass the TPM lockout hierarchy auth value, base64-encoded, in `args`:

```json
{
  "action": "fix-encryption-support",
  "fix-action": "clear-tpm",
  "args": {
    "auth-value": "<base64-auth-value>"
  }
}
```
Replace `<base64-auth-value>` with the base64-encoded auth value. This value is chosen when the hierarchy's authorization is set and snapd cannot discover it. 

In all other cases `clear-tpm` must be requested without an `args` field.

## Set up storage encryption

After completing the pre-install checks, you can prepare the installation of Ubuntu with TPM-FDE by setting up the target system's storage encryption.

Depending on the target system's characteristics, adding a PIN or passphrase might be supported or even required. To determine whether the target system supports or requires a PIN or passphrase, look at the fields `requirements` and `features` in the system details. For example:

```{code-block} json
:caption: Response body, `result.storage-encryption`
{
  ...
  "features": ["passphrase-auth", "pin-auth"],
  "requirements": ["volumes-auth"],
  ...
}
```

In this example, the target system supports both PIN and passphrase as authentication methods. Since `volumes-auth` is present in `requirements`, at least one authentication method must be set. 

If `volumes-auth` is not present in `requirements`, setting a PIN or passphrase is optional. The `features` field will tell you whether the target system supports one or both.

### Without an authentication method

If the target system does not require an authentication method, you can set up the storage encryption without it. Make a `POST` request to `/v2/systems/{label}` with `action` set to `install`, `step` set to `setup-storage-encryption`, and `on-volumes` describing the volumes to encrypt. For example:

```json
{
  "action": "install",
  "step": "setup-storage-encryption",
  "on-volumes": {
    "pc": {
      "bootloader": "grub"
    }
  }
}
```
In this example, `on-volumes` is illustrative. Replace it with the description of the volumes your installer created.

If successful, snapd will return an asynchronous response (`202 Accepted`). The response body will include a change ID. You can check the change progress by making a `GET` request to `/v2/changes/{id}`. Once it completes, the storage is encrypted and you can move on to the [Generate recovery key section](#generate-recovery-key). 

### With a PIN or passphrase

Before setting up a PIN or passphrase, your installer should check whether it meets the minimum quality requirements. This check is optional but highly recommended, as it avoids errors when setting up the PIN or passphrase.

#### Check PIN or passphrase quality

To check the quality of a PIN, make a `POST` request to `/v2/systems/{label}` with `action` set to `check-pin-quality` and `pin` set to the PIN provided by the user:

```json
{
  "action": "check-pin-quality",
  "pin": "<pin>" 
}
```

To check the quality of a passphrase, make a `POST` request to `/v2/systems/{label}` with `action` set to `check-passphrase-quality` and `passphrase` set to the passphrase provided by the user:

```json
{
  "action": "check-passphrase-quality",
  "passphrase": "<passphrase>"
}
```

If the PIN or passphrase does not meet the minimum requirements or is not supported, snapd will return an error (`400 Bad Request`) and provide details about the failure For example:

```{code-block} json
:caption: Response body, `result`
{
  "kind": "invalid-pin",
  "message": "PIN did not pass quality checks",
  "value": {
    "reasons": ["low-entropy"],
    "entropy-bits": 6,
    "min-entropy-bits": 13,
    "optimal-entropy-bits": 64
  }
}
```
If a passphrase is tested instead, `kind` will be `invalid-passphrase`.

If the PIN or passphrase is supported and meets the minimum requirements, snapd will return a synchronous response (`200 OK`) with the entropy metrics. For example:

```{code-block} json
:caption: Response body, `result`
{
  "entropy-bits": 48,
  "min-entropy-bits": 40,
  "optimal-entropy-bits": 60
}
```

The minimum and optimal entropy bits differ for PINs and passphrases, and might change in the future.

Once the PIN or passphrase meets the minimum requirements, it can be added to the storage encryption setup.

#### Add PIN or passphrase

To add a PIN, make a `POST` request to `/v2/systems/{label}` with `action` set to `install` and `step` set to `setup-storage-encryption`. The request body must also include:
- `on-volumes`, describing the volumes to encrypt; 
- `volumes-auth` with the PIN; and 
- `keyboard-config`, describing the keyboard configuration selected by the user. 

For example:

```json
{
  "action": "install",
  "step": "setup-storage-encryption",
  "on-volumes": {
    "pc": {
      "bootloader": "grub"
    }
  },
  "volumes-auth": {
    "mode": "pin",
    "pin": "<pin>"
  },
  "keyboard-config": {
    "model": "pc105",
    "layout": "us"
  }
}
```
In this example, `on-volumes` is illustrative. Replace it with the description of the volumes your installer created. `keyboard-config` is also illustrative. Set it to the keyboard layout the user selected.

To add a passphrase instead, replace `volumes-auth` in the request body above with one including the user's passphrase:
```json
{
  "volumes-auth": {
    "mode": "passphrase",
    "passphrase": "<passphrase>"
  }
}
```

When adding a PIN or passphrase to the storage encryption setup, `keyboard-config` must be defined. Snapd uses this configuration to ensure that the same keyboard layout is available when the user enters the PIN or passphrase on first boot.

If successful, snapd will return an asynchronous response (`202 Accepted`). The response body will include a change ID. You can check its progress by making a `GET` request to `/v2/changes/{id}`. Once it completes, the storage is encrypted and you can move to the next step.

## Generate recovery key

Generating a recovery key is optional, but highly recommended. A recovery key is a high-entropy fallback credential used to recover the data on the disk if all other methods fail.

To generate a recovery key, make a `POST` request to `/v2/systems/{label}`, with the following request body:

```json
{
  "action": "install",
  "step": "generate-recovery-key"
}
```

Snapd will return a synchronous response (`200 OK`) with the recovery key. For example:

```{code-block} json
:caption: Response body, `result`
{
  "recovery-key": "12345-67890-12345-67890-12345-67890-12345-67890"
}
```

```{attention}
Present the recovery key to the user and tell them clearly that, in the event of hardware failure, they might lose their data without it.
```

## Write the boot chain onto the target system

To write the boot chain onto the volumes created and encrypted in the previous steps, make a `POST` request to `/v2/systems/{label}` with `action` set to `install`, `step` set to `finish`, and `on-volumes` describing those volumes. For example:

```json
{
  "action": "install",
  "step": "finish",
  "on-volumes": {
    "pc": {
      "bootloader": "grub"
    }
  }
}
```
In this example, `on-volumes` is illustrative. Reuse the `on-volumes` value from the storage encryption setup.

If successful, snapd will return an asynchronous response (`202 Accepted`). The response body will include a change ID. Wait until the change is complete before moving to the next step. You can check its progress by making a `GET` request to `/v2/changes/{id}`.

Once the change is complete, snapd has written the following onto the target system's volumes:
- the gadget content
- the kernel snap
- the base snap
- the gadget snap
- the bootloader configuration
- the `modeenv`, and
- the disk-unlock keys.

The system is now ready to reboot and install Ubuntu with TPM-FDE, but it is highly recommended to preseed it first.

## Preseed the target system before first boot

Preseeding the target system before the first boot is optional, but highly recommended. It makes the first boot faster and detects potential failures early.

Before preseeding, create the following mount points to match the existing preseeding workflow:
- `/dev`
- `/proc`
- `/sys`
- `/sys/kernel/security`

Snapd's preseeding checks require `/sys` and `/sys/kernel/security` to be mounted independently.

Also, bind-mount the installer environment's seed directory into `<target-root>/var/lib/snapd/seed`.

To preseed the target system, make a `POST` request to `/v2/systems/{label}` with `action` set to `install`, `step` set to `preseed`, and `target-root` set to the mount point of the installer target system's decrypted system-data filesystem:

```json
{
  "action": "install",
  "step": "preseed",
  "target-root": "<target-root>"
}
```

If successful, snapd will return an asynchronous response (`202 Accepted`). The response body will include a change ID. Wait until the change is complete before moving to the next step. You can check its progress by making a `GET` request to `/v2/changes/{id}`. 

When preseeding is complete, the target system is ready to reboot and install Ubuntu with TPM-FDE.

