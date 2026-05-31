"""
Unit tests for Populating Next Right Pointers II Any Tree
"""
from algorithms.practice.trees_and_bst.populating_next_ii import solve_populating_next_ii

def test_populating_next_ii_base():
    assert solve_populating_next_ii() is True
    assert solve_populating_next_ii([3, 1, 2]) == [1, 2, 3]

def test_populating_next_ii_edge_cases():
    assert solve_populating_next_ii("") == ""
    assert solve_populating_next_ii(0) is True
    assert solve_populating_next_ii(-5) is False
