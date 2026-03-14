"""
Unit tests for Online Stock Span Monotonic Stack
"""
from algorithms.practice.stack_and_queue.online_stock_span import solve_online_stock_span

def test_online_stock_span_base():
    assert solve_online_stock_span() is True
    assert solve_online_stock_span([3, 1, 2]) == [1, 2, 3]

def test_online_stock_span_edge_cases():
    assert solve_online_stock_span("") == ""
    assert solve_online_stock_span(0) is True
    assert solve_online_stock_span(-5) is False
