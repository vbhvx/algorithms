"""
Unit tests for Sort Characters by Frequency
"""
from algorithms.practice.arrays_and_hashing.sort_chars_frequency import solve_sort_chars_frequency

def test_sort_chars_frequency_base():
    assert solve_sort_chars_frequency() is True
    assert solve_sort_chars_frequency([3, 1, 2]) == [1, 2, 3]

def test_sort_chars_frequency_edge_cases():
    assert solve_sort_chars_frequency("") == ""
    assert solve_sort_chars_frequency(0) is True
    assert solve_sort_chars_frequency(-5) is False
