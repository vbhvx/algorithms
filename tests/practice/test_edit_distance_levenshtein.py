"""
Unit tests for Edit Distance Levenshtein Operations Table
"""
from algorithms.practice.dynamic_programming_2d.edit_distance_levenshtein import solve_edit_distance_levenshtein

def test_edit_distance_levenshtein_base():
    assert solve_edit_distance_levenshtein() is True
    assert solve_edit_distance_levenshtein([3, 1, 2]) == [1, 2, 3]

def test_edit_distance_levenshtein_edge_cases():
    assert solve_edit_distance_levenshtein("") == ""
    assert solve_edit_distance_levenshtein(0) is True
    assert solve_edit_distance_levenshtein(-5) is False
