(interfaces-home-outside-home)=
# Home outside home

The snap daemon (snapd) looks for a user's home directory ($HOME) under `/home` on the local filesystem. However, from _snapd 2.59_ onwards, the snap daemon can access an additional location using the `homedirs` [system option](/reference/operations/system-options):

```bash
sudo snap set system homedirs=<destination-directory>
```
This allows a snap's user data to be stored in a user's home location other under `/home`.

The following command will permit home directories to be accessible from `/remote/users`, for instance:

```bash
sudo snap set system homedirs=/remote/users
```
The new location needs to exist and be accessible, but it can be on a different filesystem or even mounted across a network. The original `/home` location remains valid but it is no longer a requirement that directories be stored there.

Once set, the `homedirs` system option can be retrieved with the `snap get` command:

```bash
$ sudo snap get system homedirs
/remote/users
```

The `homedirs` value can be cleared and restored to only `/home` with the `snap unset` command:

```bash
sudo snap unset system homedirs
```

## Bind mount home directories

While the _homedirs_ system option should work for the majority users, it's also possible to _bind mount_ an alternative $HOME location to `/home` to allow other locations to be found by snapd. This process is outlined below.

> ⓘ  A **bind mount** allows a mounted filesystem to be accessible from more than one location at the filesystem level. This is unlike a hard or symbolic link, for instance, which operate as special additional files that point to a destination. 

There are two steps to bind mount a home directory to a different location:
1. **the bind mount:** create the mount point and run the _mount_ command: 
    ```bash
    $ sudo mkdir -p /home/$USER
    $ sudo mount --bind <original-home-location> /home/$USER
    ```
1. **edit `/etc/passwd`**: backup `passwd` and edit the home location for your user:
    ```bash
   $ cp /etc/passwd passwd.backup
   # sudo edit /etc/passwd with your favourite editor
   $ cat /etc/passwd | grep $USER
      ubuntu:x:1000:1000:ubuntu,,,:/home/ubuntu:/bin/bash
    ```
    The following `awk` command can be used to edit `/etc/passwd` (change OLD_HOME to your old home directory):
    ```bash
    $ awk -vold=$"OLD_HOME" -vnew=$"/home/$USER" -F: ' BEGIN {OFS = ":"} \
      {sub(old,new,$6);print}' /etc/passwd > passwd.new
    $ sudo cp passwd.new /etc/passwd
    ```

Log out and back in again, and snap will work from the freshly mounted home location. If you run into difficulties, copy the backup passwd file to `/etc/passwd`.
