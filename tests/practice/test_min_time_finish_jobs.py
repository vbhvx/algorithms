"""
Unit tests for Minimum Time to Finish All Jobs Bitmask DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.min_time_finish_jobs import solve_min_time_finish_jobs

def test_min_time_finish_jobs_base():
    assert solve_min_time_finish_jobs() is True
    assert solve_min_time_finish_jobs([3, 1, 2]) == [1, 2, 3]

def test_min_time_finish_jobs_edge_cases():
    assert solve_min_time_finish_jobs("") == ""
    assert solve_min_time_finish_jobs(0) is True
    assert solve_min_time_finish_jobs(-5) is False
