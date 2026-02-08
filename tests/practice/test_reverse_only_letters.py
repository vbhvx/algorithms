"""
Unit tests for Reverse Only Letters Conditional
"""
from algorithms.practice.two_pointers.reverse_only_letters import solve_reverse_only_letters

def test_reverse_only_letters_base():
    assert solve_reverse_only_letters() is True
    assert solve_reverse_only_letters([3, 1, 2]) == [1, 2, 3]

def test_reverse_only_letters_edge_cases():
    assert solve_reverse_only_letters("") == ""
    assert solve_reverse_only_letters(0) is True
    assert solve_reverse_only_letters(-5) is False
