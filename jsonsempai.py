import imp
import json
import os
import sys


class Dot(dict):

    def __init__(self, d):
        super(dict, self).__init__()
        for k, v in iter(d.items()):
            if isinstance(v, dict):
                self[k] = Dot(v)
            elif isinstance(v, list):
                a = []
                for item in v:
                    if isinstance(item, dict):
                        a.append(Dot(item))
                    else:
                        a.append(item)
                self[k] = a
            else:
                self[k] = v

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError("'{}'".format(attr))

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__


class SempaiLoader(object):

    def find_module(self, name, path=None):
        for d in sys.path:
            self.json_path = os.path.join(d, '{name}.json'.format(name=name))
            if os.path.isfile(self.json_path):
                return self

    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        mod = imp.new_module(name)
        mod.__file__ = self.json_path
        mod.__loader__ = self

        try:
            with open(self.json_path) as f:
                d = json.load(f)
        except ValueError:
            raise ImportError(
                '"{}" does not contain valid json.'.format(self.json_path))
        except:
            raise ImportError(
                'Could not open "{}".'.format(self.json_path))

        mod.__dict__.update(Dot(d))

        sys.modules[name] = mod
        return mod

sys.meta_path.append(SempaiLoader())
