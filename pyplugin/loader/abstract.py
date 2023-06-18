import abc


class AbstractPluginLoader(abc.ABC):
    
    @abc.abstractmethod
    def load_plugin(self, name, location, **kwargs):
        pass
        