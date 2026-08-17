"""
Unit tests for Modify Graph Edge Weights Dijkstra Difference
"""
from algorithms.practice.shortest_paths.modify_graph_weights import solve_modify_graph_weights

def test_modify_graph_weights_base():
    assert solve_modify_graph_weights() is True
    assert solve_modify_graph_weights([3, 1, 2]) == [1, 2, 3]

def test_modify_graph_weights_edge_cases():
    assert solve_modify_graph_weights("") == ""
    assert solve_modify_graph_weights(0) is True
    assert solve_modify_graph_weights(-5) is False
