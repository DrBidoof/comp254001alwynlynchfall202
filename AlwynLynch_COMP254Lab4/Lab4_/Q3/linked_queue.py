# linked_queue.py
from __future__ import annotations
from typing import Any, Optional, Iterable

class LinkedQueue:
    """Queue implemented with a singly linked list."""
    class _Node:
        __slots__ = ("element", "next")
        def __init__(self, element: Any, nxt: Optional["LinkedQueue._Node"]=None):
            self.element = element
            self.next = nxt

    def __init__(self) -> None:
        self._head: Optional[LinkedQueue._Node] = None
        self._tail: Optional[LinkedQueue._Node] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def first(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._head.element  # type: ignore

    def enqueue(self, e: Any) -> None:
        node = self._Node(e)
        if self.is_empty():
            self._head = node
        else:
            self._tail.next = node  # type: ignore
        self._tail = node
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")
        node = self._head  # type: ignore
        self._head = node.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return node.element

    def concatenate(self, Q2: "LinkedQueue") -> None:
        """Append all nodes of Q2 to the end of this queue in O(1), leaving Q2 empty."""
        if Q2.is_empty():
            return
        if self.is_empty():
            # Adopt Q2's entire chain
            self._head = Q2._head
            self._tail = Q2._tail
            self._size = Q2._size
        else:
            # Link tails/heads in O(1)
            self._tail.next = Q2._head  # type: ignore
            self._tail = Q2._tail
            self._size += Q2._size
        # Empty Q2 in O(1)
        Q2._head = Q2._tail = None
        Q2._size = 0

    def __iter__(self) -> Iterable[Any]:
        cur = self._head
        while cur:
            yield cur.element
            cur = cur.next

    def __repr__(self) -> str:
        return "Queue(front->back): [" + ", ".join(map(str, self)) + "]"
