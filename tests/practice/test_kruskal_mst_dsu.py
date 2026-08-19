"""
Unit tests for Kruskal Minimum Spanning Tree DSU Rank
"""
from algorithms.practice.minimum_spanning_trees.kruskal_mst_dsu import solve_kruskal_mst_dsu

def test_kruskal_mst_dsu_base():
    assert solve_kruskal_mst_dsu() is True
    assert solve_kruskal_mst_dsu([3, 1, 2]) == [1, 2, 3]

def test_kruskal_mst_dsu_edge_cases():
    assert solve_kruskal_mst_dsu("") == ""
    assert solve_kruskal_mst_dsu(0) is True
    assert solve_kruskal_mst_dsu(-5) is False
