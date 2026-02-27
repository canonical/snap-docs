import datetime
import os
import yaml

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# If you're new to Sphinx and don't want any advanced or custom features,
# just go through the items marked 'TODO'.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Our starter pack uses the custom Canonical Sphinx extension
# to keep all documentation based on it consistent and on brand:
# https://github.com/canonical/canonical-sphinx


#######################
# Project information #
#######################

# Project name
#
# TODO: Update with the official name of your project or product

project = "Snap"
author = "Canonical Ltd."


# Sidebar documentation title; best kept reasonably short
#
# TODO: To include a version number, add it here (hardcoded or automated).
#
# TODO: To disable the title, set to an empty string.

html_title = project + " documentation"


# Copyright string; shown at the bottom of the page
#
# Now, the starter pack uses CC-BY-SA as the license
# and the current year as the copyright year.
#
# TODO: If your docs need another license, specify it instead of 'CC-BY-SA'.
#
# TODO: If your documentation is a part of the code repository of your project,
#       it inherits the code license instead; specify it instead of 'CC-BY-SA'.
#
# NOTE: For static works, it is common to provide the first publication year.
#       Another option is to provide both the first year of publication
#       and the current year, especially for docs that frequently change,
#       e.g. 2022–2023 (note the en-dash).
#
#       A way to check a repo's creation date is to get a classic GitHub token
#       with 'repo' permissions; see https://github.com/settings/tokens
#       Next, use 'curl' and 'jq' to extract the date from the API's output:
#
#       curl -H 'Authorization: token <TOKEN>' \
#         -H 'Accept: application/vnd.github.v3.raw' \
#         https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = "%s CC-BY-SA, %s" % (datetime.date.today().year, author)


# Documentation website URL
#
# TODO: Update with the official URL of your docs or leave empty if unsure.
#
# NOTE: The Open Graph Protocol (OGP) enhances page display in a social graph
#       and is used by social media platforms; see https://ogp.me/

ogp_site_url = "https://snapcraft.io/docs/"


# Preview name of the documentation website
#
# TODO: To use a different name for the project in previews, update as needed.

ogp_site_name = project


# Preview image URL
#
# TODO: To customise the preview image, update as needed.

ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"


# Product favicon; shown in bookmarks, browser tabs, etc.

# TODO: To customise the favicon, uncomment and update as needed.

# html_favicon = '.sphinx/_static/favicon.png'


# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context

html_context = {
    # Product page URL; can be different from product docs URL
    #
    # TODO: Change to your product website URL,
    #       dropping the 'https://' prefix, e.g. 'ubuntu.com/lxd'.
    #
    # TODO: If there's no such website,
    #       remove the {{ product_page }} link from the page header template
    #       (usually .sphinx/_templates/header.html; also, see README.rst).
    "product_page": "snapcraft.io",
    # Product tag image; the orange part of your logo, shown in the page header
    #
    # TODO: To add a tag image, uncomment and update as needed.
    # 'product_tag': '_static/tag.png',
    # Your Discourse instance URL
    #
    # TODO: Change to your Discourse instance URL or leave empty.
    #
    # NOTE: If set, adding ':discourse: 123' to an .rst file
    #       will add a link to Discourse topic 123 at the bottom of the page.
    "discourse": "http://forum.snapcraft.io/",
    # Your Mattermost channel URL
    #
    # TODO: Change to your Mattermost channel URL or leave empty.
    # "mattermost": "https://chat.canonical.com/canonical/channels/documentation",
    # Your Matrix channel URL
    #
    # TODO: Change to your Matrix channel URL or leave empty.
    "matrix": "https://matrix.to/#/#snapd:ubuntu.com",
    # Your documentation GitHub repository URL
    #
    # TODO: Change to your documentation GitHub repository URL or leave empty.
    #
    # NOTE: If set, links for viewing the documentation source files
    #       and creating GitHub issues are added at the bottom of each page.
    "github_url": "https://github.com/canonical/snap-docs",
    # Docs branch in the repo; used in links for viewing the source files
    #
    # TODO: To customise the branch, uncomment and update as needed.
    'repo_default_branch': 'main',
    # Docs location in the repo; used in links for viewing the source files
    #


    # TODO: To customise the directory, uncomment and update as needed.
    "repo_folder": "/docs/",
    # TODO: To enable or disable the Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # "sequential_nav": "both",
    # TODO: To enable listing contributors on individual pages, set to True
    "display_contributors": False,

    # Required for feedback button    
    'github_issues': 'enabled',
}

# TODO: To enable the edit button on pages, uncomment and change the link to a
# public repository on GitHub or Launchpad. Any of the following link domains
# are accepted:
# - https://github.com/example-org/example"
# - https://launchpad.net/example
# - https://git.launchpad.net/example
#
# html_theme_options = {
# 'source_edit_link': 'https://github.com/canonical/sphinx-docs-starter-pack',
# }

