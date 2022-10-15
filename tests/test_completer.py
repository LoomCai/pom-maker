
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
import unittest
import mock
import re
from prompt_toolkit.document import Document
from awscli import completer as awscli_completer
from saws.completer import AwsCompleter
from saws.commands import AwsCommands
from saws.saws import Saws


class CompleterTest(unittest.TestCase):

    @mock.patch('saws.resources.print')
    def setUp(self, mock_print):
        self.saws = Saws(refresh_resources=False)
        self.completer = self.create_completer()
        self.completer.resources._set_resources_path(
            'data/RESOURCES_SAMPLE.txt')
        self.completer.refresh_resources_and_options()
        self.completer_event = self.create_completer_event()
        mock_print.assert_called_with('Loaded resources from cache')

    def create_completer(self):
        # TODO: Fix duplicate creation of AwsCompleter, which is already
        # created by Saws init
        self.aws_commands = AwsCommands()
        self.all_commands = self.aws_commands.all_commands
        self.commands, self.sub_commands, self.global_options, \
            self.resource_options = self.all_commands
        return AwsCompleter(awscli_completer,
                            self.all_commands,
                            self.saws.config,
                            self.saws.config_obj,
                            self.saws.logger)

    def create_completer_event(self):
        return mock.Mock()

    def _get_completions(self, command):
        position = len(command)
        result = set(self.completer.get_completions(
            Document(text=command, cursor_position=position),
            self.completer_event))
        return result

    def verify_completions(self, commands, expected):
        result = set()
        for command in commands:
            # Call the AWS CLI autocompleter
            result.update(self._get_completions(command))
        result_texts = []
        for item in result:
            # Each result item is a Completion object,
            # we are only interested in the text portion
            result_texts.append(item.text)
        assert result_texts
        if len(expected) == 1:
            assert expected[0] in result_texts
        else:
            for item in expected:
                assert item in result_texts

    def test_no_completions(self):
        command = 'aws ec2'
        expected = set([])
        assert expected == self._get_completions(command)
        command = 'aws elb'
        assert expected == self._get_completions(command)
        command = 'aws elasticache'
        assert expected == self._get_completions(command)

    def test_ec2_commands(self):
        commands = ['aws e']
        expected = ['ec2',
                    'ecs',
                    'efs',
                    'elasticache',