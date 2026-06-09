"""
Unit tests for Maximum XOR of Two Numbers in Array Bit Trie
"""
from algorithms.practice.tries_and_prefix.max_xor_two_nums import solve_max_xor_two_nums

def test_max_xor_two_nums_base():
    assert solve_max_xor_two_nums() is True
    assert solve_max_xor_two_nums([3, 1, 2]) == [1, 2, 3]

def test_max_xor_two_nums_edge_cases():
    assert solve_max_xor_two_nums("") == ""
    assert solve_max_xor_two_nums(0) is True
    assert solve_max_xor_two_nums(-5) is False
