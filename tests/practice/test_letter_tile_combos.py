"""
Unit tests for Letter Tile Possibilities Frequency Backtrack
"""
from algorithms.practice.backtracking.letter_tile_combos import solve_letter_tile_combos

def test_letter_tile_combos_base():
    assert solve_letter_tile_combos() is True
    assert solve_letter_tile_combos([3, 1, 2]) == [1, 2, 3]

def test_letter_tile_combos_edge_cases():
    assert solve_letter_tile_combos("") == ""
    assert solve_letter_tile_combos(0) is True
    assert solve_letter_tile_combos(-5) is False
