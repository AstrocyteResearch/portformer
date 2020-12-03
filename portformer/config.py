"""Helper functions to read from library."""

import os

from dotenv import dotenv_values


def load_dotenv_config(dotenv_path=None, verbose=False, **kwargs):
    """Load config file at either `dotenv_path`, env var `PF_CONFIG_DOTENV_PATH`."""
    return dotenv_values(dotenv_path=dotenv_path, verbose=verbose, **kwargs)


def get_envvar(prefix="PF_"):
    """get all variables that start with the given prefix."""
    prefix_len = len(prefix)
    return {
        k[prefix_len:].lower(): v.strip()
        for k, v in os.environ.items()
        if k.startswith(prefix)
    }


def load_config(prefix="PF_"):
    """Load configuration from environmental file and environmental variables."""
    envvar_settings = get_envvar(prefix=prefix)

    verbose = envvar_settings.get("verbose", False)
    dotenv_path = envvar_settings.get("config_dotenv_path", None)

    settings = load_dotenv_config(dotenv_path=dotenv_path, verbose=verbose)

    settings.update(envvar_settings)
    return settings
