# q2_driver.py
# Builds a small general tree and runs compute_and_print_heights to demonstrate output.
from q2_gnode import GNode
from q2_subtree_height import compute_and_print_heights

def build_demo_tree() -> GNode:
    r"""
    Example general tree:
        A
      / | \
     B  C  D
       / \
      E   F

    Expected heights:
      E=0, F=0, C=1, B=0, D=0, A=2
    (Printed in postorder visit order.)
    """
    A = GNode("A")
    B = GNode("B")
    C = GNode("C")
    D = GNode("D")
    E = GNode("E")
    F = GNode("F")

    A.add_child(B)
    A.add_child(C)
    A.add_child(D)
    C.add_child(E)
    C.add_child(F)
    return A

def main():
    root = build_demo_tree()
    # Prints "elem height" during postorder
    _ = compute_and_print_heights(root)

if __name__ == "__main__":
    main()

