---
myst:
  html_meta:
    description: Implement full-disk encryption for Ubuntu Core with the fde-setup hook and fde-reveal-key helper.
---

(reference-development-uc20-fde-hooks)=
# UC20+ FDE Hooks

[Ubuntu Core](https://documentation.ubuntu.com/core/) 20 and later (UC20+) use [full disk encryption](https://documentation.ubuntu.com/core/explanation/full-disk-encryption/) (FDE) whenever the hardware allows, protecting both the confidentiality and integrity of a device’s data when there’s physical access to a device, or after a device has been lost or stolen.

Creating a verifiable boot process on a non-standard (non-UEFI+TPM and non-OPTEE) FDE platform, such as on a Raspberry Pi or other ARM devices, is board-specific and will typically involve creating custom gadget and kernel snaps. UC20+, however, does provide a helper mechanism, via a hook interface, to ensure the integrity of any subsequently executed or accessed data. This process is outlined below.

> If your platform supports OP-TEE, we strongly encourage using the [OP-TEE full disk encryption](https://documentation.ubuntu.com/core/explanation/full-disk-encryption-op-tee/) hooks instead.

> [Get in touch](https://ubuntu.com/core/contact-us?product=core-overview) to discuss bespoke requirements for non-standard FDE platforms.

- [Using the hook](#heading--hooks)
- [Data handling](#heading--data)
  - [fde-reveal-key](#heading--fde-reveal-key)
  - [fde-setup](#heading--fde-setup)
    - [op: features](#heading--features)
    - [op: initial-setup](#heading--initial-setup)
- [Implementation examples](#heading--examples)
- [Future development](#heading--future)

<span id="heading--hooks"></span>
## Using the hook

Snapd uses the {ref}`hook <reference-development-supported-snap-hooks>` mechanism in the kernel snap to run hook-specific executable binaries. The first retrieves the encryption key and unlocks the disk while the second is called on installation/re-installation to ensure the key is sealed.

- The first binary is executed from the initrd and is located inside the _initrd_ $PATH, e.g. `usr/bin/fde-reveal-key`.

  This is used by snap-bootstrap initramfs-mounts to retrieve the key and unlock the disk. It does not run with typical snapd confinement, using systemd mechanisms instead to restrict the helper and ensure it is not misused to change the ubuntu-data partition in uncontrolled ways.

- The second binary is executed from the install/reinstall process to ensure the key is sealed.

  It is run as a normal hook `meta/hooks/fde-setup` from the kernel snap with corresponding `snapctl fde-setup-request` and `snapctl fde-setup-result` commands that can be used from the hook.

If `fde-reveal-key` and `meta/hooks/fde-setup` exist, they're used for all FDE operations instead of the built-in TPM code.

<span id="heading--data"></span>
## Data handling

The helper mechanism is stateless, with snapd providing whatever data is necessary.

When protecting a key, for instance, `fde-setup` returns a "handle" consisting of any valid JSON, such as a string with base64-encoded binary data, which could then be used as auxiliary data to help unseal/decrypt the protected key.

Apart from ensuring the data is valid JSON, or when the data is passed back to `fde-reveal-key` (see below), snapd stores and handles this data completely opaquely.

<span id="heading--fde-reveal-key"></span>
### Data for fde-reveal-key

As mentioned earlier, the `fde-reveal-key` binary is run from _initrd_. It gets data via _stdin_ and outputs the data to stdout.

<span id="heading--fde-reveal"></span>
#### op: reveal

In this operation the revealed key is written to _stdout_. The data passed via _stdin_ is JSON:

```text
{
    "op": "reveal",                 // more may be added in the future
    "sealed-key": "<base64-encoded-bytes>",
    "handle": <handle-valid-json>,  // opaque handle (can be empty)
                                    // as returned previously by fde-setup
}
```

It returns: `{"key": "base64 encoded key"}` to allow additional future capabilities.

Any exit code other than `0` is expected to return an error string to _stderr_.

<span id="heading--fde-lock"></span>
#### op: lock

When the hook is called in this way, access to the keys should be locked using a method appropriate for the underlying hardware.

<span id="heading--fde-setup"></span>
### Data for fde-setup

`fde-setup` is a normal snapd hook and uses {ref}`snapctl <how-to-guides-manage-snaps-use-snapctl>` to communicate with snapd.

The workflow for the hook is that it calls `snapctl fde-setup-request` and reads the JSON from _stdout_. The JSON will contain an `op` field that tells the hook what to do.

The result is operation dependent and should be set via _stdin_ to `snapctl fde-setup-result`.

<span id="heading--features"></span>
#### op: features

If the `fde-setup` hook is run with `"op": "features"` (see above), the hook should report, via JSON, a JSON-formatted array containing the features it supports. Initially this will just be an empty list: `[]`.

For example

```bash
$ snapctl fde-setup-request
{"op":"features"}

$ echo '{"features": []}' | snapctl fde-setup-result
```

Currently, this is mostly to future proof hooks/snapd.

<span id="heading--initial-setup"></span>
#### op: initial-setup

If the `fde-setup` hook is run with `"op": "initial-setup"`, the hook should call `snapctl fde-setup-request`, passing the following JSON to _stdout_:

```text
{
    "op": "initial-setup",      // valid: "initial-setup","update"
    "key": <base64-encoded-payload-that-should-be-encrypted/sealed>,
}
```

When the hook has completed the encryption and sealing, it will call:

```bash
$ echo '{"sealed-key": "<base64-sealed-or-encrypted-key>", "handle": <opaque-handle-valid-JSON> }' | snapctl fde-setup-result
```

Any exit code other than `0` is expected to return an error string to _stderr_.

<span id="heading--examples"></span>
## Implementation examples

- snapd example, used for integration testing in _go_ ( (insecure as it's software only):
  <https://github.com/snapcore/snapd/blob/master/tests/lib/fde-setup-hook/fde-setup.go>

- Production grade OP-TEE implementation written in C:
  <https://git.launchpad.net/~ondrak/+git/optee-uc-fde/tree/host/fde_key_manager/>

<span id="heading--future"></span>
## Future development

The current spec does not include boot chains or a method of tacking what specific boot assets are measured. Consequently, these hooks cannot currently be used for systems that require measurements.
