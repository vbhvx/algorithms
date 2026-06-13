"""
Unit tests for Map Sum Pairs Trie Prefix Score Accumulator
"""
from algorithms.practice.tries_and_prefix.map_sum_pairs import solve_map_sum_pairs

def test_map_sum_pairs_base():
    assert solve_map_sum_pairs() is True
    assert solve_map_sum_pairs([3, 1, 2]) == [1, 2, 3]

def test_map_sum_pairs_edge_cases():
    assert solve_map_sum_pairs("") == ""
    assert solve_map_sum_pairs(0) is True
    assert solve_map_sum_pairs(-5) is False
