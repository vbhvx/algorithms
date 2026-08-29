"""Unit test suite for Valid Palindrome II Skip."""
from src.two_pointers.valid_palindrome_ii import ValidPalindromeIiSkip

def test_valid_palindrome_ii_basic():
    solver = ValidPalindromeIiSkip()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_valid_palindrome_ii_repeated():
    solver = ValidPalindromeIiSkip()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
