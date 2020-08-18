"""
"""
import importlib
import portformer as pf


def set_api_backend(engine):
    if "_" in engine:
        pf._api = engine.split("_")[1]
        pf._engine = engine
    else:
        pf._engine = f"api_{pf._api}"
    try:
        pf.backend = importlib.import_module(f"portformer.engine.{pf._engine}")
    except ImportError:
        raise ValueError(
            "Invalid backend specification, set _engine to `api`, `api_v1` or other valid configuration"
        )


def set_local_backend():
    try:
        import portformer.engine.local as backend

        pf._engine = "local"

        pf.backend = backend
    except ImportError:
        raise ImportError(
            "Local backtesting engine available only to select enterprise clients: contact sales@portformer.com for more information"
        )


def set_zipline_backend():
    raise NotImplementedError(
        "Zipline isn't implemented yet, request feature by submitting a request at https://github.com/AstrocyteResearch/portformer"
    )


def set_backend(engine=None):
    if engine is None:
        engine = "api"

    if engine.startswith("api"):
        set_api_backend(engine)
    elif engine == "local":
        set_local_backend()
    elif engine == "zipline":
        set_zipline_backend()
    else:
        pf.backend = None
        raise ValueError(
            "Invalid backend specification, set _engine to `api`, `api_v1` or other valid configuration"
        )

    print(f"portformer.backend `{pf._engine}` loaded")

