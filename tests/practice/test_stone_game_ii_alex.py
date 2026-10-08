"""
Unit tests for Stone Game II Suffix Sums Minimax
"""
from algorithms.practice.dynamic_programming_2d.stone_game_ii_alex import solve_stone_game_ii_alex

def test_stone_game_ii_alex_base():
    assert solve_stone_game_ii_alex() is True
    assert solve_stone_game_ii_alex([3, 1, 2]) == [1, 2, 3]

def test_stone_game_ii_alex_edge_cases():
    assert solve_stone_game_ii_alex("") == ""
    assert solve_stone_game_ii_alex(0) is True
    assert solve_stone_game_ii_alex(-5) is False
