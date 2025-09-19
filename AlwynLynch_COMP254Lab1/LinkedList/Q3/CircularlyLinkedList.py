class CircularlyLinkedList:
    """Circularly linked list implementation."""

    class _Node:
        __slots__ = ("element", "next")

        def __init__(self, element, next=None):
            self.element = element
            self.next = next

    def __init__(self):
        """Construct an initially empty list."""
        self.tail = None
        self.size = 0

    # ----- Access methods -----
    def __len__(self):
        """Return number of elements in the list."""
        return self.size

    def is_empty(self):
        """Return True if the list is empty."""
        return self.size == 0

    def first(self):
        """Return (but do not remove) the first element (or None if empty)."""
        if self.is_empty():
            return None
        head = self.tail.next
        return head.element

    def last(self):
        """Return (but do not remove) the last element (or None if empty)."""
        if self.is_empty():
            return None
        return self.tail.element

    # ----- Update methods -----
    def rotate(self):
        """Rotate the first element to the back of the list."""
        if self.tail is not None:  # do nothing if empty
            self.tail = self.tail.next

    def addFirst(self, e):
        """Add element e to the front of the list."""
        if self.size == 0:
            self.tail = self._Node(e, None)
            self.tail.next = self.tail  # circular self-reference
        else:
            newest = self._Node(e, self.tail.next)  # new node points to head
            self.tail.next = newest                 # tail points to newest
        self.size += 1

    def addLast(self, e):
        """Add element e to the end of the list."""
        self.addFirst(e)              # insert new element at front
        self.tail = self.tail.next    # advance tail to the new node

    def removeFirst(self):
        """Remove and return the first element (or None if empty)."""
        if self.is_empty():
            return None
        head = self.tail.next
        if head is self.tail:         # only one node
            self.tail = None
        else:
            self.tail.next = head.next  # bypass the old head
        self.size -= 1
        return head.element

    # ----- Utility -----
    def __str__(self):
        """String representation, like Java's toString()."""
        if self.tail is None:
            return "()"
        result = []
        walk = self.tail
        while True:
            walk = walk.next
            result.append(str(walk.element))
            if walk is self.tail:
                break
        return "(" + ", ".join(result) + ")"

    def clone(self):
        """Return a copy of the circularly linked list (new nodes, same elements)."""
        copy = CircularlyLinkedList()
        if self.is_empty():
            return copy
        walk = self.tail.next  # start at head
        for _ in range(self.size):
            copy.addLast(walk.element)  # new node with same element
            walk = walk.next
        return copy
