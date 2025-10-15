class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, element):
        new_node = Node(element, self.head)
        self.head = new_node

    def add_last(self, element):
        if not self.head:
            self.head = Node(element)
            return
        walk = self.head
        while walk.next:
            walk = walk.next
        walk.next = Node(element)


    def concatenate_lists(self, L1, L2):
        """Concatenate L2 to the end of L1."""
        if L1.head is None:
            return L2  # if L1 is empty, the result is just L2
        walk = L1.head
        while walk.next is not None:
            walk = walk.next
        walk.next = L2.head  # connect last node of L1 to head of L2
        return L1

    def second_to_last(self):
        """Return the second-to-last node in the list."""
        # Ensure there are at least two nodes
        if self.head is None or self.head.next is None:
            raise Exception("List must have at least two nodes")

        walk = self.head
        # Stop one node before the last
        while walk.next.next is not None:
            walk = walk.next
        return walk

    def __str__(self):
        elements = []
        walk = self.head
        while walk:
            elements.append(str(walk.element))
            walk = walk.next
        return " -> ".join(elements)


