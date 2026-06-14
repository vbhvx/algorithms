"""
Unit tests for Stream of Characters Suffix Trie Search
"""
from algorithms.practice.tries_and_prefix.stream_of_chars import solve_stream_of_chars

def test_stream_of_chars_base():
    assert solve_stream_of_chars() is True
    assert solve_stream_of_chars([3, 1, 2]) == [1, 2, 3]

def test_stream_of_chars_edge_cases():
    assert solve_stream_of_chars("") == ""
    assert solve_stream_of_chars(0) is True
    assert solve_stream_of_chars(-5) is False
