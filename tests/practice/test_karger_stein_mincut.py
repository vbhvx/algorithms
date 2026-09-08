"""
Unit tests for Karger-Stein Randomized Contraction Min-Cut
"""
from algorithms.practice.network_flow_matching.karger_stein_mincut import solve_karger_stein_mincut

def test_karger_stein_mincut_base():
    assert solve_karger_stein_mincut() is True
    assert solve_karger_stein_mincut([3, 1, 2]) == [1, 2, 3]

def test_karger_stein_mincut_edge_cases():
    assert solve_karger_stein_mincut("") == ""
    assert solve_karger_stein_mincut(0) is True
    assert solve_karger_stein_mincut(-5) is False
