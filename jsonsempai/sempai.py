import contextlib
import imp
import json
import os
import sys

try:
    import yaml
except:
    pass
    
try: 
    import xmltodict
except:
    pass



class DottedDict(dict):

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError("'{}'".format(attr))
   
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    
class DateTimeEncoder(json.JSONEncoder):
    def default(self,obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstanc(obj, ModelState):
            return None
        else:
            return json.JSONEncoder.default(self, obj)



def get_markup_path(directory, name, markup):
    markup_path = os.path.join(directory, '{name}.{markup}'.format(name=name, markup=markup))       
    if os.path.isfile(markup_path):
        return markup_path



class SempaiLoader(object):
    def __init__(self, markup_path):
        self.markup_path = markup_path

    @classmethod
    def find_module(cls, name, path=None):
        for d in sys.path:
            markup_path = None
            for markup in ['json', 'yaml', 'xml']:
                if markup_path is None:
                    markup_path = get_markup_path(d, name, markup)
            if markup_path is not None:
                return cls(markup_path)

        if path is not None:
            name = name.split('.')[-1]
            for d in path:
                for markup in ['json', 'yaml', 'xml']:
                    if markup_path is None:
                        markup_path = get_markup_path(d, name, markup)
                if markup_path is not None:
                    return cls(markup_path)


    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        mod = imp.new_module(name)
        mod.__file__ = self.markup_path
        mod.__loader__ = self

        decoder = json.JSONDecoder(object_hook=DottedDict)

        try:
            markup = self.markup_path.split(".")[-1]
            with open(self.markup_path, 'r') as f:
                if markup == 'json':
                   d = decoder.decode(f.read())
                elif markup == 'xml':
                   x = xmltodict.parse(f.read())
                   d = decoder.decode(json.dumps(x, indent=4, cls=DateTimeEncoder).replace("@", ""))       
                elif markup == 'yaml':
                   y = yaml.load(f.read())
                   d = decoder.decode(json.dumps(y, indent=4, cls=DateTimeEncoder))
        except ValueError:
            raise ImportError(
                '"{name}" does not contain a valid {markup}.'.format(name=self.markup_path, markup=markup))
        except NameError:
            raise ImportError(
                '"{name}" was not imported as no {markup} parser is available on the system.'.format(name=self.markup_path, markup=markup))
        except:
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
