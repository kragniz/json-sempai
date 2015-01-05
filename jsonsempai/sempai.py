import contextlib
import imp
import json
import os
import sys


class DottedDict(dict):

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError("'{}'".format(attr))

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__


class SempaiLoader(object):
    def __init__(self, json_path):
        self.json_path = json_path

    @classmethod
    def find_module(cls, name, path=None):
        for d in sys.path:
            json_path = os.path.join(d, '{name}.json'.format(name=name))
            if os.path.isfile(json_path):
                return cls(json_path)

    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        mod = imp.new_module(name)
        mod.__file__ = self.json_path
        mod.__loader__ = self

        decoder = json.JSONDecoder(object_hook=DottedDict)

        try:
            with open(self.json_path) as f:
                d = decoder.decode(f.read())
        except ValueError:
            raise ImportError(
                '"{name}" does not contain valid json.'.format(name=self.json_path))
        except:
            raise ImportError(
                'Could not open "{name}".'.format(name=self.json_path))

        mod.__dict__.update(d)

        sys.modules[name] = mod
        return mod


class SempaiContextLoader(object):
    def __init__(self, json_path):
        self.json_path = json_path

    @classmethod
    def find_module(cls, name, path=None):

        if '.' in name:
            name = name.split('.')
            name = os.path.join(*name)

        for d, _, _ in os.walk(os.path.abspath(os.curdir)):
            json_path = os.path.join(d, '{name}.json'.format(name=name))
            if os.path.isfile(json_path):
                return cls(json_path)

    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        mod = imp.new_module(name)
        mod.__file__ = self.json_path
        mod.__loader__ = self

        decoder = json.JSONDecoder(object_hook=DottedDict)

        try:
            with open(self.json_path) as f:
                d = decoder.decode(f.read())
        except ValueError:
            raise ImportError(
                '"{name}" does not contain valid json.'.format(name=self.json_path))
        except:
            raise ImportError(
                'Could not open "{name}".'.format(name=self.json_path))

        mod.__dict__.update(d)

        sys.modules[name] = mod
        return mod


@contextlib.contextmanager
def imports():
    try:
        sys.meta_path.append(SempaiLoader)
        yield
    finally:
        sys.meta_path.remove(SempaiLoader)

