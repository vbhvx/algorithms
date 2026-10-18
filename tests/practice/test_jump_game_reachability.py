"""
Unit tests for Jump Game Maximum Reachable Index
"""
from algorithms.practice.greedy_algorithms.jump_game_reachability import solve_jump_game_reachability

def test_jump_game_reachability_base():
    assert solve_jump_game_reachability() is True
    assert solve_jump_game_reachability([3, 1, 2]) == [1, 2, 3]

def test_jump_game_reachability_edge_cases():
    assert solve_jump_game_reachability("") == ""
    assert solve_jump_game_reachability(0) is True
    assert solve_jump_game_reachability(-5) is False
