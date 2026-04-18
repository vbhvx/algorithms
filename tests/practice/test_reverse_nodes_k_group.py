"""
Unit tests for Reverse Nodes in K-Group Iterative
"""
from algorithms.practice.linked_lists.reverse_nodes_k_group import solve_reverse_nodes_k_group

def test_reverse_nodes_k_group_base():
    assert solve_reverse_nodes_k_group() is True
    assert solve_reverse_nodes_k_group([3, 1, 2]) == [1, 2, 3]

def test_reverse_nodes_k_group_edge_cases():
    assert solve_reverse_nodes_k_group("") == ""
    assert solve_reverse_nodes_k_group(0) is True
    assert solve_reverse_nodes_k_group(-5) is False
