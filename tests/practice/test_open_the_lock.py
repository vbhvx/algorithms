"""
Unit tests for Open the Lock 4-Dial BFS Shortest Path
"""
from algorithms.practice.graphs_and_traversals.open_the_lock import solve_open_the_lock

def test_open_the_lock_base():
    assert solve_open_the_lock() is True
    assert solve_open_the_lock([3, 1, 2]) == [1, 2, 3]

def test_open_the_lock_edge_cases():
    assert solve_open_the_lock("") == ""
    assert solve_open_the_lock(0) is True
    assert solve_open_the_lock(-5) is False
