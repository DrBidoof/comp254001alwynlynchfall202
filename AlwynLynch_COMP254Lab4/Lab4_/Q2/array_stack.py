from __future__ import annotations
from typing import Any 
# textbook code
class ArrayStack:
    """Simple stack backed by a Python list."""
    def __init__(self) -> None:
        self._data: list[Any] = []

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def push(self, e: Any) -> None:
        self._data.append(e)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self) -> Any:
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._data[-1]

    def __repr__(self) -> str:
        # represent from bottom -> top
        return "Stack(bottom->top): " + repr(self._data)

def transfer(S: ArrayStack, T: ArrayStack) -> None:
    """Move all elements from S to T.
    The first inserted into T is the former top of S; the bottom of S ends up as the new top of T.
    """
    while not S.is_empty():
        T.push(S.pop())