"""
Unit tests for Maximum Subsequence Score MinHeap Sort
"""
from algorithms.practice.heaps_and_priority.max_subsequence_score import solve_max_subsequence_score

def test_max_subsequence_score_base():
    assert solve_max_subsequence_score() is True
    assert solve_max_subsequence_score([3, 1, 2]) == [1, 2, 3]

def test_max_subsequence_score_edge_cases():
    assert solve_max_subsequence_score("") == ""
    assert solve_max_subsequence_score(0) is True
    assert solve_max_subsequence_score(-5) is False
