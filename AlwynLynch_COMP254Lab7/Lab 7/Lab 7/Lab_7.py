# bst_demo.py

from bst_class import BinarySearchTree
from bst_solution import bst_iterative_search


def build_unbalanced_bst():
    """Build a deliberately unbalanced BST to show no recursion limit issues."""
    bst = BinarySearchTree()
    # Insert in ascending order to create a tall, right-skewed tree
    for key in [10, 20, 30, 40, 50, 60, 70]:
        bst.insert(key)
    return bst


def main():
    bst = build_unbalanced_bst()

    for target in [10, 50, 75]:
        node = bst_iterative_search(bst, target)
        if node is not None and node.key == target:
            print(f"Search for {target}: FOUND at node with key {node.key}")
        elif node is not None:
            print(
                f"Search for {target}: NOT FOUND; stopped at node with key {node.key}"
            )
        else:
            print(f"Search for {target}: tree is empty")

if __name__ == "__main__":
    main()

