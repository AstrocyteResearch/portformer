import numpy as np
import requests
import pandas as pd
import datetime
import json
import tqdm
import tempfile
import pprint
import matplotlib.pyplot as plt
import seaborn as sns

try:
    from ar_analysis.api.api_v1.endpoints.backtester import (
        run_backtest as run_backtest_locally,
        StrategyModel,
    )

    RUN_LOCAL = True

except ImportError:
    print("Local Portformer Analysis Library not found, using Portformer API")
    RUN_LOCAL = False


# BACKTESTING CODE
def generate_backtest_spec(weights, **kwargs):
    assert isinstance(weights, pd.DataFrame)
    assert weights.isnull().sum().sum() == 0, "No NaNs should be in weights"
    weights = weights.copy(deep=True)

    if not isinstance(weights.index[0], str):
        weights.index = [dt.strftime("%Y-%m-%d") for dt in weights.index]

    rebalance_weights = weights.T.to_dict()
    start_date = weights.index[0]

    payload = {
        "funds": [{"ticker": ticker} for ticker in weights.columns],
        "rebalance_weights": rebalance_weights,
        "start_date": start_date,
        "initial_value": 1000000,
        "income_tax_rate": 0,
        "capital_gains_tax_rate": 0,
        "fractional_shares": True,
        "post_disbursement_trigger_rebal": False,
    }
    payload.update(kwargs)
    return payload


def run_backtest(payload, use_api=not RUN_LOCAL):
    if use_api:
        url = "https://analysis.portformer.com/api/v1/run"
        rs = requests.post(url, json=payload)
        if rs.ok:
            backtest = json.loads(rs.content)
        else:
            print("API Error at time {}:\n\n".format(datetime.datetime.utcnow()))
            print(rs.status_code, rs.content)
            print("\nPAYLOAD\n\n")
            print(json.dumps(payload))
            raise RuntimeError(
                "API call didn't work, provide the above printout to Sean"
            )
    else:
        strategy_model = StrategyModel(
            funds=payload["funds"],
            rebalance_weights=payload["rebalance_weights"],
            start_date=payload["start_date"],
        )
        backtest = run_backtest_locally(strategy_model)
    return backtest


# BREAKPOINT CODE
def get_breakpoint(ticker, as_of_date):
    url = f"https://analysis.portformer.com/api/v1/breakpoint/single/{ticker}?as_of_date={as_of_date}&history_timedelta=1Y&return_ts=false"
    rs = requests.get(url)
    return rs.content


def get_breakpoints(tickers, as_of_dates, show_progress=True):
    breakpoints = {}
    errors = {}

    if show_progress:
        ittr = tqdm.tqdm(total=len(tickers) * len(as_of_dates))
    for ticker in tickers:
        for dt in as_of_dates:
            assert isinstance(dt, str)
            try:
                bp = get_breakpoint(ticker, dt)
                breakpoints[(ticker, dt)] = json.loads(bp)
            except Exception as e:
                print(ticker, dt, str(e))
                errors[(ticker, dt)] = str(e)
            if show_progress:
                ittr.update(1)
    return breakpoints, errors


def get_bulk_breakpoint(tickers, as_of_dates, max_workers=10):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from itertools import product
    import tqdm
    import json

    if max_workers > 10:
        print(
            "limiting max_workers to 10, contact skruzel@astrocyte.io to raise the limit"
        )
        max_workers = 10

    total = len(tickers) * len(as_of_dates)
    args_list = [(t, dt) for t, dt in product(tickers, as_of_dates)]

    def api_request(args):
        return get_breakpoint(*args)

    errors = {}
    out = {}
    ittr = tqdm.tqdm(None, total=total, desc="Getting Breakpoints")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = (executor.submit(api_request, args) for args in args_list)

        for idx, future in enumerate(as_completed(future_to_url)):
            data = None
            try:
                data = future.result()
                data = json.loads(data)
                out[(data["ticker"], data["as_of_date"])] = data
            except Exception as exc:
                errors[idx] = str(type(exc))

            ittr.update(1)

    missing_breakpoints = set(args_list).difference(set(out.keys()))

    if len(missing_breakpoints):
        print("retrying {} missing breakpoints".format(len(missing_breakpoints)))
        for t, dt in tqdm.tqdm(
            list(missing_breakpoints), desc="retrying missing breakpoints"
        ):
            bp, e = get_breakpoints([t], [dt], show_progress=False)
            out.update(bp)
            errors.update(e)
    return out, errors
