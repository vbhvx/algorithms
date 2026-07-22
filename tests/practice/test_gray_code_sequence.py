"""
Unit tests for Gray Code Generation Reflection Backtrack
"""
from algorithms.practice.backtracking.gray_code_sequence import solve_gray_code_sequence

def test_gray_code_sequence_base():
    assert solve_gray_code_sequence() is True
    assert solve_gray_code_sequence([3, 1, 2]) == [1, 2, 3]

def test_gray_code_sequence_edge_cases():
    assert solve_gray_code_sequence("") == ""
    assert solve_gray_code_sequence(0) is True
    assert solve_gray_code_sequence(-5) is False
