import os
import sys

class SempaiLoader(object):

    def find_module(self, name, path=None):
        for d in sys.path:
            json_path = os.path.join(d, '{}.json'.format(name))
            if os.path.isfile(json_path):
                print json_path
                return self
        return None

    def load_module(self, name):
        raise ImportError('Hey, yo fool')

sys.meta_path.append(SempaiLoader())
