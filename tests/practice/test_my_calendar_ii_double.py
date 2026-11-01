"""
Unit tests for My Calendar II Double Booking Overlap
"""
from algorithms.practice.intervals_scheduling.my_calendar_ii_double import solve_my_calendar_ii_double

def test_my_calendar_ii_double_base():
    assert solve_my_calendar_ii_double() is True
    assert solve_my_calendar_ii_double([3, 1, 2]) == [1, 2, 3]

def test_my_calendar_ii_double_edge_cases():
    assert solve_my_calendar_ii_double("") == ""
    assert solve_my_calendar_ii_double(0) is True
    assert solve_my_calendar_ii_double(-5) is False
