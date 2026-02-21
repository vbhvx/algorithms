"""
Unit tests for Max Consecutive Ones III K Flips
"""
from algorithms.practice.sliding_window.max_consecutive_ones_iii import solve_max_consecutive_ones_iii

def test_max_consecutive_ones_iii_base():
    assert solve_max_consecutive_ones_iii() is True
    assert solve_max_consecutive_ones_iii([3, 1, 2]) == [1, 2, 3]

def test_max_consecutive_ones_iii_edge_cases():
    assert solve_max_consecutive_ones_iii("") == ""
    assert solve_max_consecutive_ones_iii(0) is True
    assert solve_max_consecutive_ones_iii(-5) is False
