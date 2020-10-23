# Run Backtests

# import portformer.engine.api_v1.__init__.__api_root__
import requests
import json
import pandas as pd

__api_version__ = "v1"
__api_root__ = f"https://analysis.portformer.com/api/{__api_version__}"


def make_fund(
    ticker: str,
    closes: pd.Series,
    disbursements=None,
    splits=None,
    trx_costs=None,
    accounting_mode="OPT",
    fund_events=None,
    is_crypto=False,
) -> dict:
    """"""
    return {
        "ticker": ticker,
        "data": {"closes": closes, "disbursements": disbursements, "splits": splits},
        "trx_costs": trx_costs,
        "accounting_mode": accounting_mode,
        "fund_events": fund_events,
        "is_crypto": is_crypto,
    }


def run(
    weights: pd.DataFrame = None,
    closes: pd.DataFrame = None,
    start_date: str = None,
    initial_value=1000000,
    income_tax_rate=0,
    capital_gains_tax_rate=0,
    fractional_shares=True,
    post_disbursement_trigger_rebal=False,
):
    url = f"{__api_root__}/run"

    funds = [
        make_fund(ticker, closes=closes.loc[:, ticker]) for ticker in weights.columns
    ]

    if start_date is None:
        start_date = weights.index[0]

    payload = {
        "funds": funds,
        "rebalance_weights": weights.T.to_dict(),
        "start_date": start_date,
        "initial_value": initial_value,
        "income_tax_rate": income_tax_rate,
        "capital_gains_tax_rate": capital_gains_tax_rate,
        "fractional_shares": fractional_shares,
        "post_disbursement_trigger_rebal": post_disbursement_trigger_rebal,
    }

    rs = requests.post(url, json=payload)
    if rs.ok:
        return json.loads(rs.content)
    else:
        raise Exception(str(rs))
