
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
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys


class KeyManager(object):
    """Creates a Key Manager.

    Attributes:
        * manager: An instance of a prompt_toolkit's KeyBindingManager.
    """

    def __init__(self, set_color, get_color,
                 set_fuzzy_match, get_fuzzy_match,
                 set_shortcut_match, get_shortcut_match,
                 refresh_resources_and_options, handle_docs):
        """Initializes KeyManager.

        Args:
            * set_color: A function setting the color output config.
            * get_color: A function getting the color output config.
            * set_fuzzy_match: A function setting the fuzzy match config.
            * get_fuzzy_match: A function getting the fuzzy match config.
            * set_shortcut_match: A function setting the shortcut match config.
            * get_shortcut_match: A function getting the shortcut match config.

        Returns:
            None.
        """
        self.manager = None
        self._create_key_manager(set_color, get_color,
                                 set_fuzzy_match, get_fuzzy_match,
                                 set_shortcut_match, get_shortcut_match,
                                 refresh_resources_and_options, handle_docs)

    def _create_key_manager(self, set_color, get_color,
                            set_fuzzy_match, get_fuzzy_match,
                            set_shortcut_match, get_shortcut_match,
                            refresh_resources_and_options, handle_docs):
        """Creates and initializes the keybinding manager.

        Args:
            * set_color: A function setting the color output config.
            * get_color: A function getting the color output config.
            * set_fuzzy_match: A function setting the fuzzy match config.
            * get_fuzzy_match: A function getting the fuzzy match config.
            * set_shortcut_match: A function setting the shortcut match config.
            * get_shortcut_match: A function getting the shortcut match config.

        Returns:
            A KeyBindingManager.
        """
        assert callable(set_color)
        assert callable(get_color)
        assert callable(set_fuzzy_match)
        assert callable(get_fuzzy_match)
        assert callable(set_shortcut_match)
        assert callable(get_shortcut_match)
        assert callable(refresh_resources_and_options)
        assert callable(handle_docs)
        self.manager = KeyBindingManager(