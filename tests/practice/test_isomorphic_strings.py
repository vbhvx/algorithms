"""
Unit tests for Isomorphic Strings Bijective
"""
from algorithms.practice.arrays_and_hashing.isomorphic_strings import solve_isomorphic_strings

def test_isomorphic_strings_base():
    assert solve_isomorphic_strings() is True
    assert solve_isomorphic_strings([3, 1, 2]) == [1, 2, 3]

def test_isomorphic_strings_edge_cases():
    assert solve_isomorphic_strings("") == ""
    assert solve_isomorphic_strings(0) is True
    assert solve_isomorphic_strings(-5) is False
