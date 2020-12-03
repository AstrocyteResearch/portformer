"""Misc Visualization libraries to assist in visualizing Breakpoint and Portformer Data"""
import matplotlib.pyplot as plt
import pandas as pd


# %matplotlib inline
def format_rcParams():
    plt.rcParams["figure.figsize"] = (16.0, 10.0)
    plt.rcParams["figure.titlesize"] = 20
    plt.rcParams["font.size"] = 16


# VIZ CODE
def visualize_breakpoint_metrics(metrics, fields, figsize=(24, 30), aggfn=None):
    fig = plt.figure(figsize=figsize)
    ax = None
    for i, field in enumerate(fields):
        ax = fig.add_subplot(len(fields), 1, i + 1, sharex=ax)

        m = metrics[field]
        if aggfn is not None:
            m = aggfn(m, axis=1)

        if i == 0:
            m.plot(ax=ax, title=field)
            plt.legend(
                bbox_to_anchor=(0.12, 0.05),
                loc="lower left",
                bbox_transform=fig.transFigure,
                ncol=5,
            )
        else:
            m.plot(ax=ax, title=field, legend=False)

    fig.tight_layout()
    return fig


def plot_allocations(weights: pd.DataFrame, figsize=(16, 10), title="Allocations"):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)

    (100 * weights).plot(kind="area", ax=ax, title=title)
    ax.set_ylim((0, 100))
    ax.set_xlim((weights.index[0], weights.index[-1]))
    ax.set_ylabel("% Allocation")
    ax.set_xlabel(None)
    ax.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)
    fig.tight_layout()
    return fig


def plot_timeseries(ts, figsize=(16, 10), title="Timeseries", **kwargs):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)

    ts.plot(ax=ax, title=title, **kwargs)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)
    fig.tight_layout()
    return fig
