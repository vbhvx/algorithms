"""
Unit tests for Connecting Cities With Minimum Cost Kruskal
"""
from algorithms.practice.minimum_spanning_trees.connecting_cities_cost import solve_connecting_cities_cost

def test_connecting_cities_cost_base():
    assert solve_connecting_cities_cost() is True
    assert solve_connecting_cities_cost([3, 1, 2]) == [1, 2, 3]

def test_connecting_cities_cost_edge_cases():
    assert solve_connecting_cities_cost("") == ""
    assert solve_connecting_cities_cost(0) is True
    assert solve_connecting_cities_cost(-5) is False
