# ans_q3.py
from linked_queue import LinkedQueue

class AnswerLinkedQueue(LinkedQueue):
    """Extended LinkedQueue with O(1) concatenate(Q2) method."""

    def concatenate(self, Q2: "AnswerLinkedQueue") -> None:
        """Append all nodes of Q2 to this queue in O(1) time, leaving Q2 empty."""
        if Q2.is_empty():
            return

        if self.is_empty():
            # Adopt Q2's chain entirely
            self._head = Q2._head
            self._tail = Q2._tail
            self._size = Q2._size
        else:
            # Link tails/heads directly
            self._tail.next = Q2._head  # type: ignore
            self._tail = Q2._tail
            self._size += Q2._size

        # Clear Q2 in O(1)
        Q2._head = Q2._tail = None
        Q2._size = 0