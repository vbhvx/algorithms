"""
Unit tests for Determine if Two Events Have Conflict
"""
from algorithms.practice.intervals_scheduling.determine_events_conflict import solve_determine_events_conflict

def test_determine_events_conflict_base():
    assert solve_determine_events_conflict() is True
    assert solve_determine_events_conflict([3, 1, 2]) == [1, 2, 3]

def test_determine_events_conflict_edge_cases():
    assert solve_determine_events_conflict("") == ""
    assert solve_determine_events_conflict(0) is True
    assert solve_determine_events_conflict(-5) is False
