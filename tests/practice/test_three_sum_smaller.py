"""
Unit tests for 3Sum Smaller Target Triplet Count
"""
from algorithms.practice.two_pointers.three_sum_smaller import solve_three_sum_smaller

def test_three_sum_smaller_base():
    assert solve_three_sum_smaller() is True
    assert solve_three_sum_smaller([3, 1, 2]) == [1, 2, 3]

def test_three_sum_smaller_edge_cases():
    assert solve_three_sum_smaller("") == ""
    assert solve_three_sum_smaller(0) is True
    assert solve_three_sum_smaller(-5) is False
