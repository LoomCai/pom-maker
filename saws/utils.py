
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
import re
import six
import shlex
from prompt_toolkit.completion import Completion


class TextUtils(object):
    """Utilities for parsing and matching text.

    Attributes:
        * None.
    """

    def find_matches(self, word, collection, fuzzy):
        """Finds all matches in collection for word.

        Args:
            * word: A string representing the word before
                the cursor.
            * collection: A collection of words to match.
            * fuzzy: A boolean that specifies whether to use fuzzy matching.

        Yields:
            A generator of prompt_toolkit's Completions.
        """
        word = self._last_token(word).lower()
        for suggestion in self._find_collection_matches(
                word, collection, fuzzy):
            yield suggestion

    def get_tokens(self, text):
        """Parses out all tokens.

        Args:
            * text: A string to split into tokens.

        Returns:
            A list of strings for each word in the text.