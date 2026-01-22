"""
Unit tests for Design HashMap Chaining Array
"""
from algorithms.practice.arrays_and_hashing.design_hashmap import solve_design_hashmap

def test_design_hashmap_base():
    assert solve_design_hashmap() is True
    assert solve_design_hashmap([3, 1, 2]) == [1, 2, 3]

def test_design_hashmap_edge_cases():
    assert solve_design_hashmap("") == ""
    assert solve_design_hashmap(0) is True
    assert solve_design_hashmap(-5) is False
