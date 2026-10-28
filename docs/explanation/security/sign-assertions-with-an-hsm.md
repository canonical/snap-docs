---
myst:
  html_meta:
    description: Sign snap assertions with a key held on a hardware security module or smart card, using an external key manager with snapd and Snapcraft.
---

(explanation-security-sign-assertions-with-an-hsm)=
# Sign assertions with an HSM

A hardware security module (HSM) or smart card holds a {ref}`signing key <explanation-security-signing-keys>`
that cannot be read off the device. Snapd and Snapcraft sign assertions with it
through a key manager.

Refer to your HSM manufacturer's documentation for your device's specific setup
instructions.

## Requirements

The device must support PKCS-RSA signing and public key DER output. Assertion
signing keys must be 4096-bit RSA keys.

On an Ubuntu LTS, install `pkcs11-tool` and its supporting packages:

```bash
sudo apt install gnupg-pkcs11-scd         \
                 libengine-pkcs11-openssl \
                 libp11-kit0 opensc       \
                 pcsc-tools pcscd
```

Some `pkcs11-tool` invocations need an explicit provider, given as `--module
/usr/lib/<arch triplet>/opensc-pkcs11.so`. Your HSM manufacturer may provide
their own.

## Generate the key

`snapcraft create-key` cannot be used to generate the key. Generate the key on
the device instead. The label is the name of the key:

```bash
pkcs11-tool --login --pin <user-pin> \
  --keypairgen --key-type rsa:4096   \
  --id 10 --label <key-name>
```

`<user-pin>` is the user-specific PIN you select when provisioning the HSM. This
is generally not the Security Officer (SO) PIN.

This can take a while on a smart card. The device then reports the new pair:

```text
Key pair generated:
Private Key Object; RSA
  label:      <key-name>
  ID:         10
  Usage:      decrypt, sign, signRecover
  Access:     sensitive, always sensitive, never extractable, local
Public Key Object; RSA 4096 bits
  label:      <key-name>
  ID:         10
  Usage:      encrypt, verify, verifyRecover
  Access:     none
```

## The external key manager

The key manager performs the operations snapd would otherwise perform against
the keyring: reporting which signing mechanisms and key formats it supports,
listing key names, returning a public key, and signing.

There is a [reference implementation](https://github.com/canonical/hsm-assertion-signing-reference)
of an external key manager maintained by the Devices Field team that you may use
as a starting point for creating your own.

The environment variable `SNAPD_EXT_KEYMGR` informs Snapcraft and snapd that an
external manager is used to interact with keys. Set `SNAPD_EXT_KEYMGR` to the
fully qualified path of the key manager:

```bash
export SNAPD_EXT_KEYMGR="<path to key manager>"
```

The reference implementation reads the device's user PIN from the `PKCS11_PIN`
variable:

```bash
export PKCS11_PIN=<user-pin>
```

A PIN in an environment variable is readable by other processes running as
your user, and a PIN typed at a shell prompt is usually saved in that shell's
history. It is recommended instead to use something like [systemd-creds](https://manpages.ubuntu.com/manpages/latest/man1/systemd-creds.1.html)
to manage the secret. Alternatively, keep the PIN out of the shell's environment
and history during key operations:

```bash
PKCS11_PIN="$(systemd-ask-password 'HSM user PIN:')" snapcraft register-key my-key
```

## Register the key and sign

Register the key under the label you gave it on the device:

```bash
snapcraft register-key <key-name>
```

`snapcraft keys` then lists it, which also confirms that Snapcraft can read the
public key from the device through the key manager. Signing works as it does
with a key in the on-disk keyring:

```bash
snap sign -k <key-name> <assertion>.json > <assertion>.assert
```
