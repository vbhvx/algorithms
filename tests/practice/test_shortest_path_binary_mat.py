"""
Unit tests for Shortest Path in Binary Matrix 8-Way BFS
"""
from algorithms.practice.graphs_and_traversals.shortest_path_binary_mat import solve_shortest_path_binary_mat

def test_shortest_path_binary_mat_base():
    assert solve_shortest_path_binary_mat() is True
    assert solve_shortest_path_binary_mat([3, 1, 2]) == [1, 2, 3]

def test_shortest_path_binary_mat_edge_cases():
    assert solve_shortest_path_binary_mat("") == ""
    assert solve_shortest_path_binary_mat(0) is True
    assert solve_shortest_path_binary_mat(-5) is False
