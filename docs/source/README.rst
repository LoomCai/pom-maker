.. figure:: http://i.imgur.com/vzC5zmA.gif
   :alt: 

SAWS
====

|Build Status| |Documentation Status| |Dependency Status|

|PyPI version| |PyPI| |License|

Motivation
----------

AWS CLI
~~~~~~~

Although the `AWS CLI <https://github.com/aws/aws-cli>`__ is a great
resource to manage your AWS-powered services, it's **tough to remember
usage** of:

-  70+ top-level commands
-  2000+ subcommands
-  Countless command-specific options
-  Resources such as instance tags and buckets

SAWS: A Supercharged AWS CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``SAWS`` aims to **supercharge** the AWS CLI with features focusing on:

-  **Improving ease-of-use**
-  **Increasing productivity**

Under the hood, ``SAWS`` is **powered by the AWS CLI** and supports the
**same commands** and **command structure**.

``SAWS`` and ``AWS CLI`` Usage:

::

    aws <command> <subcommand> [parameters] [options]

``SAWS`` features:

-  Auto-completion of:

   -  Commands
   -  Subcommands
   -  Options

-  Auto-completion of resources:

   -  Bucket names
   -  Instance ids
   -  Instance tags
   -  `More coming soon! <#todo-add-more-resources>`__

-  Customizable shortcuts
-  Fuzzy completion of resources and shortcuts
-  Fish-style auto-suggestions
-  Syntax and output highlighting
-  Execution of shell commands
-  Command history
-  Contextual help
-  Toolbar options

``SAWS`` is available for Mac, Linux, Unix, and
`Windows <#windows-support>`__.

.. figure:: http://i.imgur.com/Eo12q9T.png
   :alt: 

Index
-----

Features
~~~~~~~~

-  `Syntax and Output Highlighting <#syntax-and-output-highlighting>`__
-  `Auto-Completion of Commands, Subcommands, and
   Options <#auto-completion-of-commands-subcommands-and-options>`__
-  `Auto-Completion of AWS
   Resources <#auto-completion-of-aws-resources>`__

   -  `S3 Buckets <#s3-buckets>`__
   -  `EC2 Instance Ids <#ec2-instance-ids>`__
   -  `EC2 Instance Tags <#ec2-instance-tags>`__
   -  `TODO: Add More Resources <#todo-add-more-resources>`__

-  `Customizable Shortcuts <#customizable-shortcuts>`__
-  `Fuzzy Resource and Shortcut
   Completion <#fuzzy-resource-and-shortcut-completion>`__
-  `Fish-Style Auto-Suggestions <#fish-style-auto-suggestions>`__
-  `Executing Shell Commands <#executing-shell-commands>`__
-  `Command History <#command-history>`__
-  `Contextual Help <#contextual-help>`__

   -  `Contextual Command Line Help <#contextual-command-line-help>`__
   -  `Contextual Web Docs <#contextual-web-docs>`__

-  `Toolbar Options <#toolbar-options>`__
-  `Windows Support <#windows-support>`__

Installation and Tests
~~~~~~~~~~~~~~~~~~~~~~

-  `Installation <#installation>`__

   -  `Pip Installation <#pip-installation>`__
   -  `Virtual Environment and Docker
      Installation <#virtual-environment-and-docker-installation>`__
   -  `AWS Credentials and Named
      Profiles <#aws-credentials-and-named-profiles>`__
   -  `Supported Python Versions <#supported-python-versions>`__
   -  `Supported Platforms <#supported-platforms>`__

-  `Developer Installation <#developer-installation>`__

   -  `Continuous Integration <#continuous-integration>`__
   -  `Dependencies Management <#dependencies-management>`__
   -  `Unit Tests and Code Coverage <#unit-tests-and-code-coverage>`__
   -  `Documentation <#documentation>`__

Misc
~~~~

-  `Contributing <#contributing>`__
-  `Credits <#credits>`__
-  `Contact Info <#contact-info>`__
-  `License <#license>`__

Syntax and Output Highlighting
------------------------------

.. figure:: http://i.imgur.com/xQDpw70.png
   :alt: 

You can control which theme to load for syntax highlighting by updating
your
`~/.sawsrc <https://github.com/donnemartin/saws/blob/master/saws/sawsrc>`__
file:

::

    # Visual theme. Possible values: manni, igor, xcode, vim, autumn, vs, rrt,
    # native, perldoc, borland, tango, emacs, friendly, monokai, paraiso-dark,
    # colorful, murphy, bw, pastie, paraiso-light, trac, default, fruity
    theme = vim

Auto-Completion of Commands, Subcommands, and Options
-----------------------------------------------------

``SAWS`` provides smart autocompletion as you type. Entering the
following command will interactively list and auto-complete all
subcommands **specific only** to ``ec2``:

::

    aws ec2

.. figure:: http://i.imgur.com/P2tL9vW.png
   :alt: 

Auto-Completion of AWS Resources
--------------------------------

In addition to the default commands, subcommands, and options the AWS
CLI provides, ``SAWS`` supports auto-completion of your AWS resources.
Currently, bucket names, instance ids, and instance tags are included,
with additional support for more resources `under
development <#todo-add-more-resources>`__.

S3 Buckets
~~~~~~~~~~

Option for ``s3api``:

::

    --bucket

Sample Usage:

::

    aws s3api get-bucket-acl --bucket

