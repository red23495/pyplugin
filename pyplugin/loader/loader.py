from .abstract import AbstractPluginLoader
from importlib import util
import sys
import os


class PluginLoader(AbstractPluginLoader):

    def load_plugin(self, name, location, **kwargs):
        try:
            path = os.path.join(location, '__init__.py')
            spec = util.spec_from_file_location(name, path)
            module = util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            raise ImportError(
                f'Can not import {name} from location {location}. Reason: {str(e)}'
            )
