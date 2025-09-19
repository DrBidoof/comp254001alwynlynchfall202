class SinglyLinkedList:
    """Singly linked list with head and tail references."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = ("element", "next")

        def __init__(self, element, next=None):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        """Return (but do not remove) the first element of the list, or None if empty."""
        if self.is_empty():
            return None
        return self.head.element

    def last(self):
        """Return (but do not remove) the last element of the list, or None if empty."""
        if self.is_empty():
            return None
        return self.tail.element

    def add_first(self, e):
        """Insert element at the beginning. Returns the new node (so caller can keep a reference)."""
        newest = self._Node(e, self.head)
        self.head = newest
        if self.size == 0:
            self.tail = newest
        self.size += 1
        return newest

    def add_last(self, e):
        """Insert element at the end. Returns the new node (so caller can keep a reference)."""
        newest = self._Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
        return newest

    def remove_first(self):
        """Remove and return the first element; raise if empty."""
        if self.head is None:
            raise IndexError("remove_first from empty list")
        elem = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return elem

    def __iter__(self):
        cursor = self.head
        while cursor:
            yield cursor.element
            cursor = cursor.next

    def __repr__(self):
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

    def swapNodes(self, node1, node2):
        """Swap two nodes given their node references (swap links, not data)."""
        if node1 is None or node2 is None:
            raise ValueError("Cannot swap None nodes.")
        if node1 is node2:
            return  # nothing to do

        # Find previous nodes
        prev1 = prev2 = None
        curr = self.head
        while curr and (prev1 is None or prev2 is None):
            if curr.next is node1:
                prev1 = curr
            if curr.next is node2:
                prev2 = curr
            curr = curr.next

        # Ensure both nodes are in the list
        if (node1 is not self.head and prev1 is None) or (node2 is not self.head and prev2 is None):
            return  # nodes not in this list

        # Case: node1 is immediately before node2
        if node1.next is node2:
            if prev1:
                prev1.next = node2
            else:
                self.head = node2
            node1.next = node2.next
            node2.next = node1

        # Case: node2 is immediately before node1
        elif node2.next is node1:
            if prev2:
                prev2.next = node1
            else:
                self.head = node1
            node2.next = node1.next
            node1.next = node2

        # General non-adjacent case
        else:
            if prev1:
                prev1.next = node2
            else:
                self.head = node2
            if prev2:
                prev2.next = node1
            else:
                self.head = node1
            node1.next, node2.next = node2.next, node1.next

        # Fix tail if needed
        if node1.next is None:
            self.tail = node1
        elif node2.next is None:
            self.tail = node2

