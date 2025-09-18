class DoublyLinkedList:
    """Doubly linked list with header/trailer sentinels."""

    class _Node:
        __slots__ = ("element", "prev", "next")
        def __init__(self, element=None, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.header = self._Node()               # sentinel at front
        self.trailer = self._Node()              # sentinel at back
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, e, predecessor, successor):
        """Insert element e between two existing nodes."""
        newest = self._Node(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def _delete_node(self, node):
        """Remove a non-sentinel node and return its element."""
        pred, succ = node.prev, node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        elem = node.element
        # help GC
        node.prev = node.next = None
        node.element = None
        return elem

    def add_first(self, e):
        return self._insert_between(e, self.header, self.header.next)

    def add_last(self, e):
        return self._insert_between(e, self.trailer.prev, self.trailer)

    def remove_first(self):
        if self.is_empty():
            raise IndexError("remove_first from empty list")
        return self._delete_node(self.header.next)

    def remove_last(self):
        if self.is_empty():
            raise IndexError("remove_last from empty list")
        return self._delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while cursor is not self.trailer:
            yield cursor.element
            cursor = cursor.next

    def __repr__(self):
        return f"DoublyLinkedList([{', '.join(repr(x) for x in self)}])"

    def concatenate(self, other: "DoublyLinkedList"):
        """Concatenate list 'other' to the end of this list."""
        if other.is_empty():
            return

        last_L = self.trailer.prev
        first_M = other.header.next
        last_M = other.trailer.prev

        # splice
        last_L.next = first_M
        first_M.prev = last_L
        self.trailer.prev = last_M
        last_M.next = self.trailer

        self.size += other.size

        # clear 'other'
        other.header.next = other.trailer
        other.trailer.prev = other.header
        other.size = 0
