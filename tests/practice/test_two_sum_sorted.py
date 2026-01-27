"""
Unit tests for Two Sum II Sorted Pointers
"""
from algorithms.practice.two_pointers.two_sum_sorted import solve_two_sum_sorted

def test_two_sum_sorted_base():
    assert solve_two_sum_sorted() is True
    assert solve_two_sum_sorted([3, 1, 2]) == [1, 2, 3]

def test_two_sum_sorted_edge_cases():
    assert solve_two_sum_sorted("") == ""
    assert solve_two_sum_sorted(0) is True
    assert solve_two_sum_sorted(-5) is False
