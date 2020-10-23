# -*- coding: utf-8 -*-

"""
Portformer API and Portfolio analysis tools for the modern investor
"""

__version__ = "0.0.1"
__short_description__ = "Portfolios. Made Better."
__license__ = "MIT"
__author__ = "Sean Kruzel, Astrocyte Research Inc."
__author_email__ = "skruzel@portformer.com"
__maintainer__ = "Sean Kruzel"
__maintainer_email__ = "support@portformer.com"
__github_username__ = "closedLoop"

# Library Functions
__all__ = ["load_config"]

# Environmental variables
_api = "v1"
_engine = f"api_{_api}"

# Initialization functions
# from .config import load_config
# from .engine import set_backend

# _config = load_config()
# set_backend(engine=_config.get("engine", None))
