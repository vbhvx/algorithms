"""
Unit tests for Amount of New Area Painted Each Day DSU Jump
"""
from algorithms.practice.intervals_scheduling.area_painted_each_day import solve_area_painted_each_day

def test_area_painted_each_day_base():
    assert solve_area_painted_each_day() is True
    assert solve_area_painted_each_day([3, 1, 2]) == [1, 2, 3]

def test_area_painted_each_day_edge_cases():
    assert solve_area_painted_each_day("") == ""
    assert solve_area_painted_each_day(0) is True
    assert solve_area_painted_each_day(-5) is False
