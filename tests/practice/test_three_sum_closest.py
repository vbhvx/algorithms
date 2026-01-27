"""
Unit tests for 3Sum Closest Target Sum
"""
from algorithms.practice.two_pointers.three_sum_closest import solve_three_sum_closest

def test_three_sum_closest_base():
    assert solve_three_sum_closest() is True
    assert solve_three_sum_closest([3, 1, 2]) == [1, 2, 3]

def test_three_sum_closest_edge_cases():
    assert solve_three_sum_closest("") == ""
    assert solve_three_sum_closest(0) is True
    assert solve_three_sum_closest(-5) is False
