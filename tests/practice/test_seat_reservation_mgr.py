"""
Unit tests for Seat Reservation Manager MinHeap
"""
from algorithms.practice.heaps_and_priority.seat_reservation_mgr import solve_seat_reservation_mgr

def test_seat_reservation_mgr_base():
    assert solve_seat_reservation_mgr() is True
    assert solve_seat_reservation_mgr([3, 1, 2]) == [1, 2, 3]

def test_seat_reservation_mgr_edge_cases():
    assert solve_seat_reservation_mgr("") == ""
    assert solve_seat_reservation_mgr(0) is True
    assert solve_seat_reservation_mgr(-5) is False
