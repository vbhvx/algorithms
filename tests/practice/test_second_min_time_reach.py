"""
Unit tests for Second Minimum Time to Reach Destination BFS
"""
from algorithms.practice.shortest_paths.second_min_time_reach import solve_second_min_time_reach

def test_second_min_time_reach_base():
    assert solve_second_min_time_reach() is True
    assert solve_second_min_time_reach([3, 1, 2]) == [1, 2, 3]

def test_second_min_time_reach_edge_cases():
    assert solve_second_min_time_reach("") == ""
    assert solve_second_min_time_reach(0) is True
    assert solve_second_min_time_reach(-5) is False
