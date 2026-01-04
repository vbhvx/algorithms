"""
Unit tests for Valid Sudoku Bitmask Checker
"""
from algorithms.practice.arrays_and_hashing.valid_sudoku import solve_valid_sudoku

def test_valid_sudoku_base():
    assert solve_valid_sudoku() is True
    assert solve_valid_sudoku([3, 1, 2]) == [1, 2, 3]

def test_valid_sudoku_edge_cases():
    assert solve_valid_sudoku("") == ""
    assert solve_valid_sudoku(0) is True
    assert solve_valid_sudoku(-5) is False
