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

Now import jsonsempai and your json file!

.. code:: python

    >>> import jsonsempai
    >>> with jsonsempai.imports():
    ...     import tester
    >>> tester
    <module 'tester' from 'tester.json'>
    >>> tester.hello
    u'world'
    >>> tester.this.can.be
    u'nested'
    >>>

Installing
----------

Install from pip:

.. code:: bash

    $ pip install json-sempai

or clone this repo and install from source:

.. code:: bash

    $ python setup.py install

.. [#] Disclaimer: Only do this if you hate yourself and the rest of the world.
