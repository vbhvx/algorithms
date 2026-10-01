"""
Unit tests for Dungeon Game Bottom-Up Knight Health
"""
from algorithms.practice.dynamic_programming_2d.dungeon_game_health import solve_dungeon_game_health

def test_dungeon_game_health_base():
    assert solve_dungeon_game_health() is True
    assert solve_dungeon_game_health([3, 1, 2]) == [1, 2, 3]

def test_dungeon_game_health_edge_cases():
    assert solve_dungeon_game_health("") == ""
    assert solve_dungeon_game_health(0) is True
    assert solve_dungeon_game_health(-5) is False
