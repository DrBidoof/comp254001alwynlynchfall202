# q3_item.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

# Match textbook idea: store (key, value) pairs and compare by key only.
# (Goodrich keeps an Item composite with __lt__ by key.)
@dataclass(order=True)
class Item:
    key: Any
    value: Any = field(compare=False)
