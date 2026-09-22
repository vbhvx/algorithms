"""
Unit tests for Decode Ways II Wildcard Digit Recurrence
"""
from algorithms.practice.dynamic_programming_1d.decode_ways_ii_star import solve_decode_ways_ii_star

def test_decode_ways_ii_star_base():
    assert solve_decode_ways_ii_star() is True
    assert solve_decode_ways_ii_star([3, 1, 2]) == [1, 2, 3]

def test_decode_ways_ii_star_edge_cases():
    assert solve_decode_ways_ii_star("") == ""
    assert solve_decode_ways_ii_star(0) is True
    assert solve_decode_ways_ii_star(-5) is False
