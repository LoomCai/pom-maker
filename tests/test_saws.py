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
import mock
import os
import traceback
from tests.compat import unittest
from saws.saws import Saws
from saws.commands import AwsCommands


class SawsTest(unittest.TestCase):

    def setUp(self):
        self.file_name = os.path.expanduser('~') + '/' + '.saws.log'
        self.saws = Saws(refresh_resources=False)
        self.DOCS_HOME_URL = \
            'http://docs.aws.amazon.com/cli/latest/reference/index.html'

    @mock.patch('saws.saws.click')
    def test_log_exception(self, mock_click):
        exception_message = 'test_log_exception'
        e = Exception(exception_message)
        try:
            raise e
        except Exception:
            # Traceback needs to have an active exception as described in:
            # http://bugs.python.org/issue23003
            self.saws.log_exception(e, traceback, echo=True)
            mock_click.secho.assert_called_with(str(e), fg='red')
        assert os.path.isfile(self.file_name)
        with open(self.file_name, 'r') as fp:
            for line in fp:
                pass
            assert exception_message in line

    def test_set_get_color(self):
        self.saws.set_color(True)
        assert self.saws.get_color()
        self.saws.set_color(False)
        assert not self.saws.get_color()

    def test_get_set_fuzzy_match(self):
        self.saws.set_fuzzy_match(True)
        assert self.saws.get_fuzzy_match()
        self.saws.set_fuzzy_match(False)
        assert not self.saws.get_fuzzy_match()

    def test_get_set_shortcut_match(self):
        self.saws.set_shortcut_match(True)
        assert self.saws.get_shortcut_match()
        self.saws.set_shortcut_match(False)
        assert not self.saws.get_shortcut_match()

    @mock.patch('saws.saws.webbrowser')
    def test_handle_docs(self, mock_webbrowser):
        EC2_URL = \
            'http://docs.aws.amazon.com/cli/latest/reference/ec2/index.html'
        EC2_DESC_INSTANCES_URL = \
            'http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html'  # NOQA
        assert not self.saws.handle_docs('')
        assert not self.saws.handle_docs('foo bar')
        assert self.saws.handle_docs('',
                                     from_fkey=True)
        mock_webbrowser.open.assert_called_with(self.DOCS_HOME_URL)
        assert self.saws.handle_docs('baz',
                                     from_fkey=True)
        mock_webbrowser.open.assert_called_with(self.DOCS_HOME_URL)
        assert self.saws.handle_docs('aws ec2',
                                     from_fkey=True)
        mock_webbrowser.open.assert_called_with(EC2_URL)
        assert self.saws.handle_docs('aws ec2 docs',
                                     from_fkey=False)
        mock_webbrowser.open.assert_called_with(EC2_URL)
        assert self.saws.handle_docs('aws ec2 describe-instances',
                                     from_fkey=True)
        mock_webbrowser.open.assert_called_with(EC2_DESC_INSTANCES_URL)
        assert self.saws.handle_docs('aws ec2 describe-instances docs',
                                     from_fkey=False)
        mock_w