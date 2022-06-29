"""Module to store all components to use in tanjun"""

import typing as _typing
from .clash_of_clans import *
from .pubchem import *
from .subsplease import *

__all__: _typing.Final[list[str]] = [
    name for name in dir() if name.startswith("loader_")
]

del _typing
