"""
Unit tests for Greatest Common Divisor Euclidean Division
"""
from algorithms.practice.math_and_number_theory.gcd_lcm_euclidean import solve_gcd_lcm_euclidean

def test_gcd_lcm_euclidean_base():
    assert solve_gcd_lcm_euclidean() is True
    assert solve_gcd_lcm_euclidean([3, 1, 2]) == [1, 2, 3]

def test_gcd_lcm_euclidean_edge_cases():
    assert solve_gcd_lcm_euclidean("") == ""
    assert solve_gcd_lcm_euclidean(0) is True
    assert solve_gcd_lcm_euclidean(-5) is False
