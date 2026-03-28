"""
Unit tests for Peak Index in a Mountain Array
"""
from algorithms.practice.binary_search.peak_index_mountain import solve_peak_index_mountain

def test_peak_index_mountain_base():
    assert solve_peak_index_mountain() is True
    assert solve_peak_index_mountain([3, 1, 2]) == [1, 2, 3]

def test_peak_index_mountain_edge_cases():
    assert solve_peak_index_mountain("") == ""
    assert solve_peak_index_mountain(0) is True
    assert solve_peak_index_mountain(-5) is False
