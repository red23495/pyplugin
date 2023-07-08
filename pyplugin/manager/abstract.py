import abc
from collections.abc import Mapping
from typing import Iterator, Callable, Tuple
from pyplugin.package.abstract import AbstractPackage, AbstractPackageAnalyzer, AbstractPackageInstaller
from pyplugin.registry.abstract import AbstractPluginRegistry, AbstractPluginRepository
from pyplugin.loader.abstract import AbstractPluginLoader


class AbstractPluginManager(abc.ABC, Mapping):

    __plugins = {}

    @abc.abstractmethod
    def get_repository(self) -> AbstractPluginRepository:
        pass

    @abc.abstractmethod
    def get_loader(self) -> AbstractPluginLoader:
        pass

    def get_all_plugin_registry(self):
        repo = self.get_repository()
        return repo.get_all()

    def load_all_plugins(self):
        for registry in self.get_all_plugin_registry():
            self.__plugins[registry.name] = self.load_plugin(registry)

    def get_plugin_registry(self, name: str):
        repo = self.get_repository()
        return repo.get_by_name(name)

    def load_plugin(self, registry: AbstractPluginRegistry):
        loader = self.get_loader()
        return loader.load_plugin(registry)

    def unload_plugin(self, registry: AbstractPluginRegistry):
        loader = self.get_loader()
        return loader.unload_plugin(registry)

    def reload_plugin(self, registry: AbstractPluginRegistry):
        loader = self.get_loader()
        return loader.reload_plugin(registry)

    @abc.abstractmethod
    def get_installer(self) -> AbstractPackageInstaller:
        pass

    @abc.abstractmethod
    def get_analyzer(self) -> AbstractPackageAnalyzer:
        pass

    @abc.abstractmethod
    def get_package_adapter(self) -> Callable[[AbstractPackage], AbstractPluginRegistry]:
        pass

    def install(self, location: str, options: dict) -> Tuple[bool, dict]:
        installer = self.get_installer()
        package = installer.unpack(location)
        repository = self.get_repository()
        registry = repository.get_by_name(package.name)
        analyzer = self.get_analyzer()
        status, response = analyzer.analyze_package(package, registry, options)
        if not status:
            return False, response
        adapter = self.get_package_adapter()
        new_registry = adapter(package)
        self.before_plugin_install(registry, new_registry)
        new_registry = repository.install(new_registry)
        plugin = self.load_plugin(new_registry)
        self.after_plugin_install(plugin)
        return True, {}

    def after_plugin_install(self, plugin):
        pass

    def before_plugin_install(self, old, new):
        pass

    def __getitem__(self, __key: str):
        return self.__plugins.__getitem__(__key)

    def __iter__(self) -> Iterator:
        return self.__plugins.__iter__()

    def __len__(self):
        return self.__plugins.__len__()
