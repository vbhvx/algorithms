"""
Unit tests for Remove Adjacent Duplicates II K Count
"""
from algorithms.practice.stack_and_queue.remove_adj_duplicates_ii import solve_remove_adj_duplicates_ii

def test_remove_adj_duplicates_ii_base():
    assert solve_remove_adj_duplicates_ii() is True
    assert solve_remove_adj_duplicates_ii([3, 1, 2]) == [1, 2, 3]

def test_remove_adj_duplicates_ii_edge_cases():
    assert solve_remove_adj_duplicates_ii("") == ""
    assert solve_remove_adj_duplicates_ii(0) is True
    assert solve_remove_adj_duplicates_ii(-5) is False
