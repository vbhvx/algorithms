"""Unit test suite for Valid Palindrome Alphanumeric."""
from src.two_pointers.valid_palindrome import ValidPalindromeAlphanumeric

def test_valid_palindrome_basic():
    solver = ValidPalindromeAlphanumeric()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_valid_palindrome_repeated():
    solver = ValidPalindromeAlphanumeric()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
