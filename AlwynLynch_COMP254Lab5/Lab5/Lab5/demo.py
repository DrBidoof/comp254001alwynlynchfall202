# q1_driver.py
# Build a demo tree and validate the three "next" functions.

from bt_node import BTNode
from traversal_next import inorder_next, preorder_next, postorder_next, _first_postorder

def build_demo_tree() -> BTNode:
    """
    Tree (keys):
            A
                  
         B     C
              
       D   E     F
    Inorder:   D B E A C F
    Preorder:  A B D E C F
    Postorder: D E B F C A
    """
    A = BTNode("A"); B = BTNode("B"); C = BTNode("C")
    D = BTNode("D"); E = BTNode("E"); F = BTNode("F")
    A.set_left(B); A.set_right(C)
    B.set_left(D); B.set_right(E)
    C.set_right(F)
    return A

def inorder_seq(root: BTNode) -> list[str]:
    res: list[str] = []
    def dfs(x: BTNode | None):
        if not x: return
        dfs(x.left); res.append(x.key); dfs(x.right)
    dfs(root)
    return res

def preorder_seq(root: BTNode) -> list[str]:
    res: list[str] = []
    def dfs(x: BTNode | None):
        if not x: return
        res.append(x.key); dfs(x.left); dfs(x.right)
    dfs(root)
    return res

def postorder_seq(root: BTNode) -> list[str]:
    res: list[str] = []
    def dfs(x: BTNode | None):
        if not x: return
        dfs(x.left); dfs(x.right); res.append(x.key)
    dfs(root)
    return res

def leftmost(x: BTNode) -> BTNode:
    while x.left:
        x = x.left
    return x

def main():
    root = build_demo_tree()

    exp_in = inorder_seq(root)
    walked_in = []
    cur = leftmost(root)
    while cur:
        walked_in.append(cur.key)
        cur = inorder_next(cur)

    exp_pre = preorder_seq(root)
    walked_pre = []
    cur = root
    while cur:
        walked_pre.append(cur.key)
        cur = preorder_next(cur)

    exp_post = postorder_seq(root)
    walked_post = []
    cur = _first_postorder(root)
    while cur:
        walked_post.append(cur.key)
        cur = postorder_next(cur)

    print("Inorder expected:        ", exp_in)
    print("Inorder via next():      ", walked_in)
    print("Preorder expected:       ", exp_pre)
    print("Preorder via next():     ", walked_pre)
    print("Postorder expected:      ", exp_post)
    print("Postorder via next():    ", walked_post)

if __name__ == "__main__":
    main()

