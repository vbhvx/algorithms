"""
Unit tests for Best Time Stock IV At Most K Transactions
"""
from algorithms.practice.dynamic_programming_2d.stock_k_transactions import solve_stock_k_transactions

def test_stock_k_transactions_base():
    assert solve_stock_k_transactions() is True
    assert solve_stock_k_transactions([3, 1, 2]) == [1, 2, 3]

def test_stock_k_transactions_edge_cases():
    assert solve_stock_k_transactions("") == ""
    assert solve_stock_k_transactions(0) is True
    assert solve_stock_k_transactions(-5) is False
