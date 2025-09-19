from SinglyLinkedList import SinglyLinkedList

if __name__ == "__main__":

    # Helper to print nicely
    def show(title, L):
        print(title, L)

    # Case 1: Normal (non-adjacent swap)
    L = SinglyLinkedList()
    nodes = []
    for x in (1, 2, 3, 4, 5):
        nodes.append(L.add_last(x))
    show("Before (normal swap)", L)
    L.swapNodes(nodes[1], nodes[3])   # swap 2 and 4
    show("After swap (2 <-> 4)", L)
    print("-" * 40)

    # Case 2: Swap same node (no change)
    L = SinglyLinkedList()
    nodes = []
    for x in (1, 2, 3):
        nodes.append(L.add_last(x))
    show("Before (same node)", L)
    L.swapNodes(nodes[1], nodes[1])   # swap 2 with itself
    show("After swap (same node)", L)
    print("-" * 40)

    # Case 3: Swap head with another node
    L = SinglyLinkedList()
    nodes = []
    for x in (1, 2, 3, 4):
        nodes.append(L.add_last(x))
    show("Before (head swap)", L)
    L.swapNodes(nodes[0], nodes[2])   # swap 1 and 3
    show("After swap (1 <-> 3)", L)
    print("-" * 40)

    # Case 4: Swap tail with another node
    L = SinglyLinkedList()
    nodes = []
    for x in (1, 2, 3, 4):
        nodes.append(L.add_last(x))
    show("Before (tail swap)", L)
    L.swapNodes(nodes[1], nodes[3])   # swap 2 and 4 (tail)
    show("After swap (2 <-> 4)", L)
    print("-" * 40)

    # Case 5: Swap adjacent nodes
    L = SinglyLinkedList()
    nodes = []
    for x in (1, 2, 3, 4):
        nodes.append(L.add_last(x))
    show("Before (adjacent swap)", L)
    L.swapNodes(nodes[1], nodes[2])   # swap 2 and 3
    show("After swap (2 <-> 3)", L)
    print("-" * 40)
