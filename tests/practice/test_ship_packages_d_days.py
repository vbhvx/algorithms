"""
Unit tests for Capacity to Ship Packages within D Days
"""
from algorithms.practice.binary_search.ship_packages_d_days import solve_ship_packages_d_days

def test_ship_packages_d_days_base():
    assert solve_ship_packages_d_days() is True
    assert solve_ship_packages_d_days([3, 1, 2]) == [1, 2, 3]

def test_ship_packages_d_days_edge_cases():
    assert solve_ship_packages_d_days("") == ""
    assert solve_ship_packages_d_days(0) is True
    assert solve_ship_packages_d_days(-5) is False
