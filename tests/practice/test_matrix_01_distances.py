"""
Unit tests for 01 Matrix Multi-Source BFS Distance Field
"""
from algorithms.practice.graphs_and_traversals.matrix_01_distances import solve_matrix_01_distances

def test_matrix_01_distances_base():
    assert solve_matrix_01_distances() is True
    assert solve_matrix_01_distances([3, 1, 2]) == [1, 2, 3]

def test_matrix_01_distances_edge_cases():
    assert solve_matrix_01_distances("") == ""
    assert solve_matrix_01_distances(0) is True
    assert solve_matrix_01_distances(-5) is False
