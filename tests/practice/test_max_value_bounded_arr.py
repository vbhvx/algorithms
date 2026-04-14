"""
Unit tests for Maximum Value at Given Index Bounded Array
"""
from algorithms.practice.binary_search.max_value_bounded_arr import solve_max_value_bounded_arr

def test_max_value_bounded_arr_base():
    assert solve_max_value_bounded_arr() is True
    assert solve_max_value_bounded_arr([3, 1, 2]) == [1, 2, 3]

def test_max_value_bounded_arr_edge_cases():
    assert solve_max_value_bounded_arr("") == ""
    assert solve_max_value_bounded_arr(0) is True
    assert solve_max_value_bounded_arr(-5) is False
