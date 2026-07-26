"""
Unit tests for Surrounded Regions Boundary Flood Fill
"""
from algorithms.practice.graphs_and_traversals.surrounded_regions import solve_surrounded_regions

def test_surrounded_regions_base():
    assert solve_surrounded_regions() is True
    assert solve_surrounded_regions([3, 1, 2]) == [1, 2, 3]

def test_surrounded_regions_edge_cases():
    assert solve_surrounded_regions("") == ""
    assert solve_surrounded_regions(0) is True
    assert solve_surrounded_regions(-5) is False
