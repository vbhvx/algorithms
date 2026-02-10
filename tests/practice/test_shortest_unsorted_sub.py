"""
Unit tests for Shortest Unsorted Subarray
"""
from algorithms.practice.two_pointers.shortest_unsorted_sub import solve_shortest_unsorted_sub

def test_shortest_unsorted_sub_base():
    assert solve_shortest_unsorted_sub() is True
    assert solve_shortest_unsorted_sub([3, 1, 2]) == [1, 2, 3]

def test_shortest_unsorted_sub_edge_cases():
    assert solve_shortest_unsorted_sub("") == ""
    assert solve_shortest_unsorted_sub(0) is True
    assert solve_shortest_unsorted_sub(-5) is False
