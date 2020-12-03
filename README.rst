
.. image:: https://circleci.com/gh/AstrocyteResearch/portformer/tree/master.svg?style=shield
    :target: https://circleci.com/gh/AstrocyteResearch/portformer/tree/master

.. image:: https://codecov.io/gh/AstrocyteResearch/portformer/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/AstrocyteResearch/portformer

.. image:: https://img.shields.io/pypi/v/portformer.svg
    :target: https://pypi.python.org/pypi/portformer

.. image:: https://img.shields.io/pypi/l/portformer.svg
    :target: https://pypi.python.org/pypi/portformer

.. image:: https://img.shields.io/pypi/pyversions/portformer.svg
    :target: https://pypi.python.org/pypi/portformer

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/AstrocyteResearch/portformer

------


.. image:: https://img.shields.io/badge/Link-Install-blue.svg
      :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/AstrocyteResearch/portformer

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
      :target: https://github.com/AstrocyteResearch/portformer/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
      :target: https://github.com/AstrocyteResearch/portformer/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.org/pypi/portformer#files


Portformer: Portfolios. Made Better.
==============================================================================
Welcome to the documentation for the wrapper for of Portformer's API https://analysis.portformer.com/docs


This is a product of Portformer by Astrocyte Research

.. _install:

Install
------------------------------------------------------------------------------

``portformer`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install portformer

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade portformer


Usage
------------------------------------------------------------------------------

.. code-block:: python3

    from portformer import BreakpointAPI
    api = BreakpointAPI(api_key="ENTER_YOUR_KEY")

    # Get the latest breakpoint risks and forecasts for TSLA
    breakpoint_forecast = api.forecast("TSLA")


Development
------------------------------------------------------------------------------

.. code-block:: console

    $ # create venv
    $ virtualenv -p python3.8 venv

    $ # Install
    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ pip install -e .


Test
------------------------------------------------------------------------------

.. code-block:: console

    $ python ./tests/all.py



Build
------------------------------------------------------------------------------

.. code-block:: console

    $ python3 -m pip install --user --upgrade setuptools wheel
    $ python3 setup.py sdist bdist_wheel
