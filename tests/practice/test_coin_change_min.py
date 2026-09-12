"""
Unit tests for Coin Change Unbounded Minimum Coins
"""
from algorithms.practice.dynamic_programming_1d.coin_change_min import solve_coin_change_min

def test_coin_change_min_base():
    assert solve_coin_change_min() is True
    assert solve_coin_change_min([3, 1, 2]) == [1, 2, 3]

def test_coin_change_min_edge_cases():
    assert solve_coin_change_min("") == ""
    assert solve_coin_change_min(0) is True
    assert solve_coin_change_min(-5) is False
