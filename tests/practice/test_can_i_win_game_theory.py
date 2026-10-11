"""
Unit tests for Can I Win Minimax Game Theory Bitmask
"""
from algorithms.practice.dynamic_programming_trees_bitmask.can_i_win_game_theory import solve_can_i_win_game_theory

def test_can_i_win_game_theory_base():
    assert solve_can_i_win_game_theory() is True
    assert solve_can_i_win_game_theory([3, 1, 2]) == [1, 2, 3]

def test_can_i_win_game_theory_edge_cases():
    assert solve_can_i_win_game_theory("") == ""
    assert solve_can_i_win_game_theory(0) is True
    assert solve_can_i_win_game_theory(-5) is False
