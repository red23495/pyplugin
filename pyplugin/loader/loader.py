from .abstract import AbstractPluginLoader

class PluginLoader(AbstractPluginLoader):
    
    def load_plugin(self, name, location, **kwargs):
        # load plugin from a file
        # a plugin is any python file with functions and classes
        # this function should import the plugin file as module and return it
        pass