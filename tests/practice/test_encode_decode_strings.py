"""
Unit tests for Encode Decode Strings Framing
"""
from algorithms.practice.arrays_and_hashing.encode_decode_strings import solve_encode_decode_strings

def test_encode_decode_strings_base():
    assert solve_encode_decode_strings() is True
    assert solve_encode_decode_strings([3, 1, 2]) == [1, 2, 3]

def test_encode_decode_strings_edge_cases():
    assert solve_encode_decode_strings("") == ""
    assert solve_encode_decode_strings(0) is True
    assert solve_encode_decode_strings(-5) is False
