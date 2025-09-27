# uniqueness.py
# Translation of Goodrich–Tamassia–Goldwasser Uniqueness class from Java to Python.

from typing import List

def unique1(data: List[int]) -> bool:
    """
    Returns True if there are no duplicate elements in the array.
    Quadratic-time algorithm: compares every pair.
    """
    n = len(data)
    for j in range(n - 1):
        for k in range(j + 1, n):
            if data[j] == data[k]:
                return False   # found duplicate pair
    return True                # if we reach this, elements are unique


def unique2(data: List[int]) -> bool:
    """
    Returns True if there are no duplicate elements in the array.
    Uses sorting (O(n log n)) and checks neighbors.
    """
    temp = sorted(data)         # make copy and sort
    n = len(temp)
    for j in range(n - 1):
        if temp[j] == temp[j + 1]:
            return False        # found duplicate pair
    return True                 # if we reach this, elements are unique


# Example usage / quick test
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 1]

    print("unique1(arr1):", unique1(arr1))  # True
    print("unique1(arr2):", unique1(arr2))  # False
    print("unique2(arr1):", unique2(arr1))  # True
    print("unique2(arr2):", unique2(arr2))  # False
