from DoublelyLinkedList import DoublyLinkedList

if __name__ == "__main__":
    # Case 1: Normal concatenate (both non-empty)
    L = DoublyLinkedList()
    M = DoublyLinkedList()

    for x in (1, 2, 3):
        L.add_last(x)
    for x in (4, 5, 6):
        M.add_last(x)

    print("CASE 1: Both non-empty")
    print("Before:")
    print("L:", L)
    print("M:", M)

    L.concatenate(M)

    print("After concatenate:")
    print("L:", L)   # expect [1, 2, 3, 4, 5, 6]
    print("M:", M)   # expect [] (emptied out)
    print("-" * 40)


    # Case 2: Concatenate with empty M
    L = DoublyLinkedList()
    M = DoublyLinkedList()
    for x in (1, 2, 3):
        L.add_last(x)

    print("CASE 2: Concatenate with empty M")
    print("Before:")
    print("L:", L)
    print("M:", M)

    L.concatenate(M)

    print("After concatenate:")
    print("L:", L)   # expect [1, 2, 3]
    print("M:", M)   # expect []
    print("-" * 40)


    # Case 3: Concatenate empty L with non-empty M
    L = DoublyLinkedList()
    M = DoublyLinkedList()
    for x in (4, 5, 6):
        M.add_last(x)

    print("CASE 3: Concatenate empty L with non-empty M")
    print("Before:")
    print("L:", L)
    print("M:", M)

    L.concatenate(M)

    print("After concatenate:")
    print("L:", L)   # expect [4, 5, 6]
    print("M:", M)   # expect []
    print("-" * 40)


    # Case 4: Both lists empty
    L = DoublyLinkedList()
    M = DoublyLinkedList()

    print("CASE 4: Both empty")
    print("Before:")
    print("L:", L)
    print("M:", M)

    L.concatenate(M)

    print("After concatenate:")
    print("L:", L)   # expect []
    print("M:", M)   # expect []
    print("-" * 20)
