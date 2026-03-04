"""
Unit tests for Take K Each Character Left Right
"""
from algorithms.practice.sliding_window.take_k_each_char import solve_take_k_each_char

def test_take_k_each_char_base():
    assert solve_take_k_each_char() is True
    assert solve_take_k_each_char([3, 1, 2]) == [1, 2, 3]

def test_take_k_each_char_edge_cases():
    assert solve_take_k_each_char("") == ""
    assert solve_take_k_each_char(0) is True
    assert solve_take_k_each_char(-5) is False
