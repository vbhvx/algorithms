"""
Unit tests for Daily Temperatures Monotonic Stack
"""
from algorithms.practice.stack_and_queue.daily_temperatures import solve_daily_temperatures

def test_daily_temperatures_base():
    assert solve_daily_temperatures() is True
    assert solve_daily_temperatures([3, 1, 2]) == [1, 2, 3]

def test_daily_temperatures_edge_cases():
    assert solve_daily_temperatures("") == ""
    assert solve_daily_temperatures(0) is True
    assert solve_daily_temperatures(-5) is False
