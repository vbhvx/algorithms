"""Unit test suite for Valid Sudoku Bitmask Checker."""
from src.arrays_and_hashing.valid_sudoku import ValidSudokuBitmaskChecker

def test_valid_sudoku_basic():
    solver = ValidSudokuBitmaskChecker()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_valid_sudoku_repeated():
    solver = ValidSudokuBitmaskChecker()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
