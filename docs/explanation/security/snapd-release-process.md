(explanation-security-snapd-release-process)=
# Snapd release process

snapd is the background service that manages and maintains your snaps. It is itself delivered either as a snap or as a traditional Linux package, such as a _deb_ or an RPM.

There are two types of release; major and minor release, denoted by a numeric status for their version numbers with a secondary period and number reserved for minor releases:

* major version releases: 2.53, 2.54, 2.55
* minor version releases: 2.53.1, 2.53.2

The difference between a major and minor release is its planning, preparation and motivation. There is a major release cycle every few weeks, but sometimes we need an intermediate minor version release containing smaller changes and fixes.

The differences between a major release and subsequent minor release (eg. 2.53 -> 2.53.1) are as small and targeted as possible, with major code refactoring and new features omitted. This is not always possible, because sometimes bugs or features are complex, but it’s our overarching goal.

Major unit releases, such as between snapd 2.x and 3.x, are extremely rare and no further unit releases are currently planned.

## Step-by-step release process

The following is the typical release process for snapd, starting with creating a release branch and tagging it for release:

1. Code intended for the next version of snapd is merged to the [Master branch](https://github.com/canonical/snapd) on GitHub.
2. For a major release, we create a new branch from master named `release/<VERSION>`, where `<VERSION>` is always the major version number. The eventual major version release tag for a given release is always on this branch, and it’s also where we will tag subsequent minor releases for this major version.
3. If additional code is added to the new version branch, we first ensure that all required submissions are in the `release/VERSION` branch before tagging and signing the tag with the GPG key of one the maintainers of snapd who has permission to create the release.

4. From a release tag, we then build multiple artifacts for snapd for different places, including:

   * Debian packages for the minimal necessary Ubuntu distros in the snappy-dev image PPA. This is because we build both the core snap and the initrd for UC20+ from this PPA. Currently this list of distros simply contains Ubuntu 16.04 LTS (Xenial Xerus) and Ubuntu 20.04 LTS (Focal Fossa).
   * The snapd snap.
   * The core snap.
   * Source tarballs with i) the vendored Go code, ii) without the vendored Go code, and iii) with only the vendored Go code. These are used mostly by other distributions to build their packages of snapd.
   * Other traditional Linux package formats, such as debs for Debian upstream, RPMs for Fedora, and all their derivatives, etc.

5. We then release the core snap and the snapd snap to their respective beta channels.

   We do not release these snaps to their respective edge channels, and we do not release revisions from the edge channel to beta or higher channels. For our releases, channels have specific purposes, such that a revision of the snap that goes into the edge channel will never go into the beta/candidate/stable channels, and vice versa.

6. Automated tests are now run and we will put out an internal Canonical call for testing for the new version of snapd.
7. If no problems are found from the automated testing, we leave the snapd and core snaps in the beta channel for at least 2 weeks.
8. After this beta testing period, we move the snap to its candidate channel.
9. If the community and teams report positively on the candidate release, it’s released progressively to the stable channel.

   A release is almost always finalised for release on a Monday or Tuesday. This optimises bandwidth and allows for a deployment to be halted if problems are encountered by users who get the snap early.

10. We now start the SRU process to release an updated version of the Debian package of snapd to Ubuntu releases in the main archive, including doing ESM builds/uploads as necessary.

## Version number mapping

The version number of the snapd snap in its stable channel will always map 1:1 with the version number of a released revision of the snapd or core snap.

For example, the git tag [2.51.1](https://github.com/canonical/snapd/releases/tag/2.51.1), will only have a single revision published to the stable channel with this version number.

This single revision per version number policy helps simplify debugging, where the output of the snap version command enables us to isolate the revision of the snapd or core snaps that correspond to the version that was released.

However, the edge channel version number of the snapd snap does not map 1:1 with a single revision. Instead, the version number includes the git commit that the snap was built from, such as `2.53.1+git563.g5297d66`, making it easier to track a release to the git commit an edge revision was built from.

The version number of the core snap released to the edge channel is slightly more complicated, as the git commit it displays is the commit of the snapd-vendor project in launchpad, which includes the snapd source code and the vendored Go dependencies.

## Release stability and planning

For production use, the edge channel is not recommended. Functionality may break in unstable ways that may not be upgradeable between one release and the next. A stable channel release, by comparison, will remain backwards compatible with the previous release to the extent that we are technically able to while still fixing bugs or security issues.

Occasionally, when we’re not ready for a major or minor release but need to deploy a fix for a specific issue, we will build a specific branch release and share this with whoever may be affected. This branch release will usually be closed after a fix has been confirmed, landed in master, and released to the stable channel.

Unlike some projects, we do not have a specific “code freeze” where nothing unplanned can be added or removed from a release. Instead, pull requests intended for the next release are tagged to set an appropriate milestone and marked as blocked. This prohibits them from being accidentally merged into the wrong release branch, or before the next major release branch has been created.

After a release branch has been created, we usually try to tag the release as soon as possible. As mentioned earlier, sometimes new bugs need to be fixed, or features added. After merging to master, these are backported into the release branch. We may cherry-pick commits from master onto the release branch before tagging the release on the release branch.

However after a release has been tagged, we will never re-tag it. Instead, if an issue is found that prevents its actual stable release, we will create a new subsequent minor release tag. For example, if a bug was found in a beta release of 2.54, it would never reach the stable channel. Version 2.54.1 would become the first 2.54 release in the stable channel instead.

If you are curious about what new features are included in the next major release of snapd, you can look at the roadmap page here: [https://snapcraft.io/docs/snapd-roadmap](https://snapcraft.io/docs/snapd-roadmap). The timelines for future releases on that page should not be relied on for anything, they are simply estimates. The dates given for already released versions of snapd should be exact and refer to the major version, not to any associated minor versions (since minor releases generally do not include new features, only bug fixes or very small and targeted features).

The best way to determine when the next version of snapd will be released is to reach out to us on IRC or the forum and we will provide you with the best estimate we can at the time.

