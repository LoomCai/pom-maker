
.. figure:: http://i.imgur.com/vzC5zmA.gif
   :alt: 

|Build Status| |Documentation Status| |Dependency Status|

|PyPI version| |PyPI| |License|

SAWS
====

To view the latest ``README``, ``docs``, and ``code`` visit the GitHub
repo:

https://github.com/donnemartin/saws

To submit bugs or feature requests, visit the issue tracker:

https://github.com/donnemartin/saws/issues

Changelog
=========

0.4.2 (2017-04-08)
------------------

Bug Fixes
~~~~~~~~~

-  `#90 <https://github.com/donnemartin/saws/pull/90>`__ - Fix
   ``Sphinx`` document generation issues.

Updates
~~~~~~~

-  Update list of commands.
-  `#92 <https://github.com/donnemartin/saws/pull/92>`__ - Update
   ``feed_key to feed and process_keys for``\ prompt-toolkit\` v1.0.1+.

0.4.1 (2015-05-31)
------------------

Bug Fixes
~~~~~~~~~

-  `#83 <https://github.com/donnemartin/saws/pull/83>`__ - Update to
   ``prompt-toolkit`` 1.0.0, which includes a number of performance
   improvements (especially noticeable on Windows) and bug fixes.

Updates
~~~~~~~

-  `#75 <https://github.com/donnemartin/saws/pull/75>`__,
   `#76 <https://github.com/donnemartin/saws/pull/76>`__ - Fix groff
   install and follow Dockerfile best practices.
-  `#85 <https://github.com/donnemartin/saws/pull/85>`__ - Update
   packaging dependencies based on semantic versioning.
-  `#86 <https://github.com/donnemartin/saws/pull/86>`__ - Fix linter
   issues regarding imports.
-  Update list of commands.
-  Update INSTALLATION:

   -  Add install from SOURCE.
   -  Add note about OS X 10.11 pip issue (now also in README).
   -  Update intro.

-  Update link to style guide in CONTRIBUTING.

0.4.0 (2015-12-08)
------------------

Features
~~~~~~~~

-  Implemented `#67 <https://github.com/donnemartin/saws/issues/67>`__:
   Add Fish-style auto suggestions.

Bug Fixes
~~~~~~~~~

-  Fixed `#71 <https://github.com/donnemartin/saws/issues/71>`__:
   Disable color output for shell commands.
-  Fixed `#72 <https://github.com/donnemartin/saws/issues/72>`__:
   Exiting with ``F10`` does not clear the menu bar.

Updates
~~~~~~~

-  Updated list of commands.
-  Updated repo ``README``.

   -  Added auto suggestions.

-  Fixed `#66 <https://github.com/donnemartin/saws/issues/38>`__:
   Removed ``docs/build`` from source repo.

0.3.2 (2015-10-16)
------------------

Features
~~~~~~~~

-  Resolved `#38 <https://github.com/donnemartin/saws/issues/38>`__:
   Added ``Docker`` installation support, by
   `frosforever <https://github.com/frosforever>`__.
-  Resolved `#39 <https://github.com/donnemartin/saws/issues/39>`__:
   Changed completion matching to ignore case.
-  Resolved `#40 <https://github.com/donnemartin/saws/issues/40>`__:
   Added ``emr --cluster-states`` completions.
-  Resolved `#52 <https://github.com/donnemartin/saws/issues/52>`__ and
   `#58 <https://github.com/donnemartin/saws/issues/58>`__: Updated list
   of auto-completed commands and subcommands.
-  Resolved `#53 <https://github.com/donnemartin/saws/issues/53>`__:
   Moved shortcuts out of ``~/.sawsrc`` to a new file
   ``~/.saws.shortcuts`` to simplify managing shortcuts.

Bug Fixes
~~~~~~~~~

-  Fixed `#22 <https://github.com/donnemartin/saws/issues/22>`__ and
   `#26 <https://github.com/donnemartin/saws/issues/26>`__:

   -  ``ordereddict`` is now only installed with Python 2.6.
   -  ``enum34`` is now only installed with Python 3.3 and below.

-  Fixed `#29 <https://github.com/donnemartin/saws/issues/29>`__:
   ``SAWS`` is now compatible with ``prompt_toolkit`` version 0.52, by
   `jonathanslenders <https://github.com/jonathanslenders>`__.
-  Fixed `#33 <https://github.com/donnemartin/saws/issues/29>`__:
   ``SAWS`` will no longer exit on keyboard interrupt such as
   ``Ctrl-C``, which can be useful to terminate long-running ``aws-cli``
   commands.
-  Fixed `#35 <https://github.com/donnemartin/saws/issues/35>`__: Grep
   now works consistently with shortcuts, by
   `mlimaloureiro <https://github.com/mlimaloureiro>`__.
-  Fixed `#41 <https://github.com/donnemartin/saws/issues/41>`__: Blank
   entry is no longer shown in list of completion if there is no
   optional value set for a given tag's key.
-  Fixed `#60 <https://github.com/donnemartin/saws/issues/60>`__:
   Running an empty command no longer results in a pygmentize syntax
   error.
-  Fixed `#61 <https://github.com/donnemartin/saws/issues/61>`__: