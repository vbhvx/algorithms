"""
Unit tests for Coin Change II Total Combinations Unbounded
"""
from algorithms.practice.dynamic_programming_1d.coin_change_ii_ways import solve_coin_change_ii_ways

def test_coin_change_ii_ways_base():
    assert solve_coin_change_ii_ways() is True
    assert solve_coin_change_ii_ways([3, 1, 2]) == [1, 2, 3]

def test_coin_change_ii_ways_edge_cases():
    assert solve_coin_change_ii_ways("") == ""
    assert solve_coin_change_ii_ways(0) is True
    assert solve_coin_change_ii_ways(-5) is False
