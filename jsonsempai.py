import imp
import json
import os
import sys


class Dot(dict):

    def __init__(self, d):
        super(dict, self).__init__()
        for k, v in d.iteritems():
            if isinstance(v, dict):
                self[k] = Dot(v)
            else:
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__


class SempaiLoader(object):

    def find_module(self, name, path=None):
        for d in sys.path:
            self.json_path = os.path.join(d, '{}.json'.format(name))
            if os.path.isfile(self.json_path):
                print self.json_path
                return self
        return None

    def load_module(self, name):
        mod = imp.new_module(name)
        mod.__file__ = self.json_path

        try:
            with open(self.json_path) as f:
                d = json.load(f)
        except:
            raise ImportError(
                'Couldn\'t load json from"{}".'.format(self.json_path))

        mod.__dict__.update(d)
        for k, i in mod.__dict__.items():
            if isinstance(i, dict):
                mod.__dict__[k] = Dot(i)

        return mod

sys.meta_path.append(SempaiLoader())
