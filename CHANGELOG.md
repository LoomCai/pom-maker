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
* Resolved [#40](https://github.com/donnemartin/saws/issues/40): 