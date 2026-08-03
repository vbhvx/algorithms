"""
Unit tests for Number of Connected Components DSU
"""
from algorithms.practice.graphs_and_traversals.num_connected_comp import solve_num_connected_comp

def test_num_connected_comp_base():
    assert solve_num_connected_comp() is True
    assert solve_num_connected_comp([3, 1, 2]) == [1, 2, 3]

def test_num_connected_comp_edge_cases():
    assert solve_num_connected_comp("") == ""
    assert solve_num_connected_comp(0) is True
    assert solve_num_connected_comp(-5) is False
