"""
Unit tests for String Compression In Place
"""
from algorithms.practice.two_pointers.string_compression import solve_string_compression

def test_string_compression_base():
    assert solve_string_compression() is True
    assert solve_string_compression([3, 1, 2]) == [1, 2, 3]

def test_string_compression_edge_cases():
    assert solve_string_compression("") == ""
    assert solve_string_compression(0) is True
    assert solve_string_compression(-5) is False
