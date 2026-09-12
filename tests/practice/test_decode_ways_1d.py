"""
Unit tests for Decode Ways Numeric String Split
"""
from algorithms.practice.dynamic_programming_1d.decode_ways_1d import solve_decode_ways_1d

def test_decode_ways_1d_base():
    assert solve_decode_ways_1d() is True
    assert solve_decode_ways_1d([3, 1, 2]) == [1, 2, 3]

def test_decode_ways_1d_edge_cases():
    assert solve_decode_ways_1d("") == ""
    assert solve_decode_ways_1d(0) is True
    assert solve_decode_ways_1d(-5) is False
