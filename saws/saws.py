
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
import click
import os
import platform
import subprocess
import traceback
import webbrowser
from prompt_toolkit import AbortAction, Application, CommandLineInterface
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.filters import Always, HasFocus, IsDone
from prompt_toolkit.interface import AcceptAction
from prompt_toolkit.layout.processors import \
    HighlightMatchingBracketProcessor, ConditionalProcessor
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.shortcuts import create_default_layout, create_eventloop
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding.input_processor import KeyPress
from prompt_toolkit.keys import Keys
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from awscli import completer as awscli_completer
from .completer import AwsCompleter
from .lexer import CommandLexer
from .config import Config
from .style import StyleFactory
from .keys import KeyManager
from .toolbar import Toolbar
from .commands import AwsCommands
from .logger import SawsLogger
from .__init__ import __version__


class Saws(object):
    """Encapsulates the Saws CLI.

    Attributes:
        * aws_cli: An instance of prompt_toolkit's CommandLineInterface.
        * key_manager: An instance of KeyManager.
        * config: An instance of Config.
        * config_obj: An instance of ConfigObj, reads from ~/.sawsrc.
        * theme: A string representing the lexer theme.
        * logger: An instance of SawsLogger.
        * all_commands: A list of all commands, sub_commands, options, etc
            from data/SOURCES.txt.
        * commands: A list of commands from data/SOURCES.txt.
        * sub_commands: A list of sub_commands from data/SOURCES.txt.
        * completer: An instance of AwsCompleter.
    """

    PYGMENTS_CMD = ' | pygmentize -l json'

    def __init__(self, refresh_resources=True):
        """Inits Saws.

        Args:
            * refresh_resources: A boolean that determines whether to
                refresh resources.

        Returns:
            None.
        """
        self.aws_cli = None
        self.key_manager = None
        self.config = Config()
        self.config_obj = self.config.read_configuration()
        self.theme = self.config_obj[self.config.MAIN][self.config.THEME]
        self.logger = SawsLogger(
            __name__,
            self.config_obj[self.config.MAIN][self.config.LOG_FILE],
            self.config_obj[self.config.MAIN][self.config.LOG_LEVEL]).logger
        self.all_commands = AwsCommands().all_commands
        self.commands = \
            self.all_commands[AwsCommands.CommandType.COMMANDS.value]
        self.sub_commands = \
            self.all_commands[AwsCommands.CommandType.SUB_COMMANDS.value]
        self.completer = AwsCompleter(
            awscli_completer,
            self.all_commands,
            self.config,
            self.config_obj,
            self.log_exception,
            fuzzy_match=self.get_fuzzy_match(),
            shortcut_match=self.get_shortcut_match())
        if refresh_resources:
            self.completer.refresh_resources_and_options()
        self._create_cli()

    def log_exception(self, e, traceback, echo=False):
        """Logs the exception and traceback to the log file ~/.saws.log.

        Args:
            * e: A Exception that specifies the exception.
            * traceback: A Traceback that specifies the traceback.
            * echo: A boolean that specifies whether to echo the exception
                to the console using click.

        Returns:
            None.
        """
        self.logger.debug('exception: %r.', str(e))
        self.logger.error("traceback: %r", traceback.format_exc())
        if echo:
            click.secho(str(e), fg='red')

    def set_color(self, color):
        """Setter for color output mode.

        Used by prompt_toolkit's KeyBindingManager.
        KeyBindingManager expects this function to be callable so we can't use
        @property and @attrib.setter.

        Args:
            * color: A boolean that represents the color flag.

        Returns:
            None.
        """
        self.config_obj[self.config.MAIN][self.config.COLOR] = color

    def get_color(self):
        """Getter for color output mode.

        Used by prompt_toolkit's KeyBindingManager.
        KeyBindingManager expects this function to be callable so we can't use
        @property and @attrib.setter.

        Args:
            * None.

        Returns:
            A boolean that represents the color flag.
        """
        return self.config_obj[self.config.MAIN].as_bool(self.config.COLOR)

    def set_fuzzy_match(self, fuzzy):
        """Setter for fuzzy matching mode

        Used by prompt_toolkit's KeyBindingManager.
        KeyBindingManager expects this function to be callable so we can't use
        @property and @attrib.setter.

        Args:
            * color: A boolean that represents the fuzzy flag.

        Returns:
            None.
        """
        self.config_obj[self.config.MAIN][self.config.FUZZY] = fuzzy
        self.completer.fuzzy_match = fuzzy

    def get_fuzzy_match(self):
        """Getter for fuzzy matching mode

        Used by prompt_toolkit's KeyBindingManager.
        KeyBindingManager expects this function to be callable so we can't use
        @property and @attrib.setter.

        Args:
            * None.

        Returns:
            A boolean that represents the fuzzy flag.