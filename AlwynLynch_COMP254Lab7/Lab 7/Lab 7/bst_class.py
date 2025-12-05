# bst_class.py

class Node:
    """Simple node for a binary search tree."""
    __slots__ = "key", "left", "right"

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    """Minimal BST supporting insertion and root access."""

    def __init__(self):
        self._root = None

    def root(self):
        """Return the root node."""
        return self._root

    def insert(self, key):
        """Insert key into the BST (iterative).

        Returns the Node storing the key.
        """
        if self._root is None:
            self._root = Node(key)
            return self._root

        walk = self._root
        parent = None

        while walk is not None:
            parent = walk
            if key < walk.key:
                walk = walk.left
            elif key > walk.key:
                walk = walk.right
            else:
                # duplicate key – do nothing, return existing node
                return walk

        new_node = Node(key)
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node
