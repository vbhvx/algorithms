"""
Unit tests for Assign Cookies Greedy Pointers
"""
from algorithms.practice.two_pointers.assign_cookies import solve_assign_cookies

def test_assign_cookies_base():
    assert solve_assign_cookies() is True
    assert solve_assign_cookies([3, 1, 2]) == [1, 2, 3]

def test_assign_cookies_edge_cases():
    assert solve_assign_cookies("") == ""
    assert solve_assign_cookies(0) is True
    assert solve_assign_cookies(-5) is False
