"""
Unit tests for Maximum Twin Sum of Linked List
"""
from algorithms.practice.linked_lists.max_twin_sum_list import solve_max_twin_sum_list

def test_max_twin_sum_list_base():
    assert solve_max_twin_sum_list() is True
    assert solve_max_twin_sum_list([3, 1, 2]) == [1, 2, 3]

def test_max_twin_sum_list_edge_cases():
    assert solve_max_twin_sum_list("") == ""
    assert solve_max_twin_sum_list(0) is True
    assert solve_max_twin_sum_list(-5) is False
