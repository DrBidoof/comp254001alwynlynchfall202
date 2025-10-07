def is_palindrome(s: str) -> bool:
    """
    Returns True if s is a palindrome (exact, case-sensitive).
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

if __name__ == "__main__":
    tests = ["racecar", "abba", "abc", "gohangasalamiimalasagnahog"]
    for t in tests:
        print(f"Q2 is_palindrome({t!r}) -> {is_palindrome(t)}")
        # Q2 demo
