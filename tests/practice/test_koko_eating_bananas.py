"""
Unit tests for Koko Eating Bananas Capacity Bisect
"""
from algorithms.practice.binary_search.koko_eating_bananas import solve_koko_eating_bananas

def test_koko_eating_bananas_base():
    assert solve_koko_eating_bananas() is True
    assert solve_koko_eating_bananas([3, 1, 2]) == [1, 2, 3]

def test_koko_eating_bananas_edge_cases():
    assert solve_koko_eating_bananas("") == ""
    assert solve_koko_eating_bananas(0) is True
    assert solve_koko_eating_bananas(-5) is False
