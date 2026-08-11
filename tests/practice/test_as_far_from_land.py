"""
Unit tests for As Far from Land as Possible Multi-Source BFS
"""
from algorithms.practice.graphs_and_traversals.as_far_from_land import solve_as_far_from_land

def test_as_far_from_land_base():
    assert solve_as_far_from_land() is True
    assert solve_as_far_from_land([3, 1, 2]) == [1, 2, 3]

def test_as_far_from_land_edge_cases():
    assert solve_as_far_from_land("") == ""
    assert solve_as_far_from_land(0) is True
    assert solve_as_far_from_land(-5) is False
