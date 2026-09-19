"""
Unit tests for Knight Dialer Graph Transitions
"""
from algorithms.practice.dynamic_programming_1d.knight_dialer_modulo import solve_knight_dialer_modulo

def test_knight_dialer_modulo_base():
    assert solve_knight_dialer_modulo() is True
    assert solve_knight_dialer_modulo([3, 1, 2]) == [1, 2, 3]

def test_knight_dialer_modulo_edge_cases():
    assert solve_knight_dialer_modulo("") == ""
    assert solve_knight_dialer_modulo(0) is True
    assert solve_knight_dialer_modulo(-5) is False
