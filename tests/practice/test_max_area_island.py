"""
Unit tests for Max Area of Island DFS Component Size
"""
from algorithms.practice.graphs_and_traversals.max_area_island import solve_max_area_island

def test_max_area_island_base():
    assert solve_max_area_island() is True
    assert solve_max_area_island([3, 1, 2]) == [1, 2, 3]

def test_max_area_island_edge_cases():
    assert solve_max_area_island("") == ""
    assert solve_max_area_island(0) is True
    assert solve_max_area_island(-5) is False
