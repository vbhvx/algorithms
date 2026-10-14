"""
Unit tests for Count Ways to Build Good Strings Modular DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.ways_build_good_strings import solve_ways_build_good_strings

def test_ways_build_good_strings_base():
    assert solve_ways_build_good_strings() is True
    assert solve_ways_build_good_strings([3, 1, 2]) == [1, 2, 3]

def test_ways_build_good_strings_edge_cases():
    assert solve_ways_build_good_strings("") == ""
    assert solve_ways_build_good_strings(0) is True
    assert solve_ways_build_good_strings(-5) is False
