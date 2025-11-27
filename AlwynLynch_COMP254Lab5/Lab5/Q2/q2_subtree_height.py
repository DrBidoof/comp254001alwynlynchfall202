# q2_subtree_height.py
# Computes, for every node p, the height of p's subtree and prints "elem height"
# during the *postorder* visit, as required by the prompt.
#
# Complexity:
#   Time:  O(n) for n nodes (each node visited once)
#   Space: O(h) recursion stack, where h is the tree height
from __future__ import annotations
from typing import Dict, Optional
from q2_gnode import GNode

def compute_and_print_heights(root: Optional[GNode]) -> Dict[GNode, int]:
    """Postorder traversal: print 'elem height' and return a dict of heights."""
    heights: Dict[GNode, int] = {}

    def post(x: GNode) -> int:
        if not x.children:
            h = 0
        else:
            h = 1 + max(post(c) for c in x.children)
        heights[x] = h # Store computed height
        # Friendly I/O: print element followed by computed height (during postorder)
        print(f"{x.elem} {h}")
        return h

    if root:
        post(root)
    return heights
