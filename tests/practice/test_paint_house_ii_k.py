"""
Unit tests for Paint House II K Colors Running Min
"""
from algorithms.practice.dynamic_programming_1d.paint_house_ii_k import solve_paint_house_ii_k

def test_paint_house_ii_k_base():
    assert solve_paint_house_ii_k() is True
    assert solve_paint_house_ii_k([3, 1, 2]) == [1, 2, 3]

def test_paint_house_ii_k_edge_cases():
    assert solve_paint_house_ii_k("") == ""
    assert solve_paint_house_ii_k(0) is True
    assert solve_paint_house_ii_k(-5) is False
