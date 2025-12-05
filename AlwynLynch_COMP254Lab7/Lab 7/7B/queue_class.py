# queue_class.py

class Empty(Exception):
    """Custom exception to indicate an attempt to access from an empty container."""
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list."""

    class _Node:
        __slots__ = "element", "next"

        def __init__(self, element, next=None):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front."""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head.element

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        new_node = self._Node(e)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the element from the front."""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def __iter__(self):
        """Iterate over the elements from front to back."""
        walk = self._head
        while walk is not None:
            yield walk.element
            walk = walk.next
