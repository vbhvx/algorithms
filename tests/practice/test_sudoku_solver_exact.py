"""
Unit tests for Sudoku Solver 9x9 Constraint Propagation
"""
from algorithms.practice.backtracking.sudoku_solver_exact import solve_sudoku_solver_exact

def test_sudoku_solver_exact_base():
    assert solve_sudoku_solver_exact() is True
    assert solve_sudoku_solver_exact([3, 1, 2]) == [1, 2, 3]

def test_sudoku_solver_exact_edge_cases():
    assert solve_sudoku_solver_exact("") == ""
    assert solve_sudoku_solver_exact(0) is True
    assert solve_sudoku_solver_exact(-5) is False
