#map_base.py

# map_base.py
from collections.abc import MutableMapping

class MapBase(MutableMapping):
    """Base class for map implementations (textbook)."""

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
