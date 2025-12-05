# bst_solution.py

from bst_class import BinarySearchTree, Node


def iterative_tree_search(root: Node, k):
    """Nonrecursive version of TreeSearch for a BST.

    Returns:
        - the Node whose key == k if found (successful search), or
        - the last Node visited on the search path (unsuccessful search),
          or None if the tree is empty.
    """
    walk = root
    last = None

    while walk is not None:
        last = walk
        if k == walk.key:          # found exact match
            return walk
        elif k < walk.key:         # go left if possible
            walk = walk.left
        else:                      # k > walk.key – go right if possible
            walk = walk.right

    # If we leave the loop, search failed.
    # Return the last visited node (same behavior as textbook TreeSearch).
    return last


def bst_iterative_search(tree: BinarySearchTree, k):
    """Convenience wrapper: search by key directly on a BinarySearchTree."""
    return iterative_tree_search(tree.root(), k)
