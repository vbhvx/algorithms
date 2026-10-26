"""
Unit tests for Boats to Save People Heaviest Lightest Pair
"""
from algorithms.practice.greedy_algorithms.boats_to_save_people import solve_boats_to_save_people

def test_boats_to_save_people_base():
    assert solve_boats_to_save_people() is True
    assert solve_boats_to_save_people([3, 1, 2]) == [1, 2, 3]

def test_boats_to_save_people_edge_cases():
    assert solve_boats_to_save_people("") == ""
    assert solve_boats_to_save_people(0) is True
    assert solve_boats_to_save_people(-5) is False
