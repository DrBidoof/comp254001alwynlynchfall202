# driver_q2.py
from array_stack import ArrayStack
from q2_solution import transfer

def main():
    print("== Exercise 2 Driver: transfer(S, T) ==")
    S = ArrayStack()
    for x in [1, 2, 3, 4]:   # 4 is top of S
        S.push(x)
    T = ArrayStack()

    print("Before transfer:")
    print("S:", S)  # Stack(bottom->top): [1, 2, 3, 4]
    print("T:", T)  # empty

    transfer(S, T)

    print("After transfer (S emptied; bottom of S (1) now top of T):")
    print("S:", S)  # empty
    print("T:", T)  # Stack(bottom->top): [4, 3, 2, 1]

    # Verify order by popping T: expect 1, 2, 3, 4
    popped = []
    while not T.is_empty():
        popped.append(T.pop())
    print("Pop sequence from T (expect [1, 2, 3, 4]):", popped)

if __name__ == "__main__":
    main()
