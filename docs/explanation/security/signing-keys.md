---
myst:
  html_meta:
    description: Create and register a key for signing snap assertions, and choose where the private key is held.
---

(explanation-security-signing-keys)=
# Signing keys

{ref}`Assertions <explanation-security-assertions>` are signed, and a signature
is only as trustworthy as the custody of the private key that made it. Snapd
uses 4096-bit RSA keys for signing.

It is recommended that for keys used in production, e.g. to sign model or
validation-set assertions, a hardware security module (HSM) is used to generate
and store the key. For more ephemeral or less critical keys, storing them on
disk is sufficient.

One key normally covers all of your models, or a family of them, rather than
one key per device. It is recommended that keys for other purposes, such as for
signing validation-set or system-user assertions, use [key roles](https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/signing-keys/#register-a-signing-key-with-limited-roles)
to maintain key usage separation.

## Create a key

Create a key, giving it any name you like:

```bash
snapcraft create-key <key-name>
```

You are prompted for a passphrase, which you need again every time the key is
used.

`snapcraft create-key` writes the key to an OpenPGP keyring in the `$HOME/.snap/gnupg`
directory. To instead create a key on an HSM, refer to {ref}`Sign assertions with an HSM <explanation-security-sign-assertions-with-an-hsm>`.

### Why use an HSM

The primary purpose for generating a signing key on an HSM is to restrict the
ways in which a key can be compromised.

Anything that can read your home directory can copy the key if it is generated
on disk. Once it has been copied, the key can be used for signing, and
signatures from a compromised key are still valid ones.

An HSM or smart card generates the key internally and marks it non-extractable,
so it never exists as a file or leaves the device.

Keys are generally replaceable, but if a key must be backed up it should be
generated using GnuPG, imported onto the HSM, and the copy on disk shredded.

It is always recommended that production keys never be stored on disk, and if
they are that they be moved to a secure storage device and the copy on disk shredded.

## Register a key

Keys must be registered to be used. Register the key to your Ubuntu One account:

```bash
snapcraft register-key <key-name>
```

`snapcraft keys` lists your registered keys with the fingerprints that signed
assertions reference:

```bash
$ snapcraft keys
    Name        SHA3-384 fingerprint
*   <key-name>  <fingerprint>
```

