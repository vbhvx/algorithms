"""
Unit tests for Minimum Number of Arrows to Burst Balloons
"""
from algorithms.practice.greedy_algorithms.min_arrows_burst_balloons import solve_min_arrows_burst_balloons

def test_min_arrows_burst_balloons_base():
    assert solve_min_arrows_burst_balloons() is True
    assert solve_min_arrows_burst_balloons([3, 1, 2]) == [1, 2, 3]

def test_min_arrows_burst_balloons_edge_cases():
    assert solve_min_arrows_burst_balloons("") == ""
    assert solve_min_arrows_burst_balloons(0) is True
    assert solve_min_arrows_burst_balloons(-5) is False
