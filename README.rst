
``compat23`` is a python library for making it just a bit easier to write code
that's portable between python 2 and 3. It abstracts away minor differences in
the standard library well enough to be able to write portable code.

Here's a summary of what's provided:

* ``compat23.core`` provides compatibility for things in python's default
  namespace, for example basestring, unicode, and bytes.
* There are several modules that normalize import paths:

  * ``compat23.queue`` is an alias for ``queue`` on python 3 and ``Queue`` on
    python 2.
  * ``compat23.configparser`` is an alias for ``configparser``/``ConfigParser``.
