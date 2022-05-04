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
import os
try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict
import traceback
from enum import Enum
from .data_util import DataUtil
from .resource.instance_ids import InstanceIds
from .resource.instance_tag_keys import InstanceTagKeys
from .resource.instance_tag_values import InstanceTagValues
from .resource.bucket_names import BucketNames
from .resource.bucket_uris import BucketUris


class AwsResources(object):
    """Encapsulates AWS resources such as ec2 tags and buckets.

    Attributes:
        * resources_path: A string representing the full file path of
            data/RESOURCES.txt.
        * log_exception: A callable log_exception from SawsLogger.
        * resource_lists: A list where each element is a list of completions
            for each resource.
        * resources_headers_map: A dict mapping resourc