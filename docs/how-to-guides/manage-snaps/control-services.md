(how-to-guides-manage-snaps-control-services)=
# Control services

The majority of snaps expose their functionality via applications that run on the local system. Most of these applications are started either from [the command line](/how-to-guides/manage-snaps/apps-and-aliases), the graphical desktop, or as services that run automatically.

A single snap may provide multiple applications and services. With a database snap, for example, you might expect an interactive client application alongside the service daemon. 

Snaps manage their own services without the need for manual intervention. However, experienced administrators may want to interact with a snap's services to help improve their integration with the local environment.

For that reason, snapd offers a set of commands to allow a snap's services to be inspected and their statuses changed.

## User and root-level services

Prior to the release of _snapd 2.66_, all services were run with root-level access. The snap commands used to manage these services would require equivalent access, such as by preceding *snap* with `sudo`.

With the release of snapd 2.66, there is now distinction between user-level services and root-level services. User-level services can be listed and managed without requiring any privilege escalation, while services running as root still require equivalent access.

## Listing services

The `snap services` command lists the active and enabled state of snap-based services for the current user, or with the additional `--global` argument, for the entire system.


```
$ sudo snap services --global  
Service                    Startup  Current   Notes
lxd.activate               enabled  inactive  -
lxd.daemon                 enabled  active    socket-activated
lxd.user-daemon            enabled  inactive  socket-activated
multipass.multipassd       enabled  active    -
nextcloud.apache           enabled  active    -
nextcloud.logrotate        enabled  inactive  timer-activated
nextcloud.mysql            enabled  active    -
nextcloud.nextcloud-cron   enabled  active    -
nextcloud.nextcloud-fixer  enabled  active    -
nextcloud.php-fpm          enabled  active    -
nextcloud.redis-server     enabled  active    -
nextcloud.renew-certs      enabled  active    -
```

Adding a snap name as an argument will list only those services added by that snap, or with `<snap-name>.<app>`, for a single app:

```
$ snap services lxd.daemon    
Service     Startup  Current  Notes
lxd.daemon  enabled  active   socket-activated
```

The output includes the service name, whether the service is started when the system starts up, and whether it's currently running.

## Restarting, stopping and starting services

Services are restarted using the `snap restart <snap name>` command. This may be necessary if you've made custom changes to the snap application, for example, which the service needs to reload.

Using both the snap name and the specific app enables you to target a specific service:

```
$ snap restart lxd.daemon
2024-11-21T21:51:06+01:00 INFO Waiting for "snap.lxd.daemon.service" to stop.
Restarted.
```

The option to perform an operation on all of a snap's services, or on one specific service, is common to all commands that operate on services.

If a service supports _reloading_, enabling the service to remain running while loading a new configuration, this can be requested with the `--reload` option:

```
snap restart --reload lxd.daemon
```

The `start` and `stop` commands control whether a service should be currently running.

Adding the  `--system` argument can be used to manage system-level services, while `--user` and `--users=all` can be used to manage services for the current user, or for all users, respectively.

The following combination is also valid:

`snap {start,stop,restart} --system --users=all my-snap`

As root, the default behavior of not specifying anything is the equivalent of:

`snap {start,stop,restart} --system my-snap`

If operating on a snap that contains a user-service as root, the switch `--user` or `--users=all` must be provided to indicate that it’s intentional, otherwise an error will be thrown.

To prevent a service from starting on the next boot, use the `--disable` option:

```
snap stop --disable lxd.daemon
```

The *start* command includes an `--enable` option to re-enable the automatic starting of a service  when the system boots:

```
snap start --enable lxd.daemon
```

## Disabling and enabling user-services

User-services cannot be disabled or enabled individually for users currently, they can only be enabled globally or disabled globally (i.e for all users).

## Inspecting logs

If you need to see the log output for a snap's services, use the `logs`
command. As with the _services_ command, you can specify either a snap name to
see the logs for all the services it contains, or the name of a specific
service within a snap:

```
$ sudo snap logs lxd
2018-09-14T10:38:23Z lxd.daemon[11096]: => LXD is ready
(...)

$ sudo snap logs lxd.daemon
2022-07-15T17:13:04+01:00 lxd.daemon[1389234]: => LXD exited cleanly
2022-07-15T17:13:04+01:00 lxd.daemon[370462]: ==> Stopped LXD
2022-07-15T17:13:04+01:00 lxd.daemon[370462]: => Stopping LXCFS
2022-07-15T17:13:04+01:00 lxd.daemon[555302]: Running destructor lxcfs_exit
2022-07-15T17:13:05+01:00 lxd.daemon[370462]: ==> Stopped LXCFS
2022-07-15T17:13:05+01:00 lxd.daemon[370462]: => Cleaning up PID files
2022-07-15T17:13:05+01:00 lxd.daemon[370462]: => Cleaning up namespaces
2022-07-15T17:13:05+01:00 lxd.daemon[370462]: => All done
2022-07-15T17:13:05+01:00 systemd[1]: snap.lxd.daemon.service: Deactivated successfully.
2022-07-15T17:13:05+01:00 systemd[1]: Stopped Service for snap application lxd.daemon.
```

By default, only the last 10 lines are output. This can be changed with the `-n=` option which can accept either a number or `all` for the entire log:

```
snap logs -n=all lxd.daemon
```

Adding the `-f` option will keep log output open so you can follow new entries as they occur:

```
sudo snap logs lxd -f
```

The size and rate of log output can be limited by placing a snap within a quota group. See [Journal log limits](use-resource-quotas.md#journal-log-limits) for more details.
