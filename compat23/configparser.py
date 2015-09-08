# Copyright (c) 2015 Ian Denhardt <ian@zenhack.net>
# Licensed under the MIT license; see COPYING for details.
"""Alias for the standard library's queue module.

On Python 2 this is an alias for ``ConfigParser``.

On Python 3 this is an alias for ``configparser``.
"""
import sys as _sys

if _sys.version_info.major == 3:
    from configparser import *
elif _sys.version_info.major == 2:
    from ConfigParser import *
