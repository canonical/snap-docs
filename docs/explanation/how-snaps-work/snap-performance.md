(explanation-how-snaps-work-snap-performance)=
# Snap performance

The performance of a running application should not be affected by its snap environment, and any  performance or system monitoring tool will work on snapped processes in exactly the same way they would on other applications and processes.

But monitoring specific snap operations, alongside installation and distribution performance, can help with both snap _packaging_ and _configuration_ decisions, and also help to discover potential performance issues outside of an application's control. Several such approaches are outlined below.

On devices running Ubuntu Core, a [kernel boot parameter](https://ubuntu.com/core/docs/kernel-boot-parameters#heading--bootchart) can be used to generate a bootchart showing system startup times and performance.

## Snap debug timing

Timing output from a snap can be a useful measure of overall performance, but it can also reveal performance bottlenecks and targets for improvement. The [snap debug](/how-to-guides/work-with-snaps/fix-common-issues.md#generate-debug-info) command includes several options to produce timing output for execution time, internal _ensure_ activities and subsystem startup times.

### Execution time

By default, the `snap debug timings` command will produce timing output for a specific _change_, which itself represents a set of operations performed by the snap daemon.

The syntax for the command is as follows:

```
snap debug timings <change-id>
```

The change identifiers (`<change-id>`) are listed under the `ID` column in the output to `snap changes`:

```
ID    Status  Spawn                   Ready                   Summary
8302  Done    yesterday at 18:24 BST  yesterday at 18:24 BST  Install "chromium" snap
8303  Done    today at 11:46 BST      today at 11:46 BST      Remove hotplug connections and slots of device /dev/ttyACM0 (100 Series/C230 …; serial: 6564B3891339) with interface "serial-port"
8304  Done    today at 11:50 BST      today at 11:50 BST      Add hotplug slot of interface "/dev/ttyACM0 (100 Series/C230 …; serial: 6564B3891339)" for device serial-port with hotplug key "056a4e841487…"
```

Instead of a change id,  the `--last` argument can be used with a well defined name for a change, such as `auto-refresh`, `install`, `refresh`, `remove` or `try`.

With the `--verbose` argument, the output will also include a label for the change:

```
ID     Status Doing  Undoing  Label          Summary
160162 Done   750ms        -  prerequisites  Ensure prerequisites for "chromium" are available
^             681ms        -  install-prereq install "cups"
```

The ID represents a numerical identifier for tasks spawned by the change logic, with nested tasks denoted with the `^` symbol beneath their parent.

The following charts were produced from the `Doing` column output of  `snap debug timings --last=install` after installing the [Chromium snap](https://snapcraft.io/chromium), first from the cache, and secondly after a fresh install:

![Chromium snap cached install timing data](https://assets.ubuntu.com/v1/54cae8e8-chromium-cached-install-pie.png)


```{dropdown} Debug timing data for cached install of Chromium snap

```
ID      Status        Doing      Undoing  Label                          Summary
160241  Done          461ms            -  prerequisites                  Ensure prerequisites for "chromium" are available
 ^                    353ms            -  install-prereq                 install "cups"
 ^                     12ms            -  install-prereq                 install base "core22"
160242  Done           62ms            -  download-snap                  Download snap "chromium" (2556) from channel "stable"
160243  Done          607ms            -  validate-snap                  Fetch and check assertions for snap "chromium" (2556)
160244  Done         2253ms            -  mount-snap                     Mount snap "chromium" (2556)
 ^                     75ms            -  check-snap                     check snap "chromium"
 ^                   2059ms            -  setup-snap                     setup snap "chromium"
160245  Done           61ms            -  copy-snap-data                 Copy snap "chromium" data
160246  Done          241ms            -  setup-profiles                 Setup snap "chromium" (2556) security profiles
 ^                     32ms            -  setup-security-backend         setup security backend "seccomp" for snap "chromium"
 ^                    133ms            -  setup-security-backend[many]   setup security backend "apparmor" for 1 snaps
  ^                   101ms            -  load-profiles[changed-many]    load changed security profiles of 1 snaps
160247  Done          396ms            -  link-snap                      Make snap "chromium" (2556) available to the system
 ^                      8ms            -  generate-wrappers              generate wrappers for snap chromium
 ^                    290ms            -  update-fc-cache                update font config caches
160248  Done          388ms            -  auto-connect                   Automatically connect eligible plugs and slots of snap "chromium"
160267  Done           92ms            -  connect                        Connect chromium:u2f-devices to snapd:u2f-devices
160266  Done           70ms            -  connect                        Connect chromium:removable-media to snapd:removable-media
160258  Done           70ms            -  connect                        Connect chromium:screen-inhibit-control to snapd:screen-inhibit-control
160261  Done           72ms            -  connect                        Connect chromium:network to snapd:network
160264  Done           69ms            -  connect                        Connect chromium:system-packages-doc to snapd:system-packages-doc
160278  Done           76ms            -  connect                        Connect chromium:browser-sandbox to snapd:browser-support
160263  Done           70ms            -  connect                        Connect chromium:camera to snapd:camera
160270  Done           71ms            -  connect                        Connect chromium:chromium-config to snapd:personal-files
160283  Done           88ms            -  connect                        Connect chromium:icon-themes to gtk-common-themes:icon-themes
160275  Done           69ms            -  connect                        Connect chromium:sound-themes to gtk-common-themes:sound-themes
160257  Done           67ms            -  connect                        Connect chromium:gsettings to snapd:gsettings
160262  Done           97ms            -  connect                        Connect chromium:upower-observe to snapd:upower-observe
160260  Done          100ms            -  connect                        Connect chromium:joystick to snapd:joystick
160268  Done          120ms            -  connect                        Connect chromium:unity7 to snapd:unity7
160273  Done           80ms            -  connect                        Connect chromium:home to snapd:home
160259  Done           73ms            -  connect                        Connect chromium:wayland to snapd:wayland
160282  Done           66ms            -  connect                        Connect chromium:network-bind to snapd:network-bind
160272  Done           69ms            -  connect                        Connect chromium:gnome-42-2204 to gnome-42-2204:gnome-42-2204
160276  Done           69ms            -  connect                        Connect chromium:audio-playback to snapd:audio-playback
160281  Done           73ms            -  connect                        Connect chromium:desktop-legacy to snapd:desktop-legacy
160265  Done           70ms            -  connect                        Connect chromium:desktop to snapd:desktop
160277  Done           80ms            -  connect                        Connect chromium:audio-record to snapd:audio-record
160271  Done          113ms            -  connect                        Connect chromium:etc-chromium-browser-policies to snapd:system-files
160280  Done           79ms            -  connect                        Connect chromium:cups to cups:cups
160274  Done           73ms            -  connect                        Connect chromium:opengl to snapd:opengl
160269  Done           76ms            -  connect                        Connect chromium:x11 to snapd:x11
160279  Done           68ms            -  connect                        Connect chromium:gtk-3-themes to gtk-common-themes:gtk-3-themes
160256  Done         3016ms            -  setup-profiles                 Setup snap "chromium" (2556) security profiles for auto-connections
 ^                     63ms            -  setup-security-backend         setup security backend "seccomp" for snap "chromium"
 ^                   1835ms            -  setup-security-backend         setup security backend "udev" for snap "chromium"
 ^                      8ms            -  setup-security-backend         setup security backend "mount" for snap "chromium"
 ^                    163ms            -  setup-security-backend         setup security backend "mount" for snap "cups"
 ^                    828ms            -  setup-security-backend[many]   setup security backend "apparmor" for 5 snaps
  ^                   606ms            -  load-profiles[changed-many]    load changed security profiles of 5 snaps
  ^                    43ms            -  load-profiles[unchanged-many]  load unchanged security profiles 5 snaps
160249  Done          175ms            -  set-auto-aliases               Set automatic aliases for snap "chromium"
160250  Done           84ms            -  setup-aliases                  Setup snap "chromium" aliases
160251  Done           35ms            -  run-hook                       Run install hook of "chromium" snap if present
160252  Done           31ms            -  run-hook                       Run default-configure hook of "chromium" snap if present
160253  Done           61ms            -  start-snap-services            Start snap "chromium" (2556) services
160254  Done         4239ms            -  run-hook                       Run configure hook of "chromium" snap if present
160255  Done           41ms            -  run-hook                       Run health check of "chromium" snap
```

![Chromium snap cold install timing data](https://assets.ubuntu.com/v1/49e70e0e-chromium-cold-install-pie.png)

```{dropdown} Debug timing data for cold install of Chromium snap

```
ID      Status        Doing      Undoing  Label                          Summary
160162  Done          750ms            -  prerequisites                  Ensure prerequisites for "chromium" are available
^                     681ms            -  install-prereq                 install "cups"
160163  Done        44859ms            -  download-snap                  Download snap "chromium" (2556) from channel "stable"
^                   44801ms            -  download                       download snap "chromium"
160164  Done          703ms            -  validate-snap                  Fetch and check assertions for snap "chromium" (2556)
160165  Done         2177ms            -  mount-snap                     Mount snap "chromium" (2556)
^                      27ms            -  check-snap                     check snap "chromium"
^                    2048ms            -  setup-snap                     setup snap "chromium"
160166  Done           69ms            -  copy-snap-data                 Copy snap "chromium" data
160167  Done          252ms            -  setup-profiles                 Setup snap "chromium" (2556) security profiles
^                      34ms            -  setup-security-backend         setup security backend "seccomp" for snap "chromium"
^                     134ms            -  setup-security-backend[many]   setup security backend "apparmor" for 1 snaps
 ^                    102ms            -  load-profiles[changed-many]    load changed security profiles of 1 snaps
160168  Done          406ms            -  link-snap                      Make snap "chromium" (2556) available to the system
^                      12ms            -  generate-wrappers              generate wrappers for snap chromium
^                     285ms            -  update-fc-cache                update font config caches
160169  Done          396ms            -  auto-connect                   Automatically connect eligible plugs and slots of snap "chromium"
160188  Done           69ms            -  connect                        Connect chromium:home to snapd:home
160181  Done           69ms            -  connect                        Connect chromium:audio-playback to snapd:audio-playback
160202  Done           86ms            -  connect                        Connect chromium:joystick to snapd:joystick
160192  Done          104ms            -  connect                        Connect chromium:etc-chromium-browser-policies to snapd:system-fi
les
160183  Done           68ms            -  connect                        Connect chromium:desktop to snapd:desktop
160187  Done           67ms            -  connect                        Connect chromium:gnome-42-2204 to gnome-42-2204:gnome-42-2204
160184  Done           82ms            -  connect                        Connect chromium:icon-themes to gtk-common-themes:icon-themes
160191  Done           71ms            -  connect                        Connect chromium:u2f-devices to snapd:u2f-devices
160195  Done           64ms            -  connect                        Connect chromium:screen-inhibit-control to snapd:screen-inhibit-c
ontrol
160179  Done           79ms            -  connect                        Connect chromium:removable-media to snapd:removable-media
160204  Done           73ms            -  connect                        Connect chromium:upower-observe to snapd:upower-observe
160200  Done           70ms            -  connect                        Connect chromium:unity7 to snapd:unity7
160178  Done           68ms            -  connect                        Connect chromium:gtk-3-themes to gtk-common-themes:gtk-3-themes
160185  Done           81ms            -  connect                        Connect chromium:x11 to snapd:x11
160180  Done           65ms            -  connect                        Connect chromium:wayland to snapd:wayland
160198  Done           66ms            -  connect                        Connect chromium:chromium-config to snapd:personal-files
160194  Done           78ms            -  connect                        Connect chromium:network to snapd:network
160196  Done           73ms            -  connect                        Connect chromium:sound-themes to gtk-common-themes:sound-themes
160199  Done           83ms            -  connect                        Connect chromium:cups to cups:cups
160203  Done           72ms            -  connect                        Connect chromium:system-packages-doc to snapd:system-packages-doc
160182  Done           66ms            -  connect                        Connect chromium:browser-sandbox to snapd:browser-support
160201  Done           70ms            -  connect                        Connect chromium:opengl to snapd:opengl
160193  Done           66ms            -  connect                        Connect chromium:gsettings to snapd:gsettings
160186  Done           66ms            -  connect                        Connect chromium:camera to snapd:camera
160189  Done           77ms            -  connect                        Connect chromium:desktop-legacy to snapd:desktop-legacy
160190  Done           63ms            -  connect                        Connect chromium:network-bind to snapd:network-bind
160197  Done           83ms            -  connect                        Connect chromium:audio-record to snapd:audio-record
160177  Done         3200ms            -  setup-profiles                 Setup snap "chromium" (2556) security profiles auto-connections
^                      72ms            -  setup-security-backend         setup security backend "seccomp" for snap "chromium"
^                    2015ms            -  setup-security-backend         setup security backend "udev" for snap "chromium"
^                       9ms            -  setup-security-backend         setup security backend "mount" for snap "chromium"
^                     170ms            -  setup-security-backend         setup security backend "mount" for snap "cups"
^                     810ms            -  setup-security-backend[many]   setup security backend "apparmor" for 5 snaps
^                     585ms            -  load-profiles[changed-many]    load changed security profiles of 5 snaps
^                      40ms            -  load-profiles[unchanged-many]  load unchanged security profiles 5 snaps
160170  Done           67ms            -  set-auto-aliases               Set automatic aliases for snap "chromium"
160171  Done           61ms            -  setup-aliases                  Setup snap "chromium" aliases
160172  Done           72ms            -  run-hook                       Run install hook of "chromium" snap if present
160173  Done           54ms            -  run-hook                       Run default-configure hook of "chromium" snap if present
160174  Done           97ms            -  start-snap-services            Start snap "chromium" (2556) services
160175  Done         4247ms            -  run-hook                       Run configure hook of "chromium" snap if present
160176  Done           43ms            -  run-hook                       Run health check of "chromium" snap
```

### Internal activities

Alongside the execution time for a *change*, the time a taken to process internal  _snapd_ activities, called *ensure activities*, is also tracked. Ensure activities are performed on a regular basis, and they occasionally generate new tasks, as changes, to continue an initial action. They include the following:

- `auto-refresh`
- `become-operational` (Ubuntu Core only)
- `install-system` (Ubuntu Core only)
- `refresh-catalogs`
- `refresh-hints`
- `seed` (Ubuntu Core only)

Tracking the execution times of such ensure activities can be useful. For example, *auto-refresh* involves multiple processes for various already-installed snaps, including connecting to the Snap Store. Timing information can therefore help troubleshoot refresh issues.

Use the `--ensure=` argument to see the timing details for the latest specified ensure activity, or with the optional `--all` argument to show timing data for every execution of the ensure activity.

```
$ snap debug timings --ensure=refresh-catalogs
ID                Status        Doing      Undoing  Summary
refresh-catalogs                309ms            -  
 ^                               69ms            -    query store for sections
 ^                              170ms            -    query store for catalogs
```

## Subsystem startup times

The startup timing data for two subsystems, `load-state` and `ifacemgr`, are also tracked and can be output with the `--startup` argument:

```
$ snap debug timings --startup=ifacemgr
ID        Status        Doing      Undoing  Summary
ifacemgr                    -            -  
 ^                        8ms            -    setup security backend "apparmor" for snap "core"
 ^                        7ms            -    setup security backend "mount" for snap "lxd"
 ^                       16ms            -    setup security backend "apparmor" for snap "lxd"
 ^                       12ms            -    load unchanged security profiles of snap "lxd"
 ^                        7ms            -    setup security backend "apparmor" for snap "vlc"
 ^                        5ms            -    load unchanged security profiles of snap "vlc"
```

The above example shows execution times related to snapd’s interface manager, which includes the time to set up the security profiles for all installed snaps and their interfaces before snapd becomes operational.

## SquashFS performance and compression

[SquashFS](https://www.kernel.org/doc/Documentation/filesystems/squashfs.txt) is a standard Linux file system that encases an operational directory structure within a single compressed file. It’s commonly used to provide bootable live Linux environments on USB storage, but it’s also used to package a snap.

A snap is a SquashFS file that contains the library and binary environment for the snap, alongside the metadata to describe its access and capabilities. The SquashFS file is either mounted by _systemd_ when the snap is first installed, or during the early phases of the bootup for a system, such as Ubuntu Core, that already has snaps installed.

SquashFS decompression occurs when a snap is first run on a system and its performance has been closely monitored. In particular, decompression performance may differ according to the compression algorithm used, the size of the SquashFS archive, the number of files it contains, whether it’s being accessed for the first time (cold-cache) or whether it’s being accessed again (warm-cache). 

Snaps can use one of two different types of compression, either `xz` or `lzo`, with the majority of snaps defaulting to `xz`. These algorithms were chosen for their compression ratios and speed when used with snaps that differ in the number of files they contain, and their size.

```{note}
See [snapcraft.yaml compression](https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/snapcraft-yaml/#compression) for schema details on how to build a snap using compression.
```

Chromium, for example, contains over 300MB across almost 1000 files and it takes significantly longer to access every file than it does to launch the application. In this case, the xz compression format is the slowest by more than double the next slowest format, gzip. This is shown in the following “box chart”, where each test was run 10 times across 6 different compression options. Each test itself is an aggregate of times for installation, running the application twice, and hashing every file in the SquashFS archive:

![Chromium SquashFS file walk speed](https://assets.ubuntu.com/v1/4d4454ed-perf-chromium-walk.png)

The decompression speed for both cold-cache (1) and warm-cache(2) access, across a range of compression algorithms, has also been tested. Again for Chromium, measuring start speed shows that xz initially performs very poorly when first launched, but improves significantly with subsequent launches:

![chromium warm cold access speed](https://assets.ubuntu.com/v1/998d84a9-compression-speed.png)

Compression ratios for various compression algorithms are also affected by the size of files inside the snap:

![compression ratios comparison](https://assets.ubuntu.com/v1/ddc43d34-compression-ratios-barchart.png)

These comparisons ultimately led to the addition of lzo as an optional compression algorithm, but its use with snaps is entirely dependent on the type and structure of the files within the SquashFS archive.

