(interfaces-pkcs11)=
# pkcs11

The `pkcs11` interface enables the [PKCS#11 Cryptographic Token Interface Standard](https://thalesdocs.com/gphsm/ptk/5.9/docs/Content/PTK-C_Program/intro_PKCS11.htm) to be used with access to exposed tokens.

```{tip}

See [Interface management](/) and [Supported interfaces](/interfaces/index) for further details on how interfaces are used.
```

---

<h2 id='heading--dev-details'>Developer details </h2>

**[Auto-connect](/t/interface-management/6154#heading--auto-connections)**: no</br>
**[Super-privileged](/)**: yes</br>

### Code examples

The test code can be found in the snapd repository:</br>https://github.com/snapcore/snapd/blob/master/interfaces/builtin/pkcs11_test.go

The source code for the interface is in the snapd repository:
</br>https://github.com/snapcore/snapd/blob/master/interfaces/builtin/pkcs11.go

