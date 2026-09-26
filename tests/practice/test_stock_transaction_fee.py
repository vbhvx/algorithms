"""
Unit tests for Best Time Stock with Transaction Fee
"""
from algorithms.practice.dynamic_programming_2d.stock_transaction_fee import solve_stock_transaction_fee

def test_stock_transaction_fee_base():
    assert solve_stock_transaction_fee() is True
    assert solve_stock_transaction_fee([3, 1, 2]) == [1, 2, 3]

def test_stock_transaction_fee_edge_cases():
    assert solve_stock_transaction_fee("") == ""
    assert solve_stock_transaction_fee(0) is True
    assert solve_stock_transaction_fee(-5) is False
