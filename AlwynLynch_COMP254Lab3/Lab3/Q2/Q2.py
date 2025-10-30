def is_palindrome(myword: str) -> bool:
    """
    Returns True if s is a palindrome (exact, case-sensitive).
    """
    if len(myword) <= 1:
        return True # base case
    if myword[0] != myword[-1]:
        return False # base case
    return is_palindrome(myword[1:-1])

if __name__ == "__main__":
    tests = ["racecar", "abba", "abc", "gohangasalamiimalasagnahog"]
    for t in tests:
        print(f"Q2 is_palindrome({t!r}) -> {is_palindrome(t)}")
        # Q2 demo
