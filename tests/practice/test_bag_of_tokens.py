"""
Unit tests for Bag of Tokens Score Maximizer
"""
from algorithms.practice.two_pointers.bag_of_tokens import solve_bag_of_tokens

def test_bag_of_tokens_base():
    assert solve_bag_of_tokens() is True
    assert solve_bag_of_tokens([3, 1, 2]) == [1, 2, 3]

def test_bag_of_tokens_edge_cases():
    assert solve_bag_of_tokens("") == ""
    assert solve_bag_of_tokens(0) is True
    assert solve_bag_of_tokens(-5) is False
