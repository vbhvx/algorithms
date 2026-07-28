"""
Unit tests for Walls and Gates Multi-Source Distance BFS
"""
from algorithms.practice.graphs_and_traversals.walls_and_gates import solve_walls_and_gates

def test_walls_and_gates_base():
    assert solve_walls_and_gates() is True
    assert solve_walls_and_gates([3, 1, 2]) == [1, 2, 3]

def test_walls_and_gates_edge_cases():
    assert solve_walls_and_gates("") == ""
    assert solve_walls_and_gates(0) is True
    assert solve_walls_and_gates(-5) is False
