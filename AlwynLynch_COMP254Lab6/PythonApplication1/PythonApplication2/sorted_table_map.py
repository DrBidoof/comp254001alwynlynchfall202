
from map_base import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table (Goodrich & Tamassia textbook)."""

    # --------------------------- nonpublic ---------------------------
    def _find_index(self, k, low, high):
        """Return index of leftmost item with key >= k, or high+1 if none."""
        if high < low:
            return high + 1
        mid = (low + high) // 2
        if self._table[mid]._key == k:
            return mid
        elif k < self._table[mid]._key:
            return self._find_index(k, low, mid - 1)
        else:
            return self._find_index(k, mid + 1, high)

    # --------------------------- public ------------------------------
    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        if len(self._table) == 0:
            raise KeyError(f"Key Error: {k!r}")
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError(f"Key Error: {k!r}")
        return self._table[j]._value

    def __setitem__(self, k, v):
        if len(self._table) == 0:
            self._table.append(self._Item(k, v))
            return
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        if len(self._table) == 0:
            raise KeyError(f"Key Error: {k!r}")
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError(f"Key Error: {k!r}")
        self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item._key
