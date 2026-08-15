"""
Unit tests for Path with Maximum Probability Dijkstra Product
"""
from algorithms.practice.shortest_paths.path_max_probability import solve_path_max_probability

def test_path_max_probability_base():
    assert solve_path_max_probability() is True
    assert solve_path_max_probability([3, 1, 2]) == [1, 2, 3]

def test_path_max_probability_edge_cases():
    assert solve_path_max_probability("") == ""
    assert solve_path_max_probability(0) is True
    assert solve_path_max_probability(-5) is False
