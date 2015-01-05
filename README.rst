===========
json-sempai
===========

.. image:: https://travis-ci.org/kragniz/json-sempai.png?branch=master
    :target: https://travis-ci.org/kragniz/json-sempai

.. image:: https://pypip.in/version/json-sempai/badge.png?style=flat
    :target: https://pypi.python.org/pypi/json-sempai

Have you ever been kept awake at night, desperately feeling a burning desire to
do nothing else but directly import JSON files as if they were python modules
[#]_? Now you can!

This abomination allows you to write

.. code:: python

     import some_json_file

and if ``some_json_file.json`` can be found, it will be available as if it is a
python module.

Usage
-----

Slap a json file somewhere on your python path. ``tester.json``:

.. code:: json

    {
        "hello": "world",
        "this": {
            "can": {
                "be": "nested"
            }
        }
    }

Magic
~~~~~

Now import jsonsempai and import any json file residing on your Python path! 

.. code:: python

    >>> from jsonsempai import magic
    >>> # ../Python27/Scripts/tester.json
    >>> import tester
    >>> tester
    <module 'tester' from 'tester.json'>
    >>> tester.hello
    u'world'
    >>> tester.this.can.be
    u'nested'
    >>>


Voodoo
~~~~~~

Similar to Magic, but is limited to json files in the same directory

.. code:: python

    >>> from jsonsempai import voodoo
    >>> # /Python27/Scripts/tester.json
    >>> import tester
    ImportError: No module named tester_
    >>> # /foobar/voodoo_tester.json
    >>> import voodo_tester
    >>> voodoo_tester
    <module 'voodoo_tester' from 'voodoo_tester.json'>
    >>> voodoo_tester.hello
    u'world'
    >>> voodoo_tester.this.can.be
    u'nested'
    >>>


Alternatively, a context manager may be used (100% less magic, 0% voodoo):

.. code:: python

    >>> import jsonsempai
    >>> with jsonsempai.imports():
    ...     import tester
    >>> tester
    <module 'tester' from 'tester.json'>

Installing
----------

Install from pip:

.. code:: bash

    $ pip install json-sempai

or clone this repo and install from source:

.. code:: bash

    $ python setup.py install

To purge this horror from your machine:

.. code:: bash

    $ pip uninstall json-sempai

.. [#] Disclaimer: Only do this if you hate yourself and the rest of the world.
