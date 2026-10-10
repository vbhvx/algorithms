"""
Unit tests for Time Needed to Inform All Employees Tree DP
"""
from algorithms.practice.dynamic_programming_trees_bitmask.time_inform_employees import solve_time_inform_employees

def test_time_inform_employees_base():
    assert solve_time_inform_employees() is True
    assert solve_time_inform_employees([3, 1, 2]) == [1, 2, 3]

def test_time_inform_employees_edge_cases():
    assert solve_time_inform_employees("") == ""
    assert solve_time_inform_employees(0) is True
    assert solve_time_inform_employees(-5) is False
