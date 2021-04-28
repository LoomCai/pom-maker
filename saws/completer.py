# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from __future__ import unicode_literals
from __future__ import print_function
import re
import sys
import traceback
from six.moves import cStringIO
from prompt_toolkit.completion import Completer
from .utils import TextUtils
from .commands import AwsCommands
from .options import AwsOptions
from .resources import AwsResources


class AwsCompleter(Completer):
    """Completer for AWS commands, subcommands, options, and parameters.

    Attributes:
        * aws_completer: An instance of the official awscli Completer.
        * aws_completions: A set of completions to show the user.
        * all_commands: A list of all commands, sub_commands, options, etc
            from data/SOURCES.txt.
        * config: An instance of Config.
        * config_obj: An instance of ConfigObj, reads from ~/.sawsrc.
        * log_exception: A callable log_exception from SawsLogger.
        * text_utils: An instance of TextUtils.
        * fuzzy_match: A boolean that determines whether to use fuzzy matching.
        * shortcut_match: A boolean that determines whether to match shortcuts.
        * BASE_COMMAND: A string representing the 'aws' command.
        * shortcuts: An OrderedDict containing shortcuts commands as keys
            and their corresponding full commands as values.
        * resources: An instance of AwsResources.
        * options: An instance of AwsOptions
    """

    def __init__(self,
                 aws_completer,
                 all_commands,
                 config,
                 config_obj,
                 log_exception,
                 fuzzy_match=False,
                 shortcut_match=False):
        """Initializes AwsCompleter.

        Args:
            * aws_completer: The official aws cli completer module.
            * all_commands: A list of all commands, sub_commands, options, etc
                from data/SOURCES.txt.
            * config: An instance of Config.
            * config_obj: An instance of ConfigObj, reads from ~/.sawsrc.
            * log_exception: A callable log_exception from SawsLogger.
            * fuzzy_match: A boolean that determines whether to use
                fuzzy matching.
            * shortcut_match: A boolean that determines whether to
                match shortcuts.

        Returns:
            None.
        """
        self.aws_completer = aws_completer
        self.aws_completions = set()
        self.all_commands = all_commands
        self.config = config
        self.config_obj = config_obj
        self.log_exception = log_exception
        self.text_utils = TextUtils()
        self.fuzzy_match = fuzzy_match
        self.shortcut_match = shortcut_match
        self.BASE_COMMAND = AwsCommands.AWS_COMMAND
        self.shortcuts = self.config.get_shortcuts(config_obj)
        self.resources = AwsResources(self.log_exception)
        self.options = AwsOptions(self.all_commands)

    def get_completions(self, document, _):
        """Get completions for the current scope.

        Args:
            * document: An instan