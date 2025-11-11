# traversal_next.py
# Worst-case running time for each:
#   preorder_next:   O(h)
#   inorder_next:    O(h)
#   postorder_next:  O(h)
# where h is the tree height. Space: O(1) auxiliary.
from __future__ import annotations
from typing import Optional
from bt_node import BTNode

def inorder_next(p: Optional[BTNode]) -> Optional[BTNode]:
    """Return the node visited after p in an inorder traversal, or None if last."""
    if p is None:
        return None
    if p.right:
        return _leftmost(p.right)
    cur = p
    while cur.parent and cur is cur.parent.right:
        cur = cur.parent
    return cur.parent

def preorder_next(p: Optional[BTNode]) -> Optional[BTNode]:
    """Return the node visited after p in a preorder traversal, or None if last."""
    if p is None:
        return None
    if p.left:
        return p.left
    if p.right:
        return p.right
    cur = p
    while cur.parent:
        if cur is cur.parent.left and cur.parent.right:
            return cur.parent.right
        cur = cur.parent
    return None

def postorder_next(p: Optional[BTNode]) -> Optional[BTNode]:
    """Return the node visited after p in a postorder traversal, or None if last."""
    if p is None or p.parent is None:
        return None  # root is last in postorder
    u = p.parent
    if p is u.left and u.right:
        return _first_postorder(u.right)
    return u

# ----- helpers (kept public-ish for use in driver) -----
def _leftmost(x: BTNode) -> BTNode:
    while x.left:
        x = x.left
    return x

def _first_postorder(x: BTNode) -> BTNode:
    cur = x
    while True:
        if cur.left:
            cur = cur.left
        elif cur.right:
            cur = cur.right
        else:
            return cur
