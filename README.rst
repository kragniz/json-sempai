===========
json-sempai
===========

.. image:: https://travis-ci.org/kragniz/json-sempai.png?branch=master
    :target: https://travis-ci.org/kragniz/json-sempai

.. image:: https://pypip.in/d/json-sempai/badge.png
    :target: https://pypi.python.org/pypi/json-sempai

Have you ever been kept awake at night, desperately feeling a burning desire to
do nothing else but directly import json files in python [#]_? Now you can!

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
    >>> import tester
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


.. [#] Disclaimer: Only do this if you hate yourself and the rest of the world.
