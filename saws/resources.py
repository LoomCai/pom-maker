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
        * resources_headers_map: A dict mapping resource headers to
            resources to complete.  Headers denote the start of each
            set of resources in the RESOURCES.txt file.
        * resources_options_map: A dict mapping resource options to
            resources to complete.
        * resource_headers: A list of headers that denote the start of each
            set of resources in the RESOURCES.txt file.
        * data_util: An instance of DataUtil().
        * header_to_type_map: A dict mapping headers as they appear in the
            RESOURCES.txt file to their corresponding ResourceType.
    """

    class ResourceType(Enum):
        """Enum specifying the resource type.

        Append new resource class instances here and increment NUM_TYPES.
        Note: Order is important, new resources should be added to the end.

        Attributes:
            * INSTANCE_IDS: An int representing instance ids.
            * INSTANCE_TAG_KEYS: An int representing instance tag keys.
            * INSTANCE_TAG_VALUES: An int representing instance tag values.
            * BUCKET_NAMES: An int representing bucket names.
            * BUCKET_URIS: An int representing bucket uris.
            * NUM_TYPES: An int representing the number of resource types.
        """
        NUM_TYPES = 5
        INSTANCE_IDS, INSTANCE_TAG_KEYS, INSTANCE_TAG_VALUES, \
            BUCKET_NAMES, BUCKET_URIS = range(NUM_TYPES)

    def __init__(self,
                 log_exception):
        """Initializes AwsResources.

        Args:
            * log_exception: A callable log_exception from SawsLogge