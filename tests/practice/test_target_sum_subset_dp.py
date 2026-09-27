"""
Unit tests for Target Sum 0-1 Subset Partition
"""
from algorithms.practice.dynamic_programming_2d.target_sum_subset_dp import solve_target_sum_subset_dp

def test_target_sum_subset_dp_base():
    assert solve_target_sum_subset_dp() is True
    assert solve_target_sum_subset_dp([3, 1, 2]) == [1, 2, 3]

def test_target_sum_subset_dp_edge_cases():
    assert solve_target_sum_subset_dp("") == ""
    assert solve_target_sum_subset_dp(0) is True
    assert solve_target_sum_subset_dp(-5) is False
