"""
Unit tests for Reverse Words in a String III
"""
from algorithms.practice.two_pointers.reverse_words_iii import solve_reverse_words_iii

def test_reverse_words_iii_base():
    assert solve_reverse_words_iii() is True
    assert solve_reverse_words_iii([3, 1, 2]) == [1, 2, 3]

def test_reverse_words_iii_edge_cases():
    assert solve_reverse_words_iii("") == ""
    assert solve_reverse_words_iii(0) is True
    assert solve_reverse_words_iii(-5) is False
