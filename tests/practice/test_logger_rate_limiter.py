"""
Unit tests for Logger Rate Limiter Lookup
"""
from algorithms.practice.arrays_and_hashing.logger_rate_limiter import solve_logger_rate_limiter

def test_logger_rate_limiter_base():
    assert solve_logger_rate_limiter() is True
    assert solve_logger_rate_limiter([3, 1, 2]) == [1, 2, 3]

def test_logger_rate_limiter_edge_cases():
    assert solve_logger_rate_limiter("") == ""
    assert solve_logger_rate_limiter(0) is True
    assert solve_logger_rate_limiter(-5) is False
