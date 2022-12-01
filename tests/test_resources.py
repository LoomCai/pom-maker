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
from tests.compat import unittest
from saws.saws import Saws


class ResourcesTest(unittest.TestCase):

    NUM_SAMPLE_INSTANCE_IDS = 7
    NUM_SAMPLE_INSTANCE_TAG_KEYS = 3
    NUM_SAMPLE_INSTANCE_TAG_VALUES = 6
    NUM_SAMPLE_BUCKET_NAMES = 16
    NUM_SAMPLE_BUCKET_URIS = 16

    def setUp(self):
        self.create_resources()
        self.sample_resource_counts = [
            self.NUM_SAMPLE_INSTANCE_IDS,
            self.NUM_SAMPLE_INSTANCE_TAG_KEYS,
            self.NUM_SAMPLE_INSTANCE_TAG_VALUES,
            self.NUM_SAMPLE_BUCKET_NAMES,
            self.NUM_SAMPLE_BUCKET_URIS
        ]

    def create_resources(self):
        self.saws = Saws(refresh_resources=False)
        self.resources = self.saws.completer.resources
        self.resources._set_resources_path('data/RESOURCES_SAMPLE.txt')

    def verify_resources(self):
        for resource_list, sample_resource_count in zip(
                self.resources.resource_lists,
                self.sample_resource_counts):
            assert len(resource_list.resources) == sample_resource_count

    # TODO: Silence output
    @mock.patch('saws.resources.print')
    def test_refresh_forced(self, mock_print):
        self.resources._set_resources_path('data/RESOURCES_FORCED.txt')
        self.resources.clear_resources()
        self.resources.refresh(force_refresh=True)
        mock_print.assert_called_