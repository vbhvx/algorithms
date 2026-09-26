"""
Unit tests for Best Time Stock with Cooldown 3 States
"""
from algorithms.practice.dynamic_programming_2d.stock_cooldown_states import solve_stock_cooldown_states

def test_stock_cooldown_states_base():
    assert solve_stock_cooldown_states() is True
    assert solve_stock_cooldown_states([3, 1, 2]) == [1, 2, 3]

def test_stock_cooldown_states_edge_cases():
    assert solve_stock_cooldown_states("") == ""
    assert solve_stock_cooldown_states(0) is True
    assert solve_stock_cooldown_states(-5) is False
