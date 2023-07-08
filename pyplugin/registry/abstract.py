import abc
from typing import Iterable


class AbstractPluginRegistry(abc.ABC):

    @property
    @abc.abstractmethod
    def name(self):
        pass


class AbstractPluginRepository(abc.ABC):

    @abc.abstractmethod
    def get_all(self) -> Iterable[AbstractPluginRegistry]:
        pass

    @abc.abstractmethod
    def get_by_name(self, name: str) -> AbstractPluginRegistry:
        pass
    
    @abc.abstractmethod
    def install(self, registry: AbstractPluginRegistry) -> AbstractPluginRegistry:
        pass
