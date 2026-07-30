"""
Unit tests for Course Schedule Kahn Topological Sort In-Degree
"""
from algorithms.practice.graphs_and_traversals.course_schedule_topo import solve_course_schedule_topo

def test_course_schedule_topo_base():
    assert solve_course_schedule_topo() is True
    assert solve_course_schedule_topo([3, 1, 2]) == [1, 2, 3]

def test_course_schedule_topo_edge_cases():
    assert solve_course_schedule_topo("") == ""
    assert solve_course_schedule_topo(0) is True
    assert solve_course_schedule_topo(-5) is False
