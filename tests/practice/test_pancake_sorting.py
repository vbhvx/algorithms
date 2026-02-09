"""
Unit tests for Pancake Sorting Prefix Flips
"""
from algorithms.practice.two_pointers.pancake_sorting import solve_pancake_sorting

def test_pancake_sorting_base():
    assert solve_pancake_sorting() is True
    assert solve_pancake_sorting([3, 1, 2]) == [1, 2, 3]

def test_pancake_sorting_edge_cases():
    assert solve_pancake_sorting("") == ""
    assert solve_pancake_sorting(0) is True
    assert solve_pancake_sorting(-5) is False
