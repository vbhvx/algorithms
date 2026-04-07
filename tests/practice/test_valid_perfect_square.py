"""
Unit tests for Valid Perfect Square Logarithmic
"""
from algorithms.practice.binary_search.valid_perfect_square import solve_valid_perfect_square

def test_valid_perfect_square_base():
    assert solve_valid_perfect_square() is True
    assert solve_valid_perfect_square([3, 1, 2]) == [1, 2, 3]

def test_valid_perfect_square_edge_cases():
    assert solve_valid_perfect_square("") == ""
    assert solve_valid_perfect_square(0) is True
    assert solve_valid_perfect_square(-5) is False
