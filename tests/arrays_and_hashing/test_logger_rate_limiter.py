"""Unit test suite for Logger Rate Limiter Lookup."""
from src.arrays_and_hashing.logger_rate_limiter import LoggerRateLimiterLookup

def test_logger_rate_limiter_basic():
    solver = LoggerRateLimiterLookup()
    assert solver.solve() is True
    assert solver.invocations == 1

def test_logger_rate_limiter_repeated():
    solver = LoggerRateLimiterLookup()
    for _ in range(5):
        solver.solve()
    assert solver.invocations == 5
