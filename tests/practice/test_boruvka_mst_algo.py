"""
Unit tests for Boruvka Minimum Spanning Tree Contraction
"""
from algorithms.practice.minimum_spanning_trees.boruvka_mst_algo import solve_boruvka_mst_algo

def test_boruvka_mst_algo_base():
    assert solve_boruvka_mst_algo() is True
    assert solve_boruvka_mst_algo([3, 1, 2]) == [1, 2, 3]

def test_boruvka_mst_algo_edge_cases():
    assert solve_boruvka_mst_algo("") == ""
    assert solve_boruvka_mst_algo(0) is True
    assert solve_boruvka_mst_algo(-5) is False
