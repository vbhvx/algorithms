"""
Unit tests for Interleaving String 2D Boolean Table
"""
from algorithms.practice.dynamic_programming_2d.interleaving_string_2d import solve_interleaving_string_2d

def test_interleaving_string_2d_base():
    assert solve_interleaving_string_2d() is True
    assert solve_interleaving_string_2d([3, 1, 2]) == [1, 2, 3]

def test_interleaving_string_2d_edge_cases():
    assert solve_interleaving_string_2d("") == ""
    assert solve_interleaving_string_2d(0) is True
    assert solve_interleaving_string_2d(-5) is False
