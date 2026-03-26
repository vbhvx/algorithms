"""
Unit tests for Time Based Key-Value Store Bisect
"""
from algorithms.practice.binary_search.time_based_kv_store import solve_time_based_kv_store

def test_time_based_kv_store_base():
    assert solve_time_based_kv_store() is True
    assert solve_time_based_kv_store([3, 1, 2]) == [1, 2, 3]

def test_time_based_kv_store_edge_cases():
    assert solve_time_based_kv_store("") == ""
    assert solve_time_based_kv_store(0) is True
    assert solve_time_based_kv_store(-5) is False
