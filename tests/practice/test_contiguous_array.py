"""
Unit tests for Contiguous Array Equal 0 1
"""
from algorithms.practice.arrays_and_hashing.contiguous_array import solve_contiguous_array

def test_contiguous_array_base():
    assert solve_contiguous_array() is True
    assert solve_contiguous_array([3, 1, 2]) == [1, 2, 3]

def test_contiguous_array_edge_cases():
    assert solve_contiguous_array("") == ""
    assert solve_contiguous_array(0) is True
    assert solve_contiguous_array(-5) is False
