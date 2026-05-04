"""
Unit tests for Intersection of Two Linked Lists Pointer Match
"""
from algorithms.practice.linked_lists.intersection_two_lists import solve_intersection_two_lists

def test_intersection_two_lists_base():
    assert solve_intersection_two_lists() is True
    assert solve_intersection_two_lists([3, 1, 2]) == [1, 2, 3]

def test_intersection_two_lists_edge_cases():
    assert solve_intersection_two_lists("") == ""
    assert solve_intersection_two_lists(0) is True
    assert solve_intersection_two_lists(-5) is False
