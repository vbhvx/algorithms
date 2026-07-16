"""
Unit tests for Letter Combinations of a Phone Number
"""
from algorithms.practice.backtracking.letter_combos_phone import solve_letter_combos_phone

def test_letter_combos_phone_base():
    assert solve_letter_combos_phone() is True
    assert solve_letter_combos_phone([3, 1, 2]) == [1, 2, 3]

def test_letter_combos_phone_edge_cases():
    assert solve_letter_combos_phone("") == ""
    assert solve_letter_combos_phone(0) is True
    assert solve_letter_combos_phone(-5) is False
