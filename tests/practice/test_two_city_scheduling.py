"""
Unit tests for Two City Scheduling Opportunity Cost Sort
"""
from algorithms.practice.greedy_algorithms.two_city_scheduling import solve_two_city_scheduling

def test_two_city_scheduling_base():
    assert solve_two_city_scheduling() is True
    assert solve_two_city_scheduling([3, 1, 2]) == [1, 2, 3]

def test_two_city_scheduling_edge_cases():
    assert solve_two_city_scheduling("") == ""
    assert solve_two_city_scheduling(0) is True
    assert solve_two_city_scheduling(-5) is False
