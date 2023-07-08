import abc
from typing import Tuple

from pyplugin.registry.abstract import AbstractPluginRegistry

class AbstractPackage(abc.ABC):
    
    @abc.abstractmethod
    @property
    def metadata(self) -> dict:
        pass
    
    @abc.abstractmethod
    @property
    def name(self) -> str:
        pass
    
    @abc.abstractmethod
    @property
    def version(self) -> str:
        pass
    
    @abc.abstractmethod
    @property
    def source_location(self) -> str:
        pass
    
    @abc.abstractmethod
    @property
    def resources_location(self):
        pass

class AbstractPackageInstaller(abc.ABC):
    
    @abc.abstractmethod
    def unpack(self, location: str) -> AbstractPackage:
        pass


class AbstractPackageAnalyzer(abc.ABC):
    
    @abc.abstractmethod
    def analyze_package(self, package: AbstractPackage, registry: AbstractPluginRegistry, options: dict) -> Tuple[bool, dict]:
        pass