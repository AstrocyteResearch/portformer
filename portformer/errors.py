"""A collection of library specific errors."""


class PortformerError(Exception):
    """A base class for Portformer exceptions."""


class PortformerAPIError(PortformerError):
    """Error related to API request or response exceptions."""


class PortformerMissingAPIKeyError(PortformerAPIError):
    """Error related to API request or response exceptions."""


class PortformerInvalidAPIKeyError(PortformerAPIError):
    """Error related to API request or response exceptions."""
