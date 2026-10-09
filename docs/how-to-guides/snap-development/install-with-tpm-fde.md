---
myst:
  html_meta:
    description: Use the snapd REST API to install Ubuntu with hardware-backed Full Disk Encryption, including pre-install checks, error recovery, and PIN or passphrase setup.
---

(how-to-guides-install-with-tpm-fde)=

# Use the REST API to install Ubuntu with TPM-FDE

This guide shows you how to use the snapd REST API to install Ubuntu with [hardware-backed Full Disk Encryption](https://ubuntu.com/desktop/docs/en/latest/explanation/hardware-backed-disk-encryption/#hardware-backed-disk-encryption) (TPM-FDE).

Refer to the {ref}`snapd REST API reference<reference-development-snapd-rest-api>` for a list of all actions and endpoints. For general instructions, refer to the {ref}`guide on how to use the REST API<how-to-guides-manage-snaps-use-the-rest-api>`.

This guide is aimed at developers building a GUI-based custom Ubuntu installer that supports TPM-FDE. While the API can be called directly, this guide assumes that a GUI exists between the API calls and the end user.

The steps below must be followed in order:

1. [get target system's label](#get-system-label) if you do not know it already;
1. [perform pre-install checks](#perform-pre-install-checks);
1. if there are recoverable errors, [perform pre-install fixes](#perform-pre-install-fixes);
1. [add a PIN or passphrase](#add-pin-or-passphrase) or, if the system allows it, set up the storage encryption without authentication;
1. [generate a recovery key](#generate-recovery-key); this step is optional, but highly recommended;
1. [finish the installation](#finish-the-installation); and
1. for optimization purposes, [preseed the target system](#preseed-the-target-system-before-first-boot).

## Get system label

To install Ubuntu with TPM-FDE, you first need to identify the system where it will be installed. In the snapd REST API, systems are identified with a label.

To find the label of the system where you want to install Ubuntu with TPM-FDE, make a `GET` request to `/v2/systems`. This request will return a synchronous response (`200 OK`).

The response body will include a `result` object with a list of available systems. Each system will include a `label`. For example:

```json
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

Once you know the system label, you can [perform the pre-install checks](#perform-pre-install-checks).

## Perform pre-install checks

To perform the pre-install checks, use the system's label to make a `GET` request to `/v2/systems/{label}`. This request will return a synchronous response (`200 OK`).

The response body will include a `result` object with the system details. The nested object `storage-encryption` will include details about the system's storage encryption capabilities. It will state whether encryption is available. If it is not available, it will also include a list of errors and whether they can be fixed.

### Encryption is available

If encryption is available, `storage-encryption` will include the system's features and requirements, but no errors. For example:

```json
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

Since there are no errors, you can proceed with the installation. The requirements and features of the system will be used in the next step, [add a PIN or passphrase](#add-a-pin-or-passphrase).

### Encryption is unavailable due to recoverable errors

If encryption is unavailable due to recoverable errors, `storage-encryption` will include `unavailable-reason` and `availability-check-errors`. For example:

```json
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

In this example, the system has a TPM 2.0 device that is disabled in the firmware. This error can be resolved by executing the actions listed in the `actions` array, in the order in which they are presented. See the [section on how to perform pre-install fixes](#perform-pre-install-fixes) for guidelines and further details.

The initial `GET` request to `/v2/systems/{label}` runs pre-install checks and creates an in-memory pre-install check context, which will be used while fixing the errors. Another `GET` request to the same endpoint replaces that context, resetting the action sequence. The context is also lost if snapd restarts or the system reboots.

### Encryption is unavailable

If the system does not support encryption, `storage-encryption` will include `unavailable-reason`, but no `availability-check-errors`. For example:

```json
{
  ...
  "storage-encryption": {
    "support": "unavailable",
    "features": ["passphrase-auth", "pin-auth"],
    "storage-safety": "prefer-encrypted",
    "unavailable-reason": "cannot use encryption with the gadget, disabling encryption: gadget does not support encrypted data: required partition with system-save role is missing",
    "requirements": ["volumes-auth"]
  },
  ...
}
```

In this example, encryption is not possible because the gadget lacks a system-save partition. This is a fatal error that cannot be resolved by the API. No further steps are applicable until the gadget is replaced.

## Perform pre-install fixes

```{important}
Pre-install recovery actions can only be performed after an initial pre-install check. See [the section on how to perform pre-install checks](#perform-pre-install-checks) for more details.
```

If [encryption is unavailable due to recoverable errors](#encryption-is-unavailable-due-to-recoverable-errors), you can fix them by performing the actions listed in the `actions` array of each error (listed in `availability-check-errors`). These fix actions should be performed in the same order in which they appear in that array.

Some fix actions can be performed by making a `POST` request to `/v2/systems/{label}`. The request body must indicate that the API action `fix-encryption-support` is being executed and the specific fix action to apply. For example:

```json
{
  "action": "fix-encryption-support",
  "fix-action": "enable-tpm-via-firmware"
}
```

If successful, this request will return a synchronous response (`200 OK`). The response body will include a `result` object with the system details. The nested object `storage-encryption` will be updated and might show different errors. For example:

```json
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

In this example, the recommended fix action is to reboot the system. Since it requires manual intervention from the user, this fix action cannot be executed by the snapd API.

If a fix action that cannot be executed by the snapd API is requested through `fix-encryption-support`, a synchronous response (`200 OK`) with the system details will still be returned. The nested object `storage-encryption` will include the following `unavailable-reason` and `availability-check-errors`:

```json
{
  ...
  "unavailable-reason": "not encrypting device storage as checking TPM gave: specified action is not implemented directly by this package",
  "availability-check-errors": [
    {
      "kind": "unexpected-action",
      "message": "specified action is not implemented directly by this package"
    }
  ],
  ...
}
```

If this response is encountered, make a new `POST` request to `/v2/systems/{label}`, requesting the execution of the API action `fix-encryption-support` and with `fix-action` set to `""`:

```json
{
  "action": "fix-encryption-support",
  "fix-action": ""
}
```

The empty string tells the snapd API that no fix action should be executed. This request will return a synchronous response (`200 OK`) with the system details as they were before calling the unexpected fix action.

Some actions that require the user's intervention, such as `reboot`, will restart the pre-install check context created by the initial `GET` request to `/v2/systems/{label}`. After rebooting or shutting down, a new `GET` request to the same endpoint must be made, creating a new pre-install check context. Follow these steps again to fix any lingering errors. Keep in mind that fix actions should be executed in the same order in which they appear in the `actions` array of the corresponding error in `availability-check-errors`.

Once the system details show that [encryption is available](#encryption-is-available), you are ready to install Ubuntu with TPM-FDE.

## Add a PIN or passphrase

After completing the pre-install checks, you can prepare the installation of Ubuntu with TPM-FDE by setting up the system's storage encryption. Depending on the system's characteristics, adding a PIN or passphrase might be required to install Ubuntu with TPM-FDE.

To determine whether the system supports, or even requires, a PIN or passphrase, look at the fields `requirements` and `features` of the nested `storage-encryption` object in the system details. For example:

```json
{
  ...
  "features": ["passphrase-auth", "pin-auth"],
  "requirements": ["volumes-auth"],
  ...
}
```

If `volumes-auth` is present in `requirements`, at least one authentication method (PIN or passphrase) must be set up. Only authentication methods listed under `features` can be used. In this example, both PIN and passphrase are supported.

If `volumes-auth` is not present in `requirements`, setting a PIN or passphrase is optional, provided that the system supports it. You can set up the system's storage encryption without an authentication method by making a `POST` request to `/v2/systems/{label}`. The request body must indicate that you want to execute the API action `install`, step `setup-storage-encryption`, without `volumes-auth`. For example:

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

### Check PIN or passphrase quality

Before configuring the PIN or passphrase, the installer should check that it meets the minimum quality requirements. To check the PIN or passphrase quality, make a `POST` request to `/v2/systems/{label}`. The request body must indicate that you want to execute either the `check-pin-quality` or `check-passphrase-quality` API action and include the respective PIN or passphrase. For example:

```json
{
  "action": "check-pin-quality",
  "pin": "123456"
}
```

If the PIN or passphrase does not meet the minimum requirements (as is the case in this example) or is not supported, this request will return an error (`400 Bad Request`). The response body will include a `result` object with details. For example:

```json
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

If the PIN or passphrase is supported and meets the minimum requirements, this request will return a synchronous response (`200 OK`). The response body will include a `result` object with details about the assessment. For example:

```json
{
  "entropy-bits": 48,
  "min-entropy-bits": 40,
  "optimal-entropy-bits": 60
}
```

Once the PIN or passphrase meets the minimum requirements, it can be configured for the Ubuntu installation.

### Configure PIN or passphrase

To configure a PIN or passphrase, make a `POST` request to `/v2/systems/{label}`. The request body must indicate that you want to execute the API action `install`, step `setup-storage-encryption`. For example:

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
    "pin": "123456"
  },
  "keyboard-config": {
    "model": "pc105",
    "layout": "us"
  }
}
```

When setting up a PIN or a passphrase during installation, `keyboard-config` must be defined. Snapd uses this configuration to ensure that the same keyboard layout is available when entering the PIN or passphrase on first boot.

If successful, this will return an asynchronous response (`202 Accepted`). The response body will include a change ID. Wait until the process is complete before moving to the next step. You can check its progress by making a `GET` request to `/v2/changes/{id}`.

## Generate recovery key

Generating a recovery key is optional, but highly recommended. A recovery key is a high-entropy fallback credential used to recover the data on the disk if all other methods fail.

To generate a recovery key, make a `POST` request to `/v2/systems/{label}`, with the following request body:

```json
{
  "action": "install",
  "step": "generate-recovery-key"
}
```

This request will return a synchronous response (`200 OK`). The response body will include a `result` object with the recovery key. For example:

```json
{
  "recovery-key": "12345-67890-12345-67890-12345-67890-12345-67890"
}
```

Present the recovery key to the user with a clear indication that they should write it down and store it safely. The user should become aware that, in the event of hardware damage, their data might be lost without the recovery key.

## Finish the installation

To finish the installation of Ubuntu with TPM-FDE, make a `POST` request to `/v2/systems/{label}`. The request body must indicate that you want to execute the API action `install`, step `finish`. For example:

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

If successful, this will return an asynchronous response (`202 Accepted`). The response body will include a change ID. Wait until the process is complete before moving to the next step. You can check its progress by making a `GET` request to `/v2/changes/{id}`.

## Preseed the target system before first boot

Preseeding the already installed target system before the first boot is optional, but highly recommended. This makes the first boot faster and detects potential failures earlier.

To preseed the target system, make a `POST` request to `/v2/systems/{label}`. The request body must indicate that you want to execute the API action `install`, step `preseed`. Set `target-root` to the path where the installer mounted the target system's decrypted system-data filesystem. For example:

```json
{
  "action": "install",
  "step": "preseed",
  "target-root": "/run/mnt/ubuntu-data"
}
```

To align with the existing preseeding workflow, the following mount points must be created before preseeding:

- `/dev`
- `/proc`
- `/sys`
- `/sys/kernel/security`

Due to existing checks within snapd's preseeding implementation, `/sys` and `/sys/kernel/security` must be mounted independently.

Additionally, to prepare for preseeding, bind-mount the installer environment's seed directory into `<target-root>/var/lib/snapd/seed`.
