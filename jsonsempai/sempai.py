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


def get_json_path(directory, name):
    json_path = os.path.join(directory, '{name}.json'.format(name=name))
    if os.path.isfile(json_path):
        return json_path


class SempaiLoader(object):
    def __init__(self, json_path):
        self.json_path = json_path

    @classmethod
    def find_module(cls, name, path=None):
        for d in sys.path:
            json_path = get_json_path(d, name)
            if json_path is not None:
                return cls(json_path)

        if path is not None:
            name = name.split('.')[-1]
            for d in path:
                json_path = get_json_path(d, name)
                if json_path is not None:
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
