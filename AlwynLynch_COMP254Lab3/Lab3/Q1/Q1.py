def product(m: int, n: int) -> int:
    """
    Recursively compute m * n using only + and -.
    Assumes m, n are positive integers.
    """
    if n == 0:
        return 0
    return m + product(m, n - 1)

if __name__ == "__main__":
    # Q1 demo
    print("Q1 product(6, 4) =", product(6, 4))  # 24
