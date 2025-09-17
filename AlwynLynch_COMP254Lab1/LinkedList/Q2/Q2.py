from SinglyLinkedList import SinglyLinkedList

if __name__ == "__main__":
    L = SinglyLinkedList()
    nodes = []

    # Build list and keep references
    for x in (1, 2, 3, 4, 5):
        L.add_last(x)
        if L.tail:  # store actual Node references
            nodes.append(L.tail)

    print("Before swap:")
    print(L)

    # Swap node 2 and node 4
    L.swapNodes(nodes[1], nodes[3])

    print("\nAfter swap (2 <-> 4):")
    print(L)