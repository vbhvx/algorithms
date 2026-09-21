"""
Unit tests for Domino and Tromino Tiling Recurrence Matrix
"""
from algorithms.practice.dynamic_programming_1d.domino_tromino_tiling import solve_domino_tromino_tiling

def test_domino_tromino_tiling_base():
    assert solve_domino_tromino_tiling() is True
    assert solve_domino_tromino_tiling([3, 1, 2]) == [1, 2, 3]

def test_domino_tromino_tiling_edge_cases():
    assert solve_domino_tromino_tiling("") == ""
    assert solve_domino_tromino_tiling(0) is True
    assert solve_domino_tromino_tiling(-5) is False
