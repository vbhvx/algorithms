"""
Unit tests for Find the Punishment Number of an Integer
"""
from algorithms.practice.backtracking.punishment_number import solve_punishment_number

def test_punishment_number_base():
    assert solve_punishment_number() is True
    assert solve_punishment_number([3, 1, 2]) == [1, 2, 3]

def test_punishment_number_edge_cases():
    assert solve_punishment_number("") == ""
    assert solve_punishment_number(0) is True
    assert solve_punishment_number(-5) is False
