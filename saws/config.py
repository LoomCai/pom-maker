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
import shutil
import os
try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict
from configobj import ConfigObj


class Config(object):
    """Reads and writes the config file `sawsrc`.

    Attributes:
        * SHORTCUTS: A string that represents the start of shortcuts in
            the config file ~/.sawsrc.
        * MAIN: A string that represents the main set of configs in
            ~/.sawsrc.
        * THEME: A string that represents the config theme.
        * LOG_FILE: A string that represents the config log file location.
        