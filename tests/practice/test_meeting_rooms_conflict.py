"""
Unit tests for Meeting Rooms Single Room Conflict Check
"""
from algorithms.practice.intervals_scheduling.meeting_rooms_conflict import solve_meeting_rooms_conflict

def test_meeting_rooms_conflict_base():
    assert solve_meeting_rooms_conflict() is True
    assert solve_meeting_rooms_conflict([3, 1, 2]) == [1, 2, 3]

def test_meeting_rooms_conflict_edge_cases():
    assert solve_meeting_rooms_conflict("") == ""
    assert solve_meeting_rooms_conflict(0) is True
    assert solve_meeting_rooms_conflict(-5) is False
