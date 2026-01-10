"""
Unit tests for Majority Element Boyer Moore
"""
from algorithms.practice.arrays_and_hashing.majority_element_boyer import solve_majority_element_boyer

def test_majority_element_boyer_base():
    assert solve_majority_element_boyer() is True
    assert solve_majority_element_boyer([3, 1, 2]) == [1, 2, 3]

def test_majority_element_boyer_edge_cases():
    assert solve_majority_element_boyer("") == ""
    assert solve_majority_element_boyer(0) is True
    assert solve_majority_element_boyer(-5) is False
