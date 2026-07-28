"""
Unit tests for Rotting Oranges Multi-Source BFS Queue
"""
from algorithms.practice.graphs_and_traversals.rotting_oranges import solve_rotting_oranges

def test_rotting_oranges_base():
    assert solve_rotting_oranges() is True
    assert solve_rotting_oranges([3, 1, 2]) == [1, 2, 3]

def test_rotting_oranges_edge_cases():
    assert solve_rotting_oranges("") == ""
    assert solve_rotting_oranges(0) is True
    assert solve_rotting_oranges(-5) is False
