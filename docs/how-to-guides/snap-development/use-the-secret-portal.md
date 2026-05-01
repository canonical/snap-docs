(how-to-guides-use-the-secret-portal)=
# Using the Secret portal

The [Secret portal](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Secret.html) was designed as a secret storage solution for confined environments, such as snaps.

This {ref}`portal<interfaces-xdg-desktop-portals>` allows applications to get a master secret that they can use to encrypt their data. However, it requires a Secret portal backend on the host and a client that knows how to use it. The {ref}`desktop interface<interfaces-desktop-interface>` provides then grants snaps access to the Secret portal API. 

In the following  section, we will build a snap to demonstrate a fully working Secret portal example.

### Prerequisites

Make sure that your OS supports the secret-portal. `xdg-desktop-portal` version must be equal or greater than 1.5.0. On Ubuntu, it is supported on Ubuntu 20.04 onwards. 

### Building the snap

The most common way to manage secrets in Linux environments is with [libsecret](https://gnome.pages.gitlab.gnome.org/libsecret/).

When an application using libsecret runs unconfined, libsecret uses its *Secret Service* to store/retrieve secrets. However, if libsecrets detects it is being run under confinement (i.e. flatpak or snap), it will use the Secretportal instead. To showcase this behaviour, we are going to build a snap that uses libsecret to manage secrets by packaging the “secret-tool” provided by the libsecret project.

The following is the [snapcraft.yaml](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/) for our secret-tool snap:

```
name: secret-tool
version: '0.21.4-1build3'
summary: secret-tool from libsecret-tools deb.
description: |
  command line tool that can be used to store and retrieve passwords.

grade: stable
confinement: strict
base: core24

apps:
  secret-tool:
    command: usr/bin/secret-tool
    plugs:
    - desktop

parts:
  secret-tool:
    plugin: nil
    stage-packages:
    - libsecret-tools=0.21.4-1build3 
```

The snap can be built with the `snapcraft pack` command. See [Craft a snap](https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/) for further details.

When installing the snap, note that , as for the other xdg-desktop-portals, the desktop {ref}`interface must be plugged<how-to-guides-work-with-snaps-connect-interfaces>` to use the secret-portal.

### Verifying the behavior 

Install the secret-tool from the archive (sudo apt install libsecret-tools). We now have two different instances of the secret-tool:

- /usr/bin/secret-tool, which is unconfined  
- /snap/bin/secret-tool, which is confined by the snap

**Check 1:** Create a password with the unconfined instance and verify it is not accessible from the confinement. 

Create the password using the unconfined secret-tool

```
$ /usr/bin/secret-tool store \--label='My password' origin unconfined  
Password: 1234  
```

Read the password using the unconfined secret-tool

```
$ /usr/bin/secret-tool lookup origin unconfined  
1234  
```

Read the password using the confined secret-tool

```
$ /snap/bin/secret-tool lookup origin unconfined  
```

**Check 2:** Create a password from the snap and verify it is not directly accessible from the outside the confinement

Create the password using the confined secret-tool

```
$ /snap/bin/secret-tool store \--label='My password' origin confined  
Password: 1234  
```

Read the password using the confined secret-tool

```
$ /snap/bin/secret-tool lookup origin confined  
1234  
```

Read the password using system secret-tool

```
$ /usr/bin/secret-tool lookup origin snap  
```

**Check 3**: Verify a master secret was created for out secret-tool snap

Read the per-snap encryption password using the unconfined secret-tool

```
$ /usr/bin/secret-tool lookup app\_id snap.secret-tool  
xxxxxxxxxxxxx  
```

Support for the Secret portal was added to libsecret in version 0.20.0, however, it was only in version 0.20.5 when snaps started to be supported. This means that most applications using libsecret should use the secret portal out of the box when packaged using core22 and newer bases. It can be verified building the secret-tool snap using different bases and repeating the checks listed in this section. To make it process easier, you can install the secret-tool snap from the store using the appropriate track depending on the base you want to test:

```
snap install secret-tool \--channel XX/stable to use coreXX base  
```

## Electron apps

Electron is a popular framework that's often used to build snaps. Electron applications are recommended to use the [safeStorage](https://www.electronjs.org/docs/latest/api/safe-storage) API to manage secrets, although it cannot currently use the Secret portal. See [https://github.com/jslarraz/snap-secrets-electron](https://github.com/jslarraz/snap-secrets-electron) for more details.

In this case, using safeStorage is still recommended. safeStorage will use the session keyring if the user chooses to connect the password-manager-service interface manually, falling back to plain-text storage otherwise.  Once the underlying libraries (OSCrypt) are able to use the Secret portal, safeStorage will start using it without requiring any changes to the snap. 

## Tauri applications

Tauri applications are increasing in popularity in the snap ecosystem. Tauri as other rust applications can use the secret-portal by using the [Rust bindings for libsecret](https://crates.io/crates/libsecret). Please check [https://github.com/jslarraz/snap-secrets-tauri](https://github.com/jslarraz/snap-secrets-tauri) for a working example.