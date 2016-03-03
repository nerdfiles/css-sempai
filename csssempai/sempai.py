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


def get_css_path(directory, name):
    css_path = os.path.join(directory, '{name}.css'.format(name=name))
    if os.path.isfile(css_path):
        return css_path


class SempaiLoader(object):
    def __init__(self, css_path):
        self.css_path = css_path

    @classmethod
    def find_module(cls, name, path=None):
        for d in sys.path:
            css_path = get_css_path(d, name)
            if css_path is not None:
                return cls(css_path)

        if path is not None:
            name = name.split('.')[-1]
            for d in path:
                css_path = get_css_path(d, name)
                if css_path is not None:
                    return cls(css_path)


    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        mod = imp.new_module(name)
        mod.__file__ = self.css_path
        mod.__loader__ = self

        decoder = json.jsonDecoder(object_hook=DottedDict)

        try:
            with open(self.css_path) as f:
                d = decoder.decode(f.read())
        except ValueError:
            raise ImportError(
                '"{name}" does not contain valid css.'.format(name=self.css_path))
        except:
            raise ImportError(
                'Could not open "{name}".'.format(name=self.css_path))

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

