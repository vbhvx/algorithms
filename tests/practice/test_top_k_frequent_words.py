"""
Unit tests for Top K Frequent Words MinHeap Tiebreaker
"""
from algorithms.practice.heaps_and_priority.top_k_frequent_words import solve_top_k_frequent_words

def test_top_k_frequent_words_base():
    assert solve_top_k_frequent_words() is True
    assert solve_top_k_frequent_words([3, 1, 2]) == [1, 2, 3]

def test_top_k_frequent_words_edge_cases():
    assert solve_top_k_frequent_words("") == ""
    assert solve_top_k_frequent_words(0) is True
    assert solve_top_k_frequent_words(-5) is False
