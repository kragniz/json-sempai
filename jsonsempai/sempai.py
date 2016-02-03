import contextlib
import imp
import json
import os
import sys

try:
    import yaml 
except:
    pass #the lack of yaml is handled later

class DottedDict(dict):

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError("'{}'".format(attr))

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__

def get_yaml_path(directory, name):
    yaml_path = os.path.join(directory, '{name}.yaml'.format(name=name))
    if os.path.isfile(yaml_path):
        return yaml_path

def get_json_path(directory, name):
    json_path = os.path.join(directory, '{name}.json'.format(name=name))
    if os.path.isfile(json_path):
        return json_path


class SempaiLoader(object):
    def __init__(self, markup_path):
        self.markup_path = markup_path

    @classmethod
    def find_module(cls, name, path=None):
        for d in sys.path:
            markup_path = get_json_path(d, name)
            if markup_path is None:
                markup_path = get_yaml_path(d, name)
            if markup_path is not None:
                return cls(markup_path)

        if path is not None:
            name = name.split('.')[-1]
            for d in path:
                markup_path = get_json_path(d, name)
                if markup_path is None:
                    markup_path = get_yaml_path(d, name)
                if markup_path is not None:
                    return cls(markup_path)


    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        mod = imp.new_module(name)
        mod.__file__ = self.markup_path
        mod.__loader__ = self

        decoder = json.JSONDecoder(object_hook=DottedDict)

        if self.markup_path[-4:] == "json":
            try:
                with open(self.markup_path, 'r') as f:
                    d = decoder.decode(f.read())
            except ValueError:
                raise ImportError(
                    '"{name}" does not contain a valid json.'.format(name=self.markup_path))
            except:
                raise ImportError(
                    'Could not open "{name}".'.format(name=self.markup_path))  
                    
        elif self.markup_path[-4:] == "yaml":
            try:
                with open(self.markup_path, 'r') as f:
                   d = yaml.load(f.read())
            except ValueError:
                raise ImportError(
                    '"{name}" does not contain a valid yaml.'.format(name=self.markup_path))
            except NameError:
                raise ImportError(
                    '"{name}" was not imported as no yaml parser is available on the system.'.format(name=self.markup_path))
            except:
                raise ImportError(
                    'Could not open "{name}".'.format(name=self.markup_path))    

        else:
            raise ImportError(
                'Could not open "{name}".'.format(name=self.markup_path))

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
