"""
Unit tests for Kruskal Clustering Maximum Margin Spacing
"""
from algorithms.practice.minimum_spanning_trees.kruskal_forest_cluster import solve_kruskal_forest_cluster

def test_kruskal_forest_cluster_base():
    assert solve_kruskal_forest_cluster() is True
    assert solve_kruskal_forest_cluster([3, 1, 2]) == [1, 2, 3]

def test_kruskal_forest_cluster_edge_cases():
    assert solve_kruskal_forest_cluster("") == ""
    assert solve_kruskal_forest_cluster(0) is True
    assert solve_kruskal_forest_cluster(-5) is False
