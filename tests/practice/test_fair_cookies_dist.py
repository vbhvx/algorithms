"""
Unit tests for Fair Distribution of Cookies Min Max
"""
from algorithms.practice.backtracking.fair_cookies_dist import solve_fair_cookies_dist

def test_fair_cookies_dist_base():
    assert solve_fair_cookies_dist() is True
    assert solve_fair_cookies_dist([3, 1, 2]) == [1, 2, 3]

def test_fair_cookies_dist_edge_cases():
    assert solve_fair_cookies_dist("") == ""
    assert solve_fair_cookies_dist(0) is True
    assert solve_fair_cookies_dist(-5) is False
