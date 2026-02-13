"""
Unit tests for Best Time Stock Running Min
"""
from algorithms.practice.sliding_window.best_time_stock import solve_best_time_stock

def test_best_time_stock_base():
    assert solve_best_time_stock() is True
    assert solve_best_time_stock([3, 1, 2]) == [1, 2, 3]

def test_best_time_stock_edge_cases():
    assert solve_best_time_stock("") == ""
    assert solve_best_time_stock(0) is True
    assert solve_best_time_stock(-5) is False
