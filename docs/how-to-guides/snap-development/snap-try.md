(interfaces-snap-try)=
# Test snaps with snap try

The `snap try` command installs a snap from its unpackaged components within a directory. After installation, most changes to the components in that directory will immediately by visible in the installed snap.

Ordinarily, snaps cannot be modified. They are distributed as, and executed from, read-only SquashFS files whose integrity is guaranteed via [assertions](/) and the [store](/).

But it’s sometimes useful to be able to experiment with a snap locally, to help debug an issue, or to make changes to a snap when you don’t have upstream access to the packaging process. This is when `snap try` is useful.

* If you only have access to the packaged snap itself, you first need to [unsquash the snap](#heading--unsquash) and then [use snap try to test it](#heading--snaptry).
* If, instead, you are a developer with access to the source code of the snap, you first need to [use snapcraft try to build an unpacked snap](#heading--snapcrafttry), and then [use snap try to test it](#heading--snaptry).

<h2 id='heading--unsquash'>Unsquashing a snap</h2>

In order to use `snap try`, you first need to get the unpacked contents of the snap. The first step is to get the snap itself. The most practical source of snaps is the snap store, where a snap can be downloaded with the `snap download` command:

```
$ snap download hello-world
Fetching snap "hello-world"
Fetching assertions for "hello-world"
Install the snap with:
snap ack hello-world_29.assert
snap install hello-world_29.snap
```

The download includes the snap itself and a signed set of [assertions](/) from the store to validate the snap’s default state.

Alternatively, _.snap_ files for any installed snaps can be found at `/var/lib/snapd/snaps/`, from where they can be copied across to your current working directory.

To uncompress the SquashFS _.snap_ file, use `unsquashfs <snap filename>`:

```
$ unsquashfs hello-world_29.snap
Parallel unsquashfs: Using 8 processors
6 inodes (6 blocks) to write
[===========================|] 6/6 100%
created 6 files
created 4 directories
created 0 symlinks
created 0 device
```

The files associated with the snap can now be found in the `squashfs-root’ directory. You can use [snap try](#heading--snaptry) to install this unpacked snap.

<h2 id='heading--snaptry'>Using snap try</h2>

Running `snap try <directory>` installs an unpacked snap using a bind mount.

```
$ snap try squashfs-root
hello-world 6.4 mounted from /home/user/squashfs-root
$ which hello-world
/snap/bin/hello-world
```

Most changes now made to files in the `squashfs-root` folder will be immediately reflected in the installed snap. This can be helpful when debugging an application within a snap, or the snap itself.

> ⓘ Certain changes, such as adjusting a snap’s interfaces or confinement will not be reflected in the installed snap until after a reinstall. These changes include:
>
>* changes to snap interfaces, such as adding or removing a plug
>* changes to layouts
>* changes to a snap’s confinement

Using the above hello-world snap, for example, we could edit the `bin/echo` script to change its output without rebuilding or remounting the snap:

```
$ hello-world
Hello world!
$ sed -i 's/World/Everyone/g' /home/user/squashfs-root/bin/echo
$ hello-world
Hello Everyone!
```

<h2 id='heading--snapcrafttry'>Using snapcraft try</h2>

When developing a snap with [snapcraft](/), the `snapcraft try` command can be used in combination with `snap try` to quickly test a snap and fix issues.

The `snapcraft try` command runs through the build process to the completion of the _prime_ stage (see [Parts lifecycle](/) for further details). It then exposes the resultant _prime_ directory to the snapcraft directory, even from within a virtual machine or container.

This _prime_ directory includes all the staged components of a snap, which can then be installed and tested with the `snap try <prime directory>` command.

The following,  example, will build a _hello-world_ snap within [LXD](/) and offer its _prime_ directory locally:

```

$ snapcraft try --use-lxd
Pulling hello-world
+ snapcraftctl pull
Building hello-world
+ snapcraftctl build
+ cp --archive --link --no-dereference . /root/parts/hello-world/install
Staging hello-world
+ snapcraftctl stage
Priming hello-world
+ snapcraftctl prime
You can now run `snap try /home/user/hello-world/prime`.
```

The above snap can then be installed and tested with [`snap try`](#heading--snaptry) and the _prime_ directory as its target:

```
$ snap try /home/user/hello-world/prime
hello-world 0.1 mounted from /home/user/hello-world/prime
```

For further help on testing and debugging a snap, see [Iterating over a build](/) and [Debugging snaps](/reference/interfaces/debug-snaps).

