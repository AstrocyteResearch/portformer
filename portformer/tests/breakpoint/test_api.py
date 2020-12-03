import os
import unittest

from portformer import BreakpointAPI
from portformer.errors import PortformerInvalidAPIKeyError, PortformerMissingAPIKeyError


class TestBreakpointAPI(unittest.TestCase):
    def test_api_key_config(self):
        """Config from ENV VAR and from parameter"""
        os.environ["BREAKPOINT_API_KEY"] = "ENVTEST"
        api = BreakpointAPI()
        self.assertEqual(api.api_key, "ENVTEST")

        api = BreakpointAPI(api_key="TEST")
        self.assertEqual(api.api_key, "TEST")

    def test_requires_auth_key(self):
        """Should return 401 / 403 Not authenticated if given a bad or missing api_keys"""

        api = BreakpointAPI(api_key="NOT-A-VALID-KEY")
        self.assertRaises(
            PortformerInvalidAPIKeyError, api.forecast, ("TSLA",),
        )

        api = BreakpointAPI(api_key=None)
        api.api_key = None  # force non in case environ variable is set
        self.assertRaises(
            PortformerMissingAPIKeyError, api.forecast, ("TSLA",),
        )


a = TestBreakpointAPI()
a.test_requires_auth_key()
