from SinglyLinkedList import SinglyLinkedList

if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.add_first("MSP")
    list1.add_last("ATL")
    list1.add_last("BOS")

    list2 = SinglyLinkedList()
    list2.add_first("YYZ")
    list2.add_last("MTRL")
    list2.add_last("OTW")

    print("List 1:", list1)
    print("List 2:", list2)

    concatenated = list1.concatenate_lists(list1, list2)
    print("Concatenated:", concatenated)

    list3 = SinglyLinkedList()
    list3.add_first("MSP")
    list3.add_last("ATL")
    list3.add_last("BOS")

    list4 = SinglyLinkedList()
    list4.add_first("YYZ")
    list4.add_last("MTRL")
    list4.add_last("OTW")

    print("List 3:", list3)
    print("List 4:", list4)

    # Show the element in the second-to-last node
    second_last_node = list3.second_to_last()
    print("Second-to-last element:", second_last_node.element)

