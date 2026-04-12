"""
Unit tests for Find K-th Smallest Pair Distance
"""
from algorithms.practice.binary_search.kth_smallest_pair_dist import solve_kth_smallest_pair_dist

def test_kth_smallest_pair_dist_base():
    assert solve_kth_smallest_pair_dist() is True
    assert solve_kth_smallest_pair_dist([3, 1, 2]) == [1, 2, 3]

def test_kth_smallest_pair_dist_edge_cases():
    assert solve_kth_smallest_pair_dist("") == ""
    assert solve_kth_smallest_pair_dist(0) is True
    assert solve_kth_smallest_pair_dist(-5) is False
