# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import sys

from . import __version__


# put these string here so we can import them for testing
program_name = 'ab2cb'
usage_string = '%(prog)s [options] [File ...]'
version_string = '%(prog)s %(version)s' % {'prog': program_name, 'version': __version__}
description_string = '''ab2cb: convert AdBlock content filters to Safari Content Blockers'''


def parse_opts(argv, stdin=None, stdout=None, stderr=None):
    parser = argparse.ArgumentParser(
        prog=program_name,
        usage=usage_string,
        description=description_string,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--version',
        action='version',
        version=version_string
    )

    parser.add_argument(
        '--debug',
        dest='debug',
        action='store_true',
        default=False,
        help='Turn on debug logging.'
    )

    parser.add_argument(
        '--debug-log',
        dest='debug_log',
        metavar='FILE',
        help='Save debug logging to FILE.'
    )

    parser.add_argument(
        '-o',
        '--output',
        metavar='FILE',
        help='Save converted text to FILE. If not given, output to stdout.'
    )

    parser.add_argument(
        'files',
        metavar='File',
        nargs='*',
        help='Files to extract from. If not given read from stdin.'
    )

    # print('argv = %s' % argv)
    options = parser.parse_args(argv)

    # set up i/o options
    options.stdin = stdin or sys.stdin
    options.stdout = stdout or sys.stdout
    options.stderr = stderr or sys.stderr

    options.did_extract = False
    options.exit_status = 'not-set'

    return options

