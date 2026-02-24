(how-to-guides-fix-common-issues-test-snapd-fixes)=
# Test snapd fixes

The snap daemon, _snapd_, is the background service that manages and maintains your snaps.

Occasionally, _snapd_ may develop an issue or bug that is only apparent on specific devices or in specific circumstances. A fix will be developed as soon as possible, but we may need to test a fix on those devices or installations before it can be merged and more widely distributed.

In such cases, a patched _snapd_ can be provided via a pull request and installed by those affected so they can report on whether it solves the original issue. This process is outlined below.

## Access GitHub

The snap daemon, and its associated tools and projects are hosted on [GitHub](https://github.com/). The [snapd repository](https://github.com/canonical/snapd) contains all the branches, pull requests, automated tests and discussions applicable to _snapd_.

A fix will typically be contained within a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) prior to it being merged. The _snapd_ repository is configured to automatically test and build an approved pull request, creating what is called an _artifact_ that can be downloaded and tested locally.

A test release, especially from a pull request, should only be installed in a test environment as its behaviour could obviously be unpredictable. To install a test release, you will first need a GitHub account and you will need to be logged in from your favourite web browser.

## Locate the pull request

This location of the pull request will usually have been communicated separately, but open pull requests can be found linked to from the _snapd_ repository ([https://github.com/canonical/snapd/pulls](https://github.com/canonical/snapd/pulls)). Each pull request has a unique number identifier, such as `#11085`.

With the pull request opened in your web browser, select the _Checks_ tab. This contains the output from the automated tests and build processes initiated when an approved pull request is created or updated. If a pull request has only recently been submitted or updated, it can take some time for this page to become fully populated.

![image|669x453](/images/access-github.png)

## Download the artifact

Select _Tests_ from the menu on the left. This will take you to the _Actions_ tab for the snapd repository showing the test runs for the previously selected pull request. Scroll to the bottom of this list and you'll see the _artifacts_ section containing a link to the downloadable `snap-files` zip archive (GitHub stores build logs and artifacts for 90 days):

![image|669x453](/images/download-artefact.png)

Click on _snap-files_ to download the archive.

## Install the test version

First, unzip the file we downloaded:

```
$ unzip snap-files.zip
Archive:  snap-files.zip
  inflating: snapd_2.53.2+git6345be5.6345be5-dirty_amd64.snap
```

This resultant snap for the specific pull request we selected earlier can now be installed with snap's [dangerous mode](/explanation/snap-development/install-modes.md#dangerous-mode):

```
$ snap install --dangerous snapd_2.53.2+git6345be5.6345be5-dirty_amd64.snap
2021-11-24T13:06:46Z INFO Waiting for automatic snapd restart...
snapd 2.53.2+git6345be5.6345be5-dirty installed
```

At this point, the fix for the issue or bug can now be tested and the results reported.

To revert the local installation to an official _snapd_ release, simply refresh the _snapd_ snap to its stable channel:

```
$ snap refresh snapd --stable --amend
```
