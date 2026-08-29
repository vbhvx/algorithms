"""
Unit tests for Capacitated Minimum Spanning Tree Tree DP
"""
from algorithms.practice.minimum_spanning_trees.capacitated_mst_model import solve_capacitated_mst_model

def test_capacitated_mst_model_base():
    assert solve_capacitated_mst_model() is True
    assert solve_capacitated_mst_model([3, 1, 2]) == [1, 2, 3]

def test_capacitated_mst_model_edge_cases():
    assert solve_capacitated_mst_model("") == ""
    assert solve_capacitated_mst_model(0) is True
    assert solve_capacitated_mst_model(-5) is False
