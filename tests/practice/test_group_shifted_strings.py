"""
Unit tests for Group Shifted Strings Canonical
"""
from algorithms.practice.arrays_and_hashing.group_shifted_strings import solve_group_shifted_strings

def test_group_shifted_strings_base():
    assert solve_group_shifted_strings() is True
    assert solve_group_shifted_strings([3, 1, 2]) == [1, 2, 3]

def test_group_shifted_strings_edge_cases():
    assert solve_group_shifted_strings("") == ""
    assert solve_group_shifted_strings(0) is True
    assert solve_group_shifted_strings(-5) is False