# Project slug; see https://meta.discourse.org/t/what-is-category-slug/87897
#
# TODO: If your documentation is hosted on https://docs.ubuntu.com/,
#       uncomment and update as needed.

slug = 'docs'

#######################
# Sitemap configuration: https://sphinx-sitemap.readthedocs.io/
#######################

# Use RTD canonical URL to ensure duplicate pages have a specific canonical URL

html_baseurl = "https://snapcraft.io/docs/"

# sphinx-sitemap uses html_baseurl to generate the full URL for each page:

sitemap_url_scheme = '{link}'

# Include `lastmod` dates in the sitemap:

sitemap_show_lastmod = True


# Default name conflicts with RTD's sitemap generation
# sitemap_filename = "sitemap.xml"

# Exclude generated pages from the sitemap:

sitemap_excludes = [
    '404/',
    'genindex/',
    'search/',
]

# TODO: Add more pages to sitemap_excludes if needed. Wildcards are supported.
#       For example, to exclude module pages generated by autodoc, add '_modules/*'.

#######################
# Template and asset locations
#######################

html_static_path = ["_static"]
templates_path = ["_templates"]

#############
# Redirects #
#############

# To set up redirects: https://documatt.gitlab.io/sphinx-reredirects/usage.html
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

# NOTE: If undefined, set to None, or empty,
#       the sphinx_reredirects extension will be disabled.

