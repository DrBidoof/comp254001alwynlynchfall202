from CircularlyLinkedList import CircularlyLinkedList

if __name__ == "__main__":
    # Build an original list
    L = CircularlyLinkedList()
    for x in (1, 2, 3, 4, 5):
        L.addLast(x)
    print("Original L:", L)

    # Clone it
    C = L.clone()
    print("Cloned   C:", C)

    # Mutate the original
    L.removeFirst()      # remove head (1)
    L.addLast(99)        # add at tail
    print("\nAfter mutating L:")
    print("Original L:", L)
    print("Cloned   C (should be unchanged):", C)

    # Mutate the clone
    C.addFirst(0)
    C.rotate()
    print("\nAfter mutating C:")
    print("Original L (should be unchanged):", L)
    print("Cloned   C:", C)

    E = CircularlyLinkedList()
    EC = E.clone()
    print("\nEmpty list E:", E)
    print("Cloned empty EC:", EC)

