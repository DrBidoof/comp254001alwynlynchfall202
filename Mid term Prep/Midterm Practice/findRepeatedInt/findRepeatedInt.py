def find_repeated_int(A):
    """Return the repeated integer in array A (1 to n-1 inclusive)."""
    found = [False] * len(A)  # all initially False
    for val in A:
        if found[val]:
            return val
        else:
            found[val] = True
    return -1  # shouldn't happen if input is valid

if __name__ == "__main__":
    A = [1, 2, 3, 3, 4, 5]
    print("Repeated integer:", find_repeated_int(A))


