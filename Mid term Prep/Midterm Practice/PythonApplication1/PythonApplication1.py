def reverse(s):
    """Recursively print the reverse of a string."""
    reverse_helper(s, len(s) - 1)


def reverse_helper(s, n):
    """Helper function to handle recursion by index."""
    if n >= 0:
        print(s[n], end="")  # print character without newline
        reverse_helper(s, n - 1)

if __name__ == "__main__":
    s = "pots&pans"
    print("Original:", s)
    print("Reversed:", end=" ")
    reverse(s)
    print()  # newline after recursion finishes

