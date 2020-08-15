
.. image:: https://travis-ci.org/closedLoop/portformer.svg?branch=master
    :target: https://travis-ci.org/closedLoop/portformer?branch=master

.. image:: https://codecov.io/gh/closedLoop/portformer/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/closedLoop/portformer

.. image:: https://img.shields.io/pypi/v/portformer.svg
    :target: https://pypi.python.org/pypi/portformer

.. image:: https://img.shields.io/pypi/l/portformer.svg
    :target: https://pypi.python.org/pypi/portformer

.. image:: https://img.shields.io/pypi/pyversions/portformer.svg
    :target: https://pypi.python.org/pypi/portformer

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/closedLoop/portformer

------


.. image:: https://img.shields.io/badge/Link-Install-blue.svg
      :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/closedLoop/portformer

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
      :target: https://github.com/closedLoop/portformer/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
      :target: https://github.com/closedLoop/portformer/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.org/pypi/portformer#files


Welcome to ``portformer`` Documentation
==============================================================================

Documentation for ``portformer``.


.. _install:

Install
------------------------------------------------------------------------------

``portformer`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install portformer

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade portformer


# portformer
Portfolios. Made Better.

A wrapper for portformer API https://analysis.portformer.com


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

# Development

```
# create venv
make -f make/python_env.mk up

# Install
make -f make/python_env.mk install

```

# Build

```
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
```

This should generate

```
dist/
  example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz
```

# Deplo


pip install . # install your library and dependencies
pip install pytest
mkdir tests # write some test
pip install sphinx
sphinx-quickstart # initiate doc
vim docs/source/conf.py # configure your doc settings
