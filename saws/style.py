# -*- coding: utf-8

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

from pygments.token import Token
from pygments.util import ClassNotFound
from prompt_toolkit.styles import default_style_extensions, style_from_dict
import pygments.styles


class StyleFactory(object):
    """Creates a custom saws style.

    Provides styles for the completions menu and toolbar.

    Attributes:
        * style: An instance of a Pygments Style.
    """

    def __init__(self, name):
        """Initializes StyleFactory.

        Args:
            * name: A string representing the pygments style.

        Returns:
            An instance of CliStyle.
        """
        self.style = self.style_factory(name)

    def style_factory(self, name):
        """Retrieves the specified pygments style.

        If the specified style is not found, the native style is returned.

        Args:
            * name: A string representing the pygments style.

        Returns:
            An instance of CliStyle.
        """
        try:
            style = pygments.styles.get_style_by_name(name)
        except ClassNotFound:
            style = pygments.styles.get_style_by_name('native')

        # Create styles dictionary.
        styles = {}
        styles.update(style.styles)
        styles.update(default_style_extensions)
        styles.update({
            Token.Menu.Completions.Completion.Current: 'bg:#00aaaa 