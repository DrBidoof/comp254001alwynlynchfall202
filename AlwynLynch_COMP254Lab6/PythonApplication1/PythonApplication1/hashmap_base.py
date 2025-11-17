# hashmap_base.py
from collections.abc import MutableMapping
import random

class HashMapBase(MutableMapping):
    """Base class for hash maps with configurable max load factor."""

    _DEFAULT_PRIME = 109345121

    def __init__(self, capacity=11, max_load=0.5):
        
        self._table = [None] * capacity
        self._n = 0
        self._prime = HashMapBase._DEFAULT_PRIME
        self._scale = 1 + random.randrange(self._prime - 1)
        self._shift = random.randrange(self._prime)
        self._max_load = max_load

    # ---------- public API required by MutableMapping ----------

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        j = self._hash_function(key)
        return self._bucket_getitem(j, key)

    def __setitem__(self, key, value):
        j = self._hash_function(key)
        old_size = self._n
        self._bucket_setitem(j, key, value)
        # if a *new* item was added, check load factor
        if self._n > old_size:
            if self.load_factor() > self._max_load:
                self._resize(2 * len(self._table))

    def __delitem__(self, key):
        j = self._hash_function(key)
        self._bucket_delitem(j, key)
        self._n -= 1

    def __iter__(self):
        for bucket in self._table:
            if bucket is None:
                continue
            # delegate to concrete bucket iterator implementation
            for key in self._bucket_iter_from_bucket(bucket):
                yield key

    # ---------- helper / utility methods ----------

    def load_factor(self):
       
        return self._n / len(self._table)

    def _hash_function(self, key):
        
        return ( (hash(key) * self._scale + self._shift) % self._prime ) % len(self._table)

    def _resize(self, new_cap):
        """Resize bucket array to new_cap and rehash all existing items."""
        old_items = [(k, self[k]) for k in self]  # iterate over existing keys
        self._table = [None] * new_cap
        self._n = 0
        # new random parameters for the hash function
        self._scale = 1 + random.randrange(self._prime - 1)
        self._shift = random.randrange(self._prime)
        for (k, v) in old_items:
            self[k] = v

    # ---------- abstract bucket methods (template methods) ----------

    def _bucket_getitem(self, j, key):
        """Get item from bucket at index j; must be implemented by subclasses."""
        raise NotImplementedError()

    def _bucket_setitem(self, j, key, value):
        """Insert/update item in bucket at index j; must be implemented by subclasses."""
        raise NotImplementedError()

    def _bucket_delitem(self, j, key):
        """Delete item from bucket at index j; must be implemented by subclasses."""
        raise NotImplementedError()

    def _bucket_iter_from_bucket(self, bucket):
        """Iterate keys stored in the given bucket structure."""
        raise NotImplementedError()


# =====================================================================
# Separate chaining implementation
# =====================================================================

class ChainHashMap(HashMapBase):
    """Hash map with separate chaining using Python lists for buckets."""

    def _bucket_getitem(self, j, key):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f"Key not found: {key}")
        for (k, v) in bucket:
            if k == key:
                return v
        raise KeyError(f"Key not found: {key}")

    def _bucket_setitem(self, j, key, value):
        if self._table[j] is None:
            self._table[j] = []
        bucket = self._table[j]
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)   # update
                return
        bucket.append((key, value))         # new item
        self._n += 1

    def _bucket_delitem(self, j, key):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f"Key not found: {key}")
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(idx)
                return
        raise KeyError(f"Key not found: {key}")

    def _bucket_iter_from_bucket(self, bucket):
        # bucket is a list of (key, value) pairs
        for (k, v) in bucket:
            yield k


# =====================================================================
# Open addressing with linear probing
# =====================================================================

class ProbeHashMap(HashMapBase):
    """Hash map with open addressing and linear probing."""

    _AVAIL = object()   # sentinel for deleted slots

    def __init__(self, capacity=11, max_load=0.5):
        super().__init__(capacity=capacity, max_load=max_load)

    # override iterator because buckets are not lists here
    def __iter__(self):
        for entry in self._table:
            if entry is not None and entry is not ProbeHashMap._AVAIL:
                (k, v) = entry
                yield k

    # private helper
    def _find_slot(self, j, key):
        """
        Search for key starting at index j.
        Returns (found, index):
          - found = True, index where key resides
          - found = False, index of first empty/available slot for insertion
        """
        first_avail = None
        N = len(self._table)
        while True:
            entry = self._table[j]
            if entry is None:
                # empty slot: key not present
                return (False, first_avail or j)
            elif entry is ProbeHashMap._AVAIL:
                if first_avail is None:
                    first_avail = j
            else:
                k, _ = entry
                if k == key:
                    return (True, j)
            j = (j + 1) % N

    # bucket-specific methods use the probe logic

    def _bucket_getitem(self, j, key):
        found, idx = self._find_slot(j, key)
        if not found:
            raise KeyError(f"Key not found: {key}")
        return self._table[idx][1]

    def _bucket_setitem(self, j, key, value):
        found, idx = self._find_slot(j, key)
        if found:
            self._table[idx] = (key, value)   # update
        else:
            self._table[idx] = (key, value)   # new item
            self._n += 1

    def _bucket_delitem(self, j, key):
        found, idx = self._find_slot(j, key)
        if not found:
            raise KeyError(f"Key not found: {key}")
        self._table[idx] = ProbeHashMap._AVAIL

    def _bucket_iter_from_bucket(self, bucket):
        """
        Not used in this implementation because buckets are individual cells.
        Required by the base class, so we just raise if ever called accidentally.
        """
        raise RuntimeError("ProbeHashMap does not use bucket-based iteration")
