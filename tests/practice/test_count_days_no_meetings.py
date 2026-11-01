"""
Unit tests for Count Days Without Meetings Merged Gaps
"""
from algorithms.practice.intervals_scheduling.count_days_no_meetings import solve_count_days_no_meetings

def test_count_days_no_meetings_base():
    assert solve_count_days_no_meetings() is True
    assert solve_count_days_no_meetings([3, 1, 2]) == [1, 2, 3]

def test_count_days_no_meetings_edge_cases():
    assert solve_count_days_no_meetings("") == ""
    assert solve_count_days_no_meetings(0) is True
    assert solve_count_days_no_meetings(-5) is False
