import unittest

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from portformer.viz._rcparams import rcParams
from portformer.viz.main import (
    plot_allocations,
    plot_timeseries,
    visualize_breakpoint_metrics,
)


class TestVizMain(unittest.TestCase):
    def test_visualize_breakpoint_metrics(self):
        """Should return a figure"""
        N = 200
        seed = 42

        # Generate a random price series
        np.random.seed(seed)
        metrics = np.exp(pd.DataFrame(np.random.normal(size=(N, 4)) * 0.01).cumsum())
        metrics.index = pd.bdate_range("2020-01-01", periods=N)

        fig = visualize_breakpoint_metrics(metrics, fields=metrics.columns)
        self.assertIsInstance(fig, plt.Figure)

    def test_plot_allocations(self):
        """Should return a figure"""
        N = 200
        seed = 42

        # Generate a random price series
        np.random.seed(seed)
        weights = pd.DataFrame(np.random.uniform(size=(N, 4)))
        weights.index = pd.bdate_range("2020-01-01", periods=N)

        fig = plot_allocations(weights)
        self.assertIsInstance(fig, plt.Figure)

    def test_plot_timeseries(self):
        """Should return a figure"""
        N = 200
        seed = 42

        # Generate a random price series
        np.random.seed(seed)
        ts = np.exp(pd.Series(np.random.normal(size=(N,)) * 0.01).cumsum())
        ts.index = pd.bdate_range("2020-01-01", periods=N)

        fig = plot_timeseries(ts)
        self.assertIsInstance(fig, plt.Figure)

    def test_rcparams(self):
        self.assertIsInstance(rcParams, dict)
