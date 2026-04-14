"""
Unit tests for Online Majority Element In Subarray
"""
from algorithms.practice.binary_search.online_majority_sub import solve_online_majority_sub

def test_online_majority_sub_base():
    assert solve_online_majority_sub() is True
    assert solve_online_majority_sub([3, 1, 2]) == [1, 2, 3]

def test_online_majority_sub_edge_cases():
    assert solve_online_majority_sub("") == ""
    assert solve_online_majority_sub(0) is True
    assert solve_online_majority_sub(-5) is False
