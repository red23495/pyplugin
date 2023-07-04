from pyplugin.loader.loader import PluginLoader
import unittest
import os


class TestPluginLoader(unittest.TestCase):

    def setUp(self):
        self.loader = PluginLoader()

    def test_load_module(self):
        self.assertEqual(
            self.loader.load_plugin(
                'sample',
                os.path.normpath(
                    os.path.join(__file__, '..', '..', 'packages', 'sample')
                )
            ).add(2, 3), 5
        )

        self.assertRaises(
            ImportError, lambda: self.loader.load_plugin(
                'sample',
                os.path.normpath(
                    os.path.join(__file__, '..', '..', 'packages', 'invalid')
                )
            )
        )
