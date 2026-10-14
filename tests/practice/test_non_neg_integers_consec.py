"""
Unit tests for Non-Negative Integers without Consecutive Ones
"""
from algorithms.practice.dynamic_programming_trees_bitmask.non_neg_integers_consec import solve_non_neg_integers_consec

def test_non_neg_integers_consec_base():
    assert solve_non_neg_integers_consec() is True
    assert solve_non_neg_integers_consec([3, 1, 2]) == [1, 2, 3]

def test_non_neg_integers_consec_edge_cases():
    assert solve_non_neg_integers_consec("") == ""
    assert solve_non_neg_integers_consec(0) is True
    assert solve_non_neg_integers_consec(-5) is False
