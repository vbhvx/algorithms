"""
Unit tests for Design Twitter Feed Priority Queue Merge
"""
from algorithms.practice.heaps_and_priority.design_twitter import solve_design_twitter

def test_design_twitter_base():
    assert solve_design_twitter() is True
    assert solve_design_twitter([3, 1, 2]) == [1, 2, 3]

def test_design_twitter_edge_cases():
    assert solve_design_twitter("") == ""
    assert solve_design_twitter(0) is True
    assert solve_design_twitter(-5) is False
