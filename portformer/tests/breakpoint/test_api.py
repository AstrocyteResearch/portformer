import os
import unittest

import numpy as np
import pandas as pd

from portformer import BreakpointAPI
from portformer.errors import PortformerInvalidAPIKeyError, PortformerMissingAPIKeyError


class TestBreakpointAPI(unittest.TestCase):
    def setUp(self):
        # Read environment variable = BREAKPOINT_API_KEY
        self.api = BreakpointAPI(api_key=None)

    def test_api_key_config(self):
        """Config from ENV VAR and from parameter"""
        cur_env_var = os.environ.get("BREAKPOINT_API_KEY", None)
        os.environ["BREAKPOINT_API_KEY"] = "ENVTEST"
        api = BreakpointAPI()
        self.assertEqual(api.api_key, "ENVTEST")

        api = BreakpointAPI(api_key="TEST")
        self.assertEqual(api.api_key, "TEST")

        # reset BREAKPOINT_API_KEY
        if cur_env_var is not None:
            os.environ["BREAKPOINT_API_KEY"] = cur_env_var

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

    def test_example_forecast(self):
        """Get Latest AAPL forecasts."""

        breakpoint_forecast = self.api.forecast("AAPL")

        self.assertEqual(breakpoint_forecast["ticker"], "AAPL")
        self.assertIsNotNone(breakpoint_forecast["as_of_date"])
        self.assertIsNotNone(breakpoint_forecast["mu"])
        self.assertIsNotNone(breakpoint_forecast["std"])

    def test_example_historical_forecasts(self):
        """Get Historical TSLA forecasts"""
        historical_breakpoints = self.api.historical_forecasts(
            "TSLA", start_date="2020-02-01", end_date="2020-04-01"
        )
        self.assertGreater(len(historical_breakpoints["agg"]), 0)

    def test_example_cross_sectional_forecasts(self):
        """Get Latest SPY AGG GLD forecasts."""
        breakpoint_cross_section = self.api.cross_sectional_forecasts(
            tickers=["SPY", "AGG", "GLD"]
        )
        results = {x["ticker"]: x["sharpe"] for x in breakpoint_cross_section}
        self.assertIsNotNone(results["SPY"])
        self.assertIsNotNone(results["AGG"])
        self.assertIsNotNone(results["GLD"])

    def test_example_crypto_forecasts(self):
        """Get Crypto Universe Bitcoin forecasts"""
        btc = self.api.crypto_forecasts(ticker="BTCUSD")

        self.assertEqual(btc["ticker"], "BTCUSD")
        self.assertIsNotNone(btc["as_of_date"])
        self.assertIsNotNone(btc["mu"])
        self.assertIsNotNone(btc["std"])

    def test_example_crypto_universe(self):
        """Get full crypto_universe list"""
        universe = self.api.crypto_universe()
        self.assertGreater(len(universe), 0)

    def test_example_custom(self):
        """API request with custom timeseries data"""

        N = 200
        seed = 42

        # Generate a random price series
        np.random.seed(seed)
        data = np.exp(pd.Series(np.random.normal(size=(N,)) * 0.01).cumsum())
        data.index = pd.bdate_range("2020-01-01", periods=N)

        bp = self.api.custom_timeseries_forecasts(
            data,
            name=None,
            history_timedelta=None,
            tform="log-diff",
            no_whitten=False,
            seed=seed,
        )
        self.assertIsNotNone(bp)
