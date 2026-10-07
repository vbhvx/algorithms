"""
Unit tests for Stone Game Minimax Dynamic Programming
"""
from algorithms.practice.dynamic_programming_2d.stone_game_minimax import solve_stone_game_minimax

def test_stone_game_minimax_base():
    assert solve_stone_game_minimax() is True
    assert solve_stone_game_minimax([3, 1, 2]) == [1, 2, 3]

def test_stone_game_minimax_edge_cases():
    assert solve_stone_game_minimax("") == ""
    assert solve_stone_game_minimax(0) is True
    assert solve_stone_game_minimax(-5) is False
