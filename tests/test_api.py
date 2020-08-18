#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx

"""

import portformer as pf

# Run Local libraries
pf.set_backend('local') # could be 'api', 'api_v1', 'zipline'

# Run backtest from wts
bt = pf.Backtest(wts, **spec)
bt.run()
# or 
bt = pf.Backtest(weights=wts, **spec)
bt.run()

# Run backtest from trades
bt = pf.Backtest(trades=trades, **spec)
bt.run()

# Run backtest from positions
bt = pf.Backtest(positions=positions, **spec)
bt.run()

# Generate Tearsheet
bt.tearsheet(compare=bt2, **kwargs)
pf.tearsheet(bt, compare=bt2, **kwargs)
pf.tearsheet(returns=rtns, **kwargs)
pf.tearsheet(trades=trades, **kwargs)
pf.tearsheet(positions=positions, **kwargs)


# Breakpoint API
bp = pf.Breakpoint(ticker, as_of_dates=None)
bp = pf.get_breakpoints(tickers=None, as_of_dates=None) # bulk call

bt2 = bt.breakpoint_enhance(bp=None, **kwargs)
bp2 = bp.update(latest_prices) # updates regime probabilities given new data.  Should be used with live feeds


# Plotting
bp.plot() # plot breakpoints against timeseries

# Alerts
bp.alerts(top_n=10, metrics=None) # Returns a dictionary of top alerts for the given universe

# Views into data
bp.subdists  # @property of a big dataframe
bp.sharpe_pvalue # Dataframe of dates by tickers

"""

def test_v1_api_init():
    from portformer import 

def test():
    import portformer
    pass
