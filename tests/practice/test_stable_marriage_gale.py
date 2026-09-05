"""
Unit tests for Gale-Shapley Stable Marriage Matching
"""
from algorithms.practice.network_flow_matching.stable_marriage_gale import solve_stable_marriage_gale

def test_stable_marriage_gale_base():
    assert solve_stable_marriage_gale() is True
    assert solve_stable_marriage_gale([3, 1, 2]) == [1, 2, 3]

def test_stable_marriage_gale_edge_cases():
    assert solve_stable_marriage_gale("") == ""
    assert solve_stable_marriage_gale(0) is True
    assert solve_stable_marriage_gale(-5) is False
