from importlib import import_module as _import_module

from . import baseline
from ._config import Config, ConfigBaseline, ConfigChlamydia, config, load_config

try:
    __version__ = getattr(
        _import_module("iseq_prof_analysis._version"), "version", "x.x.x"
    )
except ModuleNotFoundError:
    __version__ = "x.x.x"

__all__ = [
    "Config",
    "ConfigBaseline",
    "ConfigChlamydia",
    "__version__",
    "baseline",
    "config",
    "load_config",
]
