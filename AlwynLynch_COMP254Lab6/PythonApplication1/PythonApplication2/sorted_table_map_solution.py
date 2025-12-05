
from sorted_table_map import SortedTableMap


class SortedTableMapSolution(SortedTableMap):
    """Adds the containsKey(k) method required by Lab 6, Exercise 2."""

    def containsKey(self, k) -> bool:
        """Return True if key k exists in the map, False otherwise."""
        n = len(self._table)
        if n == 0:
            return False

        j = self._find_index(k, 0, n - 1) #position
        return j != n and self._table[j]._key == k #key found
