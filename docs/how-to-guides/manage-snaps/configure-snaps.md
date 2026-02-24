(how-to-guides-work-with-snaps-configure-snaps)=
# Configure snaps

Certain snaps, such as those providing a background service, have configuration options that can be viewed and changed. The commands for viewing and changing these configuration options are `snap get`, `snap set` and `snap unset`.

To see the configuration options of an installed snap, enter `snap get <snap name>`:

```
$ sudo snap get nextcloud
Key        Value
mode       production
nextcloud  {...}
php        {...}
ports      {...}
private    {...}
```

The `{...}` in the output indicates that there are further options beneath the current key name level.

```{caution}
If there are no configuration options, you will see `error: snap <snap name> has no configuration`.
```

To explore configuration options, append the key name to the *get* command:

```
$ sudo snap get nextcloud ports
Key          Value
ports.http   80
ports.https  443
```

Alternatively, the entire set of configuration options can be dumped as JSON by adding the `-d` option:

```
$ sudo snap get -d nextcloud
{
        "http": {
                "compression": false
        },
        "mode": "production",
        "nextcloud": {
                "cron-interval": "5m"
        },
        "php": {
                "memory-limit": "512M"
        },
        "ports": {
                "http": 80,
                "https": 443
        },
        "private": {
                "http": {
                        "compression": false
                },
                "mode": "production",
                "nextcloud": {
                        "cron-interval": "5m"
                },
                "php": {
                        "memory-limit": "512M"
                },
                "ports": {
                        "http": 80,
                        "https": 443
                }
        }
}
```

Use the *set* command to change a configuration option:

```
$ sudo snap set nextcloud ports.http=81
$ sudo snap get nextcloud ports
Key          Value
ports.http   81
ports.https  443
```

To clear and return a value to its default state, use the *unset* command  (from _snapd 2.41+_):
```
$ sudo snap unset nextcloud ports.http
# sudo snap get nextcloud ports
Key          Value
ports.http   80
ports.https  443
```

Adding an exclamation mark (`!`) to the end of an option name  also clears its value:

```
$ sudo snap set nextcloud ports.http!
```

Un-setting with an exclamation mark can be mixed with setting other options at the same time:

```
$ sudo snap set nextcloud ports.https! ports.http=81
```

The update process will test the validity of the configuration options. If any errors are detected, the overall change is cancelled and the previous configuration reinstated.

Similarly, if the configuration update process takes longer than a reasonable amount of time, currently 5 minutes, the update is forcefully aborted and the once again the configuration is rolled back.
