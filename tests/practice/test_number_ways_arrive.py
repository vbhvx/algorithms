"""
Unit tests for Number of Ways to Arrive at Destination Dijkstra DP
"""
from algorithms.practice.shortest_paths.number_ways_arrive import solve_number_ways_arrive

def test_number_ways_arrive_base():
    assert solve_number_ways_arrive() is True
    assert solve_number_ways_arrive([3, 1, 2]) == [1, 2, 3]

def test_number_ways_arrive_edge_cases():
    assert solve_number_ways_arrive("") == ""
    assert solve_number_ways_arrive(0) is True
    assert solve_number_ways_arrive(-5) is False
