"""
Unit tests for Sort Colors Dutch National Flag
"""
from algorithms.practice.two_pointers.sort_colors_dutch import solve_sort_colors_dutch

def test_sort_colors_dutch_base():
    assert solve_sort_colors_dutch() is True
    assert solve_sort_colors_dutch([3, 1, 2]) == [1, 2, 3]

def test_sort_colors_dutch_edge_cases():
    assert solve_sort_colors_dutch("") == ""
    assert solve_sort_colors_dutch(0) is True
    assert solve_sort_colors_dutch(-5) is False
