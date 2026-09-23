(explanation-security-snapd-release-process)=
# Snapd release process

The snapd release process is maintained in the snapd repository. It is written primarily for release engineers on the snapd team, and it is published for transparency. Carrying out a release requires administrative privileges that most people do not have.

## Release planning

At the start of every six-month cycle, snapd agrees a release plan with stakeholders. The plan gives estimated start and end dates for each release, and those dates determine what the release contains. The process is date-driven: if you want a change in a particular release, it needs to fit that plan.

## Release artifacts

A release produces:

* The [snapd snap](https://snapcraft.io/snapd), as a regular build and a FIPS build
* [snapd Debian packages](https://launchpad.net/ubuntu/+source/snapd/)
* A [GitHub release](https://github.com/canonical/snapd/releases)
* {ref}`Cross-distro artifacts <reference-administration-distribution-support>`

## Security releases

Security releases are prepared in private. They address vulnerabilities identified during routine security scanning and through external reports. To report a suspected vulnerability, see {ref}`How to report vulnerabilities <explanation-security-security-policies-how-to-report-vulnerabilities>`.

## Ubuntu package updates

Updates of the snapd Debian package in Ubuntu follow a package-specific, non-standard Stable Release Update (SRU) process. The [snapd SRU exception] documents where that process deviates from the standard SRU process. A refresh of that documentation is in progress and is expected to become available by November 2026.

## Full process

For the step-by-step release process, follow the instructions in [RELEASE.md].

[snapd SRU exception]: https://documentation.ubuntu.com/sru/en/latest/reference/package-specific/#snapd
[RELEASE.md]: https://github.com/canonical/snapd/blob/master/RELEASE.md
