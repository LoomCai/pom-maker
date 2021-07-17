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
            * document: An instance of prompt_toolkit's Document.
            * _: An instance of prompt_toolkit's CompleteEvent (not used).

        Returns:
            A generator of prompt_toolkit's Completion objects, containing
            matched completions.
        """
        # Get completions from the official AWS CLI
        aws_completer_results_list = self._get_aws_cli_completions(document)
        self.aws_completions = set()
        if len(document.text) < len(self.BASE_COMMAND):
            # Autocomplete 'aws' at the beginning of the command
            self.aws_completions.update([self.BASE_COMMAND])
        else:
            self.aws_completions.update(aws_completer_results_list)
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        words = self.text_utils.get_tokens(document.text)
        if len(words) == 0:
            return []
        # Determine if we should insert shortcuts
        elif len(words) == 2 and \
            words[0] == self.BASE_COMMAND and \
                word_before_cursor != '':
            # Insert shortcuts if the user typed 'aws' as the first
            # command and is inputting the subcommand
            if self.shortcut_match:
                self.aws_completions.update(self.shortcuts.keys())
        # Try to get completions for enabled AWS resources
        completions = self._get_custom_completions(
            words, word_before_cursor, self.resources.resources_options_map)
        # Try to get completions for global options, filter options, etc
        if completions is None:
            completions = self._get_custom_completions(
                words, word_before_cursor, self.options.options_map)
        # Try to get completions from the official AWS CLI
        if completions is None:
            fuzzy_aws_completions = self.fuzzy_match
            if self.fuzzy_match and word_before_cursor in \
                    self.all_commands[AwsCommands.CommandType.COMMANDS.value]:
                # Fuzzy completion currently only works with resources, options
                # and shortcuts.  If we have just completed a top-level
                # command (ie. ec2, elb, s3) then disable fuzzy completions,
                # otherwise the corresponding subcommands will be fuzzy
                # completed and incorrectly shown.
                # See: https://github.com/donnemartin/saws/issues/14
                fuzzy_aws_completions = False
            completions = self.text_utils.find_matches(word_before_cursor,
                                                       self.aws_completions,
                                                       fuzzy_aws_completions)
        return completions

    def refresh_resources_and_options(self, force_refresh=False):
        """Convenience function to refresh resources for completion.

        Args:
            * force_refresh: A boolean determines whether to force a cache
                refresh.  This value is set to True when the user presses `F5`.

        Returns:
            None.
        """
        self.resources.refresh(force_refresh)

    def replace_shortcut(self, text):
        """Replaces matched shortcut commands with their full command.

        Currently, only one shortcut is replaced before shortcut replacement
        terminates, although this function could potentially be extended
        to replace mutliple shortcuts.

        Args:
            * text: A string representing the input command text to replace.

        Returns:
            A string representing input command text with a shortcut
                replaced, if one has been found.
        """
        for key, value in self.shortcuts.items():
            if key in text:
                text = re.sub(key, value, text)
                text = self.replace_substitution(text)
                break
        