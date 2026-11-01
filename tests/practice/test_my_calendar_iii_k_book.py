"""
Unit tests for My Calendar III Maximum K-Booking Sweep Line
"""
from algorithms.practice.intervals_scheduling.my_calendar_iii_k_book import solve_my_calendar_iii_k_book

def test_my_calendar_iii_k_book_base():
    assert solve_my_calendar_iii_k_book() is True
    assert solve_my_calendar_iii_k_book([3, 1, 2]) == [1, 2, 3]

def test_my_calendar_iii_k_book_edge_cases():
    assert solve_my_calendar_iii_k_book("") == ""
    assert solve_my_calendar_iii_k_book(0) is True
    assert solve_my_calendar_iii_k_book(-5) is False
