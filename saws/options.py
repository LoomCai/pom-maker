
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
from enum import Enum
import os
from awscli.customizations.emr.constants import LIST_CLUSTERS_ACTIVE_STATES, \
    LIST_CLUSTERS_TERMINATED_STATES, LIST_CLUSTERS_FAILED_STATES
from .data_util import DataUtil


class AwsOptions(object):
    """Encapsulates AWS command options such as ec2 running states.

    Some options can be obtained from the awscli, while others cannot.
    For example:
        Option: --ec2-state completions are not found in the awscli
            Completions for --ec2-state should be added to data/OPTIONS.txt
        Option: --cluster-states are found in the awscli
            See get_cluster_states()

    Attributes:
        * OPTIONS_DIR: A string representing the directory containing
            data/OPTIONS.txt.
        * OPTIONS_PATH: A string representing the full file path of
            data/OPTIONS.txt.
        * all_commands: A list of all commands, sub_commands, options, etc
            from data/SOURCES.txt.
        * EC2_STATE_OPT: A string representing the option for ec2 states
        * CLUSTER_STATE_OPT: A string representing the option for cluster states
        * option_headers:
        * data_util: An instance of DataUtil().
        * header_to_type_map: A dict mapping headers as they appear in the
            OPTIONS.txt file to their corresponding OptionType.
        * ec2_states: A list of the possible EC2 instance states.
        * cluster_states: A list of the possible cluster states.
        * options_map: A dict mapping of options keywords and
            options to complete
    """

    class OptionType(Enum):
        """Enum specifying the command type.

        Attributes:
            * EC2_STATES: An int representing ec2 running states.
            * CLUSTER_STATES: An int representing cluster running states.
            * NUM_TYPES: An int representing the number of option types.
        """

        NUM_TYPES = 2
        EC2_STATES, CLUSTER_STATES = range(NUM_TYPES)

    OPTIONS_DIR = os.path.dirname(os.path.realpath(__file__))
    OPTIONS_PATH = os.path.join(OPTIONS_DIR, 'data/OPTIONS.txt')
