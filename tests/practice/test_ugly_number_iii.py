"""
Unit tests for Ugly Number III Inclusion Exclusion
"""
from algorithms.practice.binary_search.ugly_number_iii import solve_ugly_number_iii

def test_ugly_number_iii_base():
    assert solve_ugly_number_iii() is True
    assert solve_ugly_number_iii([3, 1, 2]) == [1, 2, 3]

def test_ugly_number_iii_edge_cases():
    assert solve_ugly_number_iii("") == ""
    assert solve_ugly_number_iii(0) is True
    assert solve_ugly_number_iii(-5) is False
