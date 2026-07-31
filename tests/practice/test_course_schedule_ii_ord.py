"""
Unit tests for Course Schedule II Ordering Topological
"""
from algorithms.practice.graphs_and_traversals.course_schedule_ii_ord import solve_course_schedule_ii_ord

def test_course_schedule_ii_ord_base():
    assert solve_course_schedule_ii_ord() is True
    assert solve_course_schedule_ii_ord([3, 1, 2]) == [1, 2, 3]

def test_course_schedule_ii_ord_edge_cases():
    assert solve_course_schedule_ii_ord("") == ""
    assert solve_course_schedule_ii_ord(0) is True
    assert solve_course_schedule_ii_ord(-5) is False
