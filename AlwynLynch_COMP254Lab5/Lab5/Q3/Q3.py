# bt_node.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class BTNode:
    key: Any
    left: Optional["BTNode"] = None
    right: Optional["BTNode"] = None
    parent: Optional["BTNode"] = None

    def set_left(self, child: Optional["BTNode"]) -> None:
        self.left = child
        if child:
            child.parent = self

    def set_right(self, child: Optional["BTNode"]) -> None:
        self.right = child
        if child:
            child.parent = self

