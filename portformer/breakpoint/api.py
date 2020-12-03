"""A python wrapper for Breakpoint API whose documentation is found here.

https://analysis.portformer.com/docs#/
"""

import json
import os
from typing import Dict, List, Union

import pandas as pd
import requests

from ..errors import (
    PortformerAPIError,
    PortformerInvalidAPIKeyError,
    PortformerMissingAPIKeyError,
)


class BreakpointAPI:
    """Wrapper of Breakpoint API."""

    def __init__(self, api_key: str = None):
        """Save the API KEY

        api_key is either defined in string or if None,
        will look in BREAKPOINT_API_KEY environmental variable
        """
        self._base_url = "https://analysis.portformer.com/api/v1"
        self.api_key = api_key or os.environ.get("BREAKPOINT_API_KEY", None)

    def _get_request(self, url, params):
        headers = {"Content-Type": "application/json"}
        if self.api_key is not None:
            headers["Authentication"] = f"Bearer {self.api_key}"

        r = requests.get(
            url,
            params={k: v for k, v in params.items() if v is not None},
            headers=headers,
        )
        if not r.ok:
            if r.status_code == 401:
                raise PortformerInvalidAPIKeyError(
                    "Error in request: {} - {}".format(r.status_code, r.content)
                )
            elif r.status_code == 403:
                raise PortformerMissingAPIKeyError(
                    "Error in request: {} - {}".format(r.status_code, r.content)
                )
            else:
                raise PortformerAPIError(
                    "Error in request: {} - {}".format(r.status_code, r.content)
                )
        return json.loads(r.content)

    def _post_request(self, url, params, body):
        headers = {"Content-Type": "application/json"}
        if self.api_key is not None:
            headers["Authentication"] = f"Bearer {self.api_key}"

        r = requests.post(
            url,
            params={k: v for k, v in params.items() if v is not None},
            headers=headers,
            json=body,
        )
        if not r.ok:
            raise PortformerAPIError(
                "Error in request: {} - {}".format(r.status_code, r.content)
            )
        return json.loads(r.content)

    def forecast(
        self, ticker, as_of_date=None, history_timedelta="1Y", return_ts=False, seed=None,
    ):
        """GET REQUEST /breakpoint/single/{ticker}"""
        url = f"{self._base_url}/breakpoint/single/{ticker}"
        params = {
            "as_of_date": as_of_date,
            "history_timedelta": history_timedelta,
            "return_ts": return_ts,
            "seed": seed,
        }
        return self._get_request(url, params)

    def historical_forecasts(
        self, ticker, start_date=None, end_date=None, subdists=False
    ):
        """GET REQUEST /breakpoint/ts/{ticker}"""
        url = f"{self._base_url}/breakpoint/ts/{ticker}"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "subdists": subdists,
        }
        return self._get_request(url, params)

    def cross_sectional_forecasts(self, tickers, as_of_date=None, subdists=False):
        """GET REQUEST /breakpoint/xs"""
        if isinstance(tickers, list):
            tickers = ",".join(tickers)

        url = f"{self._base_url}/breakpoint/xs"
        params = {"tickers": tickers, "as_of_date": as_of_date, "subdists": subdists}
        return self._get_request(url, params)

    def custom_timeseries_forecasts(
        self,
        data: Union[Dict, pd.Series],
        name=None,
        history_timedelta=None,
        tform="log-diff",
        no_whitten=False,
        seed=None,
    ):
        """POST REQUEST /breakpoint/custom_timeseries/series_name"""
        params = {
            "history_timedelta": history_timedelta,
            "tform": tform,
            "no_whitten": no_whitten,
            "seed": seed,
        }

        if isinstance(data, pd.Series):
            # reformat index
            data.index = pd.Index(
                [
                    dt if isinstance(dt, str) else str(dt)[0:10]
                    for dt in pd.to_datetime(data.index)
                ],
                name=data.index.name,
            )
            body = data.to_dict()
            name = name or data.index.name
        elif isinstance(data, dict):
            body = data
        else:
            raise PortformerAPIError(
                "data should be a pd.Series or a dict with dates as keys"
            )

        name = name or "unknown"
        url = f"{self._base_url}/breakpoint/custom_timeseries/{name}"
        return self._post_request(url, params, body)

    def crypto_forecasts(
        self, ticker, as_of_date=None, history_timedelta="1Y", return_ts=False, seed=None,
    ):
        """GET REQUEST /breakpoint/crypto/{ticker}"""

        url = f"{self._base_url}/breakpoint/crypto/{ticker}"
        params = {
            "as_of_date": as_of_date,
            "history_timedelta": history_timedelta,
            "return_ts": return_ts,
            "seed": seed,
        }
        return self._get_request(url, params)

    def crypto_universe(self) -> List:
        """GET REQUEST /breakpoint/crypto"""
        url = f"{self._base_url}/breakpoint/crypto"
        return self._get_request(url, {})
