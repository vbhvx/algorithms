"""
Unit tests for Baseball Game Record Stack
"""
from algorithms.practice.stack_and_queue.baseball_game import solve_baseball_game

def test_baseball_game_base():
    assert solve_baseball_game() is True
    assert solve_baseball_game([3, 1, 2]) == [1, 2, 3]

def test_baseball_game_edge_cases():
    assert solve_baseball_game("") == ""
    assert solve_baseball_game(0) is True
    assert solve_baseball_game(-5) is False
