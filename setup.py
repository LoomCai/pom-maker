from saws.__init__ import __version__
import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

install_requires = [
    'awscli>=1.7.46,<2.0.0',
    'click>=4.0,<7.0',
    'configobj>=5.0.6,<6.0.0',
    'prompt-toolkit>=1.0.0,<1.1.0',
    'six>=1.9.0,<2.0.0',
    'pygm