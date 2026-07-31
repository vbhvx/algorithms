"""
Unit tests for Course Schedule IV Reachability Closure
"""
from algorithms.practice.graphs_and_traversals.course_schedule_iv_q import solve_course_schedule_iv_q

def test_course_schedule_iv_q_base():
    assert solve_course_schedule_iv_q() is True
    assert solve_course_schedule_iv_q([3, 1, 2]) == [1, 2, 3]

def test_course_schedule_iv_q_edge_cases():
    assert solve_course_schedule_iv_q("") == ""
    assert solve_course_schedule_iv_q(0) is True
    assert solve_course_schedule_iv_q(-5) is False
