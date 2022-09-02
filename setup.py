from saws.__init__ import __version__
import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

install_req