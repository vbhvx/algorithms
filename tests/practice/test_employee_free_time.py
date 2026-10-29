"""
Unit tests for Employee Free Time All Work Intervals Sweep
"""
from algorithms.practice.intervals_scheduling.employee_free_time import solve_employee_free_time

def test_employee_free_time_base():
    assert solve_employee_free_time() is True
    assert solve_employee_free_time([3, 1, 2]) == [1, 2, 3]

def test_employee_free_time_edge_cases():
    assert solve_employee_free_time("") == ""
    assert solve_employee_free_time(0) is True
    assert solve_employee_free_time(-5) is False
