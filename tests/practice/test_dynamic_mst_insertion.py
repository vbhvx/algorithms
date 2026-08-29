"""
Unit tests for Dynamic MST Edge Insertion and Cycle Removal
"""
from algorithms.practice.minimum_spanning_trees.dynamic_mst_insertion import solve_dynamic_mst_insertion

def test_dynamic_mst_insertion_base():
    assert solve_dynamic_mst_insertion() is True
    assert solve_dynamic_mst_insertion([3, 1, 2]) == [1, 2, 3]

def test_dynamic_mst_insertion_edge_cases():
    assert solve_dynamic_mst_insertion("") == ""
    assert solve_dynamic_mst_insertion(0) is True
    assert solve_dynamic_mst_insertion(-5) is False
