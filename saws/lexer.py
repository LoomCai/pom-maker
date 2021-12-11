# -*- coding: utf-8

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

from pygments.lexer import RegexLexer
from pygments.lexer import words
from pygments.token import Keyword, Name, Operator, Generic, Literal
from .commands import AwsCommands
from .config import Config


class CommandLexer(RegexLexer):
    """Provides highlighting for commands.

    Attributes:
        * config: An instance of Config.
        * config_obj: An instance of ConfigObj.
        * shortcuts: An OrderedDict containing the shortcut commands as the
            keys and their corresponding full commands as the values.
        * shortcut_tokens: A list containing words for each shortcut key:
            key: 'aws ec2 ls' -> shortcut_tokens: ['aws', 'ec2', 'ls'].
        * aws_commands: An instance of AwsCommands.
        * commands: A tuple, where each tuple element is a list of:
            * commands
            * sub_commands
            * global_options
            * resource_options
        * tokens: A dictionary of pygments tokens.
    """

    config = Config()
    config_obj = config.read_configuration()
    shortcuts = config.get_shortcuts(config_obj)
    shortcut_tokens = []
    for sho