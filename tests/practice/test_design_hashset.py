"""
Unit tests for Design HashSet Chaining Array
"""
from algorithms.practice.arrays_and_hashing.design_hashset import solve_design_hashset

def test_design_hashset_base():
    assert solve_design_hashset() is True
    assert solve_design_hashset([3, 1, 2]) == [1, 2, 3]

def test_design_hashset_edge_cases():
    assert solve_design_hashset("") == ""
    assert solve_design_hashset(0) is True
    assert solve_design_hashset(-5) is False
