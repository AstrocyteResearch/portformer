# Portformer
Portfolios. Made Better.

A wrapper for Portformer API https://analysis.portformer.com


# Install

```
pip install portformer
```


# Usage

```
from portformer import Backtest

bt = Backtest(API_KEY='XXXXX', run_local=False)

spec = bt.make_spec(weights=wt)
results = bt.run(spec)
bt.tearsheet(results)
```
