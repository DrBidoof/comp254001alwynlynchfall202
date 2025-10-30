# driver_q1.py
from Ans import ExtendedPositionalList


def main():
    print("== Q1 Driver: indexOf(p) on Positional List ==")
    L = ExtendedPositionalList()
    p1 = L.add_last("A")
    p2 = L.add_last("B")
    p3 = L.add_last("C")
    p4 = L.add_last("D")
    print("List:", L)

    print("indexOf(p1) ->", L.indexOf(p1))  # 0
    print("indexOf(p3) ->", L.indexOf(p3))  # 2
    print("indexOf(p4) ->", L.indexOf(p4))  # 3

    # Negative test: position from another list should raise ValueError
    other = ExtendedPositionalList()
    foreign = other.add_last("X")
    try:
        L.indexOf(foreign)
    except ValueError as e:
        print("Foreign position test ->", e)

    # Show iteration via public positions()
    print("Elements via positions():", [pos.element() for pos in L.positions()])

if __name__ == "__main__":
    main()
