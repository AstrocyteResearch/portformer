import os
import unittest

from portformer import BreakpointAPI


class TestBreakpointAPI(unittest.TestCase):
    def test_api_key_config(self):
        """Config from ENV VAR and from parameter"""
        os.environ["BREAKPOINT_API_KEY"] = "ENVTEST"
        api = BreakpointAPI()
        self.assertEqual(api.api_key, "ENVTEST")

        api = BreakpointAPI(api_key="TEST")
        self.assertEqual(api.api_key, "TEST")
