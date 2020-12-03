"""Basic Breakpoint API Examples."""

import numpy as np
import pandas as pd

from portformer import BreakpointAPI


def examples():
    """List of major Breakpoint API examples"""
    # Read environment variable = BREAKPOINT_API_KEY
    api = BreakpointAPI(api_key=None)

    # Get Latest AAPL forecasts

    breakpoint_forecast = api.forecast("AAPL")
    print(
        "breakpoint_forecast for {} on {}:\t\tmu:{}, std:{}".format(
            breakpoint_forecast["ticker"],
            breakpoint_forecast["as_of_date"],
            breakpoint_forecast["mu"],
            breakpoint_forecast["std"],
        )
    )

    # Get Historical TSLA forecasts
    historical_breakpoints = api.historical_forecasts(
        "TSLA", start_date="2020-02-01", end_date="2020-04-01"
    )
    print(
        "number of historical_breakpoints:\t\t\t{}".format(
            len(historical_breakpoints["agg"])
        )
    )

    # Get Latest SPY AGG GLD forecasts
    breakpoint_cross_section = api.cross_sectional_forecasts(
        tickers=["SPY", "AGG", "GLD"]
    )
    print(
        "breakpoint_cross_section forecasted sharpe ratios:\t",
        {x["ticker"]: x["sharpe"] for x in breakpoint_cross_section},
    )

    # Get Latest Bitcoin forecasts
    btc = api.crypto_forecasts(ticker="BTCUSD")
    print(
        "BTCUSD for {} on {}:\t\t\tmu:{}, std:{}".format(
            btc["ticker"], btc["as_of_date"], btc["mu"], btc["std"],
        )
    )

    # Get Crypto Universe Bitcoin forecasts
    universe = api.crypto_universe()
    print("number of crypto tickers in universe:\t\t\t{}".format(len(universe)))


def custom_examples():
    """API request with custom timeseries data"""
    # Read environment variable = BREAKPOINT_API_KEY
    api = BreakpointAPI(api_key=None)

    N = 200
    seed = 42

    # Generate a random price series
    np.random.seed(seed)
    data = np.exp(pd.Series(np.random.normal(size=(N,)) * 0.01).cumsum())
    data.index = pd.bdate_range("2020-01-01", periods=N)

    bp = api.custom_timeseries_forecasts(
        data,
        name=None,
        history_timedelta=None,
        tform="log-diff",
        no_whitten=False,
        seed=seed,
    )
    print(bp)


if __name__ == "__main__":
    # examples()
    custom_examples()
