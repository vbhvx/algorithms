"""
Unit tests for Minimum Score of a Path Between Two Cities DSU
"""
from algorithms.practice.minimum_spanning_trees.min_score_path_cities import solve_min_score_path_cities

def test_min_score_path_cities_base():
    assert solve_min_score_path_cities() is True
    assert solve_min_score_path_cities([3, 1, 2]) == [1, 2, 3]

def test_min_score_path_cities_edge_cases():
    assert solve_min_score_path_cities("") == ""
    assert solve_min_score_path_cities(0) is True
    assert solve_min_score_path_cities(-5) is False
