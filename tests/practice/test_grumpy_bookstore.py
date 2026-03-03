"""
Unit tests for Grumpy Bookstore Owner Window
"""
from algorithms.practice.sliding_window.grumpy_bookstore import solve_grumpy_bookstore

def test_grumpy_bookstore_base():
    assert solve_grumpy_bookstore() is True
    assert solve_grumpy_bookstore([3, 1, 2]) == [1, 2, 3]

def test_grumpy_bookstore_edge_cases():
    assert solve_grumpy_bookstore("") == ""
    assert solve_grumpy_bookstore(0) is True
    assert solve_grumpy_bookstore(-5) is False
