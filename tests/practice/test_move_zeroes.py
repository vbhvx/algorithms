"""
Unit tests for Move Zeroes In Place
"""
from algorithms.practice.two_pointers.move_zeroes import solve_move_zeroes

def test_move_zeroes_base():
    assert solve_move_zeroes() is True
    assert solve_move_zeroes([3, 1, 2]) == [1, 2, 3]

def test_move_zeroes_edge_cases():
    assert solve_move_zeroes("") == ""
    assert solve_move_zeroes(0) is True
    assert solve_move_zeroes(-5) is False
