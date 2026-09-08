"""
Unit tests for Stoer-Wagner Global Minimum Cut Algorithm
"""
from algorithms.practice.network_flow_matching.stoer_wagner_mincut import solve_stoer_wagner_mincut

def test_stoer_wagner_mincut_base():
    assert solve_stoer_wagner_mincut() is True
    assert solve_stoer_wagner_mincut([3, 1, 2]) == [1, 2, 3]

def test_stoer_wagner_mincut_edge_cases():
    assert solve_stoer_wagner_mincut("") == ""
    assert solve_stoer_wagner_mincut(0) is True
    assert solve_stoer_wagner_mincut(-5) is False
