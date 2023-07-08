from pyplugin.loader.abstract import AbstractPluginLoader
from pyplugin.manager.abstract import AbstractPluginManager
from pyplugin.registry.abstract import AbstractPluginRepository


class PluginManager(AbstractPluginManager):

    def __init__(self, repository: AbstractPluginRepository, loader: AbstractPluginLoader):
        self._repository = repository
        self._loader = loader

    def get_repository(self) -> AbstractPluginRepository:
        return self._repository

    def get_loader(self) -> AbstractPluginLoader:
        return self._loader
