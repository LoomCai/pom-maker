
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