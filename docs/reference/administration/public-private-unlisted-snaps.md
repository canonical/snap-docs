(interfaces-public-private-unlisted-snaps)=
# Public, private and unlisted-snaps

Alongside using [tracks and channels](/) to control which releases are available, and [restrictions per-territory](/t/release-management/12442#heading--distribution), Snap developers can also control _who_ has access to their snaps by marking a published snap as either public, private or unlisted.

When [registering a snap](https://forum.snapcraft.io/t/registering-your-app-name/6793), there is an option to make its listing either public or private. After registration, this value can be changed from the _Settings page_ of the [Snap Store web UI](/)  for the  registered snap:

![Snap Store settings tab](https://assets.ubuntu.com/v1/617fa9e2-private_03.png) 

A snap's  _Visibility_ settings can be one of the following:

- **Unlisted**: the snap is omitted from search results but it can still be installed by any user when they explicitly asks for it by name
- **Public** : the snap will appear in local  `snap find`  searches, in the Snap Store, and other application installers that access the store
- **Private** : the snap is hidden from search results, and can only be installed from your account and from accounts linked to your account

If a previously public snap is made private, installed versions are unaffected. However, those snaps will no longer receive updates, and if the user removes them, they can't be re-installed from the store.

Access to a private snap can be shared by adding individual email addresses to the text field on the _Collaboration_ page of a snap's [dashboard.snapcraft.io](https://dashboard.snapcraft.io/) entry:

![Snap Store private settings](https://assets.ubuntu.com/v1/74e9f011-private_02.png) 

## Visibility from snapcraft

With [Snapcraft](/) installed and logged-in to a developer account, the _snapcraft names_ command can be used to check the visibility status of snaps associated with the developer account:

```
$ snapcraft names
Name             Since                 Visibility    Notes
cameractrls      2022-11-28T18:15:44Z  public        -
domoticz         2020-01-17T17:21:43Z  public        -
```

