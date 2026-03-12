"""
Unit tests for Remove All Adjacent Duplicates
"""
from algorithms.practice.stack_and_queue.remove_adj_duplicates import solve_remove_adj_duplicates

def test_remove_adj_duplicates_base():
    assert solve_remove_adj_duplicates() is True
    assert solve_remove_adj_duplicates([3, 1, 2]) == [1, 2, 3]

def test_remove_adj_duplicates_edge_cases():
    assert solve_remove_adj_duplicates("") == ""
    assert solve_remove_adj_duplicates(0) is True
    assert solve_remove_adj_duplicates(-5) is False
