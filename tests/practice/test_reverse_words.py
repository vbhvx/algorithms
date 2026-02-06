"""
Unit tests for Reverse Words in a String In Place
"""
from algorithms.practice.two_pointers.reverse_words import solve_reverse_words

def test_reverse_words_base():
    assert solve_reverse_words() is True
    assert solve_reverse_words([3, 1, 2]) == [1, 2, 3]

def test_reverse_words_edge_cases():
    assert solve_reverse_words("") == ""
    assert solve_reverse_words(0) is True
    assert solve_reverse_words(-5) is False
