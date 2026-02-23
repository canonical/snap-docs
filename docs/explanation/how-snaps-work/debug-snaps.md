(interfaces-debug-snaps)=
# Debug snaps

Each snap runs inside its own [confined environment](/), also called "sandbox". The policy of each sandbox describes what the application is allowed to do. When an application tries to do something that is not allowed, the system logs a policy violation.

The following techniques can help you investigate and solve these policy violations.

- Use [`snap try`](/how-to-guides/snap-development/snap-try) to quickly test changes without rebuilding your snap.
- Use `snap run --shell` to inspect and test the confined environment.
- Use _developer mode_ to try your snap without confinement.
- Investigating policy violation logs:
  - Use [`snappy-debug`](#heading--snappy-debug) to investigate violation logs and receive suggestions.
  - Manually search the raw logs
  - Understanding AppArmor
  - Understanding seccomp
- Investigate file permissions and cgroup device access violations.
- Use GDB and gdbserver from within a snap's environment to isolate and identify potential issues.

For more details on how AppArmor, seccomp and device permission security policies are implemented, see [Security policy and sandboxing](/explanation/security/security-policies).

## Run a shell in the confined environment

To investigate and test the confined environment of a snap, you can open a `bash` shell in it. After the snap is installed, use the `--shell  <name>.<command>` argument of `snap run`.

```
$ snap run --shell mysnap.mycommand
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
```

This will create the confined environment of the Snap, execute the [command-chain](/how-to-guides/manage-snaps/control-services) and then run `bash` inside that environment.

You can then investigate which files your snap has access to by running commands such as `ls` and `cat`.

It's important to put `--shell` _before_ the name of the snap. Otherwise it will be interpreted as an argument to the application instead of an argument to `snap run`.

## Run a snap under strace

Note that this requires _snapd 2.62_.

Viewing which [system calls](https://en.wikipedia.org/wiki/System_call) are made by an application, and how the Linux kernel responds to them,  can be beneficial in gaining insights into a failure.  This can be accomplished with the widely used [strace](https://strace.io/) utility.

Running the standard _strace_ command on a snapped application, however, can produce confusing results due to the [confined environment](/explanation/security/snap-confinement) most snaps run within. To solve this problem, _snapd_ includes specific support for running an application under strace.

To use this, you first have to install the [strace-static](https://snapcraft.io/strace-static) snap:

```
sudo snap install strace-static
```

With _strace-static_ installed, you can now use the `--strace` argument with the _snap_ command to launch _strace_ within the snap environment:

```sh
snap run --strace <snap-name>
```

You will be asked for your password because the internal strace logic relies on _sudo_.

Additionally, you can disable post-processing of the strace output by passing `--raw` to `--strace=`:

```
snap run --strace=--raw <snap-name>
```

Strace is highly versatile. You can learn more about it by reading the manual page [strace(1)](https://www.man7.org/linux/man-pages/man1/strace.1.html).

## Developer mode

To help isolate runtime errors when building and testing a snap, a snap can be installed using _developer mode_.

To install a snap in developer mode, use the `--devmode` argument:

```
sudo snap install --devmode mysnap
```

When a snap is installed with developer mode, violations against a snap's security policy are permitted to proceed but logged via journald.

## Debugging policy violation logs

### Using snappy-debug to show violations

The easiest way to find and fix policy violations is to use [the `snappy-debug` tool](https://snapcraft.io/snappy-debug). It

- watches syslog for policy violations,
- shows them in a human readable format,
- and makes recommendations for how to solve them.

First, install the tool by running the following command.

```shell
sudo snap install snappy-debug
```

Then, run the following command to start watching policy violations.

```shell
$ sudo snappy-debug
INFO: Following '/var/log/syslog'. If have dropped messages, use:
INFO: $ sudo journalctl --output=short --follow --all | sudo snappy-debug
```

If you have dropped messages, try the following command instead.

```shell
sudo journalctl --output=short --follow --all | sudo snappy-debug
```

Note: these commands only show policy violations that happen _after_ you run them. So first run one of these commands and then run the snap that you want to debug.

See `snappy-debug --help` for more information about this tool.

If you believe there is a bug in a security policy or want to request and/or contribute a new interface, please [file a bug](https://bugs.launchpad.net/snappy/+filebug), adding the `snapd-interface` tag, and feel free to discuss policy issues [on the forum](https://forum.snapcraft.io/c/snapd).


### Manually extracting violation logs

> Note that this method does not show _all_ violation logs, since not all logs contain the term "audit" in them. Use `snappy-debug` to see all violation logs.

You can also manually show snap policy violations by searching the logs for _audit_.

```
$ sudo journalctl --since=yesterday | grep audit
```

The above command uses `--since=yesterday` to limit the typically verbose logging output from journalctl.

A handy debugging technique is to tail/follow journalctl output while exercising the snap:

```
$ sudo sysctl -w kernel.printk_ratelimit=0 ; journalctl --follow | grep audit
```

As shown above, kernel log rate limiting can be disabled manually with:
 ```
$ sudo sysctl -w kernel.printk_ratelimit=0
```

### Understanding AppArmor violations

An AppArmor violation will look something like the following and include `apparmor=DENIED`:

```
audit: type=1400 audit(1431384420.408:319): apparmor="DENIED" operation="mkdir" profile="snap.foo.bar" name="/var/lib/foo" pid=637 comm="bar" requested_mask="c" denied_mask="c" fsuid=0 ouid=0
```

If there are no AppArmor denials, AppArmor shouldn't be blocking the snap.

To better understand AppArmor policy for a strictly installed snap, modify the AppArmor policy _in place_ on the target system. Changes aren't persistent, but this can help when considering a snapd patch or bug report.

For example:

1. build the  snap
1. copy the snap to the target device and install it (or use [snap try](/reference/interfaces/snap-try))
1. use the snap (perhaps using [`snap run --shell <name>.<command>`](#heading--shell)), monitoring via journalctl for denials
1. modifying `/var/lib/snapd/apparmor/profiles/snap.<name>.<command>` as needed (eg, adding rules before the final `'}'`)and running `sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap.<name>.<command>` to compile and load the policy into the kernel
1. use `sudo service snap.<name>.<command> stop/start/etc` as needed for daemons
1. repeat until AppArmor policy issues are resolved

### Understanding seccomp violations

A seccomp violation will look something like:

```
audit: type=1326 audit(1430766107.122:16): auid=1000 uid=1000 gid=1000 ses=15 pid=1491 comm="env" exe="/bin/bash" sig=31 arch=40000028 syscall=983045 compat=0 ip=0xb6fb0bd6 code=0x0
```

The `syscall=983045` can be resolved by running the `scmp_sys_resolver` command on a system of the same architecture as the one with the seccomp violation:

```
$ scmp_sys_resolver 983045
set_tls
```

If there are no seccomp violations, seccomp isn't blocking the snap.

If you notice `compat=1` in the seccomp denial, then specify the correct compatibility architecture to `scmp_sys_resolver` with `-a <arch>`. For example, when on an amd64 system, use `scmp_sys_resolver -a x86 191` (use `-a arm` on arm64 systems).

The seccomp filter profile in expected to be located in /var/lib/snapd/seccomp/bpf/*.src (formerly /var/lib/snapd/seccomp/profiles).

The seccomp profile source (the `*.src` file in the profile directory) needs to be recompiled into the profile binary (`*.bin` in the profile directory) as follows:

```
sudo /usr/lib/snapd/snap-seccomp compile /var/lib/snapd/seccomp/bpf/snap.$SNAP_NAME.src /var/lib/snapd/seccomp/bpf/snap.$SNAP_NAME.bin
```

The `snap-confine` command will load the bpf in the `.bin` file for the command when you (re)launch the command or `snap run --shell`. The seccomp policy language is considerably simpler and is essentially a list of allowed syscalls.

When done, copy any changes you make to `/var/lib/snapd/apparmor/profiles/snap.<name>.<command>` or `/var/lib/snapd/seccomp/bpf/snap.<name>.<command>.src` to your interface code.

#### snap-seccomp versions and paths

Tools such as snap-confine, snap-seccomp and snap-exec are internal to snapd and are initially installed with a distribution's snapd package.

On certain distributions, these tools can become superseded by versions embedded in subsequently installed core and snapd snaps. When developing a seccomp profile, it is important that the correct snap-seccomp binary is used. This can be determined by inspecting which binary is running as _snapd_.

With re-execution from the subsequently installed core and snapd snaps, these tools get called using their full path from the same location as the currently running binary. This is visible from `/proc`:

```
# with reexecution
$ sudo ls -l /proc/$(pidof snapd)/exe
lrwxrwxrwx 1 root root 0 Jun  5 10:10 /proc/1994/exe -> /snap/snapd/7777/usr/lib/snapd/snapd
```

Thus tools such as snap-seccomp will be called using its full path, `/snap/snapd/7777/usr/lib/snapd/snap-seccomp`.

Without re-execution, the snapd process is using a binary located in the host filesystem:

```
# no reexecution
$ sudo ls -l /proc/$(pidof snapd)/exe
lrwxrwxrwx 1 root root 0 06-05 12:49 /proc/808335/exe -> /usr/lib/snapd/snapd
```

Correspondingly, `snap-seccomp` will be called using its full path `/usr/lib/snapd/snapd`.

## File permissions

While tradition file permissions are respected and enforced, any violations are not currently logged. Similarly, device cgroups may also block access without logging denials.

To check whether device cgroups are affecting a snap's device access:

1. see if there are any snapd-generated udev rules in `/etc/udev/rules.d/70-snap.$SNAPNAME.rules`
1. if rules are defined, use `udevadm info /dev/$DEVICE` to see if the snap shows up in TAGS, or see if the `/run/udev/tags/snap_$SNAPNAME_$COMMAND` directory exists
1. examine if the `/sys/fs/cgroup/snap.$SNAPNAME.$COMMAND` directory exists and if the device is listed in `/sys/fs/cgroup/devices/snap.$SNAPNAME.$COMMAND/devices.allow` (eg, `/dev/kmsg` would have '`c 1:11 rwm`' since `/dev/kmsg` is a character device with MAJOR:MINOR as 1:11 (see `ls -l /dev/kmsg`))

For device cgroups, create or modify `/etc/udev/rules.d/70-snap.$SNAPNAME.rules` as necessary (eg, `KERNEL=="kmsg" TAGS+="snap_$YOURSNAPNAME_$YOURCOMMAND"` would tag `/dev/kmsg` for your snap), then run `sudo udevadm trigger --action=change`. To undo the access, remove the file and run the `udevadm` command again. When done, update the interfaces code based on your changes.

If you believe there is a bug in the security policy or want to request and/or contribute a new interface, please [file a bug](https://bugs.launchpad.net/snappy/+filebug), adding the `snapd-interface` tag.

<!--
### Interface development and security policy

When participating in snappy development and implementing new interfaces for others to use, you will almost always need to write security policy for both the slots and the plugs side of the interface but keep in mind you are not expected to write perfect security policy on the first try. The review process for snapd includes a security review of the interface security policy and it is expected that the security policy will be iterated on during the review process (in other words, if you are stuck on writing security policy but the interface otherwise works, feel free to submit the interface and ask for help).

In addition to the above, here are some other useful techniques when debugging/developing policy:

 * temporarily specify `@unrestricted` in the seccomp policy and this will allow all syscalls
 * temporarily use a combination of bare AppArmor rules to focus on only the parts you want. For example:

    ```
    file,
    capability,
    network,
    mount,
    remount,
    pivot_root,
    umount,
    dbus,
    signal,
    ptrace,
    unix,
    ```
 * look at existing policy in `interfaces/apparmor/template.go`, `interfaces/seccomp/template.go` and `interfaces/builtin/*` for examples of the policy language
 * [stracing snaps](https://forum.snapcraft.io/t/stracing-snap-commands/1433). In addition to simply stracing the app, it can also be helpful to strace the app in both devmode and strict confinement and comparing the results.
 * when testing new versions of snappy-app-dev, if re-exec is enabled you will need to copy the new version to the location udev expects it (eg, `/lib/udev`) and then bind mount it over where the re-exec'd snap-confine expects it (eg, `mount --bind /lib/udev/snappy-app-dev /snap/core/<version>/lib/udev/snappy-app-dev`)

The above command has changed to snap-device-helper
-->

## Further reading

- https://github.com/canonical/snapd/tree/master/interfaces for existing interface code and policy
- https://manpages.ubuntu.com/manpages/jammy/man5/apparmor.d.5.html
- https://gitlab.com/apparmor/apparmor/-/wikis/Profiling_by_hand (but use the paths listed above and don't use the `aa-genprof` or `aa-logprof` tools because they are not yet snappy-aware)
- https://github.com/canonical/snapd/wiki/snap-confine-Overview
- https://assets.ubuntu.com/v1/66fcd858-ubuntu-core-security-whitepaper.pdf
- https://github.com/canonical/snapd/wiki/Snap-Execution-Environment
- https://forum.snapcraft.io/t/stracing-snap-commands/1433

