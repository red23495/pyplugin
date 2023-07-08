from pyplugin.loader.module import ModulePluginLoader
import unittest
import os


class TestPluginLoader(unittest.TestCase):

    def setUp(self):
        self.loader = ModulePluginLoader()

    def test_load_module(self):
        from collections import namedtuple
        Registry = namedtuple('Registry', ['name', 'location'])
        registry = Registry(
            'sample',
            os.path.normpath(
                os.path.join(__file__, '..', '..', 'packages', 'sample')
            )
        )
        self.assertEqual(self.loader.load_plugin(registry).add(2, 3), 5)

        invalid_registry = Registry(
            'sample',
            os.path.normpath(
                os.path.join(__file__, '..', '..', 'packages', 'invalid')
            )
        )

        self.assertRaises(
            ImportError, lambda: self.loader.load_plugin(invalid_registry)
        )
