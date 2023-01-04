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
            for line 