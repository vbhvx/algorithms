"""
Unit tests for Minimum Speed to Arrive on Time
"""
from algorithms.practice.binary_search.min_speed_arrive_time import solve_min_speed_arrive_time

def test_min_speed_arrive_time_base():
    assert solve_min_speed_arrive_time() is True
    assert solve_min_speed_arrive_time([3, 1, 2]) == [1, 2, 3]

def test_min_speed_arrive_time_edge_cases():
    assert solve_min_speed_arrive_time("") == ""
    assert solve_min_speed_arrive_time(0) is True
    assert solve_min_speed_arrive_time(-5) is False
