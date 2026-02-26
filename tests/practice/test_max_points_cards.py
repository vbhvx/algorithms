"""
Unit tests for Max Points You Can Obtain from Cards
"""
from algorithms.practice.sliding_window.max_points_cards import solve_max_points_cards

def test_max_points_cards_base():
    assert solve_max_points_cards() is True
    assert solve_max_points_cards([3, 1, 2]) == [1, 2, 3]

def test_max_points_cards_edge_cases():
    assert solve_max_points_cards("") == ""
    assert solve_max_points_cards(0) is True
    assert solve_max_points_cards(-5) is False
