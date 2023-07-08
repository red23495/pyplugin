import abc
from pyplugin.registry.abstract import AbstractPluginRegistry


class AbstractPluginLoader(abc.ABC):

    @abc.abstractmethod
    def load_plugin(self, registry: AbstractPluginRegistry):
        pass

    @abc.abstractmethod
    def unload_plugin(self, registry: AbstractPluginRegistry):
        pass

    @abc.abstractmethod
    def reload_plugin(self, registry: AbstractPluginRegistry):
        pass
