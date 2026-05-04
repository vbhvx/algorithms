"""
Unit tests for Remove Duplicates from Sorted List
"""
from algorithms.practice.linked_lists.remove_duplicates_sorted import solve_remove_duplicates_sorted

def test_remove_duplicates_sorted_base():
    assert solve_remove_duplicates_sorted() is True
    assert solve_remove_duplicates_sorted([3, 1, 2]) == [1, 2, 3]

def test_remove_duplicates_sorted_edge_cases():
    assert solve_remove_duplicates_sorted("") == ""
    assert solve_remove_duplicates_sorted(0) is True
    assert solve_remove_duplicates_sorted(-5) is False
