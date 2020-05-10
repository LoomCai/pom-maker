
![](http://i.imgur.com/vzC5zmA.gif)

SAWS
============

[![Build Status](https://travis-ci.org/donnemartin/saws.svg?branch=master)](https://travis-ci.org/donnemartin/saws) [![Documentation Status](https://readthedocs.org/projects/saws/badge/?version=latest)](http://saws.readthedocs.org/en/latest/?badge=latest) [![Dependency Status](https://gemnasium.com/donnemartin/saws.svg)](https://gemnasium.com/donnemartin/saws)

[![PyPI version](https://badge.fury.io/py/saws.svg)](http://badge.fury.io/py/saws) [![PyPI](https://img.shields.io/pypi/pyversions/saws.svg)](https://pypi.python.org/pypi/saws/) [![License](http://img.shields.io/:license-apache-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)

## Motivation

### AWS CLI

Although the [AWS CLI](https://github.com/aws/aws-cli) is a great resource to manage your AWS-powered services, it's **tough to remember usage** of:

* 70+ top-level commands
* 2000+ subcommands
* Countless command-specific options
* Resources such as instance tags and buckets

### SAWS: A Supercharged AWS CLI

`SAWS` aims to **supercharge** the AWS CLI with features focusing on:

* **Improving ease-of-use**
* **Increasing productivity**

Under the hood, `SAWS` is **powered by the AWS CLI** and supports the **same commands** and **command structure**.

`SAWS` and `AWS CLI` Usage:

    aws <command> <subcommand> [parameters] [options]

`SAWS` features:

* Auto-completion of:
    * Commands
    * Subcommands
    * Options
* Auto-completion of resources:
    * Bucket names
    * Instance ids
    * Instance tags
    * [More coming soon!](#todo-add-more-resources)
* Customizable shortcuts
* Fuzzy completion of resources and shortcuts
* Fish-style auto-suggestions
* Syntax and output highlighting
* Execution of shell commands
* Command history
* Contextual help
* Toolbar options

`SAWS` is available for Mac, Linux, Unix, and [Windows](#windows-support).

![](http://i.imgur.com/Eo12q9T.png)

## Index

### Features

* [Syntax and Output Highlighting](#syntax-and-output-highlighting)
* [Auto-Completion of Commands, Subcommands, and Options](#auto-completion-of-commands-subcommands-and-options)
* [Auto-Completion of AWS Resources](#auto-completion-of-aws-resources)
    * [S3 Buckets](#s3-buckets)
    * [EC2 Instance Ids](#ec2-instance-ids)
    * [EC2 Instance Tags](#ec2-instance-tags)
    * [TODO: Add More Resources](#todo-add-more-resources)
* [Customizable Shortcuts](#customizable-shortcuts)
* [Fuzzy Resource and Shortcut Completion](#fuzzy-resource-and-shortcut-completion)
* [Fish-Style Auto-Suggestions](#fish-style-auto-suggestions)
* [Executing Shell Commands](#executing-shell-commands)
* [Command History](#command-history)
* [Contextual Help](#contextual-help)
    * [Contextual Command Line Help](#contextual-command-line-help)
    * [Contextual Web Docs](#contextual-web-docs)
* [Toolbar Options](#toolbar-options)
* [Windows Support](#windows-support)

### Installation and Tests

* [Installation](#installation)
    * [Pip Installation](#pip-installation)
    * [Virtual Environment and Docker Installation](#virtual-environment-and-docker-installation)
    * [AWS Credentials and Named Profiles](#aws-credentials-and-named-profiles)
    * [Supported Python Versions](#supported-python-versions)
    * [Supported Platforms](#supported-platforms)
* [Developer Installation](#developer-installation)
    * [Continuous Integration](#continuous-integration)
    * [Dependencies Management](#dependencies-management)
    * [Unit Tests and Code Coverage](#unit-tests-and-code-coverage)
    * [Documentation](#documentation)

### Misc

* [Contributing](#contributing)
* [Credits](#credits)
* [Contact Info](#contact-info)
* [License](#license)

## Syntax and Output Highlighting

![](http://i.imgur.com/xQDpw70.png)

You can control which theme to load for syntax highlighting by updating your [~/.sawsrc](https://github.com/donnemartin/saws/blob/master/saws/sawsrc) file:

```
# Visual theme. Possible values: manni, igor, xcode, vim, autumn, vs, rrt,
# native, perldoc, borland, tango, emacs, friendly, monokai, paraiso-dark,
# colorful, murphy, bw, pastie, paraiso-light, trac, default, fruity
theme = vim
```

## Auto-Completion of Commands, Subcommands, and Options

`SAWS` provides smart autocompletion as you type.  Entering the following command will interactively list and auto-complete all subcommands **specific only** to `ec2`:

    aws ec2

![](http://i.imgur.com/P2tL9vW.png)

## Auto-Completion of AWS Resources

In addition to the default commands, subcommands, and options the AWS CLI provides, `SAWS` supports auto-completion of your AWS resources.  Currently, bucket names, instance ids, and instance tags are included, with additional support for more resources [under development](#todo-add-more-resources).

### S3 Buckets

Option for `s3api`:

    --bucket

Sample Usage:

    aws s3api get-bucket-acl --bucket

Syntax for `s3`:

    s3://

Sample Usage:

    aws s3 ls s3://

Note:  The example below demonstrates the use of [fuzzy resource completion](fuzzy-resource-and-shortcutcompletion):

![](http://i.imgur.com/39CAS5T.png)

### EC2 Instance Ids

Option for `ec2`:

    --instance-ids

Sample Usage:

    aws ec2 describe-instances --instance-ids
    aws ec2 ls --instance-ids

Note:  The `ls` command demonstrates the use of [customizable shortcuts](#customizable-shortcuts):

![](http://i.imgur.com/jFyCSXl.png)

### EC2 Instance Tags

Option for `ec2`:

    --ec2-tag-key
    --ec2-tag-value

Sample Usage:

    aws ec2 ls --ec2-tag-key
    aws ec2 ls --ec2-tag-value

**Tags support wildcards** with the `*` character.

Note:  `ls`, `--ec2-tag-value`, and `--ec2-tag-key` demonstrate the use of [customizable shortcuts](#customizable-shortcuts):

![](http://i.imgur.com/VIKwG3Z.png)

### TODO: Add More Resources

Feel free to [submit an issue or a pull request](#contributions) if you'd like support for additional resources.

## Customizable Shortcuts

The [~/.saws.shortcuts](https://github.com/donnemartin/saws/blob/master/saws/saws.shortcuts) file contains shortcuts that you can modify.  It comes pre-populated with several [handy shortcuts](https://github.com/donnemartin/saws/blob/master/saws/saws.shortcuts) out of the box.  You can combine shortcuts with [fuzzy completion](#fuzzy-resource-and-shortcut-completion) for even less keystrokes.  Below are a few examples.

List all EC2 instances:

    aws ec2 ls

List all running EC2 instances:

    aws ec2 ls --ec2-state running  # fuzzy shortcut: aws ecstate

![](http://i.imgur.com/jYFEsoM.png)

List all EC2 instances with a matching tag (supports wildcards `*`):

    aws ec2 ls --ec2-tag-key    # fuzzy shortcut: aws ectagk
    aws ec2 ls --ec2-tag-value  # fuzzy shortcut: aws ectagv

![](http://i.imgur.com/PSuwUIw.png)

List EC2 instance with matching id:

    aws ec2 ls --instance-ids  # fuzzy shortcut: aws eclsi

![](http://i.imgur.com/wGcUCsa.png)

List all DynamoDB tables:

    aws dynamodb ls  # fuzzy shortcut: aws dls

List all EMR clusters:

    aws emr ls  # fuzzy shortcut: aws emls
