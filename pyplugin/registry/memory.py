from .abstract import AbstractPluginRepository

class InMemoryPluginRepositroy(AbstractPluginRepository, dict):
        
    def get_all(self):
        return tuple(self.values())

    def get_by_name(self, name: str):
        return self[name]
