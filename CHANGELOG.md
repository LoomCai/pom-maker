![](http://i.imgur.com/vzC5zmA.gif)

[![Build Status](https://travis-ci.org/donnemartin/saws.svg?branch=master)](https://travis-ci.org/donnemartin/saws) [![Documentation Status](https://readthedocs.org/projects/saws/badge/?version=latest)](http://saws.readthedocs.org/en/latest/?badge=latest) [![Dependency Status](https://gemnasium.com/donnemartin/saws.svg)](https://gemnasium.com/donnemartin/saws)

[![PyPI version](https://badge.fury.io/py/saws.svg)](http://badge.fury.io/py/saws) [![PyPI](https://img.shields.io/pypi/pyversions/saws.svg)](https://pypi.python.org/pypi/saws/) [![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)

SAWS
====

To view the latest `README`, `docs`, and `code` visit the GitHub repo:

https://github.com/donnemartin/saws

To submit bugs or feature requests, visit the issue tracker:

https://github.com/donnemartin/saws/issues

Changelog
=========

0.4.2 (2017-04-08)
------------------

### Bug Fixes

* [#90](https://github.com/donnemartin/saws/pull/90) - Fix `Sphinx` document generation issues.

### Updates

* Update list of commands.
* [#92](https://github.com/donnemartin/saws/pull/92) - Update `feed_key to feed and process_keys for `prompt-toolkit` v1.0.1+.

0.4.1 (2015-05-31)
------------------

### Bug Fixes

* [#83](https://github.com/donnemartin/saws/pull/83) - Update to `prompt-toolkit` 1.0.0, which includes a number of performance improvements (especially noticeable on Windows) and bug fixes.

### Updates

* [#75](https://github.com/donnemartin/saws/pull/75), [#76](https://github.com/donnemartin/saws/pull/76) - Fix groff install and follow Dockerfile best practices.
* [#85](https://github.com/donnemartin/saws/pull/85) - Update packaging dependencies based on semantic versioning.
* [#86](https://github.com/donnemartin/saws/pull/86) - Fix linter issues regarding imports.
* Update list of commands.
* Update INSTALLATION:
    * Add install from SOURCE.
    * Add note about OS X 10.11 pip issue (now also in README).
    * Update intro.
* Update link to style guide in CONTRIBUTING.

0.4.0 (2015-12-08)
------------------

### Features

* Implemented [#67](https://github.com/donnemartin/saws/issues/67): Add Fish-style auto suggestions.

### Bug Fixes

* Fixed [#71](https://github.com/donnemartin/saws/issues/71): Disable color output for shell commands.
* Fixed [#72](https://github.com/donnemartin/saws/issues/72): Exiting with `F10` does not clear the menu bar.

### Updates

* Updated list of commands.
* Updated repo `README`.
    * Added auto suggestions.
* Fixed [#66](https://github.com/donnemartin/saws/issues/38): Removed `docs/build` from source repo.

0.3.2 (2015-10-16)
------------------

### Features

* Resolved [#38](https://github.com/donnemartin/saws/issues/38): Added `Docker` installation support, by [frosforever](https://github.com/frosforever).
* Resolved [#39](https://github.com/donnemartin/saws/issues/39): Changed completion matching to ignore case.
* Resolved [#40](https://github.com/donnemartin/saws/issues/40): Added `emr --cluster-states` completions.
* Resolved [#52](https://github.com/donnemartin/saws/issues/52) and [#58](https://github.com/donnemartin/saws/issues/58): Updated list of auto-completed commands and subcommands.
* Resolved [#53](https://github.com/donnemartin/saws/issues/53): Moved shortcuts out of `~/.sawsrc` to a new file `~/.saws.shortcuts` to simplify managing shortcuts.

### Bug Fixes

* Fixed [#22](https://github.com/donnemartin/saws/issues/22) and [#26](https://github.com/donnemartin/saws/issues/26):
    * `ordereddict` is now only installed with Python 2.6.
    * `enum34` is now only installed with Python 3.3 and below.
* Fixed [#29](https://github.com/donnemartin/saws/issues/29): `SAWS` is now compatible with  `prompt_toolkit` version 0.52, by [jonathanslenders](https://github.com/jonathanslenders).
* Fixed [#33](https://github.com/donnemartin/saws/issues/29): `SAWS` will no longer exit on keyboard interrupt such as `Ctrl-C`, which can be useful to terminate long-running `aws-cli` commands.
* Fixed [#35](https://github.com/donnemartin/saws/issues/35): Grep now works consistently with shortcuts, by [mlimaloureiro](https://github.com/mlimaloureiro).
* Fixed [#41](https://github.com/donnemartin/saws/issues/41): Blank entry is no longer shown in list of completion if there is no optional value set for a given tag's key.
* Fixed [#60](https://github.com/donnemartin/saws/issues/60): Running an empty command no longer results in a pygmentize syntax error.
* Fixed [#61](https://github.com/donnemartin/saws/issues/61): Refreshing resources multiple times no longer results in an exception.

### Updates

* Added PyPI keywords for easier searching.
* Updated PyPI `README`.
    * Added GitHub repo link, issue tracker, and repo gif.
* Added `INSTALLATION` doc, with the following updates:
    * Added `virtualenv` installation section.
    * Added `Pipsi` installation section [#44](https://github.com/donnemartin/saws/issues/44), by [svieira](https://github.com/svieira).
    * Added `Docker` installation section [#38](https://github.com/donnemartin/saws/issues/38), by [frosforever](https://github.com/frosforever).
* Updated repo `README`.
    * Updated discussion of shortcuts with the new `~/.saws.shortcuts` file.
    * Added Command History section.
    * Updated AWS Credentials and Named Profiles s