"""
Unit tests for Matchsticks to Square Bitmask Memoization
"""
from algorithms.practice.dynamic_programming_trees_bitmask.matchsticks_square_bm import solve_matchsticks_square_bm

def test_matchsticks_square_bm_base():
    assert solve_matchsticks_square_bm() is True
    assert solve_matchsticks_square_bm([3, 1, 2]) == [1, 2, 3]

def test_matchsticks_square_bm_edge_cases():
    assert solve_matchsticks_square_bm("") == ""
    assert solve_matchsticks_square_bm(0) is True
    assert solve_matchsticks_square_bm(-5) is False
