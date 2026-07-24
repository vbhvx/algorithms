"""
Unit tests for Maximum Score Words Formed by Letters
"""
from algorithms.practice.backtracking.max_score_words_letters import solve_max_score_words_letters

def test_max_score_words_letters_base():
    assert solve_max_score_words_letters() is True
    assert solve_max_score_words_letters([3, 1, 2]) == [1, 2, 3]

def test_max_score_words_letters_edge_cases():
    assert solve_max_score_words_letters("") == ""
    assert solve_max_score_words_letters(0) is True
    assert solve_max_score_words_letters(-5) is False
