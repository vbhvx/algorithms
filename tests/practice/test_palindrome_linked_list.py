"""
Unit tests for Palindrome Linked List In Place Mid Reverse
"""
from algorithms.practice.linked_lists.palindrome_linked_list import solve_palindrome_linked_list

def test_palindrome_linked_list_base():
    assert solve_palindrome_linked_list() is True
    assert solve_palindrome_linked_list([3, 1, 2]) == [1, 2, 3]

def test_palindrome_linked_list_edge_cases():
    assert solve_palindrome_linked_list("") == ""
    assert solve_palindrome_linked_list(0) is True
    assert solve_palindrome_linked_list(-5) is False
