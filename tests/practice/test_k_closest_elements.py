"""
Unit tests for Find K Closest Elements Window
"""
from algorithms.practice.two_pointers.k_closest_elements import solve_k_closest_elements

def test_k_closest_elements_base():
    assert solve_k_closest_elements() is True
    assert solve_k_closest_elements([3, 1, 2]) == [1, 2, 3]

def test_k_closest_elements_edge_cases():
    assert solve_k_closest_elements("") == ""
    assert solve_k_closest_elements(0) is True
    assert solve_k_closest_elements(-5) is False
