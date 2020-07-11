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
~~