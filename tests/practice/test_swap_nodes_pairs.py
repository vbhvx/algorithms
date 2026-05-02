"""
Unit tests for Swap Nodes in Pairs Iterative Pointer Swaps
"""
from algorithms.practice.linked_lists.swap_nodes_pairs import solve_swap_nodes_pairs

def test_swap_nodes_pairs_base():
    assert solve_swap_nodes_pairs() is True
    assert solve_swap_nodes_pairs([3, 1, 2]) == [1, 2, 3]

def test_swap_nodes_pairs_edge_cases():
    assert solve_swap_nodes_pairs("") == ""
    assert solve_swap_nodes_pairs(0) is True
    assert solve_swap_nodes_pairs(-5) is False
