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

   -  C