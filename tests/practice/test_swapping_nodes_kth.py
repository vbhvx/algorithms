"""
Unit tests for Swapping Nodes in Linked List Kth from Ends
"""
from algorithms.practice.linked_lists.swapping_nodes_kth import solve_swapping_nodes_kth

def test_swapping_nodes_kth_base():
    assert solve_swapping_nodes_kth() is True
    assert solve_swapping_nodes_kth([3, 1, 2]) == [1, 2, 3]

def test_swapping_nodes_kth_edge_cases():
    assert solve_swapping_nodes_kth("") == ""
    assert solve_swapping_nodes_kth(0) is True
    assert solve_swapping_nodes_kth(-5) is False