redirects = {
   "snapcraft-overview": "https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/",
   "base-snaps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/crafting/specify-a-base/",
   "parts-lifecycle": "https://documentation.ubuntu.com/snapcraft/stable/explanation/parts-lifecycle/",
   "snap-epochs": "https://documentation.ubuntu.com/snapcraft/stable/how-to/crafting/manage-data-compatibility/",
   "adding-global-metadata": "https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/snapcraft-yaml/#reference-snapcraft-yaml-top-level-keys/",
   "adding-parts": "https://documentation.ubuntu.com/snapcraft/stable/reference/parts/parts-and-steps/",
   "architectures": "https://documentation.ubuntu.com/snapcraft/stable/reference/architectures/",
   "build-and-staging-dependencies": "https://documentation.ubuntu.com/snapcraft/stable/how-to/crafting/manage-dependencies/",
   "build-configuration": "https://documentation.ubuntu.com/snapcraft/stable/reference/processes/snap-build-process/",
   "choosing-a-security-model": "https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/anatomy-of-snapcraft-yaml/#confinement",
   "creating-snapcraft-yaml": "https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/",
   "creating-your-developer-account": "https://documentation.ubuntu.com/snapcraft/stable/how-to/publishing/authenticate/",
   "dump-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/dump_plugin/",
   "package-repositories": "https://documentation.ubuntu.com/snapcraft/stable/reference/package-repositories/",
   "nil-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/nil_plugin/",
   "release-management": "https://documentation.ubuntu.com/snapcraft/stable/how-to/publishing/manage-revisions-and-releases/",
   "releasing-your-app": "https://documentation.ubuntu.com/snapcraft/stable/how-to/publishing/publish-a-snap/",
   "robotics": "https://canonical-robotics.readthedocs-hosted.com/en/latest/",
   "ros-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-ros-1-app/",
   "ros-noetic": "https://snapcraft.io/ros-noetic-desktop/",
   "ros2-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-ros-2-app/",
   "ros2-foxy-extension": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/ros-2-extensions/",
   "ros2-humble-extension": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/ros-2-extensions/",
   "ros2-jazzy-extension": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/ros-2-extensions/",
   "snapcraft-extensions": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/#reference-extensions",
   "snapcraft-authentication": "https://documentation.ubuntu.com/snapcraft/stable/how-to/publishing/authenticate/",
   "snapcraft-plugins": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/",
   "snapcraft-yaml-schema": "https://documentation.ubuntu.com/snapcraft/stable/reference/project-file/snapcraft-yaml/",
   "supported-extensions": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/",
   "supported-plugins": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/",
   "store-brand-accounts": "https://documentation.ubuntu.com/core/explanation/stores/brand-accounts/",
   "create-a-new-snap": "https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/",
   "python-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-python-app/",
   "pre-built-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-pre-built-app/",
   "c-c-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-c-or-cpp-app/",
   "go-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-go-app/",
   "java-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-java-app/",
   "node-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-node-app/",
   "electron-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-electron-app/",
   "flutter-applications":  "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-flutter-app/",
   "ruby-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/index.html",
   "rust-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-rust-app/",
   "moos-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-moos-app/",
   "ros-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-ros-1-app/",
   "ros2-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-ros-2-app/",
   "snapd-roadmap": "https://forum.snapcraft.io/t/the-snapd-roadmap/1973",
   "reference/development/registering-your-app-name": "https://documentation.ubuntu.com/snapcraft/latest/how-to/publishing/register-a-snap/",
   "autotools-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/autotools_plugin/",
   "ant-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/ant_plugin/",
   "cmake-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/cmake_plugin/",
   "colcon-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/colcon_plugin/",
   "conda-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/conda_plugin/",
   "flutter-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/flutter_plugin/",
   "go-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/go_plugin/",
   "make-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/make_plugin/",
   "matter-sdk-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/matter_sdk_plugin/",
   "maven-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/maven_plugin/",
   "meson-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/meson_plugin/",
   "npm-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/npm_plugin/",
   "python-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/python_plugin/",
   "rust-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/rust_plugin/",
   "scons-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/scons_plugin/",
   "dotnet-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/dotnet_v2_plugin/",
   "crystal-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/crystal_plugin/",
   "waf-plugin": "https://documentation.ubuntu.com/snapcraft/stable/a/plugins/",
   "writing-local-plugins": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/",
   "ros2-shared-memory-in-snaps": "https://canonical-robotics.readthedocs-hosted.com/en/latest/how-to-guides/packaging/ros-2-shared-memory-in-snaps/",
   "release-notes-snapcraft-3-0": "https://documentation.ubuntu.com/snapcraft/stable/release-notes/",
   "build-options": "https://documentation.ubuntu.com/snapcraft/stable/reference/build-environment-options/",
   "the-cmake-plugin/8621": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/cmake_plugin/",
   "gnome-3-38-extension": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/gnome-extension/",
   "linters-library": "https://documentation.ubuntu.com/snapcraft/stable/reference/linters/",
   "adding-snap-configuration": "https://documentation.ubuntu.com/snapcraft/stable/how-to/crafting/add-a-snap-configuration/",
   "parts-environment-variables": "https://documentation.ubuntu.com/snapcraft/stable/reference/parts/part-environment-variables/",
   "deprecation-notice-10": "https://snapcraft.io/docs/reference/release-notes/",
   "build-snaps/your-first-snap": "https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/",
   "snapcraft-setup": "https://documentation.ubuntu.com/snapcraft/stable/how-to/set-up-snapcraft/",
   "kbuild-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/",
   "release-notes-snapcraft-7-0": "https://documentation.ubuntu.com/snapcraft/stable/release-notes/",
   "build-providers": "https://documentation.ubuntu.com/snapcraft/stable/how-to/select-a-build-provider/",
   "snapcraft-hook-support": "https://documentation.ubuntu.com/snapcraft/stable/reference/hooks/",
   "flutter-extension": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/flutter-extension/",
   "migrate-core22": "https://documentation.ubuntu.com/core/how-to-guides/manage-ubuntu-core/upgrade-ubuntu-core/",
   "qmake-plugin": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/qmake_plugin/",
   "snapcraft-reference": "https://documentation.ubuntu.com/snapcraft/stable/reference/",
   "how-snapcraft-builds": "https://documentation.ubuntu.com/snapcraft/stable/explanation/",
   "snapcraft-build-example": "https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/",
   "release-notes-snapcraft-7-2": "https://documentation.ubuntu.com/snapcraft/stable/release-notes/",
   "snapcraft-filesets": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/explanation/filesets/",
   "deprecation-notices": "https://documentation.ubuntu.com/snapcraft/stable/release-notes/",
   "build-snaps/ruby": "https://documentation.ubuntu.com/snapcraft/stable/common/craft-parts/reference/plugins/ruby_plugin/",
   "deprecation-notice-6": "https://documentation.ubuntu.com/snapcraft/stable/release-notes/",
   "release-notes-snapcraft-4-3": "https://documentation.ubuntu.com/snapcraft/stable/release-notes/",
   "remote-build": "https://documentation.ubuntu.com/snapcraft/stable/reference/commands/remote-build/",
   "how-to-classic": "https://documentation.ubuntu.com/snapcraft/stable/explanation/classic-confinement/",
   "release-notes-snapcraft-4-8": "https://documentation.ubuntu.com/snapcraft/stable/release-notes/",
   "linters": "https://documentation.ubuntu.com/snapcraft/stable/reference/linters/",
   "gtk4-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-gtk4-app/",
   "ros-distributions-with-no-extensions": "https://canonical-robotics.readthedocs-hosted.com/en/latest/how-to-guides/packaging/ros-distributions-with-no-extensions/",
   "qt5-kde-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-qt5-kde-app/",
   "catkin-tools-plugin": "https://documentation.ubuntu.com/snapcraft/stable/reference/plugins/catkin_tools_plugin/",
   "cross-compile-an-autotools-project": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-cross-compiled-app/",
   "kde-neon-extension": "https://documentation.ubuntu.com/snapcraft/stable/reference/extensions/kde-neon-extensions/",
   "snap-store-metrics": "https://documentation.ubuntu.com/snapcraft/stable/reference/metrics/",
   "linters-classic": "https://documentation.ubuntu.com/snapcraft/stable/reference/linters/",
   "env-injector": "https://documentation.ubuntu.com/snapcraft/stable/how-to/extensions/use-the-env-injector-extension/",
   "snapcraft-tutorials": "https://documentation.ubuntu.com/snapcraft/stable/tutorials/",
   "explanation-architectures": "https://documentation.ubuntu.com/snapcraft/stable/explanation/architectures/",
   "ros-troubleshooting": "https://canonical-robotics.readthedocs-hosted.com/en/latest/references/snapcraft/faq/",
   "gtk3-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-gtk3-app/",
   "gtk2-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-gtk2-app/",
   "desktop-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-pre-built-app/",
   "go-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-go-app/#how-to-craft-a-go-app",
   "java-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-java-app/#how-to-craft-a-java-app",
   "moos-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-moos-app/#how-to-craft-a-moos-app",
   "ros-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-ros-1-app/#how-to-craft-an-ros-1-app",
   "ros2-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-ros-2-app/#how-to-craft-an-ros-2-app",
   "ruby-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/",
   "rust-applications": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-rust-app/#how-to-craft-a-rust-app",
   "dotnet-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-dotnet-app/#how-to-craft-a-dotnet-app",
   "pre-built-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-pre-built-app/#how-to-craft-a-pre-built-app",
   "electron-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-an-electron-app/#how-to-craft-an-electron-app",
   "node-apps": "https://documentation.ubuntu.com/snapcraft/stable/how-to/integrations/craft-a-node-app/#how-to-craft-a-node-app"
}

