
from __future__ import annotations
from array_stack import ArrayStack

def transfer(S: ArrayStack, T: ArrayStack) -> None:
    """
    Transfer all elements from stack S onto stack T.
    Result: former top(S) is inserted first into T; former bottom(S) becomes new top(T).
    Runs in O(n) time with O(1) extra space.
    """
    while not S.is_empty():
        T.push(S.pop())
