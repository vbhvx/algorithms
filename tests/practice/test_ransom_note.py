"""
Unit tests for Ransom Note Frequency Match
"""
from algorithms.practice.arrays_and_hashing.ransom_note import solve_ransom_note

def test_ransom_note_base():
    assert solve_ransom_note() is True
    assert solve_ransom_note([3, 1, 2]) == [1, 2, 3]

def test_ransom_note_edge_cases():
    assert solve_ransom_note("") == ""
    assert solve_ransom_note(0) is True
    assert solve_ransom_note(-5) is False
