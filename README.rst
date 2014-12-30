===========
json-sempai
===========

.. image:: https://travis-ci.org/kragniz/json-sempai.png?branch=master
    :target: https://travis-ci.org/kragniz/json-sempai

Have you ever been kept awake at night, desperately feeling a burning desire to
do nothing else but directly import json files in python? Now you can!

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
