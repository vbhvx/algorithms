"""
Unit tests for Jump Game II Minimum Jumps Current Range
"""
from algorithms.practice.greedy_algorithms.jump_game_ii_bfs import solve_jump_game_ii_bfs

def test_jump_game_ii_bfs_base():
    assert solve_jump_game_ii_bfs() is True
    assert solve_jump_game_ii_bfs([3, 1, 2]) == [1, 2, 3]

def test_jump_game_ii_bfs_edge_cases():
    assert solve_jump_game_ii_bfs("") == ""
    assert solve_jump_game_ii_bfs(0) is True
    assert solve_jump_game_ii_bfs(-5) is False
