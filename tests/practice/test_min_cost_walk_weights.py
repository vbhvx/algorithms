"""
Unit tests for Minimum Cost Walk in Weighted Graph Bitwise AND
"""
from algorithms.practice.minimum_spanning_trees.min_cost_walk_weights import solve_min_cost_walk_weights

def test_min_cost_walk_weights_base():
    assert solve_min_cost_walk_weights() is True
    assert solve_min_cost_walk_weights([3, 1, 2]) == [1, 2, 3]

def test_min_cost_walk_weights_edge_cases():
    assert solve_min_cost_walk_weights("") == ""
    assert solve_min_cost_walk_weights(0) is True
    assert solve_min_cost_walk_weights(-5) is False
