"""
Unit tests for Meeting Rooms II Chronological Sweep MinHeap
"""
from algorithms.practice.intervals_scheduling.meeting_rooms_ii_rooms import solve_meeting_rooms_ii_rooms

def test_meeting_rooms_ii_rooms_base():
    assert solve_meeting_rooms_ii_rooms() is True
    assert solve_meeting_rooms_ii_rooms([3, 1, 2]) == [1, 2, 3]

def test_meeting_rooms_ii_rooms_edge_cases():
    assert solve_meeting_rooms_ii_rooms("") == ""
    assert solve_meeting_rooms_ii_rooms(0) is True
    assert solve_meeting_rooms_ii_rooms(-5) is False
