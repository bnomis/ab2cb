# -*- coding: utf-8 -*-
from __future__ import print_function

import datetime
import logging
import logging.handlers
import os

# logging

# the logger
glogger = None

# init default root object logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s %(levelname)s %(message)s', filename=os.devnull)


class FileFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.datetime.utcfromtimestamp(record.created)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            s = dt.strftime('%Y-%m-%d %H:%M:%S %Z')
        return s


def open_logging_console():
    log_console = logging.StreamHandler()
    log_console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s %(levelname)s %(message)s')
    log_console.setFormatter(formatter)
    return log_console


def open_logging_file(fname):
    # make sure the destination directory exists
    try:
        os.makedirs(os.path.dirname(fname))
    except:
        pass
    log_file = logging.handlers.TimedRotatingFileHandler(fname, when='midnight', backupCount=10, encoding='utf8')
    log_file.setLevel(logging.DEBUG)
    formatter = FileFormatter('%(asctime)s %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
    log_file.setFormatter(formatter)
    return log_file


def init_logging(options):
    if not options.debug:
        return

    global glogger

    glogger = logging.getLogger('ab2cb')

    # console
    try:
        l = open_logging_console()
    except Exception as e:
        print('Exception initing logging to console: %s' % e)
    else:
        glogger.addHandler(l)

    # file
    if options.debug_log:
        try:
            l = open_logging_file(options.debug_log)
        except Exception as e:
            print('Exception initing logging to file %s: %s' % (options.debug_log, e))
        else:
            glogger.addHandler(l)


def deinit_logging():
    logging.shutdown()


# catches potential logging errors
def do_log(msg, which, **kwargs):
    global glogger

    if not glogger:
        return

    try:
        func = getattr(glogger, which, None)
        if func and callable(func):
            func(msg.encode('unicode_escape', errors='replace'), **kwargs)
        else:
            pass
            # print('do_log: no function: %s' % which)
    except Exception:
        pass
        # print('do_log: exception: %s' % e)


def debug(msg, **kwargs):
    do_log(msg, 'debug', **kwargs)


def info(msg, **kwargs):
    do_log(msg, 'info', **kwargs)


def warning(msg, **kwargs):
    do_log(msg, 'warning', **kwargs)


def error(msg, **kwargs):
    do_log(msg, 'error', **kwargs)


def critical(msg, **kwargs):
    do_log(msg, 'critical', **kwargs)


def exception(msg, **kwargs):
    do_log(msg, 'exception', **kwargs)

