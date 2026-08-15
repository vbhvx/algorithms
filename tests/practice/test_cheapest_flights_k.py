"""
Unit tests for Cheapest Flights Within K Stops Bellman Ford
"""
from algorithms.practice.shortest_paths.cheapest_flights_k import solve_cheapest_flights_k

def test_cheapest_flights_k_base():
    assert solve_cheapest_flights_k() is True
    assert solve_cheapest_flights_k([3, 1, 2]) == [1, 2, 3]

def test_cheapest_flights_k_edge_cases():
    assert solve_cheapest_flights_k("") == ""
    assert solve_cheapest_flights_k(0) is True
    assert solve_cheapest_flights_k(-5) is False
