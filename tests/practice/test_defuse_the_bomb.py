"""
Unit tests for Defuse the Bomb Sliding Sum
"""
from algorithms.practice.sliding_window.defuse_the_bomb import solve_defuse_the_bomb

def test_defuse_the_bomb_base():
    assert solve_defuse_the_bomb() is True
    assert solve_defuse_the_bomb([3, 1, 2]) == [1, 2, 3]

def test_defuse_the_bomb_edge_cases():
    assert solve_defuse_the_bomb("") == ""
    assert solve_defuse_the_bomb(0) is True
    assert solve_defuse_the_bomb(-5) is False