Syntax for ``s3``:

::

    s3://

Sample Usage:

::

    aws s3 ls s3://

Note: The example below demonstrates the use of `fuzzy resource
completion <fuzzy-resource-and-shortcutcompletion>`__:

.. figure:: http://i.imgur.com/39CAS5T.png
   :alt: 

EC2 Instance Ids
~~~~~~~~~~~~~~~~

Option for ``ec2``:

::

    --instance-ids

Sample Usage:

::

    aws ec2 describe-instances --instance-ids
    aws ec2 ls --instance-ids

Note: The ``ls`` command demonstrates the use of `customizable
shortcuts <#customizable-shortcuts>`__:

.. figure:: http://i.imgur.com/jFyCSXl.png
   :alt: 

EC2 Instance Tags
~~~~~~~~~~~~~~~~~

Option for ``ec2``:

::

    --ec2-tag-key
    --ec2-tag-value

Sample Usage:

::

    aws ec2 ls --ec2-tag-key
    aws ec2 ls --ec2-tag-value

**Tags support wildcards** with the ``*`` character.

Note: ``ls``, ``--ec2-tag-value``, and ``--ec2-tag-key`` demonstrate the
use of `customizable shortcuts <#customizable-shortcuts>`__:

.. figure:: http://i.imgur.com/VIKwG3Z.png
   :alt: 

TODO: Add More Resources
~~~~~~~~~~~~~~~~~~~~~~~~

Feel free to `submit an issue or a pull request <#contributions>`__ if
you'd like support for additional resources.

Customizable Shortcuts
----------------------

The
`~/.saws.shortcuts <https://github.com/donnemartin/saws/blob/master/saws/saws.shortcuts>`__
file contains shortcuts that you can modify. It comes pre-populated with
several `handy
shortcuts <https://github.com/donnemartin/saws/blob/master/saws/saws.shortcuts>`__
out of the box. You can combine shortcuts with `fuzzy
completion <#fuzzy-resource-and-shortcut-completion>`__ for even less
keystrokes. Below are a few examples.

List all EC2 instances:

::

    aws ec2 ls

List all running EC2 instances:

::

    aws ec2 ls --ec2-state running  # fuzzy shortcut: aws ecstate

.. figure:: http://i.imgur.com/jYFEsoM.png
   :alt: 

List all EC2 instances with a matching tag (supports wildcards ``*``):

::

    aws ec2 ls --ec2-tag-key    # fuzzy shortcut: aws ectagk
    aws ec2 ls --ec2-tag-value  # fuzzy shortcut: aws ectagv

.. figure:: http://i.imgur.com/PSuwUIw.png
   :alt: 

List EC2 instance with matching id:

::

    aws ec2 ls --instance-ids  # fuzzy shortcut: aws eclsi

.. figure:: http://i.imgur.com/wGcUCsa.png
   :alt: 

List all DynamoDB tables:

::

    aws dynamodb ls  # fuzzy shortcut: aws dls

List all EMR clusters:

::

    aws emr ls  # fuzzy shortcut: aws emls

Add/remove/modify shortcuts in your
`~/.saws.shortcuts <https://github.com/donnemartin/saws/blob/master/saws/shortcuts>`__
file to suit your needs.

Feel free to submit:

-  An issue to request additional shortcuts
-  A pull request if you'd like to share your shortcuts (see
   `contributing guidelines <#contributions>`__)

Fuzzy Resource and Shortcut Completion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To toggle fuzzy completion of AWS resources and shortcuts, use ``F3``
key.

Sample fuzzy shortcuts to start and stop EC2 instances:

::

    aws ecstop
    aws ecstart

Note: Fuzzy completion currently only works with AWS
`resources <#auto-completion-of-aws-resources>`__ and
`shortcuts <customizable-shortcuts>`__.

.. figure:: http://i.imgur.com/7OvFHCw.png
   :alt: 

Fish-Style Auto-Suggestions
---------------------------

``SAWS`` supports Fish-style auto-suggestions. Use the ``right arrow``
key to complete a suggestion.

.. figure:: http://i.imgur.com/t5200q1.png
   :alt: 

Executing Shell Commands
------------------------

``SAWS`` allows you to execute shell commands from the ``saws>`` prompt.

.. figure:: http://i.imgur.com/FiSn6b2.png
   :alt: 

Command History
---------------

``SAWS`` keeps track of commands you enter and stores them in
``~/.saws-history``. Use the up and down arrow keys to cycle through the
command history.

.. figure:: http://i.imgur.com/z8RrDQB.png
   :alt: 

Contextual Help
---------------

``SAWS`` supports contextual command line ``help`` and contextual web
``docs``.

Contextual Command Line Help
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``help`` command is powered by the AWS CLI and outputs help within
the command line.

Usage:

::

    aws <command> <subcommand> help

.. figure:: http://i.imgur.com/zSkzt6y.png
   :alt: 

Contextual Web Docs
~~~~~~~~~~~~~~~~~~~

Sometimes you're not quite sure what specific command/subcommand/option
combination you need to use. In such cases, browsing through several
combinations with the ``help`` command line is cumbersome versus
browsing the online AWS CLI docs through a web browser.

``SAWS`` supports contextual web docs with the ``docs`` command or the
``F9`` key. ``SAWS`` will display the web docs specific to the currently
entered command and subcommand.

Usage:

::

    aws <command>