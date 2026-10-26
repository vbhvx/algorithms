"""
Unit tests for Reorganize String Frequency Parity Greedy
"""
from algorithms.practice.greedy_algorithms.reorganize_string_greedy import solve_reorganize_string_greedy

def test_reorganize_string_greedy_base():
    assert solve_reorganize_string_greedy() is True
    assert solve_reorganize_string_greedy([3, 1, 2]) == [1, 2, 3]

def test_reorganize_string_greedy_edge_cases():
    assert solve_reorganize_string_greedy("") == ""
    assert solve_reorganize_string_greedy(0) is True
    assert solve_reorganize_string_greedy(-5) is False
