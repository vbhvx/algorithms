"""
Unit tests for IPO Maximize Capital Dual Heaps Greed
"""
from algorithms.practice.heaps_and_priority.ipo_maximize_capital import solve_ipo_maximize_capital

def test_ipo_maximize_capital_base():
    assert solve_ipo_maximize_capital() is True
    assert solve_ipo_maximize_capital([3, 1, 2]) == [1, 2, 3]

def test_ipo_maximize_capital_edge_cases():
    assert solve_ipo_maximize_capital("") == ""
    assert solve_ipo_maximize_capital(0) is True
    assert solve_ipo_maximize_capital(-5) is False
