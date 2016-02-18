===========
json-sempai
===========

.. image:: https://travis-ci.org/kragniz/json-sempai.svg?branch=master
    :target: https://travis-ci.org/kragniz/json-sempai

.. image:: https://img.shields.io/pypi/v/json-sempai.svg
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

Slap a json file somewhere on your python path. ``me.json``:

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

    >>> from jsonsempai import magic
    >>> import me
    >>> me
    <module 'me' from 'me.json'>
    >>> me.hello
    u'world'
    >>> me.this.can.be
    u'nested'
    >>>

Alternatively, a context manager may be used (100% less magic):

.. code:: python

    >>> import jsonsempai
    >>> with jsonsempai.notice():
    ...     import me
    >>> me
    <module 'me' from 'me.json'>


Python packages are also supported:

.. code:: bash

    $ tree
    .
    └── python_package
        ├── file.json
        ├── __init__.py
        └── nested_package
            ├── __init__.py
            └── second.json

.. code:: python

    >>> from jsonsempai import magic
    >>> from python_package import file
    >>> file
    <module 'python_package.file' from 'python_package/file.json'>
    >>> import python_package.nested_package.second
    >>> python_package.nested_package.second
    <module 'python_package.nested_package.second' from 'python_package/nested_package/second.json'>


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
