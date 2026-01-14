"""
Unit tests for Insert Delete GetRandom O1
"""
from algorithms.practice.arrays_and_hashing.randomized_set import solve_randomized_set

def test_randomized_set_base():
    assert solve_randomized_set() is True
    assert solve_randomized_set([3, 1, 2]) == [1, 2, 3]

def test_randomized_set_edge_cases():
    assert solve_randomized_set("") == ""
    assert solve_randomized_set(0) is True
    assert solve_randomized_set(-5) is False
