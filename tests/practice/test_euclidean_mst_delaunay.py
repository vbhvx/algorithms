"""
Unit tests for Euclidean MST via Delaunay Triangulation
"""
from algorithms.practice.minimum_spanning_trees.euclidean_mst_delaunay import solve_euclidean_mst_delaunay

def test_euclidean_mst_delaunay_base():
    assert solve_euclidean_mst_delaunay() is True
    assert solve_euclidean_mst_delaunay([3, 1, 2]) == [1, 2, 3]

def test_euclidean_mst_delaunay_edge_cases():
    assert solve_euclidean_mst_delaunay("") == ""
    assert solve_euclidean_mst_delaunay(0) is True
    assert solve_euclidean_mst_delaunay(-5) is False
