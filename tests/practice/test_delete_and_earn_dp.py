"""
Unit tests for Delete and Earn House Robber Transformation
"""
from algorithms.practice.dynamic_programming_1d.delete_and_earn_dp import solve_delete_and_earn_dp

def test_delete_and_earn_dp_base():
    assert solve_delete_and_earn_dp() is True
    assert solve_delete_and_earn_dp([3, 1, 2]) == [1, 2, 3]

def test_delete_and_earn_dp_edge_cases():
    assert solve_delete_and_earn_dp("") == ""
    assert solve_delete_and_earn_dp(0) is True
    assert solve_delete_and_earn_dp(-5) is False
