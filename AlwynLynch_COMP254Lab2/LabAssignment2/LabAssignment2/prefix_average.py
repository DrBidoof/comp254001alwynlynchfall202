# -*- coding: utf-8 -*-
from typing import List

def prefix_average1(x: List[float]) -> List[float]:
    """
    Returns an array a such that, for all j,
    a[j] equals the average of x[0], ..., x[j].
    Naive quadratic-time version.
    """
    n = len(x)
    a = [0.0] * n
    for j in range(n):
        total = 0.0
        for i in range(j + 1):  # sum x[0]..x[j]
            total += x[i]
        a[j] = total / (j + 1)
    return a

def prefix_average2(x: List[float]) -> List[float]:
    """
    Returns an array a such that, for all j,
    a[j] equals the average of x[0], ..., x[j].
    Optimized linear-time version using running total.
    """
    n = len(x)
    a = [0.0] * n
    total = 0.0
    for j in range(n):
        total += x[j]
        a[j] = total / (j + 1)
    return a
