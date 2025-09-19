class CircularlyLinkedList:
    """Circularly linked list storing elements; tail points to last node, tail.next is head."""

    class _Node:
        __slots__ = ("element", "next")
        def __init__(self, element, next=None):
            self.element = element
            self.next = next
