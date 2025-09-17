class Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = ("element", "next")

    def __init__(self, element, next=None):
        self.element = element      # data stored in this node
        self.next = next            # link to the next node

class SinglyLinkedList:
    """Singly linked list with head and tail references."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        """Insert element at the beginning."""
        newest = Node(e, self.head)
        self.head = newest
        if self.size == 0:
            self.tail = newest
        self.size += 1

    def add_last(self, e):
        """Insert element at the end."""
        newest = Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def __iter__(self):
        cursor = self.head
        while cursor:
            yield cursor.element
            cursor = cursor.next

    def __repr__(self):
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

