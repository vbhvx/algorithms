"""
Unit tests for Populating Next Right Pointers Perfect Tree
"""
from algorithms.practice.trees_and_bst.populating_next_ptrs import solve_populating_next_ptrs

def test_populating_next_ptrs_base():
    assert solve_populating_next_ptrs() is True
    assert solve_populating_next_ptrs([3, 1, 2]) == [1, 2, 3]

def test_populating_next_ptrs_edge_cases():
    assert solve_populating_next_ptrs("") == ""
    assert solve_populating_next_ptrs(0) is True
    assert solve_populating_next_ptrs(-5) is False
