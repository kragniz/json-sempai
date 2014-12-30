import imp
import json
import os
import sys


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

        return mod

sys.meta_path.append(SempaiLoader())
