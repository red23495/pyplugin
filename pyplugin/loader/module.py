from .abstract import AbstractPluginLoader
from importlib import util, invalidate_caches, reload
import sys
import os
import abc
from pyplugin.registry.abstract import AbstractPluginRegistry
import pyplugin.loader.dummy as dummy


class AbstractModulePluginRegistry(AbstractPluginRegistry):

    @property
    @abc.abstractmethod
    def location(self):
        pass


class ModulePluginLoader(AbstractPluginLoader):

    def load_plugin(self, registry: AbstractModulePluginRegistry):
        try:
            path = os.path.join(registry.location, '__init__.py')
            spec = util.spec_from_file_location(registry.name, path)
            module = util.module_from_spec(spec)
            sys.modules[registry.name] = module
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            raise ImportError(
                f'Can not import {registry.name} from location {registry.location}. Reason: {str(e)}'
            )
            
    def unload_plugin(self, registry: AbstractPluginRegistry):
        sys.modules[registry.name] = dummy
        invalidate_caches()
        
    def reload_plugin(self, registry: AbstractPluginRegistry):
        reload(sys.modules[registry.name])
