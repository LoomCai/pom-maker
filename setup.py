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
    'pygments>=2.0.2,<3.0.0'
]

if sys.version_info < (2, 7):
    # Introduced in Python 2.7
    install_requires.append('ordereddict>=1.1')
if sys.version_info < (3, 4):
    # Backport of Python 3.4 enums to earlier versions
    install_requires.append('enum34>=1.0.4')

setup(
    description='SAWS: A Supercharged AWS Command Line Interface (CLI)',
    author='Donne Martin',
    url='https://github.com/donnemartin/saws',
    download_url='https://pypi.python.org/pypi/saws',
    author_email='donne.martin@gmail.com',
    version=__version__,
    license='Apache License 2.0',
    install_requires=install_requires,
    extras_require={
        'testing': [
            'mock>=1.0.1',
            'tox>=1.9.2'
        ],
    },
    entry_points={
        'console_scripts': 'saws = saws.main:cli'
    },
    packages=find_packages(),
    package_data={'saws': ['sawsrc',
          