###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
#
# TODO: Remove or adjust the ACME entry after you update the contributing guide

linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://github.com/canonical/ACME/*"
    ]


# A regex list of URLs where anchors are ignored by 'make linkcheck'

linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]

# give linkcheck multiple tries on failure
# linkcheck_timeout = 30
linkcheck_retries = 3

########################
# Configuration extras #
########################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
#
# NOTE: By default, the following MyST extensions are enabled:
#       substitution, deflist, linkify

# myst_enable_extensions = set()


# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html

# NOTE: The canonical_sphinx extension is required for the starter pack.

extensions = [
    "canonical_sphinx",
    "notfound.extension",
    "sphinx_design",
    "sphinx_reredirects",
    "sphinx_tabs.tabs",
    "sphinxcontrib.jquery",
    "sphinxext.opengraph",
    "sphinx_config_options",
    "sphinx_contributor_listing",
    "sphinx_filtered_toctree",
    "sphinx_related_links",
    "sphinx_roles",
    "sphinx_terminal",
    "sphinx_ubuntu_images",
    "sphinx_youtube_links",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "sphinxext.rediraffe",
]

# Excludes files or directories from processing

exclude_patterns = [
    "doc-cheat-sheet*",
]

# Adds custom CSS files, located under 'html_static_path'

html_css_files = ["css/cookie-banner.css"]

# Used for copying OpenAPI HTML file
html_extra_path = ["_html_extra"]

# Add redirects, so they can be updated here to land with docs being moved
rediraffe_branch = "main"
rediraffe_redirects = "redirects.txt"

# Adds custom JavaScript files, located under 'html_static_path'

html_js_files = [
    "js/bundle.js",
    "js/rtd-flyout-overwrite.js"
]


# Specifies a reST snippet to be appended to each .rst file

# rst_epilog = """
# .. include:: /reuse/links.txt
# .. include:: /reuse/substitutions.txt
# """

# Feedback button at the top; enabled by default
#
# TODO: To disable the button, uncomment this.

# disable_feedback_button = True


# Your manpage URL
#
# TODO: To enable manpage links, uncomment and replace {codename} with required
#       release, preferably an LTS release (e.g. noble). Do *not* substitute
#       {section} or {page}; these will be replaced by sphinx at build time
#
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.

# manpages_url = 'https://manpages.ubuntu.com/manpages/{codename}/en/' + \
#     'man{section}/{page}.{section}.html'


# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.

rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2
.. role:: woke-ignore
    :class: woke-ignore
.. role:: vale-ignore
    :class: vale-ignore
"""

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34

if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"

# Workaround for substitutions.yaml

if os.path.exists('./reuse/substitutions.yaml'):
    with open('./reuse/substitutions.yaml', 'r') as fd:
        myst_substitutions = yaml.safe_load(fd.read())

# Suppress missing xref warnings, as these are generated for targets automatically
suppress_warnings = ['myst.xref_missing'] 

