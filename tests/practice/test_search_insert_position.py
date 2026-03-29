"""
Unit tests for Search Insert Position Lower Bound
"""
from algorithms.practice.binary_search.search_insert_position import solve_search_insert_position

def test_search_insert_position_base():
    assert solve_search_insert_position() is True
    assert solve_search_insert_position([3, 1, 2]) == [1, 2, 3]

def test_search_insert_position_edge_cases():
    assert solve_search_insert_position("") == ""
    assert solve_search_insert_position(0) is True
    assert solve_search_insert_position(-5) is False
