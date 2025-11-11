# q3_heap.py
from __future__ import annotations
from typing import Any, List, Tuple
from q3_item import Item

class HeapPriorityQueue:
    """
    Min-oriented priority queue implemented with an array-based binary heap.

    Operations:
      add(key, value)   -> O(log n)
      min()             -> O(1)
      remove_min()      -> O(log n)

    Follows the array-based complete binary tree layout and recursive bubbling
    pattern described in Section 9.3.4 of Goodrich, Tamassia, and Goldwasser
    (Data Structures and Algorithms in Python, 2013).
    """

    def __init__(self) -> None:
        self._data: List[Item] = []

    # ----- index helpers -----
    def _parent(self, j: int) -> int: return (j - 1) // 2
    def _left(self, j: int) -> int: return 2 * j + 1
    def _right(self, j: int) -> int: return 2 * j + 2
    def _has_left(self, j: int) -> bool: return self._left(j) < len(self._data)
    def _has_right(self, j: int) -> bool: return self._right(j) < len(self._data)

    # ----- core utilities -----
    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    # recursive upheap
    def _upheap(self, j: int) -> None:
        if j == 0:
            return
        p = self._parent(j)
        if self._data[j] < self._data[p]:
            self._swap(j, p)
            self._upheap(p)

    # recursive downheap
    def _downheap(self, j: int) -> None:
        if not self._has_left(j):
            return
        left = self._left(j)
        small = left
        if self._has_right(j):
            right = self._right(j)
            if self._data[right] < self._data[left]:
                small = right
        if self._data[small] < self._data[j]:
            self._swap(j, small)
            self._downheap(small)

    # ----- public API -----
    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def add(self, key: Any, value: Any) -> None:
        self._data.append(Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self) -> Tuple[Any, Any]:
        if self.is_empty():
            raise IndexError("Priority queue is empty.")
        item = self._data[0]
        return (item.key, item.value)

    def remove_min(self) -> Tuple[Any, Any]:
        if self.is_empty():
            raise IndexError("Priority queue is empty.")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        if self._data:
            self._downheap(0)
        return (item.key, item.value)
