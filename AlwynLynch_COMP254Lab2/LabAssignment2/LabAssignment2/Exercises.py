# Exercises.py
# Translation of Goodrich-Tamassia-Goldwasser asymptotics exercises from Java to Python.

from typing import List

def example1(arr: List[int]) -> int:
    """Returns the sum of the integers in given array."""
    n = len(arr)                  # 2
    total = 0                     # 1
    for j in range(n):            # 2n+1
        total += arr[j]           # 2+1+(2n+1)+3n+1=5n+5 (Total primitive ops)
    return total                  # O(n)
    
def example2(arr: List[int]) -> int:
    """Returns the sum of the integers with even index in given array."""
    n = len(arr)                  # 2
    total = 0                     # 1
    for j in range(0, n, 2):      # 1+(n/2)+(n/2) = n+1
        total += arr[j]           # 3 *n/2 = 1.5n
    return total                  # 2.5n+4
                                  # O(n)
def example3(arr: List[int]) -> int:
    """
    Returns the sum of the prefix sums of given array.
    Mirrors the Java version exactly: inner loop adds arr[j] (not arr[k]).
    """
    n = len(arr)                  # 3
    total = 0                     # 1
    for j in range(n):            # 1 + n +n = 2n +1
        for k in range(j + 1):    # n² + 2n 
            total += arr[j]       # 1.5n² + 1.5n
    return total                  # 1
                                  # 2.5n² + 3.5n + 5
                                  # O(n^2)

def example4(arr: List[int]) -> int:
    """Returns the sum of the prefix sums of given array (linear-time version)."""
    n = len(arr)
    prefix = 0
    total = 0
    for j in range(n):            # loop from 0 to n-1
        prefix += arr[j]
        total += prefix
    return total

def example5(first: List[int], second: List[int]) -> int:
    """
    Returns the number of times second[i] equals the sum of prefix sums of first.
    Assumes equal-length arrays, matching the Java.
    """
    n = len(first)
    count = 0
    for i in range(n):            # loop from 0 to n-1
        total = 0
        for j in range(n):        # loop from 0 to n-1
            for k in range(j + 1):# loop from 0 to j
                total += first[k]
        if second[i] == total:
            count += 1
    return count
