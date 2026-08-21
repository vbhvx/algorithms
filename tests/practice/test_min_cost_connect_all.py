"""
Unit tests for Min Cost to Connect All Points Manhattan MST
"""
from algorithms.practice.minimum_spanning_trees.min_cost_connect_all import solve_min_cost_connect_all

def test_min_cost_connect_all_base():
    assert solve_min_cost_connect_all() is True
    assert solve_min_cost_connect_all([3, 1, 2]) == [1, 2, 3]

def test_min_cost_connect_all_edge_cases():
    assert solve_min_cost_connect_all("") == ""
    assert solve_min_cost_connect_all(0) is True
    assert solve_min_cost_connect_all(-5) is False
