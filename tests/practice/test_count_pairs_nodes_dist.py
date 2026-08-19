"""
Unit tests for Count Pairs of Nodes in Distance Bound
"""
from algorithms.practice.shortest_paths.count_pairs_nodes_dist import solve_count_pairs_nodes_dist

def test_count_pairs_nodes_dist_base():
    assert solve_count_pairs_nodes_dist() is True
    assert solve_count_pairs_nodes_dist([3, 1, 2]) == [1, 2, 3]

def test_count_pairs_nodes_dist_edge_cases():
    assert solve_count_pairs_nodes_dist("") == ""
    assert solve_count_pairs_nodes_dist(0) is True
    assert solve_count_pairs_nodes_dist(-5) is False
