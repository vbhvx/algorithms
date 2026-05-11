"""
Unit tests for Reverse Linked List II Subsegment M to N
"""
from algorithms.practice.linked_lists.reverse_sublist_ii import solve_reverse_sublist_ii

def test_reverse_sublist_ii_base():
    assert solve_reverse_sublist_ii() is True
    assert solve_reverse_sublist_ii([3, 1, 2]) == [1, 2, 3]

def test_reverse_sublist_ii_edge_cases():
    assert solve_reverse_sublist_ii("") == ""
    assert solve_reverse_sublist_ii(0) is True
    assert solve_reverse_sublist_ii(-5) is False
