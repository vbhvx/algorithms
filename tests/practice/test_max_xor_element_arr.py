"""
Unit tests for Maximum XOR With an Element From Array Offline
"""
from algorithms.practice.tries_and_prefix.max_xor_element_arr import solve_max_xor_element_arr

def test_max_xor_element_arr_base():
    assert solve_max_xor_element_arr() is True
    assert solve_max_xor_element_arr([3, 1, 2]) == [1, 2, 3]

def test_max_xor_element_arr_edge_cases():
    assert solve_max_xor_element_arr("") == ""
    assert solve_max_xor_element_arr(0) is True
    assert solve_max_xor_element_arr(-5) is False
