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

    def remove_first(self):
        if self.head is None:              # list empty
            raise IndexError("remove_first from empty list")
        self.head = self.head.next         # move head forward
        self.size -= 1                     # shrink size
        if self.size == 0:                 # if list became empty
            self.tail = None               # reset tail as well

    def swapNodes(self, node1, node2):
        """Swap two nodes given their references (not just their data)."""
        if node1 == node2:
            return  # nothing to do

        # Find previous nodes
        prev1 = prev2 = None
        curr = self.head
        while curr and (not prev1 or not prev2):
            if curr.next == node1:
                prev1 = curr
            if curr.next == node2:
                prev2 = curr
            curr = curr.next

        # If either node not in list, do nothing
        if not node1 or not node2:
            return

        # If node1 is not head
        if prev1:
            prev1.next = node2
        else:
            self.head = node2

        # If node2 is not head
        if prev2:
            prev2.next = node1
        else:
            self.head = node1

        # Swap next pointers
        node1.next, node2.next = node2.next, node1.next

        # Fix tail if needed
        if node1.next is None:
            self.tail = node1
        if node2.next is None:
            self.tail = node2

