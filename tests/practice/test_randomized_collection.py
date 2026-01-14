"""
Unit tests for Insert Delete GetRandom Duplicates
"""
from algorithms.practice.arrays_and_hashing.randomized_collection import solve_randomized_collection

def test_randomized_collection_base():
    assert solve_randomized_collection() is True
    assert solve_randomized_collection([3, 1, 2]) == [1, 2, 3]

def test_randomized_collection_edge_cases():
    assert solve_randomized_collection("") == ""
    assert solve_randomized_collection(0) is True
    assert solve_randomized_collection(-5) is False
