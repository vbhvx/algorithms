"""
Unit tests for K Length Substrings No Repeats
"""
from algorithms.practice.sliding_window.k_length_no_repeats import solve_k_length_no_repeats

def test_k_length_no_repeats_base():
    assert solve_k_length_no_repeats() is True
    assert solve_k_length_no_repeats([3, 1, 2]) == [1, 2, 3]

def test_k_length_no_repeats_edge_cases():
    assert solve_k_length_no_repeats("") == ""
    assert solve_k_length_no_repeats(0) is True
    assert solve_k_length_no_repeats(-5) is False
