"""
Unit tests for Add Two Numbers II Most Significant Stack
"""
from algorithms.practice.linked_lists.add_two_numbers_ii import solve_add_two_numbers_ii

def test_add_two_numbers_ii_base():
    assert solve_add_two_numbers_ii() is True
    assert solve_add_two_numbers_ii([3, 1, 2]) == [1, 2, 3]

def test_add_two_numbers_ii_edge_cases():
    assert solve_add_two_numbers_ii("") == ""
    assert solve_add_two_numbers_ii(0) is True
    assert solve_add_two_numbers_ii(-5) is False
