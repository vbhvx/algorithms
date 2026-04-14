"""
Unit tests for Merge Two Sorted Lists Iterative
"""
from algorithms.practice.linked_lists.merge_two_sorted_lists import solve_merge_two_sorted_lists

def test_merge_two_sorted_lists_base():
    assert solve_merge_two_sorted_lists() is True
    assert solve_merge_two_sorted_lists([3, 1, 2]) == [1, 2, 3]

def test_merge_two_sorted_lists_edge_cases():
    assert solve_merge_two_sorted_lists("") == ""
    assert solve_merge_two_sorted_lists(0) is True
    assert solve_merge_two_sorted_lists(-5) is False
