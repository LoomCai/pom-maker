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
from .resource import Resource


class InstanceTagKeys(Resource):
    """Encapsulates the EC2 instance tag keys resources.

    Attributes:
        * OPTION: A string representing the option for instance tag keys.
        * QUERY: A string representing the AWS query to list all instance
            tag keys.
        * resources: A list of instance tag keys.
    """

    OPTION = '--ec2-tag-key'
    QUERY = 'aws ec2 describe-instances --filters "Name=tag-key,Values=*" --query Reservations[].Instances[].Tags[].Key --output text'  # NOQA

    def __init__(self):
        """Initializes InstanceTagKeys.

        Args:
            * None.

        Returns:
            None.
        """
        super(InstanceTagKeys, self).__init__()

    def query_resource(self):
        """Queries and stores instance ids from AWS.

        Args:
            * None.

        Returns:
            The list of resources.

        Raises:
            A subprocess.CalledProcessError if check_output returns a non-zero
                exit status, which is called by self._query_aws.
        """
        # TODO: Refactor query_resource in InstanceTagKeys and InstanceTagValues