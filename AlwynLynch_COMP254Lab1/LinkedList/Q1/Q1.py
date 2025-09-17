from DoublelyLinkedList import DoublyLinkedList

if __name__ == "__main__":
    L = DoublyLinkedList()
    M = DoublyLinkedList()

    for x in (1, 2, 3):
        L.add_last(x)
    for x in (4, 5, 6):
        M.add_last(x)

    print("Before:")
    print("L:", L)
    print("M:", M)

    L.concatenate(M)

    print("\nAfter concatenate:")
    print("L:", L)
    print("M:", M)