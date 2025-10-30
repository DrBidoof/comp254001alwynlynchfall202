# positional_list.py
from __future__ import annotations
from typing import Any, Optional, Iterator

class PositionalList:
    """A Positional List ADT with a public Position abstraction."""

    class _Node:
        __slots__ = ("element", "prev", "next")
        def __init__(self, element: Any, prev: Optional["PositionalList._Node"]=None, nxt: Optional["PositionalList._Node"]=None):
            self.element = element
            self.prev = prev
            self.next = nxt

    class Position:
        __slots__ = ("_container", "_node")
        def __init__(self, container: "PositionalList", node: "PositionalList._Node"):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__(self, other) -> bool:
            # positions are equal if they refer to the same node in the same container
            return (
                type(other) is type(self)
                and self._container is other._container
                and self._node is other._node
            )

    # ---------------- core structure ----------------
    def __init__(self) -> None:
        self._header = self._Node(None)
        self._trailer = self._Node(None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    # ---------------- public navigation ----------------
    def first(self) -> Optional["PositionalList.Position"]:
        return self._make_position(self._header.next)

    def last(self) -> Optional["PositionalList.Position"]:
        return self._make_position(self._trailer.prev)

    def before(self, p: "PositionalList.Position") -> Optional["PositionalList.Position"]:
        return self._make_position(p._node.prev)

    def after(self, p: "PositionalList.Position") -> Optional["PositionalList.Position"]:
        return self._make_position(p._node.next)

    # ---------------- public updates ----------------
    def add_first(self, e: Any) -> "PositionalList.Position":
        return self._insert_between(e, self._header, self._header.next)

    def add_last(self, e: Any) -> "PositionalList.Position":
        return self._insert_between(e, self._trailer.prev, self._trailer)

    def add_before(self, p: "PositionalList.Position", e: Any) -> "PositionalList.Position":
        return self._insert_between(e, p._node.prev, p._node)

    def add_after(self, p: "PositionalList.Position", e: Any) -> "PositionalList.Position":
        return self._insert_between(e, p._node, p._node.next)

    def positions(self) -> Iterator["PositionalList.Position"]:
        cur = self.first()
        while cur is not None:
            yield cur
            cur = self.after(cur)

    # ---------------- internal helpers ----------------
    def _make_position(self, node: "PositionalList._Node") -> Optional["PositionalList.Position"]:
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def _insert_between(self, e: Any, predecessor: "PositionalList._Node", successor: "PositionalList._Node") -> "PositionalList.Position":
        node = self._Node(e, predecessor, successor)
        predecessor.next = node
        successor.prev = node
        self._size += 1
        return self._make_position(node)

    def __repr__(self) -> str:
        return "[" + ", ".join(str(pos.element()) for pos in self.positions()) + "]"
