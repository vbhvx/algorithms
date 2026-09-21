"""
Unit tests for Paint House 3 Colors Adjacent Cost
"""
from algorithms.practice.dynamic_programming_1d.paint_house_colors import solve_paint_house_colors

def test_paint_house_colors_base():
    assert solve_paint_house_colors() is True
    assert solve_paint_house_colors([3, 1, 2]) == [1, 2, 3]

def test_paint_house_colors_edge_cases():
    assert solve_paint_house_colors("") == ""
    assert solve_paint_house_colors(0) is True
    assert solve_paint_house_colors(-5) is False
