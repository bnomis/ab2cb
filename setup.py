#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from ab2cb import __version__


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


desc = 'ab2cb: convert AdBlock content filters to Safari Content Blockers'

here = os.path.abspath(os.path.dirname(__file__))
try:
    long_description = open(os.path.join(here, 'docs/README.rst')).read()
except:
    long_description = desc


# https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: POSIX',
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.4",
    'Topic :: Security',
    'Topic :: Text Processing',
    'Topic :: Utilities',
    'Topic :: Text Processing :: Filters',
]

keywords = ['advertising', 'privacy', 'web']
platforms = ['macosx', 'linux', 'unix']

setup(
    name='ab2cb',
    version=__version__,
    description=desc,
    long_description=long_description,
    author='Simon Blanchard',
    author_email='bnomis@gmail.com',
    license='MIT',
    url='https://github.com/bnomis/ab2cb',

    classifiers=classifiers,
    keywords=keywords,
    platforms=platforms,

    packages=find_packages(exclude=['tests']),

    entry_points={
        'console_scripts': [
            'ab2cb = ab2cb.ab2cb:run',
        ]
    },

    tests_require=['tox'],
    cmdclass={
        'test': Tox
    },
)

