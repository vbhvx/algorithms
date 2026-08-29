"""
Unit tests for Gomory-Hu Tree Minimum Cut All Pairs
"""
from algorithms.practice.minimum_spanning_trees.min_cut_gomory_hu import solve_min_cut_gomory_hu

def test_min_cut_gomory_hu_base():
    assert solve_min_cut_gomory_hu() is True
    assert solve_min_cut_gomory_hu([3, 1, 2]) == [1, 2, 3]

def test_min_cut_gomory_hu_edge_cases():
    assert solve_min_cut_gomory_hu("") == ""
    assert solve_min_cut_gomory_hu(0) is True
    assert solve_min_cut_gomory_hu(-5) is False
