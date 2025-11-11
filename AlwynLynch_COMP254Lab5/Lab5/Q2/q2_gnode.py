# q2_gnode.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional

@dataclass(eq=False)
class GNode:
    elem: Any
    children: List["GNode"] = field(default_factory=list)
    parent: Optional["GNode"] = None

    def add_child(self, child: "GNode") -> None:
        self.children.append(child)
        child.parent = self
