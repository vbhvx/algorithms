"""
Unit tests for Student Attendance Record II Matrix DP
"""
from algorithms.practice.dynamic_programming_1d.student_attendance_ii import solve_student_attendance_ii

def test_student_attendance_ii_base():
    assert solve_student_attendance_ii() is True
    assert solve_student_attendance_ii([3, 1, 2]) == [1, 2, 3]

def test_student_attendance_ii_edge_cases():
    assert solve_student_attendance_ii("") == ""
    assert solve_student_attendance_ii(0) is True
    assert solve_student_attendance_ii(-5) is False
