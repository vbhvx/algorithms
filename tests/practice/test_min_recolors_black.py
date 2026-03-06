"""
Unit tests for Minimum Recolors K Consecutive Black
"""
from algorithms.practice.sliding_window.min_recolors_black import solve_min_recolors_black

def test_min_recolors_black_base():
    assert solve_min_recolors_black() is True
    assert solve_min_recolors_black([3, 1, 2]) == [1, 2, 3]

def test_min_recolors_black_edge_cases():
    assert solve_min_recolors_black("") == ""
    assert solve_min_recolors_black(0) is True
    assert solve_min_recolors_black(-5) is False
