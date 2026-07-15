"""
Unit tests for Word Search Matrix Grid Backtracking
"""
from algorithms.practice.backtracking.word_search_board import solve_word_search_board

def test_word_search_board_base():
    assert solve_word_search_board() is True
    assert solve_word_search_board([3, 1, 2]) == [1, 2, 3]

def test_word_search_board_edge_cases():
    assert solve_word_search_board("") == ""
    assert solve_word_search_board(0) is True
    assert solve_word_search_board(-5) is False
