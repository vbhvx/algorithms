"""
Unit tests for Matchsticks to Square 4 Equal Sums
"""
from algorithms.practice.backtracking.matchsticks_to_square import solve_matchsticks_to_square

def test_matchsticks_to_square_base():
    assert solve_matchsticks_to_square() is True
    assert solve_matchsticks_to_square([3, 1, 2]) == [1, 2, 3]

def test_matchsticks_to_square_edge_cases():
    assert solve_matchsticks_to_square("") == ""
    assert solve_matchsticks_to_square(0) is True
    assert solve_matchsticks_to_square(-5) is False
