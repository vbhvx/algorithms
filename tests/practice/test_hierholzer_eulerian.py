"""
Unit tests for Reconstruct Itinerary Hierholzer Eulerian Circuit
"""
from algorithms.practice.shortest_paths.hierholzer_eulerian import solve_hierholzer_eulerian

def test_hierholzer_eulerian_base():
    assert solve_hierholzer_eulerian() is True
    assert solve_hierholzer_eulerian([3, 1, 2]) == [1, 2, 3]

def test_hierholzer_eulerian_edge_cases():
    assert solve_hierholzer_eulerian("") == ""
    assert solve_hierholzer_eulerian(0) is True
    assert solve_hierholzer_eulerian(-5) is False
