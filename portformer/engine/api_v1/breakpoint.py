import requests
import tqdm
import json


def get_custom_breakpoint(
    ticker, as_of_date, rtns, tform="log-diff", history_timedelta="1Y"
):
    url = f"https://analysis.portformer.com/api/v1/breakpoint/custom_timeseries/{ticker}?history_timedelta={history_timedelta}&tform={tform}"

    dates = sorted([dt for dt in rtns.keys() if dt <= as_of_date])
    insample_rtns = {dt: rtns[dt] for dt in dates}
    rs = requests.post(url, json=insample_rtns)
    return rs.content


def get_custom_breakpoints(rtns, as_of_dates):
    breakpoints = {}
    errors = {}

    tickers = sorted(list(rtns.keys()))

    ittr = tqdm.tqdm(total=len(tickers) * len(as_of_dates))
    for ticker in tickers:
        for dt in as_of_dates:
            assert isinstance(dt, str)
            try:
                bp = get_custom_breakpoint(ticker, dt, rtns[ticker])
                breakpoints[(ticker, dt)] = json.loads(bp)
            except Exception as e:
                print(ticker, dt, str(e))
                errors[(ticker, dt)] = str(e)
            ittr.update(1)
    return breakpoints, errors


def get_breakpoint(ticker, as_of_date):
    url = f"https://analysis.portformer.com/api/v1/breakpoint/single/{ticker}?as_of_date={as_of_date}&history_timedelta=1Y&return_ts=false"
    rs = requests.get(url)
    return rs.content


def get_breakpoints(tickers, as_of_dates):
    breakpoints = {}
    errors = {}

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
            ittr.update(1)
    return breakpoints, errors


def get_bulk_breakpoint(tickers, as_of_dates, max_workers=20):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from itertools import product
    import tqdm
    import json

    total = len(tickers) * len(as_of_dates)
    args_list = product(tickers, as_of_dates)

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
    return out, errors
