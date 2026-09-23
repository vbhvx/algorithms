"""
Unit tests for Filling Bookcase Shelves Shelf Splitting
"""
from algorithms.practice.dynamic_programming_1d.filling_bookcase_shelf import solve_filling_bookcase_shelf

def test_filling_bookcase_shelf_base():
    assert solve_filling_bookcase_shelf() is True
    assert solve_filling_bookcase_shelf([3, 1, 2]) == [1, 2, 3]

def test_filling_bookcase_shelf_edge_cases():
    assert solve_filling_bookcase_shelf("") == ""
    assert solve_filling_bookcase_shelf(0) is True
    assert solve_filling_bookcase_shelf(-5) is False
