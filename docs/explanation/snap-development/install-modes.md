(interfaces-install-modes)=
# Install modes

A snap can be installed with the following optional arguments, typically used to help test a snap under development, troubleshoot interface issues, or debug application crashes.

In addition to the modes described below, `--transaction` can be used to install a set of snaps as a single transaction. See [Transactional updates](/explanation/how-snaps-work/transactional-updates) for more details.
				      
## Classic confinement

The `--classic` argument is required for snaps that need access to more system resources.

By default, a snap will attempt to install with _strict confinement_. Strict confinement is used by the majority of snaps, enabling them to run their applications and services in complete isolation with a minimal access level that’s always deemed safe.

Certain snaps, however, require unfettered access to the system, and these are packaged as _classic snaps_. Installing a snap that requires classic access will prompt the user to use the additional `--classic` argument:

```
sudo snap install snapcraft --classic
```

Only _classic_ snaps can be installed with the `--classic` argument. However, while the argument is silently accepted when installing a strict snap, it won't make any difference to its confinement. The snap will still be strictly confined.

See [Snap confinement](/explanation/security/snap-confinement) for more details on confinement levels.

## Dangerous mode

The `--dangerous` argument will install a local snap without validating or checking its assertions or signatures. These signatures are used to link a snap to its publisher and store, and to ensure that a snap remains unchanged during delivery and storage.

This option is useful when testing snaps shared through a trusted channel, and for testing snaps built locally, before eventually being published to the store.

The `snap refresh --ammend` command can be used to replace a locally installed snap with an identically named snap on the store.

## Developer mode

The `--devmode` argument grants the snap **full access to system resources** but will also report each access when no appropriate interface has been specified. This report is sent to the system log. This mode is intended to help snap developers identify the [interfaces](/explanation/interfaces/all-about-interfaces) an application needs.

This feature allows developers to iterate over their snap, selectively adding interfaces to their application before switching to _strict mode_ after all necessary interfaces have been specified.

The validity of a snap's signed assertions will also be checked, linking a snap to its developer and store, but the installation will progress even when the validity cannot be verified. In this case, the _devmode_ snap is additionally equivalent to being installed with `--dangerous`.

A strictly confined snap running in _devmode_ will generate log and AppArmor profile output associated with the snap, helping snap developers and testers understand access issues and other confinement problems.

The _devmode_ argument is also a requirement  if a snap has been built and published with `confinement: devmode` in its snapcraft.yaml. These snaps are built for testing and cannot be released to their respective stable channels.

Additionally, snaps running in development mode will not be updated. This is because it's assumed the snap developer wishes to test, and continue testing, a specific release.

## Jail mode

The `--jailmode` argument will force the snap to install with strict confinement. 

Only non-classic snaps can be placed in jail mode. This can be useful when testing how a snap published with developer mode will behave when strictly confined, and is usually a precursor to a snap being published as confined and stable after a period of testing.

## Check snap install mode

The `snap list` command will include the install mode status in the _Notes_ column for each respective snap:

```
Name        Version            Rev    Tracking        Publisher     Notes
liquidctl   1.7.1-11-g6295354  1      latest/stable   morrisong     devmode
snapcraft   5.0                6751   latest/stable   canonical✓    classic
```
