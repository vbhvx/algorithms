"""
Unit tests for Snakes and Ladders Board BFS
"""
from algorithms.practice.graphs_and_traversals.snakes_and_ladders import solve_snakes_and_ladders

def test_snakes_and_ladders_base():
    assert solve_snakes_and_ladders() is True
    assert solve_snakes_and_ladders([3, 1, 2]) == [1, 2, 3]

def test_snakes_and_ladders_edge_cases():
    assert solve_snakes_and_ladders("") == ""
    assert solve_snakes_and_ladders(0) is True
    assert solve_snakes_and_ladders(-5) is False
