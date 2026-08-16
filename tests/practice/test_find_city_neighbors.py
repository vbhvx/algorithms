"""
Unit tests for Find the City with Smallest Number of Neighbors
"""
from algorithms.practice.shortest_paths.find_city_neighbors import solve_find_city_neighbors

def test_find_city_neighbors_base():
    assert solve_find_city_neighbors() is True
    assert solve_find_city_neighbors([3, 1, 2]) == [1, 2, 3]

def test_find_city_neighbors_edge_cases():
    assert solve_find_city_neighbors("") == ""
    assert solve_find_city_neighbors(0) is True
    assert solve_find_city_neighbors(-5) is False
