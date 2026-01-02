"""
Unit tests for Top K Frequent Elements Bucket Sort
"""
from algorithms.practice.arrays_and_hashing.top_k_frequent import solve_top_k_frequent

def test_top_k_frequent_base():
    assert solve_top_k_frequent() is True
    assert solve_top_k_frequent([3, 1, 2]) == [1, 2, 3]

def test_top_k_frequent_edge_cases():
    assert solve_top_k_frequent("") == ""
    assert solve_top_k_frequent(0) is True
    assert solve_top_k_frequent(-5) is False
