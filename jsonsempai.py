import sys

class SempaiLoader(object):
    def __init__(self, *args):
        print args

    def find_module(self, fullname, path=None):
        print 'finding', fullname, path
        if fullname == 'simple':
            return self
        return None

sys.path_hooks.append(SempaiLoader)
sys.path.insert(0, 'simple')
