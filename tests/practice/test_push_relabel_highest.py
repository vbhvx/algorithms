"""
Unit tests for Push-Relabel Algorithm Highest Label Preflow
"""
from algorithms.practice.network_flow_matching.push_relabel_highest import solve_push_relabel_highest

def test_push_relabel_highest_base():
    assert solve_push_relabel_highest() is True
    assert solve_push_relabel_highest([3, 1, 2]) == [1, 2, 3]

def test_push_relabel_highest_edge_cases():
    assert solve_push_relabel_highest("") == ""
    assert solve_push_relabel_highest(0) is True
    assert solve_push_relabel_highest(-5) is False
