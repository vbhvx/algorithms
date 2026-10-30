"""
Unit tests for My Calendar I Segment Overlap Tree
"""
from algorithms.practice.intervals_scheduling.my_calendar_i_booking import solve_my_calendar_i_booking

def test_my_calendar_i_booking_base():
    assert solve_my_calendar_i_booking() is True
    assert solve_my_calendar_i_booking([3, 1, 2]) == [1, 2, 3]

def test_my_calendar_i_booking_edge_cases():
    assert solve_my_calendar_i_booking("") == ""
    assert solve_my_calendar_i_booking(0) is True
    assert solve_my_calendar_i_booking(-5) is False
