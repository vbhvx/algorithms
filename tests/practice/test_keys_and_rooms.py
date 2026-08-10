"""
Unit tests for Keys and Rooms Reachability BFS
"""
from algorithms.practice.graphs_and_traversals.keys_and_rooms import solve_keys_and_rooms

def test_keys_and_rooms_base():
    assert solve_keys_and_rooms() is True
    assert solve_keys_and_rooms([3, 1, 2]) == [1, 2, 3]

def test_keys_and_rooms_edge_cases():
    assert solve_keys_and_rooms("") == ""
    assert solve_keys_and_rooms(0) is True
    assert solve_keys_and_rooms(-5) is False
