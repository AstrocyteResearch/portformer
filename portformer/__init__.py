"""
Portformer API and Portfolio analysis tools for the modern investor
"""

__version__ = "1.0.0"
__short_description__ = "Portfolios. Made Better."
__license__ = "Astrocyte Research, Inc"
__author__ = "Sean Kruzel, Astrocyte Research Inc."
__author_email__ = "skruzel@portformer.com"
__maintainer__ = "Sean Kruzel"
__maintainer_email__ = "support@portformer.com"
__github_username__ = "closedLoop"

# Library Functions
__all__ = ["load_config", "BreakpointAPI"]

from .breakpoint.api import BreakpointAPI

# Environmental variables
from .config import load_config

_api = "v1"
