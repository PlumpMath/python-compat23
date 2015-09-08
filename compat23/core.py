# Copyright (c) 2015 Ian Denhardt <ian@zenhack.net>
# Licensed under the MIT license; see COPYING for details.
"""Provide compatibility helpers for the default namespace.

On Python 2:

    * bytes is an alias for str
    * range is an alias for xrange clients should call list(range(...))
      if they want the old behavior (as in Python 3).

On Python 3:

    * basestring and unicode are aliases for str
    * xrange is an alias for range

It is safe to write::

    from compat23.core import *

In that the above changes are guaranteed to be the only things affected.
"""
import sys as _sys

if _sys.version_info.major == 3:
    basestring = str
    unicode = str
elif _sys.version_info.major == 2:
    bytes = str
    range = xrange
