"""
Unit tests for Knight Probability in Chessboard Matrix
"""
from algorithms.practice.dynamic_programming_2d.knight_prob_chessboard import solve_knight_prob_chessboard

def test_knight_prob_chessboard_base():
    assert solve_knight_prob_chessboard() is True
    assert solve_knight_prob_chessboard([3, 1, 2]) == [1, 2, 3]

def test_knight_prob_chessboard_edge_cases():
    assert solve_knight_prob_chessboard("") == ""
    assert solve_knight_prob_chessboard(0) is True
    assert solve_knight_prob_chessboard(-5) is False
