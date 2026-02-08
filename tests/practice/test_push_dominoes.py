"""
Unit tests for Push Dominoes Segment Pointers
"""
from algorithms.practice.two_pointers.push_dominoes import solve_push_dominoes

def test_push_dominoes_base():
    assert solve_push_dominoes() is True
    assert solve_push_dominoes([3, 1, 2]) == [1, 2, 3]

def test_push_dominoes_edge_cases():
    assert solve_push_dominoes("") == ""
    assert solve_push_dominoes(0) is True
    assert solve_push_dominoes(-5) is False
