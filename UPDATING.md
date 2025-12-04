<!--
    SPDX-FileCopyrightText: 2025 Canonical Ltd
    SPDX-License-Identifier: GPL-3.0-only
-->

# Updating Read The Docs integration
In order to update the Read The Docs (RTD) project, there are a series of steps
that must be performed to ensure the changes are present and consistent between
the hosted and local builds of the project.

## Local build process
The local build process should be triggered using `make run` in the `docs`
project directory. The Makefile orchestrates the build process, serves the
webpage, and provides checks for many different compliance metrics. To view a
list of supported compliance checks run `make` without arguments.
- `conf.py` - Used by the Sphinx document generator to configure the build
    process. Configures the context for the HTML page. The metadata for this
    project has not been configured yet.
- `pre-build-job.sh` - Used with Sphinx to create a standard set of actions that
    are run before every build. For the Snap project, this script gets the
    latest build artifacts from
    [snapd-rest-openapi](https://github.com/canonical/snapd-rest-openapi) and
    places them in a directory that Sphinx has been configured to include in the
    build process.

## Read The Docs Build Process
Since the RTD build process uses a hosted environment, configuration is done via
files located in the GitHub repository. The following file is used for exclusive
modifications to the RTD build process:
- `.readthedocs.yaml` - Used by RTD to control the build process. This file
    contains information necessary for environment setup, and allows for
    configuring the build jobs that sphinx uses.

For the Snap documentation use case, we are interacting with actions in other
GitHub repositories, requiring the use of the `gh` command line tool. To prevent
any issues with rate limiting on the RTD build servers, a token is configured in
the RTD project settings, which is only accessible by organization admins. The
token is assigned to an environment variable prior to launching the
pre-build-job, and upon running `gh` will read this token and use it to
authenticate with GitHub.

The hosted build process is handled remotely by RTD, with little intervention
allowed outside the GitHub repository, according to the following workflow:
1. Upon a pull request being merged to the main repo, RTD detects changes have
    been made and checks out the latest commit.
2. The build process begins and a console output is available via the
    [RTD Webpage](https://app.readthedocs.com/projects/canonical-snap/).
    The build takes approximately 20 minutes.
3. If the build process is successful, the generated documentation will be
    hosted [here](https://canonical-snap.readthedocs-hosted.com/).