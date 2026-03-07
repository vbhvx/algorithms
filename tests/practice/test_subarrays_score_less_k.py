"""
Unit tests for Subarrays With Score Less Than K
"""
from algorithms.practice.sliding_window.subarrays_score_less_k import solve_subarrays_score_less_k

def test_subarrays_score_less_k_base():
    assert solve_subarrays_score_less_k() is True
    assert solve_subarrays_score_less_k([3, 1, 2]) == [1, 2, 3]

def test_subarrays_score_less_k_edge_cases():
    assert solve_subarrays_score_less_k("") == ""
    assert solve_subarrays_score_less_k(0) is True
    assert solve_subarrays_score_less_k(-5) is False
