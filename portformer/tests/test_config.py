import os
import unittest

from portformer import load_config


class TestLoadConfig(unittest.TestCase):
    def test_load_config(self):
        """Should return a dictionary"""
        os.environ["RANDOMPREFIX_randomvar"] = "1"
        config = load_config(prefix="RANDOMPREFIX_")
        del os.environ["RANDOMPREFIX_randomvar"]
        self.assertDictEqual(config, {"randomvar": "1"})
